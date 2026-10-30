#!/usr/bin/env bash
#
# linuxkpi-diff.sh - find Linux kernel interfaces that LinuxKPI consumers
# (drm-kmod's DRM drivers, the wireless drivers in sys/contrib/dev, ...)
# newly use, stop using, or whose types changed, between Linux versions.
#
# Consumers are Linux code that FreeBSD carries itself; they are defined by
# source-path prefixes in groups.conf, organized in a hierarchy (drm/amdgpu,
# wifi/iwlwifi, ...).  Everything else -- vmlinux and every other module,
# e.g. mac80211/cfg80211 -- is a provider, i.e. what LinuxKPI must supply.
#
# For each version it:
#   1. shallow-fetches the ref and builds x86_64 defconfig plus the Kconfig
#      fragments in kconfig/*.config (out of tree, one reused build dir);
#   2. records every provider symbol imported by a consumer module
#      (imports.tsv: symbol, kind, exporter, export type, namespace, users,
#      groups);
#   3. indexes header-level interfaces -- macros, static inlines, struct/
#      union/enum tags, typedefs, enumerators -- from the provider headers
#      the consumer objects were compiled against, that consumer code names
#      (headers-used.tsv);
#   4. runs abidw on vmlinux and each provider module that supplies symbols.
# Then for each consecutive pair of versions it writes a report for all
# consumers and one per group node (drm, drm/amdgpu, wifi, wifi/iwlwifi,
# ...): newly used / no longer used interfaces, likely renames (same
# signature, similar name), export changes, interfaces whose declaration
# changed, changed types reachable from used interfaces (abidiff), and the
# same add/remove/rename/signature view for header-level interfaces.
#
# Usage:
#   ./linuxkpi-diff.sh [v6.15 v6.16 v6.17 v6.18 ...]
#
# Environment knobs (defaults in brackets):
#   WORK            work directory                      [./linuxkpi-diff-work]
#   JOBS            make -j                             [nproc]
#   LINUX_GIT       git URL to fetch refs from          [github torvalds mirror]
#   GROUPS_CONF     consumer groups                     [<script dir>/groups.conf]
#   KCONFIG_DIR     Kconfig fragments (*.config, scripts/config arguments,
#                   one per line), applied in name order [<script dir>/kconfig]
#   EXTRA_CONFIG    one more fragment applied last                    [""]
#   PORTED_BUILTIN_DIRS  space-separated build-tree dirs of *built-in* code
#                   that FreeBSD carries itself (e.g. "drivers/dma-buf");
#                   their exports are not reported as provider interfaces [""]
#   CONSUMER_DEBUG_INFO  1 = keep DWARF in consumer code (slower, bigger) [0]
#   KEEP_TREES      1 = keep a copy of each version's vmlinux           [0]
#
# Requirements: kernel build deps (gcc, make, flex, bison, bc, libelf-dev,
# libssl-dev), git, python3, libabigail tools (abidw, abidiff >= 2.0).
#
# Output: $WORK/out/<ver>/{imports.tsv,headers-used.tsv,modules-groups.tsv,
#                          abi/*.xml,config}
#         $WORK/out/diff-<a>..<b>/{report.md,groups/*.md,overview.tsv,
#                                  impacted.tsv,abidiff-*.txt}
#         $WORK/out/summary.md, $WORK/out/matrix.tsv
#
set -euo pipefail

SELF_DIR=$(cd "$(dirname "$0")" && pwd)
WORK=${WORK:-$PWD/linuxkpi-diff-work}
JOBS=${JOBS:-$(nproc)}
LINUX_GIT=${LINUX_GIT:-https://github.com/torvalds/linux}
GROUPS_CONF=${GROUPS_CONF:-$SELF_DIR/groups.conf}
KCONFIG_DIR=${KCONFIG_DIR:-$SELF_DIR/kconfig}
EXTRA_CONFIG=${EXTRA_CONFIG:-}
PORTED_BUILTIN_DIRS=${PORTED_BUILTIN_DIRS:-}
CONSUMER_DEBUG_INFO=${CONSUMER_DEBUG_INFO:-0}
KEEP_TREES=${KEEP_TREES:-0}

if [ $# -gt 0 ]; then VERSIONS=("$@"); else VERSIONS=(v6.15 v6.16 v6.17 v6.18); fi

SRC=$WORK/linux
BUILD=$WORK/build
OUT=$WORK/out
HELPER=$SELF_DIR/linuxkpi-diff.py
mkdir -p "$WORK" "$OUT"

log() { printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*" >&2; }
die() { log "ERROR: $*"; exit 1; }
py() { python3 -I "$HELPER" "$@"; }

for t in git make gcc python3 abidw abidiff nm flex bison bc; do
	command -v "$t" >/dev/null || die "missing tool: $t"
done
[ -f "$GROUPS_CONF" ] || die "no groups file: $GROUPS_CONF"

fragments() {
	ls "$KCONFIG_DIR"/*.config 2>/dev/null || true
	[ -z "$EXTRA_CONFIG" ] || echo "$EXTRA_CONFIG"
}

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
	local ver=$1 frag
	mkdir -p "$BUILD"
	make -s -C "$SRC" O="$BUILD" defconfig >/dev/null
	"$SRC/scripts/config" --file "$BUILD/.config" \
		-e MODULES -e MODULE_UNLOAD \
		-d DEBUG_INFO_NONE -e DEBUG_INFO_DWARF4 \
		-d DEBUG_INFO_REDUCED -d DEBUG_INFO_SPLIT \
		-d DEBUG_INFO_COMPRESSED_ZLIB -d DEBUG_INFO_COMPRESSED_ZSTD \
		-e DEBUG_INFO_COMPRESSED_NONE \
		-d DEBUG_INFO_BTF -d MODVERSIONS -d MODULE_SIG \
		-d WERROR -d RUST -d GCOV_KERNEL -d KASAN
	while read -r frag; do
		[ -n "$frag" ] || continue
		# shellcheck disable=SC2046
		"$SRC/scripts/config" --file "$BUILD/.config" \
			$(grep -v -e '^[[:space:]]*#' -e '^[[:space:]]*$' "$frag")
	done < <(fragments)
	make -s -C "$SRC" O="$BUILD" olddefconfig >/dev/null
	grep -q '^CONFIG_DEBUG_INFO=y' "$BUILD/.config" || die "DEBUG_INFO not enabled"
	# Report fragment settings Kconfig did not honour (missing symbol in
	# this version, unmet dependency, ...).
	local opt sym want have
	while read -r frag; do
		[ -n "$frag" ] || continue
		while read -r opt sym; do
			case $opt in -m) want=m ;; -e) want=y ;; *) continue ;; esac
			have=$(sed -n "s/^CONFIG_$sym=//p" "$BUILD/.config")
			if [ "$have" != "$want" ] && ! { [ "$want" = y ] && [ "$have" = m ]; }; then
				log "WARNING: $ver: $(basename "$frag"): CONFIG_$sym=${have:-unset}, wanted $want"
			fi
		done < <(grep -E '^[[:space:]]*-[em][[:space:]]' "$frag")
	done < <(fragments)
}

build() {
	local ver=$1 dir
	if [ "$CONSUMER_DEBUG_INFO" != 1 ]; then
		# Provider code needs DWARF for abidw; consumer code (huge for DRM)
		# does not, we only read its ELF undefined symbols.  -g0 comes after
		# the global -g flags, so it wins.  Reverted below.
		while read -r dir; do
			echo 'subdir-ccflags-y += -g0' >> "$SRC/$dir/Makefile"
		done < <(py g0dirs "$GROUPS_CONF" "$SRC")
	fi
	log "building $ver (-j$JOBS); log: $OUT/$ver/build.log"
	if ! make -C "$SRC" O="$BUILD" -j"$JOBS" vmlinux modules \
		> "$OUT/$ver/build.log" 2>&1; then
		tail -40 "$OUT/$ver/build.log" >&2
		git -C "$SRC" checkout -q -- .
		die "build of $ver failed"
	fi
	git -C "$SRC" checkout -q -- .
}

extract() {
	local ver=$1 d=$OUT/$ver dir
	cp "$BUILD/.config" "$d/config"
	cp "$BUILD/Module.symvers" "$BUILD/modules.order" "$BUILD/System.map" "$d/"

	# Built-in code that FreeBSD carries itself.
	: > "$d/ported-builtin-syms.txt"
	for dir in $PORTED_BUILTIN_DIRS; do
		[ -d "$BUILD/$dir" ] || { log "WARNING: no $BUILD/$dir"; continue; }
		find "$BUILD/$dir" -name '*.o' ! -name '*.mod.o' -print0 |
			xargs -0 -r nm --defined-only 2>/dev/null |
			awk 'NF==3 && $2 ~ /[A-Z]/ {print $3}' >> "$d/ported-builtin-syms.txt"
	done
	sort -u -o "$d/ported-builtin-syms.txt" "$d/ported-builtin-syms.txt"

	py imports "$d" "$BUILD" "$GROUPS_CONF"
	# Needs the source tree and the build's .mod/.cmd files of this exact
	# version, so it runs before the next version is checked out.
	py headers "$d" "$SRC" "$BUILD" "$GROUPS_CONF"
}

abi_dump() {
	# One abidw corpus per binary (vmlinux and each provider module that
	# supplies something to consumers).  libabigail's --linux-tree mode
	# would do this in one go, but 2.4 segfaults on it.
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
	# (libabigail 2.4 only honours the [abi_whitelist] section name.)
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
	py pair "$OUT/$a" "$OUT/$b" "$d" "$GROUPS_CONF"
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
py summary "$OUT" "$GROUPS_CONF" "${VERSIONS[@]}"
log "done: $OUT/summary.md"
