#!/usr/bin/env bash
#
# drm-kpi-diff.sh - find Linux kernel interfaces that the DRM drivers
# (amdgpu, i915, xe, radeon, ttm, drm core, ...) newly use, stop using, or
# whose types changed, between Linux versions.
#
# For each version it:
#   1. shallow-fetches the tag and builds x86_64 defconfig + DRM drivers as
#      modules (out of tree, incrementally re-using one build directory);
#   2. classifies modules as "ported" (default: everything under
#      drivers/gpu/drm/) or "provider" (vmlinux + every other module, i.e.
#      what LinuxKPI has to supply);
#   3. records every provider symbol imported by a ported module
#      (imports.tsv: symbol, kind, exporter, export type, namespace, users);
#   4. runs abidw on vmlinux and each supplying provider module;
#   5. indexes header-level interfaces (macros, static inlines, struct/
#      union/enum tags, typedefs, enumerators) from non-DRM Linux headers
#      that the compiled DRM sources name (headers-used.tsv).
# Then for each consecutive pair of versions it reports added / removed
# imports, likely renames (same signature, similar name), export-type
# changes, an abidiff of the types of every interface used in both
# versions, and the same add/remove/rename/signature view for the
# header-level interfaces.
#
# Usage:
#   ./drm-kpi-diff.sh [v6.15 v6.16 v6.17 v6.18 ...]
#
# Environment knobs (defaults in brackets):
#   WORK            work directory                      [./drm-kpi-work]
#   JOBS            make -j                             [nproc]
#   LINUX_GIT       git URL to fetch refs from          [github torvalds mirror]
#   PORTED_RE       ERE on module path = ported code    [^drivers/gpu/drm/]
#   PORTED_BUILTIN_DIRS  space-separated build-tree dirs of *built-in* code
#                   that the FreeBSD port carries itself, e.g.
#                   "drivers/dma-buf drivers/video"; their exports are then
#                   not reported as provider interfaces            [""]
#   EXTRA_CONFIG    file of scripts/config arguments, one per line
#                   (e.g. "-e HSA_AMD"), applied after the defaults [""]
#   DRM_DEBUG_INFO  1 = keep DWARF in the DRM modules (slower, bigger)  [0]
#   KEEP_TREES      1 = keep a copy of each version's vmlinux           [0]
#
# Requirements: kernel build deps (gcc, make, flex, bison, bc, libelf-dev,
# libssl-dev), git, python3, libabigail tools (abidw, abidiff >= 2.0).
#
# Output: $WORK/out/<ver>/{imports.tsv,headers-used.tsv,abi/*.xml,config}
#         $WORK/out/diff-<a>..<b>/{report.md,impacted.tsv,abidiff-*.txt}
#         $WORK/out/summary.md, $WORK/out/matrix.tsv
#
set -euo pipefail

WORK=${WORK:-$PWD/drm-kpi-work}
JOBS=${JOBS:-$(nproc)}
LINUX_GIT=${LINUX_GIT:-https://github.com/torvalds/linux}
PORTED_RE=${PORTED_RE:-^drivers/gpu/drm/}
PORTED_BUILTIN_DIRS=${PORTED_BUILTIN_DIRS:-}
EXTRA_CONFIG=${EXTRA_CONFIG:-}
DRM_DEBUG_INFO=${DRM_DEBUG_INFO:-0}
KEEP_TREES=${KEEP_TREES:-0}

if [ $# -gt 0 ]; then VERSIONS=("$@"); else VERSIONS=(v6.15 v6.16 v6.17 v6.18); fi

SRC=$WORK/linux
BUILD=$WORK/build
OUT=$WORK/out
SELF_DIR=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$WORK" "$OUT"

log() { printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*" >&2; }
die() { log "ERROR: $*"; exit 1; }

for t in git make gcc python3 abidw abidiff nm flex bison bc; do
	command -v "$t" >/dev/null || die "missing tool: $t"
done

# --------------------------------------------------------------------------
fetch_ref() {
	local ref=$1
	if [ ! -d "$SRC/.git" ]; then
		git init -q "$SRC"
		git -C "$SRC" remote add origin "$LINUX_GIT"
	fi
	log "fetching $ref"
	# Tags first, then branches / SHAs.
	git -C "$SRC" fetch -q --depth 1 origin "refs/tags/$ref" 2>/dev/null ||
		git -C "$SRC" fetch -q --depth 1 origin "$ref"
	git -C "$SRC" checkout -q -f FETCH_HEAD
	git -C "$SRC" clean -q -fdx
}

configure() {
	local ver=$1
	mkdir -p "$BUILD"
	make -s -C "$SRC" O="$BUILD" defconfig >/dev/null
	local args=(
		-e MODULES -e MODULE_UNLOAD
		-m DRM
		-m DRM_AMDGPU -e DRM_AMDGPU_SI -e DRM_AMDGPU_CIK
		-e DRM_AMDGPU_USERPTR -e DRM_AMD_DC
		-m DRM_RADEON
		-m DRM_I915
		-m DRM_XE
		-d DEBUG_INFO_NONE -e DEBUG_INFO_DWARF4
		-d DEBUG_INFO_REDUCED -d DEBUG_INFO_SPLIT
		-d DEBUG_INFO_COMPRESSED_ZLIB -d DEBUG_INFO_COMPRESSED_ZSTD
		-e DEBUG_INFO_COMPRESSED_NONE
		-d DEBUG_INFO_BTF -d MODVERSIONS -d MODULE_SIG
		-d WERROR -d RUST -d GCOV_KERNEL -d KASAN
	)
	"$SRC/scripts/config" --file "$BUILD/.config" "${args[@]}"
	if [ -n "$EXTRA_CONFIG" ]; then
		# shellcheck disable=SC2046
		"$SRC/scripts/config" --file "$BUILD/.config" \
			$(grep -v '^[[:space:]]*#' "$EXTRA_CONFIG")
	fi
	make -s -C "$SRC" O="$BUILD" olddefconfig >/dev/null
	for c in DRM DRM_AMDGPU DRM_RADEON DRM_I915 DRM_XE; do
		grep -q "^CONFIG_$c=m" "$BUILD/.config" ||
			log "WARNING: CONFIG_$c is not =m in $ver ($(grep "CONFIG_$c[= ]" "$BUILD/.config" || echo unset))"
	done
	grep -q '^CONFIG_DEBUG_INFO=y' "$BUILD/.config" || die "DEBUG_INFO not enabled"
}

build() {
	local ver=$1
	if [ "$DRM_DEBUG_INFO" != 1 ]; then
		# Provider code needs DWARF for abidw; the (huge) DRM modules do not,
		# we only read their ELF undefined symbols.  -g0 comes after the
		# global -g flags, so it wins.  Reverted by the next checkout.
		echo 'subdir-ccflags-y += -g0' >> "$SRC/drivers/gpu/drm/Makefile"
	fi
	log "building $ver (-j$JOBS); log: $OUT/$ver/build.log"
	if ! make -C "$SRC" O="$BUILD" -j"$JOBS" vmlinux modules \
		> "$OUT/$ver/build.log" 2>&1; then
		tail -40 "$OUT/$ver/build.log" >&2
		die "build of $ver failed"
	fi
	git -C "$SRC" checkout -q -- drivers/gpu/drm/Makefile
}

extract() {
	local ver=$1 d=$OUT/$ver
	cp "$BUILD/.config" "$d/config"
	cp "$BUILD/Module.symvers" "$d/Module.symvers"
	cp "$BUILD/modules.order" "$d/modules.order"
	cp "$BUILD/System.map" "$d/System.map"

	# Undefined symbols of every ported module, and defined symbols (with
	# nm type letter) of every provider module.
	: > "$d/ported-undef.txt"
	: > "$d/provider-defs.txt"
	local o ko
	while read -r o; do
		ko=${o%.o}.ko
		if [[ $ko =~ $PORTED_RE ]]; then
			nm -u "$BUILD/$ko" | awk -v m="${ko%.ko}" '{print m "\t" $NF}' \
				>> "$d/ported-undef.txt"
		else
			nm --defined-only "$BUILD/$ko" |
				awk -v m="${ko%.ko}" 'NF==3 {print m "\t" $3 "\t" $2}' \
				>> "$d/provider-defs.txt"
		fi
	done < "$BUILD/modules.order"

	# Built-in code the port carries itself.
	: > "$d/ported-builtin-syms.txt"
	local dir
	for dir in $PORTED_BUILTIN_DIRS; do
		[ -d "$BUILD/$dir" ] || { log "WARNING: no $BUILD/$dir"; continue; }
		find "$BUILD/$dir" -name '*.o' ! -name '*.mod.o' -print0 |
			xargs -0 -r nm --defined-only 2>/dev/null |
			awk 'NF==3 && $2 ~ /[A-Z]/ {print $3}' >> "$d/ported-builtin-syms.txt"
	done
	sort -u -o "$d/ported-builtin-syms.txt" "$d/ported-builtin-syms.txt"

	python3 -I "$SELF_DIR/drm-kpi-diff.py" imports "$d" "$PORTED_RE"
	# Header-level interfaces (macros, inlines, types).  Needs the source
	# tree and the build's <module>.mod lists for this exact version.
	python3 -I "$SELF_DIR/drm-kpi-diff.py" headers "$d" "$SRC" "$BUILD" "$PORTED_RE"
}

abi_dump() {
	# One abidw corpus per binary (vmlinux and each provider module that
	# supplies something to the ported code).  libabigail's --linux-tree
	# mode would do this in one go, but 2.4 segfaults on it.
	local ver=$1 d=$OUT/$ver m bin
	rm -rf "$d/abi"; mkdir -p "$d/abi"
	log "abidw $ver ($(($(wc -l < "$d/symbols.list") - 1)) symbols)"
	for m in vmlinux $(tail -n +2 "$d/imports.tsv" | cut -f3 | sort -u |
			grep -v -e '^vmlinux$' -e '^UNRESOLVED$' || true); do
		if [ "$m" = vmlinux ]; then bin=$BUILD/vmlinux; else bin=$BUILD/$m.ko; fi
		mkdir -p "$d/abi/$(dirname "$m")"
		abidw --kmi-whitelist "$d/symbols.list" "$bin" \
			--out-file "$d/abi/$m.xml" 2>> "$d/abidw.log" ||
			die "abidw failed on $m for $ver (see $d/abidw.log)"
	done
	if [ "$KEEP_TREES" = 1 ]; then
		mkdir -p "$d/bin"; cp "$BUILD/vmlinux" "$d/bin/"
	fi
	touch "$d/abi.done"
}

compare() {
	local a=$1 b=$2 d=$OUT/diff-$1..$2
	mkdir -p "$d"
	# Interfaces used in both versions: type changes matter.
	comm -12 <(tail -n +2 "$OUT/$a/imports.tsv" | cut -f1 | sort) \
		 <(tail -n +2 "$OUT/$b/imports.tsv" | cut -f1 | sort) |
		{ echo '[abi_whitelist]'; sed 's/^/  /'; } > "$d/common.list"
	log "abidiff $a..$b"
	: > "$d/abidiff-leaf.txt"; : > "$d/abidiff-full.txt"
	local x rel rc
	while read -r x; do
		rel=${x#"$OUT/$a/abi/"}
		[ -f "$OUT/$b/abi/$rel" ] || continue
		printf '==== %s ====\n' "${rel%.xml}" | tee -a "$d/abidiff-full.txt" \
			>> "$d/abidiff-leaf.txt"
		set +e
		abidiff --kmi-whitelist "$d/common.list" --leaf-changes-only \
			--impacted-interfaces --no-added-syms \
			"$x" "$OUT/$b/abi/$rel" >> "$d/abidiff-leaf.txt" 2>&1
		rc=$?
		abidiff --kmi-whitelist "$d/common.list" --no-added-syms \
			"$x" "$OUT/$b/abi/$rel" >> "$d/abidiff-full.txt" 2>&1
		set -e
		# abidiff rc bits: 1=error 2=usage error 4=change 8=incompatible
		[ $((rc & 3)) -eq 0 ] ||
			log "WARNING: abidiff error on $rel (rc=$rc), see $d/abidiff-leaf.txt"
	done < <(find "$OUT/$a/abi" -name '*.xml' | sort)
	python3 -I "$SELF_DIR/drm-kpi-diff.py" pair "$OUT/$a" "$OUT/$b" "$d"
}

# --------------------------------------------------------------------------
for ver in "${VERSIONS[@]}"; do
	mkdir -p "$OUT/$ver"
	if [ -f "$OUT/$ver/abi.done" ]; then
		log "$ver already done, skipping (delete $OUT/$ver to redo)"
		continue
	fi
	fetch_ref "$ver"
	configure "$ver"
	build "$ver"
	extract "$ver"
	abi_dump "$ver"
	log "$ver done"
done

prev=
for ver in "${VERSIONS[@]}"; do
	[ -n "$prev" ] && compare "$prev" "$ver"
	prev=$ver
done
python3 -I "$SELF_DIR/drm-kpi-diff.py" summary "$OUT" "${VERSIONS[@]}"
log "done: $OUT/summary.md"
