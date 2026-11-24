"""Interview-experience reels (from one LeetCode Discuss post each). Same NB look, no array."""
from engine.nbspec import L, epd, build
from config import IG_HANDLE
def intro(co, role, verdict, vcol='grn', at_co=None, s=130):
    return dict(vis=False, y0=560, lines=[L(co, at_co or co.split()[0].lower(), 'blk', s, b=True), L(role, None, 'blue', 80), L(verdict, None, vcol, 66, b=True), L('from a LeetCode Discuss post', None, 'gry', 44)])
def rnd(title, *lines, big=None):
    d = dict(vis=False, y0=520, h=dict(t=title, at=.02, s=min(74, int(74 * 25 / max(25, len(title)))), c='red'), lines=list(lines))
    if big: d['big'] = dict(t=big[0], at=big[1], c=big[2] if len(big) > 2 else 'grn')
    return d
def outro():
    return dict(vis=False, y0=700, lines=[L('Follow', 'follow', 'blk', 120, b=True), L('@' + IG_HANDLE, 'follow', 'blue', 70), L('real interviews, decoded', 'real', 'red', 60)])
OUTRO = 'Follow for more real interview breakdowns.'
def make(S): return build(S, 'char', ['x'])
