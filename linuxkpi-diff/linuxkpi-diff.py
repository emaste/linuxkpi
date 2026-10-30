#!/usr/bin/env python3
"""Helper for linuxkpi-diff.sh.

  linuxkpi-diff.py g0dirs  <groups.conf> <srctree>
  linuxkpi-diff.py imports <verdir> <buildtree> <groups.conf>
  linuxkpi-diff.py headers <verdir> <srctree> <buildtree> <groups.conf>
  linuxkpi-diff.py pair    <verdir_a> <verdir_b> <outdir> <groups.conf>
  linuxkpi-diff.py summary <outdir> <groups.conf> <ver>...

"Consumers" are Linux modules/headers that FreeBSD carries itself on top of
LinuxKPI, assigned to hierarchical groups by groups.conf.  "Providers" are
everything else: what LinuxKPI has to supply.
"""
import collections
import difflib
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

FUNC_TYPES = set("TtWwi")
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


def md_escape(s):
    return s.replace("|", "\\|")


# ----------------------------------------------------------------- groups
class Groups:
    """groups.conf: '<group> <prefix>... [!<prefix>...]' per line."""

    def __init__(self, path):
        self.incl = []                       # (prefix, group)
        self.excl = collections.defaultdict(list)
        self.order = []
        with open(path) as f:
            for line in f:
                line = line.split("#", 1)[0].split()
                if not line:
                    continue
                g, prefixes = line[0], line[1:]
                if g not in self.order:
                    self.order.append(g)
                for p in prefixes:
                    if p.startswith("!"):
                        self.excl[g].append(p[1:])
                    else:
                        self.incl.append((p, g))

    def classify(self, path):
        """Group of a source/build path (longest matching prefix), or None."""
        best, blen = None, -1
        for p, g in self.incl:
            if path.startswith(p) and len(p) > blen and \
                    not any(path.startswith(x) for x in self.excl[g]):
                best, blen = g, len(p)
        return best

    def all_nodes(self):
        """Leaf groups and their ancestors, parents before children."""
        nodes = []
        for g in self.order:
            parts = g.split("/")
            for i in range(1, len(parts) + 1):
                n = "/".join(parts[:i])
                if n not in nodes:
                    nodes.append(n)
        top = [n for n in nodes if "/" not in n]
        out = []
        for t in top:
            out.append(t)
            out += [n for n in nodes if n.startswith(t + "/")]
        return out

    @staticmethod
    def covers(node, group):
        return group == node or group.startswith(node + "/")


def split_list(s):
    return [x for x in s.split(",") if x] if s else []


def read_rows(path, key):
    rows = {}
    if not os.path.exists(path):
        return None
    with open(path) as f:
        hdr = f.readline().rstrip("\n").split("\t")
        for line in f:
            r = dict(zip(hdr, line.rstrip("\n").split("\t")))
            rows[r[key]] = r
    return rows


def read_modgroups(d):
    """module short name -> group, for the consumer modules of a version."""
    res = {}
    p = os.path.join(d, "modules-groups.tsv")
    if os.path.exists(p):
        with open(p) as f:
            next(f)
            for line in f:
                m, path, g = line.rstrip("\n").split("\t")
                res[m] = g
    return res


# ----------------------------------------------------------------- g0dirs
def cmd_g0dirs(gconf, src):
    G = Groups(gconf)
    seen = set()
    for p, _ in G.incl:
        p = p.rstrip("/")
        if p not in seen and not p.startswith("include/") and \
                os.path.exists(os.path.join(src, p, "Makefile")):
            seen.add(p)
            print(p)


# ---------------------------------------------------------------- imports
def nm(args, path):
    return subprocess.run(["nm"] + args + [path], check=True, text=True,
                          capture_output=True).stdout.splitlines()


def cmd_imports(d, build, gconf):
    G = Groups(gconf)
    symvers = {}
    with open(os.path.join(d, "Module.symvers")) as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) >= 4:
                symvers[p[1]] = (p[2], p[3], p[4] if len(p) > 4 else "")

    kinds = {}
    with open(os.path.join(d, "System.map")) as f:
        for line in f:
            p = line.split()
            if len(p) == 3:
                kinds.setdefault(p[2], p[1])

    with open(os.path.join(d, "ported-builtin-syms.txt")) as f:
        ported_builtin = set(l.strip() for l in f if l.strip())

    consumers = {}       # module path -> group
    undef = []
    with open(os.path.join(d, "modules.order")) as f:
        mods = [l.strip()[:-2] for l in f if l.strip()]
    for m in mods:
        ko = os.path.join(build, m + ".ko")
        g = G.classify(m)
        if g:
            consumers[m] = g
            for line in nm(["-u"], ko):
                undef.append((m, line.split()[-1]))
        else:
            for line in nm(["--defined-only"], ko):
                p = line.split()
                if len(p) == 3:
                    kinds.setdefault(p[2], p[1])

    with open(os.path.join(d, "modules-groups.tsv"), "w") as f:
        f.write("module\tpath\tgroup\n")
        for m in sorted(consumers, key=lambda m: (consumers[m], m)):
            f.write("%s\t%s\t%s\n" % (short(m), m, consumers[m]))

    users = collections.defaultdict(set)
    for m, sym in undef:
        exp = symvers.get(sym)
        if exp is not None:
            if exp[0] in consumers:
                continue              # provided by carried code itself
            if exp[0] == "vmlinux" and sym in ported_builtin:
                continue
        users[sym].add(m)

    with open(os.path.join(d, "imports.tsv"), "w") as out, \
         open(os.path.join(d, "symbols.list"), "w") as wl:
        out.write("symbol\tkind\texporter\texport\tnamespace\tused_by\tgroups\n")
        # libabigail 2.4 only honours this section name
        wl.write("[abi_whitelist]\n")
        for sym in sorted(users):
            exp = symvers.get(sym, ("UNRESOLVED", "", ""))
            t = kinds.get(sym, "?")
            kind = "func" if t in FUNC_TYPES else ("?" if t == "?" else "data")
            us = sorted(users[sym])
            out.write("\t".join([sym, kind, exp[0], exp[1], exp[2],
                                 ",".join(short(m) for m in us),
                                 ",".join(sorted(set(consumers[m] for m in us)))])
                      + "\n")
            if exp[0] != "UNRESOLVED":
                wl.write("  %s\n" % sym)
    per = collections.Counter(g for m, g in consumers.items())
    print("%s: %d provider interfaces imported by %d consumer modules (%s)" % (
        os.path.basename(d), len(users), len(consumers),
        ", ".join("%s:%d" % kv for kv in sorted(per.items()))), file=sys.stderr)


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


def abi_scan(abidir):
    """From the abidw XMLs of a version: symbol -> defining source file, and
    symbol -> normalized signature (types + parameter names; comparable
    across versions, unlike type-ids)."""
    files, sigs = {}, {}
    xmls = []
    for root, _, fns in os.walk(abidir):
        xmls += [os.path.join(root, f) for f in fns if f.endswith(".xml")]
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
                files.setdefault(sym, norm_path(el.get("filepath")))
                ps = ["%s %s" % (_render(p.get("type-id"), types), p.get("name") or "")
                      for p in el.findall("parameter")]
                r = el.find("return")
                sigs.setdefault(sym, "%s(%s)" % (
                    _render(r.get("type-id"), types) if r is not None else "?",
                    ", ".join(p.strip() for p in ps)))
            elif el.tag == "var-decl":
                files.setdefault(sym, norm_path(el.get("filepath")))
                sigs.setdefault(sym, _render(el.get("type-id"), types))
    return files, sigs


def name_similarity(a, b):
    ta, tb = set(a.lower().strip("_").split("_")), set(b.lower().strip("_").split("_"))
    jac = len(ta & tb) / max(1, len(ta | tb))
    return max(jac, difflib.SequenceMatcher(None, a, b).ratio())


def find_renames(added, removed, sig_new, sig_old, strong=lambda s: False,
                 min_sim=lambda s: 0.5):
    """Pair added/removed names with identical signatures, if the names are
    similar or the signature is distinctive on its own (strong(sig)).  Each
    name is used at most once, best match first."""
    cands = []
    for a in added:
        sa = sig_new.get(a)
        if not sa:
            continue
        for r in removed:
            if sig_old.get(r) != sa:
                continue
            sim = name_similarity(a, r)
            if sim >= min_sim(sa) or strong(sa):
                cands.append((sim, r, a))
    cands.sort(reverse=True)
    used_a, used_r, res = set(), set(), []
    for sim, r, a in cands:
        if a in used_a or r in used_r:
            continue
        used_a.add(a)
        used_r.add(r)
        res.append((r, a, sig_new[a]))
    return sorted(res)


# ---------------------------------------------------------------- headers
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
        if re.search(r"_H_*$", name):
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


def cmd_deps(build, src, obj):
    """Source-relative headers an object was compiled against (Kbuild .cmd)."""
    d, b = os.path.split(obj)
    p = os.path.join(build, d, "." + b + ".cmd")
    res = []
    try:
        text = open(p, errors="replace").read()
    except OSError:
        return res
    m = re.search(r"^deps_\S+ := (.*?)(?:\n\n|\n\S)", text, re.S | re.M)
    if not m:
        return res
    # Kbuild records the resolved source path; the caller's may be a symlink.
    roots = sorted(set([os.path.realpath(src) + "/", os.path.abspath(src) + "/"]),
                   key=len, reverse=True)
    for tok in m.group(1).replace("\\\n", " ").split():
        if not tok.endswith(".h") or tok.startswith("$("):
            continue
        root = next((r for r in roots if tok.startswith(r)), None)
        if root:
            res.append(tok[len(root):])
        elif not tok.startswith("/"):
            res.append(tok)          # build-tree generated header
    return res


def cmd_headers(d, src, build, gconf):
    """Header-level interfaces (macros, static inlines, struct/union/enum
    tags, typedefs, enumerators) defined in provider headers -- headers the
    consumer objects were compiled against that are not consumer-owned --
    and named in consumer code."""
    G = Groups(gconf)
    modgroups = {}
    with open(os.path.join(d, "modules-groups.tsv")) as f:
        next(f)
        for line in f:
            m, path, g = line.rstrip("\n").split("\t")
            modgroups[path] = g

    # Compiled sources per consumer module (Kbuild <module>.mod lists) and
    # the headers each object was compiled against (.cmd deps).
    srcs = []                                 # (relpath, module)
    hdr_users = collections.defaultdict(set)  # header -> modules
    for path in modgroups:
        modfile = os.path.join(build, path + ".mod")
        if not os.path.exists(modfile):
            continue
        for obj in open(modfile).read().split():
            base = obj[:-2]
            for ext in (".c", ".S"):
                if os.path.exists(os.path.join(src, base + ext)):
                    srcs.append((base + ext, short(path)))
                    break
            for h in cmd_deps(build, src, obj):
                hdr_users[h].add(short(path))
    with open(os.path.join(d, "consumer-sources.txt"), "w") as f:
        for s, m in sorted(srcs, key=lambda x: (x[1], x[0])):
            f.write("%s\t%s\n" % (m, s))

    consumer_hdrs = {h: ms for h, ms in hdr_users.items() if G.classify(h)}
    provider_hdrs = sorted(h for h in hdr_users
                           if not G.classify(h) and os.path.exists(os.path.join(src, h)))

    users = collections.defaultdict(set)
    consumer_defined = {}
    files = [(s, {m}) for s, m in srcs] + list(consumer_hdrs.items())
    for rel, ms in files:
        try:
            text = strip_code(open(os.path.join(src, rel), errors="replace").read())
        except OSError:
            continue
        if rel.endswith(".h"):
            index_header_file(os.path.join(src, rel), rel, consumer_defined)
        else:
            for m in DEFINE_RE.finditer(text.replace("\\\n", " ")):
                consumer_defined.setdefault(m.group(1), None)
        for ident in set(IDENT_RE.findall(text)):
            users[ident] |= ms

    idx = {}
    for h in provider_hdrs:
        index_header_file(os.path.join(src, h), h, idx)
    mod2group = {short(p): g for p, g in modgroups.items()}
    rows = []
    for name, (kind, hdr, sig, body) in idx.items():
        if name not in users or name in consumer_defined or SKIP_IDENT.match(name):
            continue
        us = sorted(users[name])
        rows.append((name, kind, hdr, sig, body, ",".join(us),
                     ",".join(sorted(set(mod2group[m] for m in us)))))
    rows.sort()
    with open(os.path.join(d, "headers-used.tsv"), "w") as f:
        f.write("name\tkind\theader\tsignature\tbody\tused_by\tgroups\n")
        for r in rows:
            f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
    print("%s: %d header-level interfaces from %d provider headers, %d consumer "
          "sources" % (os.path.basename(d), len(rows), len(provider_hdrs), len(srcs)),
          file=sys.stderr)


# --------------------------------------------------------- abidiff parse
IMPACT_RE = re.compile(r"^(\s+)(\d+|one) impacted interfaces?:?$")
TYPE_RE = re.compile(r"^'(.+?)(?: at (\S+))?' changed:$")
DIRECT_RE = re.compile(r"^  \[([CDA])\] (.*)$")


def parse_leaf(path):
    """Parse 'abidiff --leaf-changes-only --impacted-interfaces' output made
    of '==== <binary> ====' sections.  Returns (direct, types):
      direct: interfaces whose own declaration changed
      types:  each changed type once (merged across binaries) with the used
              interfaces it reaches.  Impacted lists are stripped from
              'detail'."""
    direct, types = [], []
    if not os.path.exists(path):
        return direct, types
    with open(path, errors="replace") as f:
        lines = f.read().splitlines()
    binary, cur, in_impact = "?", None, None
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
            cur = {"binary": binary, "type": m.group(1), "loc": m.group(2) or "",
                   "detail": [], "impacted": [], "impacted_set": set()}
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
        if not l.startswith(" "):
            cur = None
            continue
        cur["detail"].append(l)
    types = [t for t in types if not (len(t["detail"]) == 1 and
             "reported earlier" in t["detail"][0])]
    merged = {}
    for t in types:
        m = merged.get(t["type"])
        if m is None:
            merged[t["type"]] = dict(t, impacted=list(t["impacted"]))
            continue
        if len(t["detail"]) > len(m["detail"]):
            m["detail"], m["loc"] = t["detail"], t["loc"]
        seen = set(m["impacted"])
        m["impacted"] += [i for i in t["impacted"] if i not in seen]
    return direct, list(merged.values())


def iface_name(s):
    """Symbol name from an abidiff interface string such as
    "function dma_buf* dma_buf_get(int)", "'function void f(x*)' at ...",
    "const dma_fence_ops dma_fence_array_ops" or "[D] phys_base"."""
    s = s.strip().strip("'")
    m = re.match(r"^'?(function|variable)?\s*(.*?)'?(?: at \S+.*| was changed.*| has .*|"
                 r"\s+\{.*\})?:?$", s)
    body = m.group(2) if m else s
    if s.startswith("function") or (m and m.group(1) == "function"):
        m2 = re.search(r"(\w+)\s*\(", body)
        return m2.group(1) if m2 else body
    ids = re.findall(r"\w+", body)
    return ids[-1] if ids else body


def type_summary(detail):
    top = [x.strip() for x in detail if len(x) - len(x.lstrip()) == 2]
    top = [x for x in top if x != "type size hasn't changed"]
    if not top:
        top = [x.strip() for x in detail[:3]]
    s = "; ".join(x.rstrip(":") for x in top)
    return s if len(s) < 300 else s[:297] + "..."


# ------------------------------------------------------------------- pair
class PairData:
    """Everything for one version pair; reports are views filtered by group."""

    def __init__(self, da, db, out):
        self.va, self.vb = os.path.basename(da), os.path.basename(db)
        self.A = read_rows(os.path.join(da, "imports.tsv"), "symbol")
        self.B = read_rows(os.path.join(db, "imports.tsv"), "symbol")
        self.fa, sa = abi_scan(os.path.join(da, "abi"))
        self.fb, sb = abi_scan(os.path.join(db, "abi"))
        added = sorted(set(self.B) - set(self.A))
        removed = sorted(set(self.A) - set(self.B))
        self.renames = find_renames(added, removed, sb, sa,
                                    strong=lambda s: s.count(",") >= 1)
        rn_old = set(r for r, _, _ in self.renames)
        rn_new = set(a for _, a, _ in self.renames)
        self.added = [x for x in added if x not in rn_new]
        self.removed = [x for x in removed if x not in rn_old]
        common = sorted(set(self.A) & set(self.B))
        self.common = common
        self.exp_chg = [s for s in common
                        if (self.A[s]["exporter"], self.A[s]["export"], self.A[s]["namespace"]) !=
                           (self.B[s]["exporter"], self.B[s]["export"], self.B[s]["namespace"])]
        self.direct, self.types = parse_leaf(os.path.join(out, "abidiff-leaf.txt"))

        self.HA = read_rows(os.path.join(da, "headers-used.tsv"), "name")
        self.HB = read_rows(os.path.join(db, "headers-used.tsv"), "name")
        self.hdr = None
        if self.HA is not None and self.HB is not None:
            HA, HB = self.HA, self.HB
            hadd = sorted(set(HB) - set(HA))
            hrem = sorted(set(HA) - set(HB))
            # Without parameters a "signature" says little: object-like
            # macros must also have the same body, and tags/typedefs/
            # enumerators need clearly similar names.
            def hsig(H, k):
                r = H[k]
                if r["kind"] == "macro" and not r["signature"]:
                    return "macro=" + r["body"]
                return r["kind"] + r["signature"]
            sig_a = {k: hsig(HA, k) for k in hrem}
            sig_b = {k: hsig(HB, k) for k in hadd}
            ren = find_renames(hadd, hrem, sig_b, sig_a,
                               strong=lambda s: (s.startswith("macro(") and "," in s)
                               or (s.startswith("inline") and "," in s),
                               min_sim=lambda s: 0.5 if "(" in s or "=" in s else 0.8)
            ra = set(r for r, _, _ in ren)
            rb = set(a for _, a, _ in ren)
            hc = sorted(set(HA) & set(HB))
            self.hdr = {
                "added": [x for x in hadd if x not in rb],
                "removed": [x for x in hrem if x not in ra],
                "renames": ren,
                "sigchg": [k for k in hc if HA[k]["kind"] in ("macro", "inline")
                           and HA[k]["signature"] != HB[k]["signature"]],
                "bodychg": [k for k in hc if HA[k]["kind"] == "macro"
                            and HA[k]["signature"] == HB[k]["signature"]
                            and HA[k]["body"] != HB[k]["body"]],
                "moved": [k for k in hc if HA[k]["header"] != HB[k]["header"]],
            }

    # --- filtering --------------------------------------------------
    @staticmethod
    def _in(row, node):
        return node is None or any(Groups.covers(node, g)
                                   for g in split_list(row.get("groups", "")))

    def sym_set(self, node):
        s = set(k for k, r in self.A.items() if self._in(r, node))
        s |= set(k for k, r in self.B.items() if self._in(r, node))
        return s

    def view(self, node):
        """Counts and filtered lists for a group node (None = everything)."""
        A, B = self.A, self.B
        syms = self.sym_set(node)
        v = {
            "used_a": sum(1 for r in A.values() if self._in(r, node)),
            "used_b": sum(1 for r in B.values() if self._in(r, node)),
            "added": [s for s in self.added if self._in(B[s], node)],
            "removed": [s for s in self.removed if self._in(A[s], node)],
            "renames": [x for x in self.renames if self._in(B[x[1]], node)],
            "exp_chg": [s for s in self.exp_chg if s in syms],
            "direct": [d for d in self.direct if iface_name(d["head"]) in syms],
        }
        types = []
        for t in self.types:
            imp = [i for i in t["impacted"] if iface_name(i) in syms]
            if imp:
                types.append(dict(t, impacted=imp))
        types.sort(key=lambda t: (len(t["impacted"]), t["type"]))
        v["types"] = types
        v["newusers"] = [s for s in self.common if s in syms and
                         A[s]["used_by"] != B[s]["used_by"]]
        if self.hdr is not None:
            HA, HB, h = self.HA, self.HB, self.hdr
            v["hdr"] = {
                "used_a": sum(1 for r in HA.values() if self._in(r, node)),
                "used_b": sum(1 for r in HB.values() if self._in(r, node)),
                "added": [k for k in h["added"] if self._in(HB[k], node)],
                "removed": [k for k in h["removed"] if self._in(HA[k], node)],
                "renames": [x for x in h["renames"] if self._in(HB[x[1]], node)],
                "sigchg": [k for k in h["sigchg"] if self._in(HB[k], node)],
                "bodychg": [k for k in h["bodychg"] if self._in(HB[k], node)],
                "moved": [k for k in h["moved"] if self._in(HB[k], node)],
            }
        else:
            v["hdr"] = None
        return v


def counts_row(v):
    h = v["hdr"]
    hcols = ("%d | %d | %d | %d" % (len(h["added"]), len(h["removed"]),
                                    len(h["renames"]), len(h["sigchg"]))
             if h else "n/a | n/a | n/a | n/a")
    return "%d | %d | %d | %d | %d | %d | %s" % (
        v["used_b"], len(v["added"]), len(v["removed"]), len(v["renames"]),
        len(v["direct"]), len(v["types"]), hcols)


COUNTS_HDR = ("| group | used | newly used | no longer used | renames | "
              "declaration changed | changed types | hdr: newly used | "
              "hdr: no longer used | hdr: renames | hdr: signature changed |\n"
              "|---|---|---|---|---|---|---|---|---|---|---|\n")


def group_file(node):
    return node.replace("/", "-") + ".md"


def write_report(P, v, path, title, node, G=None, overview=None):
    va, vb, A, B = P.va, P.vb, P.A, P.B

    def table(syms, rows, files):
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
                s, r["kind"], r["exporter"], exp, files.get(s, ""), r["used_by"]))
        f.write("\n")

    with open(path, "w") as f:
        f.write("# %s: %s → %s\n\n" % (title, va, vb))
        if overview:
            f.write("## Overview by group\n\n")
            f.write("Interface counts per consumer group (parents include "
                    "their children). Per-group reports are in `groups/`.\n\n")
            f.write(COUNTS_HDR)
            for n, nv in overview:
                ind = "&nbsp;&nbsp;" * n.count("/")
                f.write("| %s[%s](groups/%s) | %s |\n" % (ind, n, group_file(n),
                                                        counts_row(nv)))
            f.write("\n")

        f.write("## Symbol-level summary\n\n| | count |\n|---|---|\n")
        f.write("| interfaces used in %s | %d |\n" % (va, v["used_a"]))
        f.write("| interfaces used in %s | %d |\n" % (vb, v["used_b"]))
        f.write("| likely renames | %d |\n" % len(v["renames"]))
        f.write("| newly used (excluding renames) | %d |\n" % len(v["added"]))
        f.write("| no longer used (excluding renames) | %d |\n" % len(v["removed"]))
        f.write("| export kind/owner/namespace changed | %d |\n" % len(v["exp_chg"]))
        f.write("| used in both, own declaration changed | %d |\n" % len(v["direct"]))
        f.write("| changed types reachable from used interfaces | %d |\n\n"
                % len(v["types"]))

        f.write("## Likely renames\n\n")
        if v["renames"]:
            f.write("Dropped and newly used symbols with identical signatures "
                    "(types and parameter names) and similar names.\n\n")
            f.write("| %s | %s | signature | used by |\n|---|---|---|---|\n" % (va, vb))
            for r, a, sig in v["renames"]:
                f.write("| `%s` | `%s` | `%s` | %s |\n" % (
                    r, a, md_escape(sig), B[a]["used_by"]))
            f.write("\n")
        else:
            f.write("None.\n\n")
        f.write("## Newly used in %s\n\n" % vb)
        table(v["added"], B, P.fb)
        f.write("## No longer used in %s\n\n" % vb)
        table(v["removed"], A, P.fa)
        if v["exp_chg"]:
            f.write("## Export changes\n\n| symbol | %s | %s |\n|---|---|---|\n" % (va, vb))
            for s in v["exp_chg"]:
                fa = "%s %s %s" % (A[s]["exporter"], A[s]["export"], A[s]["namespace"])
                fb = "%s %s %s" % (B[s]["exporter"], B[s]["export"], B[s]["namespace"])
                f.write("| `%s` | %s | %s |\n" % (s, fa.strip(), fb.strip()))
            f.write("\n")

        f.write("## Interfaces whose own declaration changed\n\n")
        f.write("Return/parameter types, variable types, or interfaces that "
                "lost their debug info. `[C]` changed, `[D]` deleted.\n\n")
        if v["direct"]:
            for d in v["direct"]:
                f.write("**[%s] %s** (%s)\n\n" % (d["op"], md_escape(d["head"]),
                                                 d["binary"]))
                if d["detail"]:
                    f.write("```\n%s\n```\n\n" % "\n".join(d["detail"][:60]))
        else:
            f.write("None.\n\n")

        f.write("## Changed types\n\n")
        f.write("Each changed type reachable from an interface this group uses, "
                "with the number of those interfaces it reaches, fewest first: "
                "low counts are targeted changes, high counts are churn reached "
                "through hub types (reachability is transitive through pointers, "
                "so e.g. `struct device` or `struct module` pull in hundreds).\n\n")
        if v["types"]:
            f.write("| type | declared at | change | used interfaces reached |\n")
            f.write("|---|---|---|---|\n")
            for t in v["types"]:
                f.write("| `%s` | %s | %s | %d |\n" % (
                    md_escape(t["type"]), t["loc"],
                    md_escape(type_summary(t["detail"])), len(t["impacted"])))
            f.write("\n### Details\n\n")
            for t in v["types"]:
                imp = t["impacted"]
                f.write("<details><summary><code>%s</code> (%s)</summary>\n\n"
                        "```\n%s\n```\n\n" % (
                            t["type"], t["loc"], "\n".join(t["detail"][:40]) +
                            ("\n  ..." if len(t["detail"]) > 40 else "")))
                f.write("Reaches: %s%s\n\n</details>\n\n" % (
                    ", ".join("`%s`" % md_escape(x) for x in imp[:15]),
                    " … (+%d more)" % (len(imp) - 15) if len(imp) > 15 else ""))
        else:
            f.write("None.\n\n")

        write_header_section(f, P, v)

        if v["newusers"]:
            f.write("## Same interface, different set of users\n\n")
            f.write("| symbol | %s | %s |\n|---|---|---|\n" % (va, vb))
            for s in v["newusers"]:
                f.write("| `%s` | %s | %s |\n" % (s, A[s]["used_by"], B[s]["used_by"]))
            f.write("\n")


def write_header_section(f, P, v):
    va, vb = P.va, P.vb
    h = v["hdr"]
    if h is None:
        f.write("## Header-level interfaces\n\nNot available for this pair "
                "(header pass missing for %s or %s).\n\n" % (va, vb))
        return
    HA, HB = P.HA, P.HB
    f.write("## Header-level interfaces\n\n")
    f.write("Macros, static inline functions, struct/union/enum tags, typedefs "
            "and enumerators defined in provider headers (headers the consumer "
            "objects were compiled against that are not consumer code) and "
            "named in consumer code. They never appear as ELF symbols, but "
            "LinuxKPI has to provide them. Name-based, so an occasional false "
            "positive is possible (e.g. a local variable or member sharing a "
            "macro's name).\n\n")
    f.write("| | count |\n|---|---|\n")
    f.write("| used in %s | %d |\n| used in %s | %d |\n" % (va, h["used_a"], vb, h["used_b"]))
    f.write("| newly used | %d |\n| no longer used | %d |\n| likely renames | %d |\n"
            % (len(h["added"]), len(h["removed"]), len(h["renames"])))
    f.write("| macro/inline signature changed | %d |\n| macro body changed | %d |\n"
            "| moved to another header | %d |\n\n"
            % (len(h["sigchg"]), len(h["bodychg"]), len(h["moved"])))

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
    if h["renames"]:
        f.write("| %s | %s | kind | signature |\n|---|---|---|---|\n" % (va, vb))
        for r, a, sig in h["renames"]:
            f.write("| `%s` (%s) | `%s` (%s) | %s | `%s` |\n" % (
                r, HA[r]["header"], a, HB[a]["header"], HB[a]["kind"],
                md_escape(HB[a]["signature"]) or "-"))
        f.write("\n")
    else:
        f.write("None.\n\n")
    f.write("### Newly used (header)\n\n")
    htable(h["added"], HB)
    f.write("### No longer used (header)\n\n")
    htable(h["removed"], HA)
    f.write("### Signature changed (header)\n\n")
    if h["sigchg"]:
        f.write("| name | kind | header | %s | %s |\n|---|---|---|---|---|\n" % (va, vb))
        for k in h["sigchg"]:
            f.write("| `%s` | %s | %s | `%s` | `%s` |\n" % (
                k, HB[k]["kind"], HB[k]["header"], md_escape(HA[k]["signature"]),
                md_escape(HB[k]["signature"])))
        f.write("\n")
    else:
        f.write("None.\n\n")
    if h["moved"]:
        f.write("### Moved to another header\n\n| name | %s | %s |\n|---|---|---|\n"
                % (va, vb))
        for k in h["moved"]:
            f.write("| `%s` | %s | %s |\n" % (k, HA[k]["header"], HB[k]["header"]))
        f.write("\n")
    if h["bodychg"]:
        f.write("<details><summary>Macro body changed (%d)</summary>\n\n"
                % len(h["bodychg"]))
        f.write("| macro | header | %s | %s |\n|---|---|---|---|\n" % (va, vb))
        for k in h["bodychg"]:
            f.write("| `%s` | %s | `%s` | `%s` |\n" % (
                k, HB[k]["header"], md_escape(HA[k]["body"][:200]),
                md_escape(HB[k]["body"][:200])))
        f.write("\n</details>\n\n")


def cmd_pair(da, db, out, gconf):
    G = Groups(gconf)
    P = PairData(da, db, out)
    nodes = G.all_nodes()
    views = [(n, P.view(n)) for n in nodes]
    os.makedirs(os.path.join(out, "groups"), exist_ok=True)
    for n, v in views:
        write_report(P, v, os.path.join(out, "groups", group_file(n)),
                     "Interfaces used by %s" % n, n)
    vall = P.view(None)
    write_report(P, vall, os.path.join(out, "report.md"),
                 "Kernel interfaces used by LinuxKPI consumers", None,
                 overview=views)
    # interface -> changed types reaching it
    reach = collections.defaultdict(set)
    for t in P.types:
        for i in t["impacted"]:
            reach[i].add(t["type"])
    with open(os.path.join(out, "impacted.tsv"), "w") as f:
        f.write("interface\tgroups\tn_changed_types\tchanged_types\n")
        for i in sorted(reach, key=lambda k: (-len(reach[k]), k)):
            r = P.B.get(iface_name(i)) or P.A.get(iface_name(i)) or {}
            f.write("%s\t%s\t%d\t%s\n" % (i, r.get("groups", ""), len(reach[i]),
                                         ", ".join(sorted(reach[i]))))
    with open(os.path.join(out, "overview.tsv"), "w") as f:
        f.write("group\tused\tnewly_used\tno_longer_used\trenames\t"
                "declaration_changed\tchanged_types\thdr_newly_used\t"
                "hdr_no_longer_used\thdr_renames\thdr_signature_changed\n")
        for n, v in [("all", vall)] + views:
            f.write(n + "\t" + counts_row(v).replace(" | ", "\t") + "\n")
    h = vall["hdr"]
    print("%s..%s: +%d -%d used, %d renames, %d declaration changes, %d changed "
          "types%s; %d group reports" % (
              P.va, P.vb, len(vall["added"]), len(vall["removed"]),
              len(vall["renames"]), len(vall["direct"]), len(vall["types"]),
              "; headers +%d -%d, %d renames, %d signature changes" % (
                  len(h["added"]), len(h["removed"]), len(h["renames"]),
                  len(h["sigchg"])) if h else "", len(views)), file=sys.stderr)


# ---------------------------------------------------------------- summary
def cmd_summary(outdir, gconf, vers):
    G = Groups(gconf)
    nodes = G.all_nodes()
    tables = {v: read_rows(os.path.join(outdir, v, "imports.tsv"), "symbol")
              for v in vers}

    def used(t, node):
        return sum(1 for r in t.values() if PairData._in(r, node))

    with open(os.path.join(outdir, "summary.md"), "w") as f:
        f.write("# Kernel interfaces used by LinuxKPI consumers, %s … %s\n\n"
                % (vers[0], vers[-1]))
        f.write("Provider symbols imported, per consumer group (parents include "
                "their children).\n\n")
        f.write("| group | " + " | ".join(vers) + " |\n|---" + "|---" * len(vers) + "|\n")
        f.write("| **all** | " + " | ".join(str(len(tables[v])) for v in vers) + " |\n")
        for n in nodes:
            ind = "&nbsp;&nbsp;" * n.count("/")
            f.write("| %s%s | %s |\n" % (ind, n, " | ".join(
                str(used(tables[v], n)) for v in vers)))
        for a, b in zip(vers, vers[1:]):
            d = "diff-%s..%s" % (a, b)
            p = os.path.join(outdir, d, "overview.tsv")
            f.write("\n## %s → %s\n\n[full report](%s/report.md)\n\n" % (a, b, d))
            if not os.path.exists(p):
                f.write("Not available.\n")
                continue
            f.write(COUNTS_HDR)
            with open(p) as tf:
                next(tf)
                for line in tf:
                    c = line.rstrip("\n").split("\t")
                    n = c[0]
                    if n == "all":
                        label = "**all**"
                    else:
                        label = "%s[%s](%s/groups/%s)" % (
                            "&nbsp;&nbsp;" * n.count("/"), n, d, group_file(n))
                    f.write("| %s | %s |\n" % (label, " | ".join(c[1:])))

    allsyms = sorted(set().union(*[set(t) for t in tables.values()]))
    with open(os.path.join(outdir, "matrix.tsv"), "w") as f:
        f.write("\t".join(["symbol", "kind", "exporter"] + vers +
                          ["groups_latest", "used_by_latest"]) + "\n")
        for s in allsyms:
            last = next(tables[v][s] for v in reversed(vers) if s in tables[v])
            f.write("\t".join([s, last["kind"], last["exporter"]] +
                              ["x" if s in tables[v] else "" for v in vers] +
                              [last.get("groups", ""), last["used_by"]]) + "\n")


def main():
    cmd, a = sys.argv[1], sys.argv[2:]
    if cmd == "g0dirs":
        cmd_g0dirs(*a)
    elif cmd == "imports":
        cmd_imports(*a)
    elif cmd == "headers":
        cmd_headers(*a)
    elif cmd == "pair":
        cmd_pair(*a)
    elif cmd == "summary":
        cmd_summary(a[0], a[1], a[2:])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
