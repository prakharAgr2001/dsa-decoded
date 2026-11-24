from engine.iespec import *
from engine.aitools import T, OUT
# Sources: see engine/aitools.py docstring. Repo: https://github.com/openclaw/openclaw
EP = epd('Y17', 'OpenClaw', 'AI tools', 'Easy', 'openclaw', hook='385K ⭐', cover_t=1.5)
repo, name, stars, sc, find = T[16]
def sz(t, m=66): return min(m, int(1700 / max(1, len(t))))
def blk(ls, c='blue'): return [L(t, None, c if k else 'red', sz(t), b=(k == 0)) for k, t in enumerate(ls)]
S = [
 (sc[0][0], dict(vis=False, y0=520, lines=blk(sc[0][1]) + [L(name, None, 'blk', sz(name, 110), b=True), L(stars, None, 'grn', 64, b=True)])),
 (sc[1][0], dict(vis=False, y0=600, lines=blk(sc[1][1], 'blk'))),
 (sc[2][0], dict(vis=False, y0=600, lines=blk(sc[2][1], 'blk'))),
 (find, dict(vis=False, y0=640, lines=[L('find it on GitHub', None, 'gry', 56), L(repo, None, 'red', sz(repo, 72), b=True)])),
 (OUT, outro_ai()),
]
NARRATION, NB = make(S)
