#!/usr/bin/env python3
"""Helper for drm-kpi-diff.sh.

  drm-kpi-diff.py imports <verdir> <ported_re>
  drm-kpi-diff.py headers <verdir> <srctree> <buildtree> <ported_re>
  drm-kpi-diff.py pair    <verdir_a> <verdir_b> <outdir>
  drm-kpi-diff.py summary <outdir> <ver>...
"""
import collections
import difflib
import os
import re
import sys
import xml.etree.ElementTree as ET

FUNC_TYPES = set("TtWwi")
TSV_COLS = ["symbol", "kind", "exporter", "export", "namespace", "used_by"]
TOP_DIRS = ("include|arch|kernel|mm|drivers|lib|fs|net|block|security|crypto|"
            "init|ipc|sound|virt|io_uring|certs|samples|scripts|tools|usr|rust")
PATH_RE = re.compile(r"(?:^|/)((?:%s)/.*)$" % TOP_DIRS)


def short(mod):
    return os.path.basename(mod)


def norm_path(p):
    if not p:
        return ""
    m = PATH_RE.search(p)
    return m.group(1) if m else p


def read_tsv(path):
    rows = {}
    with open(path) as f:
        hdr = f.readline().rstrip("\n").split("\t")
        for line in f:
            r = dict(zip(hdr, line.rstrip("\n").split("\t")))
            rows[r["symbol"]] = r
    return rows


# ---------------------------------------------------------------- imports
def cmd_imports(d, ported_re):
    ported = re.compile(ported_re)
    symvers = {}
    with open(os.path.join(d, "Module.symvers")) as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < 4:
                continue
            symvers[p[1]] = (p[2], p[3], p[4] if len(p) > 4 else "")

    kinds = {}
    with open(os.path.join(d, "System.map")) as f:
        for line in f:
            p = line.split()
            if len(p) == 3:
                kinds.setdefault(p[2], p[1])
    with open(os.path.join(d, "provider-defs.txt")) as f:
        for line in f:
            mod, sym, t = line.rstrip("\n").split("\t")
            kinds.setdefault(sym, t)

    with open(os.path.join(d, "ported-builtin-syms.txt")) as f:
        ported_builtin = set(l.strip() for l in f if l.strip())

    users = collections.defaultdict(set)
    skipped_builtin = set()
    with open(os.path.join(d, "ported-undef.txt")) as f:
        for line in f:
            mod, sym = line.rstrip("\n").split("\t")
            exp = symvers.get(sym)
            if exp is not None:
                if ported.search(exp[0] + ".ko"):
                    continue          # DRM-internal
                if exp[0] == "vmlinux" and sym in ported_builtin:
                    skipped_builtin.add(sym)
                    continue
            users[sym].add(short(mod))

    with open(os.path.join(d, "imports.tsv"), "w") as out, \
         open(os.path.join(d, "symbols.list"), "w") as wl:
        out.write("\t".join(TSV_COLS) + "\n")
        wl.write("[abi_whitelist]\n")
        for sym in sorted(users):
            exp = symvers.get(sym, ("UNRESOLVED", "", ""))
            t = kinds.get(sym, "?")
            kind = "func" if t in FUNC_TYPES else ("?" if t == "?" else "data")
            out.write("\t".join([sym, kind, exp[0], exp[1], exp[2],
                                 ",".join(sorted(users[sym]))]) + "\n")
            if exp[0] != "UNRESOLVED":
                wl.write("  %s\n" % sym)
    unresolved = sum(1 for s in users if s not in symvers)
    print("%s: %d provider interfaces imported (%d unresolved, %d skipped as "
          "ported built-in)" % (os.path.basename(d), len(users), unresolved,
                                len(skipped_builtin)), file=sys.stderr)


# ------------------------------------------------------------ signatures
def _render(tid, types, depth=0):
    el = types.get(tid)
    if el is None or depth > 12:
        return "?"
    t = el.tag
    if t in ("type-decl", "typedef-decl", "class-decl", "union-decl",
             "enum-decl"):
        n = el.get("name") or "anon"
        return {"class-decl": "struct ", "union-decl": "union ",
                "enum-decl": "enum "}.get(t, "") + n
    if t == "pointer-type-def":
        return _render(el.get("type-id"), types, depth + 1) + "*"
    if t == "reference-type-def":
        return _render(el.get("type-id"), types, depth + 1) + "&"
    if t == "qualified-type-def":
        q = " ".join(k for k in ("const", "volatile", "restrict")
                     if el.get(k) == "yes")
        return (q + " " if q else "") + _render(el.get("type-id"), types, depth + 1)
    if t == "array-type-def":
        return _render(el.get("element-type-id"), types, depth + 1) + "[]"
    if t == "function-type":
        ps = [_render(p.get("type-id"), types, depth + 1)
              for p in el.findall("parameter")]
        r = el.find("return")
        return "fn(%s)->%s" % (", ".join(ps), _render(r.get("type-id"), types,
                                                     depth + 1) if r is not None else "?")
    return "?"


def abi_signatures(abidir):
    """symbol -> normalized signature string (types + parameter names),
    comparable across versions (type-ids are not)."""
    sigs = {}
    xmls = []
    for root, _, files in os.walk(abidir):
        xmls += [os.path.join(root, f) for f in files if f.endswith(".xml")]
    for x in sorted(xmls):
        tree = ET.parse(x)
        types = {}
        for el in tree.iter():
            i = el.get("id")
            if i:
                types[i] = el
        for el in tree.iter():
            sym = el.get("elf-symbol-id")
            if not sym:
                continue
            sym = sym.split("@")[0]
            if el.tag == "function-decl":
                ps = ["%s %s" % (_render(p.get("type-id"), types), p.get("name") or "")
                      for p in el.findall("parameter")]
                r = el.find("return")
                sigs.setdefault(sym, "%s(%s)" % (
                    _render(r.get("type-id"), types) if r is not None else "?",
                    ", ".join(x.strip() for x in ps)))
            elif el.tag == "var-decl":
                sigs.setdefault(sym, _render(el.get("type-id"), types))
    return sigs


def name_similarity(a, b):
    ta, tb = set(a.lower().strip("_").split("_")), set(b.lower().strip("_").split("_"))
    jac = len(ta & tb) / max(1, len(ta | tb))
    return max(jac, difflib.SequenceMatcher(None, a, b).ratio())


def find_renames(added, removed, sig_new, sig_old, strong=lambda s: False):
    """Pair added/removed names with identical signatures.  A pair is kept
    if the names are similar, or the signature is distinctive enough on its
    own (strong(sig)).  Each name is used at most once, best match first."""
    cands = []
    for a in added:
        sa = sig_new.get(a)
        if not sa:
            continue
        for r in removed:
            if sig_old.get(r) != sa:
                continue
            sim = name_similarity(a, r)
            if sim >= 0.5 or strong(sa):
                cands.append((sim, r, a))
    cands.sort(reverse=True)
    used_a, used_r, res = set(), set(), []
    for sim, r, a in cands:
        if a in used_a or r in used_r:
            continue
        used_a.add(a)
        used_r.add(r)
        res.append((r, a, sig_new[a], sim))
    return sorted(res)


# --------------------------------------------------------------- headers
COMMENT_RE = re.compile(r"/\*.*?\*/|//[^\n]*", re.S)
STRING_RE = re.compile(r'"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])*\'')
IDENT_RE = re.compile(r"\b[A-Za-z_]\w*\b")
DEFINE_RE = re.compile(r"^[ \t]*#[ \t]*define[ \t]+(\w+)(\([^)]*\))?(.*)$", re.M)
INLINE_RE = re.compile(
    r"\bstatic\s+(?:(?:__always_inline|inline|__inline__|__inline|__maybe_unused|"
    r"notrace|__attribute_const__|__pure|__must_check|__cold|noinstr|"
    r"__no_kcsan|__no_sanitize_\w+)\s+)*"
    r"([^;{}()=#]*?)\b(\w+)\s*\(([^{};#]*?)\)\s*"
    r"(?:(?:__\w+|\w+_attribute)(?:\s*\([^()]*\))?\s*)*\{")
TAG_RE = re.compile(r"\b(struct|union|enum)\s+(\w+)\s*\{")
TYPEDEF_RE = re.compile(r"\btypedef\b[^;{}]*?\b(\w+)\s*(?:\[[^\]]*\])?\s*;")
TYPEDEF_BLOCK_RE = re.compile(r"\btypedef\s+(?:struct|union|enum)\b[^{;]*\{")
ENUM_BODY_RE = re.compile(r"\benum\b[^{;()]*\{([^{}]*)\}")
SKIP_IDENT = re.compile(r"^(CONFIG_|__UNIQUE_ID|__PASTE)")


def strip_code(text):
    text = COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    return STRING_RE.sub('""', text)


def norm_ws(s):
    return re.sub(r"\s+", " ", s).strip()


def index_header_file(path, rel, idx):
    try:
        raw = open(path, errors="replace").read()
    except OSError:
        return
    text = strip_code(raw)
    joined = text.replace("\\\n", " ")
    for m in DEFINE_RE.finditer(joined):
        name, params, body = m.group(1), m.group(2), m.group(3)
        if name.startswith("_") and name.endswith("_H") or name.endswith("_H_") \
                or name.endswith("_H__"):
            continue              # include guards
        sig = "(%s)" % norm_ws(params[1:-1]).replace(" ", "") if params else ""
        idx.setdefault(name, ("macro", rel, sig, norm_ws(body)))
    nopp = re.sub(r"^[ \t]*#.*$", "", joined, flags=re.M)
    for m in INLINE_RE.finditer(nopp):
        ret, name, params = norm_ws(m.group(1)), m.group(2), norm_ws(m.group(3))
        if name in ("if", "while", "for", "switch", "sizeof"):
            continue
        sig = "%s(%s)" % (ret, params)
        sig = re.sub(r"\s*(\*+)\s*", r" \1", sig)     # 'T * x', 'T *x' -> 'T *x'
        sig = re.sub(r"\(\s+", "(", re.sub(r"\s+\)", ")", sig))
        idx.setdefault(name, ("inline", rel, sig, ""))
    for m in TAG_RE.finditer(nopp):
        idx.setdefault(m.group(2), (m.group(1), rel, "", ""))
    for m in TYPEDEF_RE.finditer(nopp):
        idx.setdefault(m.group(1), ("typedef", rel, "", ""))
    for m in ENUM_BODY_RE.finditer(nopp):
        for ent in m.group(1).split(","):
            e = ent.strip().split("=")[0].strip()
            if re.match(r"^[A-Za-z_]\w*$", e):
                idx.setdefault(e, ("enumerator", rel, "", ""))


def header_index(src, roots, skip):
    idx = {}
    for root in roots:
        top = os.path.join(src, root)
        for dp, dns, fns in os.walk(top):
            reldir = os.path.relpath(dp, src)
            dns[:] = sorted(d for d in dns
                            if not any((reldir + "/" + d).startswith(s) for s in skip))
            for fn in sorted(fns):
                if fn.endswith(".h"):
                    index_header_file(os.path.join(dp, fn),
                                      os.path.join(reldir, fn), idx)
    return idx


def cmd_headers(d, src, build, ported_re):
    """Header-level interfaces (macros, static inlines, struct/union/enum
    tags, typedefs, enumerators) defined in non-DRM Linux headers and named
    by the compiled source of the ported modules."""
    ported = re.compile(ported_re)
    # Compiled sources per ported module, from Kbuild's <module>.mod lists.
    mod_src = {}
    with open(os.path.join(d, "modules.order")) as f:
        for line in f:
            o = line.strip()
            if not ported.search(o[:-2] + ".ko"):
                continue
            modfile = os.path.join(build, o[:-2] + ".mod")
            if not os.path.exists(modfile):
                continue
            srcs = []
            for obj in open(modfile).read().split():
                base = obj[:-2]
                for ext in (".c", ".S"):
                    if os.path.exists(os.path.join(src, base + ext)):
                        srcs.append(base + ext)
                        break
            mod_src[short(o[:-2])] = srcs
    with open(os.path.join(d, "drm-sources.txt"), "w") as f:
        for m in sorted(mod_src):
            for s in mod_src[m]:
                f.write("%s\t%s\n" % (m, s))

    # Headers that belong to the ported code: include/drm, uapi/drm, and
    # every .h under a directory holding a compiled ported source.
    src_dirs = set(os.path.dirname(s) for ss in mod_src.values() for s in ss)
    drm_headers = {}
    for top in ["include/drm", "include/uapi/drm"] + sorted(src_dirs):
        for dp, _, fns in os.walk(os.path.join(src, top)):
            for fn in fns:
                if fn.endswith(".h"):
                    rel = os.path.relpath(os.path.join(dp, fn), src)
                    drm_headers.setdefault(rel, set())
    for m, ss in mod_src.items():
        dirs = set(os.path.dirname(s) for s in ss)
        for h in drm_headers:
            if os.path.dirname(h) in dirs:
                drm_headers[h].add(m)

    users = collections.defaultdict(set)
    drm_defined = {}
    files = [(s, {m}) for m, ss in mod_src.items() for s in ss]
    files += [(h, ms or {"drm-headers"}) for h, ms in drm_headers.items()]
    for rel, ms in files:
        try:
            text = strip_code(open(os.path.join(src, rel), errors="replace").read())
        except OSError:
            continue
        if rel.endswith(".h"):
            index_header_file(os.path.join(src, rel), rel, drm_defined)
        else:
            for m in DEFINE_RE.finditer(text.replace("\\\n", " ")):
                drm_defined.setdefault(m.group(1), None)
        for ident in set(IDENT_RE.findall(text)):
            for m in ms:
                users[ident].add(m)

    idx = header_index(src, ["include", "arch/x86/include"],
                       skip=["include/drm", "include/uapi/drm", "include/generated",
                             "include/config"])
    rows = []
    for name, (kind, hdr, sig, body) in idx.items():
        if name not in users or name in drm_defined or SKIP_IDENT.match(name):
            continue
        rows.append((name, kind, hdr, sig, body, ",".join(sorted(users[name]))))
    rows.sort()
    with open(os.path.join(d, "headers-used.tsv"), "w") as f:
        f.write("name\tkind\theader\tsignature\tbody\tused_by\n")
        for r in rows:
            f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
    print("%s: %d header-level interfaces used by %d modules (%d sources)" % (
        os.path.basename(d), len(rows), len(mod_src),
        sum(len(s) for s in mod_src.values())), file=sys.stderr)


def read_headers(d):
    p = os.path.join(d, "headers-used.tsv")
    if not os.path.exists(p):
        return None
    rows = {}
    with open(p) as f:
        hdr = f.readline().rstrip("\n").split("\t")
        for line in f:
            r = dict(zip(hdr, line.rstrip("\n").split("\t")))
            rows[r["name"]] = r
    return rows


def header_section(f, da, db):
    va, vb = os.path.basename(da), os.path.basename(db)
    HA, HB = read_headers(da), read_headers(db)
    if HA is None or HB is None:
        f.write("## Header-level interfaces\n\nNot available for this pair "
                "(header pass not run for %s).\n\n" %
                " and ".join(v for v, h in ((va, HA), (vb, HB)) if h is None))
        return None
    added = sorted(set(HB) - set(HA))
    removed = sorted(set(HA) - set(HB))
    sig_a = {k: HA[k]["kind"] + HA[k]["signature"] for k in removed}
    sig_b = {k: HB[k]["kind"] + HB[k]["signature"] for k in added}
    # macro with >= 2 named parameters or an inline prototype is distinctive
    ren = find_renames(added, removed, sig_b, sig_a,
                       strong=lambda s: (s.startswith("macro(") and s.count(",") >= 1)
                       or (s.startswith("inline") and "," in s))
    rn_a = set(r for r, _, _, _ in ren)
    rn_b = set(a for _, a, _, _ in ren)
    added = [x for x in added if x not in rn_b]
    removed = [x for x in removed if x not in rn_a]
    common = sorted(set(HA) & set(HB))
    sigchg = [k for k in common if HA[k]["kind"] in ("macro", "inline")
              and HA[k]["signature"] != HB[k]["signature"]]
    bodychg = [k for k in common if HA[k]["kind"] == "macro"
               and HA[k]["signature"] == HB[k]["signature"]
               and HA[k]["body"] != HB[k]["body"]]
    moved = [k for k in common if HA[k]["header"] != HB[k]["header"]]

    f.write("## Header-level interfaces\n\n")
    f.write("Macros, static inline functions, struct/union/enum tags, typedefs "
            "and enumerators defined in non-DRM Linux headers (`include/`, "
            "`arch/x86/include/`) and named in the compiled DRM sources. These "
            "never appear as ELF symbols, but LinuxKPI has to provide them. "
            "Name-based, so a name can occasionally be a false positive (e.g. "
            "a struct member that happens to share a macro's name).\n\n")
    f.write("| | count |\n|---|---|\n")
    f.write("| used in %s | %d |\n| used in %s | %d |\n" % (va, len(HA), vb, len(HB)))
    f.write("| newly used | %d |\n| no longer used | %d |\n| likely renames | %d |\n"
            % (len(added), len(removed), len(ren)))
    f.write("| macro/inline signature changed | %d |\n| macro body changed | %d |\n"
            "| moved to another header | %d |\n\n" % (len(sigchg), len(bodychg), len(moved)))

    def htable(names, H):
        if not names:
            f.write("None.\n\n")
            return
        f.write("| name | kind | header | signature | used by |\n|---|---|---|---|---|\n")
        for k in names:
            r = H[k]
            f.write("| `%s` | %s | %s | %s | %s |\n" % (
                k, r["kind"], r["header"],
                ("`%s`" % md_escape(r["signature"])) if r["signature"] else "",
                r["used_by"]))
        f.write("\n")

    f.write("### Likely renames (header)\n\n")
    if ren:
        f.write("| %s | %s | kind | signature |\n|---|---|---|---|\n" % (va, vb))
        for r, a, sig, _ in ren:
            f.write("| `%s` (%s) | `%s` (%s) | %s | `%s` |\n" % (
                r, HA[r]["header"], a, HB[a]["header"], HB[a]["kind"],
                md_escape(HB[a]["signature"]) or "-"))
        f.write("\n")
    else:
        f.write("None.\n\n")
    f.write("### Newly used (header)\n\n")
    htable(added, HB)
    f.write("### No longer used (header)\n\n")
    htable(removed, HA)
    f.write("### Signature changed (header)\n\n")
    if sigchg:
        f.write("| name | kind | header | %s | %s |\n|---|---|---|---|---|\n" % (va, vb))
        for k in sigchg:
            f.write("| `%s` | %s | %s | `%s` | `%s` |\n" % (
                k, HB[k]["kind"], HB[k]["header"], md_escape(HA[k]["signature"]),
                md_escape(HB[k]["signature"])))
        f.write("\n")
    else:
        f.write("None.\n\n")
    if moved:
        f.write("### Moved to another header\n\n| name | %s | %s |\n|---|---|---|\n"
                % (va, vb))
        for k in moved:
            f.write("| `%s` | %s | %s |\n" % (k, HA[k]["header"], HB[k]["header"]))
        f.write("\n")
    if bodychg:
        f.write("<details><summary>Macro body changed (%d)</summary>\n\n" % len(bodychg))
        f.write("| macro | header | %s | %s |\n|---|---|---|---|\n" % (va, vb))
        for k in bodychg:
            f.write("| `%s` | %s | `%s` | `%s` |\n" % (
                k, HB[k]["header"], md_escape(HA[k]["body"][:200]),
                md_escape(HB[k]["body"][:200])))
        f.write("\n</details>\n\n")
    return {"added": len(added), "removed": len(removed), "renames": len(ren),
            "sigchg": len(sigchg)}


# ------------------------------------------------------------------- pair
def abi_info(abidir):
    """symbol -> defining source file, from the abidw XMLs of a version."""
    info = {}
    xmls = []
    for root, _, files in os.walk(abidir):
        xmls += [os.path.join(root, f) for f in files if f.endswith(".xml")]
    for xml_path in sorted(xmls):
        _abi_info_one(xml_path, info)
    return info


def _abi_info_one(xml_path, info):
    for _, el in ET.iterparse(xml_path, events=("end",)):
        if el.tag in ("function-decl", "var-decl"):
            sym = el.get("elf-symbol-id")
            if sym:
                sym = sym.split("@")[0]
                info.setdefault(sym, norm_path(el.get("filepath")))
            if el.tag == "function-decl":
                el.clear()


IMPACT_RE = re.compile(r"^(\s+)(\d+|one) impacted interfaces?:?$")
TYPE_RE = re.compile(r"^'(.+?)(?: at (\S+))?' changed:$")
DIRECT_RE = re.compile(r"^  \[([CDA])\] (.*)$")


def parse_leaf(path):
    """Parse an abidiff --leaf-changes-only --impacted-interfaces report made
    of '==== <binary> ====' sections.

    Returns (direct, types):
      direct: list of dicts {binary, op, head, detail, n_impacted}
              -- functions/variables whose own declaration changed
      types:  list of dicts {binary, type, loc, detail, impacted}
              -- each changed leaf type once, with the used interfaces it
                 reaches
    Impacted-interface lists are stripped from 'detail'."""
    direct, types = [], []
    if not os.path.exists(path):
        return direct, types
    with open(path, errors="replace") as f:
        lines = f.read().splitlines()
    binary = "?"
    cur = None
    in_impact = None      # indentation of the "N impacted" header
    for l in lines:
        if l.startswith("==== ") and l.endswith(" ===="):
            binary, cur, in_impact = l[5:-5], None, None
            continue
        if in_impact is not None:
            if l.strip() and len(l) - len(l.lstrip()) > in_impact:
                if cur is not None and "impacted" in cur and \
                        l.strip() not in cur["impacted_set"]:
                    cur["impacted"].append(l.strip())
                    cur["impacted_set"].add(l.strip())
                continue
            in_impact = None
        m = TYPE_RE.match(l)
        if m:
            cur = {"binary": binary, "type": m.group(1),
                   "loc": m.group(2) or "", "detail": [], "impacted": [],
                   "impacted_set": set()}
            types.append(cur)
            continue
        m = DIRECT_RE.match(l)
        if m:
            cur = {"binary": binary, "op": m.group(1), "head": m.group(2),
                   "detail": [], "n_impacted": 0}
            direct.append(cur)
            continue
        m = IMPACT_RE.match(l)
        if m and cur is not None:
            in_impact = len(m.group(1))
            n = 1 if m.group(2) == "one" else int(m.group(2))
            cur["n_impacted"] = max(cur.get("n_impacted", 0), n)
            continue
        if cur is None or not l.strip():
            continue
        if not l.startswith(" "):     # section headings, summaries
            cur = None
            continue
        cur["detail"].append(l)
    # "details were reported earlier" duplicates carry no new information
    types = [t for t in types if not (len(t["detail"]) == 1 and
             "reported earlier" in t["detail"][0])]
    # The same type shows up once per binary (vmlinux and each module);
    # merge, keeping the longest detail and the union of impacted interfaces.
    merged = {}
    for t in types:
        m = merged.get(t["type"])
        if m is None:
            merged[t["type"]] = dict(t, impacted=list(t["impacted"]),
                                     binaries=[t["binary"]])
            continue
        m["binaries"].append(t["binary"])
        if len(t["detail"]) > len(m["detail"]):
            m["detail"], m["loc"] = t["detail"], t["loc"]
        seen = set(m["impacted"])
        m["impacted"] += [i for i in t["impacted"] if i not in seen]
    return direct, list(merged.values())


def type_summary(detail):
    """One-line summary from the top-level lines of a type's detail."""
    top = [x.strip() for x in detail if len(x) - len(x.lstrip()) == 2]
    top = [x for x in top if x != "type size hasn't changed"]
    if not top:   # only nested detail, e.g. a change inside an anonymous member
        top = [x.strip() for x in detail[:3]]
    s = "; ".join(x.rstrip(":") for x in top)
    return s if len(s) < 300 else s[:297] + "..."


def md_escape(s):
    return s.replace("|", "\\|")


def cmd_pair(da, db, out):
    va, vb = os.path.basename(da), os.path.basename(db)
    A = read_tsv(os.path.join(da, "imports.tsv"))
    B = read_tsv(os.path.join(db, "imports.tsv"))
    ia = abi_info(os.path.join(da, "abi"))
    ib = abi_info(os.path.join(db, "abi"))
    added = sorted(set(B) - set(A))
    removed = sorted(set(A) - set(B))
    common = sorted(set(A) & set(B))
    exp_chg = [s for s in common
               if (A[s]["exporter"], A[s]["export"], A[s]["namespace"]) !=
                  (B[s]["exporter"], B[s]["export"], B[s]["namespace"])]
    newusers = [s for s in common if A[s]["used_by"] != B[s]["used_by"]]
    direct, types = parse_leaf(os.path.join(out, "abidiff-leaf.txt"))

    # Renames: a dropped and a newly used symbol with identical signature
    # (parameter types and names) and a similar name.
    sig_a = abi_signatures(os.path.join(da, "abi"))
    sig_b = abi_signatures(os.path.join(db, "abi"))
    renames = find_renames(added, removed, sig_b, sig_a,
                           strong=lambda s: s.count(",") >= 1)
    rn_old = set(r for r, _, _, _ in renames)
    rn_new = set(a for _, a, _, _ in renames)
    added = [x for x in added if x not in rn_new]
    removed = [x for x in removed if x not in rn_old]

    # interface -> changed types reaching it
    reach = collections.defaultdict(set)
    for t in types:
        for i in t["impacted"]:
            reach[i].add(t["type"])
    with open(os.path.join(out, "impacted.tsv"), "w") as f:
        f.write("interface\tn_changed_types\tchanged_types\n")
        for i in sorted(reach, key=lambda k: (-len(reach[k]), k)):
            f.write("%s\t%d\t%s\n" % (i, len(reach[i]), ", ".join(sorted(reach[i]))))

    def table(syms, rows, info, f):
        if not syms:
            f.write("None.\n\n")
            return
        f.write("| symbol | kind | exporter | export | defined in | used by |\n")
        f.write("|---|---|---|---|---|---|\n")
        for s in syms:
            r = rows[s]
            exp = r["export"].replace("EXPORT_SYMBOL", "").lstrip("_") or "plain"
            if r["namespace"]:
                exp += " ns=" + r["namespace"]
            f.write("| `%s` | %s | %s | %s | %s | %s |\n" % (
                s, r["kind"], r["exporter"], exp, info.get(s, ""), r["used_by"]))
        f.write("\n")

    with open(os.path.join(out, "report.md"), "w") as f:
        f.write("# Kernel interfaces used by DRM: %s → %s\n\n" % (va, vb))
        f.write("| | count |\n|---|---|\n")
        f.write("| interfaces used in %s | %d |\n" % (va, len(A)))
        f.write("| interfaces used in %s | %d |\n" % (vb, len(B)))
        f.write("| likely renames | %d |\n" % len(renames))
        f.write("| newly used (excluding renames) | %d |\n" % len(added))
        f.write("| no longer used (excluding renames) | %d |\n" % len(removed))
        f.write("| export kind/owner/namespace changed | %d |\n" % len(exp_chg))
        f.write("| used in both, own declaration changed | %d |\n" % len(direct))
        f.write("| changed types reachable from used interfaces | %d |\n" % len(types))
        f.write("| used interfaces reaching at least one changed type | %d |\n\n" % len(reach))

        f.write("## Likely renames\n\n")
        if renames:
            f.write("Dropped and newly used symbols with identical signatures "
                    "(types and parameter names) and similar names.\n\n")
            f.write("| %s | %s | signature | used by |\n|---|---|---|---|\n" % (va, vb))
            for r, a, sig, _ in renames:
                f.write("| `%s` | `%s` | `%s` | %s |\n" % (
                    r, a, md_escape(sig), B[a]["used_by"]))
            f.write("\n")
        else:
            f.write("None.\n\n")
        f.write("## Newly used in %s\n\n" % vb)
        table(added, B, ib, f)
        f.write("## No longer used in %s\n\n" % vb)
        table(removed, A, ia, f)
        if exp_chg:
            f.write("## Export changes\n\n| symbol | %s | %s |\n|---|---|---|\n" % (va, vb))
            for s in exp_chg:
                fa = "%s %s %s" % (A[s]["exporter"], A[s]["export"], A[s]["namespace"])
                fb = "%s %s %s" % (B[s]["exporter"], B[s]["export"], B[s]["namespace"])
                f.write("| `%s` | %s | %s |\n" % (s, fa.strip(), fb.strip()))
            f.write("\n")

        f.write("## Interfaces whose own declaration changed\n\n")
        f.write("Return/parameter types, variable types, or interfaces that "
                "lost their debug info. `[C]` changed, `[D]` deleted.\n\n")
        if direct:
            for d in direct:
                f.write("**[%s] %s** (%s)\n\n" % (d["op"], md_escape(d["head"]),
                                                 d["binary"]))
                if d["detail"]:
                    f.write("```\n%s\n```\n\n" % "\n".join(d["detail"][:60]))
                if d.get("n_impacted"):
                    f.write("Reaches %d used interfaces.\n\n" % d["n_impacted"])
        else:
            f.write("None.\n\n")

        f.write("## Changed types\n\n")
        f.write("Each type that changed and is reachable from an interface DRM "
                "uses, with the number of used interfaces it reaches, fewest "
                "first: low counts are targeted changes, high counts are "
                "churn reached via hub types "
                "(reachability is transitive through pointers, so e.g. "
                "`struct device` or `struct module` pull in hundreds). "
                "Per-interface index: `impacted.tsv`; raw report: "
                "`abidiff-leaf.txt`.\n\n")
        if types:
            f.write("| type | declared at | change | used interfaces reached |\n")
            f.write("|---|---|---|---|\n")
            types.sort(key=lambda t: (len(t["impacted"]), t["type"]))
            for t in types:
                f.write("| `%s` | %s | %s | %d |\n" % (
                    md_escape(t["type"]), t["loc"],
                    md_escape(type_summary(t["detail"])), len(t["impacted"])))
            f.write("\n### Details\n\n")
            for t in types:
                imp = t["impacted"]
                f.write("<details><summary><code>%s</code> (%s)</summary>\n\n"
                        "```\n%s\n```\n\n" % (t["type"], t["loc"],
                                             "\n".join(t["detail"][:40]) +
                                             ("\n  ..." if len(t["detail"]) > 40 else "")))
                if imp:
                    f.write("Reaches: %s%s\n\n" % (
                        ", ".join("`%s`" % md_escape(x) for x in imp[:15]),
                        " … (+%d more, see impacted.tsv)" % (len(imp) - 15)
                        if len(imp) > 15 else ""))
                f.write("</details>\n\n")
        else:
            f.write("None.\n\n")

        hs = header_section(f, da, db)

        if newusers:
            f.write("## Same interface, different set of DRM users\n\n")
            f.write("| symbol | %s | %s |\n|---|---|---|\n" % (va, vb))
            for s in newusers:
                f.write("| `%s` | %s | %s |\n" % (s, A[s]["used_by"], B[s]["used_by"]))
            f.write("\n")
    print("%s..%s: +%d -%d used, %d renames, %d export changes, %d declaration "
          "changes, %d changed types%s" % (
              va, vb, len(added), len(removed), len(renames), len(exp_chg),
              len(direct), len(types),
              "; headers: +%(added)d -%(removed)d, %(renames)d renames, "
              "%(sigchg)d signature changes" % hs if hs else ""),
          file=sys.stderr)


# ---------------------------------------------------------------- summary
def cmd_summary(outdir, vers):
    tables = {v: read_tsv(os.path.join(outdir, v, "imports.tsv")) for v in vers}
    info = {}
    for v in vers:
        for s, p in abi_info(os.path.join(outdir, v, "abi")).items():
            info[s] = p
    allsyms = sorted(set().union(*[set(t) for t in tables.values()]))
    with open(os.path.join(outdir, "matrix.tsv"), "w") as f:
        f.write("\t".join(["symbol", "kind", "exporter", "defined_in"] + vers +
                          ["used_by_latest"]) + "\n")
        for s in allsyms:
            last = next(tables[v][s] for v in reversed(vers) if s in tables[v])
            f.write("\t".join([s, last["kind"], last["exporter"], info.get(s, "")] +
                              ["x" if s in tables[v] else "" for v in vers] +
                              [last["used_by"]]) + "\n")
    with open(os.path.join(outdir, "summary.md"), "w") as f:
        f.write("# DRM → kernel interface usage, %s … %s\n\n" % (vers[0], vers[-1]))
        f.write("| version | interfaces used |\n|---|---|\n")
        for v in vers:
            f.write("| %s | %d |\n" % (v, len(tables[v])))
        f.write("\nSymbol-level counts include renames; see each report.\n\n")
        f.write("| step | newly used | no longer used | declaration changed "
                "| changed types | header: newly / no longer used | report |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for a, b in zip(vers, vers[1:]):
            d = "diff-%s..%s" % (a, b)
            direct, types = parse_leaf(os.path.join(outdir, d, "abidiff-leaf.txt"))
            ha = read_headers(os.path.join(outdir, a))
            hb = read_headers(os.path.join(outdir, b))
            hcol = ("%d / %d" % (len(set(hb) - set(ha)), len(set(ha) - set(hb)))
                    if ha is not None and hb is not None else "n/a")
            f.write("| %s → %s | %d | %d | %d | %d | %s | %s/report.md |\n" % (
                a, b, len(set(tables[b]) - set(tables[a])),
                len(set(tables[a]) - set(tables[b])), len(direct), len(types),
                hcol, d))
        new = sorted(set(tables[vers[-1]]) - set(tables[vers[0]]))
        f.write("\n## Used in %s but not in %s (%d)\n\n" % (vers[-1], vers[0], len(new)))
        f.write("| symbol | first used | exporter | defined in | used by |\n|---|---|---|---|---|\n")
        for s in new:
            first = next(v for v in vers if s in tables[v])
            r = tables[vers[-1]][s]
            f.write("| `%s` | %s | %s | %s | %s |\n" % (
                s, first, r["exporter"], info.get(s, ""), r["used_by"]))


def main():
    cmd = sys.argv[1]
    if cmd == "imports":
        cmd_imports(sys.argv[2], sys.argv[3])
    elif cmd == "pair":
        cmd_pair(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "headers":
        cmd_headers(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif cmd == "summary":
        cmd_summary(sys.argv[2], sys.argv[3:])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
