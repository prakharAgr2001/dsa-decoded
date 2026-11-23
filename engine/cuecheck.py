"""Report NB cues that don't resolve to a word in their scene (they'd silently fall back to 30%)."""
import re, sys, importlib
def norm(w): return re.sub(r'[^a-z0-9]', '', w.lower())
def check(epid):
    m = importlib.import_module(f'webreels.{epid.lower()}.spec')
    bad = []
    for i, (sc, line) in enumerate(zip(m.NB['scenes'], m.NARRATION)):
        toks = [norm(t) for t in line.split()]
        cues = [e[0] for e in sc.get('ev', [])] + [x.get('at') for x in sc.get('lines', [])] + [(sc.get('h') or {}).get('at'), (sc.get('big') or {}).get('at'), (sc.get('table') or {}).get('at')] + list(sc.get('draw', []) or [])
        for c in cues:
            if c is None or isinstance(c, (int, float)): continue
            w, _, n = str(c).partition('#'); n = int(n or 1)
            if toks.count(norm(w)) < n: bad.append((i, c))
    return bad
if __name__ == '__main__':
    for e in sys.argv[1:]:
        b = check(e); print(e, 'OK' if not b else b)
