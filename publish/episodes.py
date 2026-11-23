"""Load episode metadata (EP dict) from webreels/<id>/spec.py. Shared by covers, queue and site."""
import glob, importlib.util, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def key(eid): m = re.fullmatch(r'S(\d+)E(\d+)', eid); return int(m.group(1)), int(m.group(2))

def load(eid):
    p = os.path.join(ROOT, 'webreels', eid.lower(), 'spec.py')
    s = importlib.util.spec_from_file_location('spec_' + eid, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.EP

def all_eps():
    ids = [os.path.basename(os.path.dirname(p)).upper() for p in glob.glob(os.path.join(ROOT, 'webreels', 's[0-9]*e[0-9]*', 'spec.py'))]
    return [load(i) for i in sorted(ids, key=key)]

def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def claim_line(ep):
    """Company line used in captions/site. Follows the sourcing rule in CLAUDE.md."""
    c, y = ep.get('company'), ep.get('year')
    if not c: return 'A classic at product-company interviews'
    return f'Asked in {c} interviews ({y})' if ep.get('claim') == 'asked' else f'Reported in a {c} interview'
