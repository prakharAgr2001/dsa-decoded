"""Compact builders for notebook (NB) episode specs. A spec does:  from engine.nbspec import *;  S = [(narration, scene), ...];  NARRATION, NB = build(S, kind, arr)"""
def L(t, at=None, c='blue', s=56, **kw): return dict(t=t, at=at, c=c, s=s, **kw)
def hook(co=None, lpa=None, role='SDE-1', claim='asked', year=2025, src=None, **kw):
    return dict(type='hook', hook=dict(co=co, lpa=lpa, role=role, claim=claim, year=year, src=src, **kw))
def ques(*lines, note=None):
    ls = [L('Q. ' + lines[0], 0.05, 'red', 66, b=True)] + [L(x, None, 'blue', 62) for x in lines[1:]] + ([L(note, None, 'gry', 44)] if note else [])
    return dict(vis=False, lines=ls)
def ex(arr, line, big=None, big_at=None, ev=None, spoken=True, h=None, **kw):
    seen, cues = {}, []
    for v in arr:
        k = str(v); seen[k] = seen.get(k, 0) + 1
        cues.append(f'{k}#{seen[k]}' if spoken and k.lower() in [w.strip('.,?!:').lower() for w in line.split()] else None)
    d = dict(draw=cues, ev=ev or [], **kw)
    if big: d['big'] = dict(t=big, at=big_at)
    if h: d['h'] = dict(t=h, at=0.02)
    return d
def cx(time, brute=None, pattern='', note=''): return dict(type='cx', cx=dict(time=time, brute=brute, pattern=pattern, note=note))
def cta(t): return dict(type='cta', cta=dict(t=t))
def build(S, kind, arr, water=None):
    return [a for a, b in S], dict(kind=kind, arr=arr, water=water, scenes=[b for a, b in S])
def epd(id, title, pattern, difficulty, slug, company=None, claim=None, year=2025, lpa=None, role='SDE-1', hook='', **kw):
    d = dict(id=id, short=title, title=title, pattern=pattern, difficulty=difficulty, official=f'https://leetcode.com/problems/{slug}/', company=company, claim=claim,
             year=year, lpa=lpa, role=role, hook=hook, cover_t=14.0, tail=.8, bpm=108, drop_scenes=(4,), music_gain=.7, duck=.45); d.update(kw); return d
def T(cols, rows, w=None, at=0): return dict(cols=cols, rows=rows, w=w, at=at)
