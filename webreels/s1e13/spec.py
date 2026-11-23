from engine.nbspec import *
# Classic. Numbers: compute.py E13 ([1,2,0,2,0,1] -> [0,0,1,1,2,2], 6 steps)
EP = epd('S1E13', 'Sort Colors', 'Dutch national flag', 'Medium', 'sort-colors', hook='three pointers, one pass')
A = [1, 2, 0, 2, 0, 1]
S = [
 ('Asked a lot, solved badly a lot. Sort three colours in one pass, without a sort function.', hook(big='One pass', sub='Dutch flag problem', at_co='asked', at_lpa='pass')),
 ('Sort a list of 0s, 1s and 2s. In one pass, in place.', ques('sort 0s, 1s and 2s', 'in one pass, in place')),
 ('Numbers: 1, 2, 0, 2, 0, 1. After: 0, 0, 1, 1, 2, 2.', ex(A, 'Numbers: 1, 2, 0, 2, 0, 1.', big='→ 0 0 1 1 2 2', big_at='after')),
 ('Counting first takes two passes. A normal sort is n log n. The interviewer wants one pass.',
  dict(h=dict(t='The obvious answers', at=.05), lines=[L('count, then rewrite → 2 passes', 'counting', 'red'), L('sort() → O(n log n)', 'normal', 'red'), L('→ do it in ONE pass', 'wants', 'blk', 62, b=True)])),
 ('The trick: three pointers. Zeros go behind low. Twos go after high. Mid scans the middle.',
  dict(lines=[L('0 → swap with lo; lo++, mid++', 'zeros', 'red', 54), L('1 → mid++', 'mid', 'grn', 54), L('2 → swap with hi; hi−−', 'twos', 'blue', 54)], ev=[['three', dict(ptr={'lo': 0, 'mid': 0, 'hi': 5})]])),
 ('Mid sees 1, move on. 2, swap with high. 1, move on. 0, swap with low. 2, swap with high. 0, swap with low. Sorted!',
  dict(ev=[[0.05, dict(ptr={'lo': 0, 'mid': 0, 'hi': 5})], ['on#1', dict(ptr={'mid': 1})], ['high#1', dict(set={1: 1, 5: 2}, ptr={'hi': 4})], ['on#2', dict(ptr={'mid': 2})],
           ['low#1', dict(set={0: 0, 2: 1}, ptr={'lo': 1, 'mid': 3})], ['high#2', dict(set={3: 0, 4: 2}, ptr={'hi': 3})], ['low#2', dict(set={1: 0, 3: 1}, ptr={'lo': 2, 'mid': 4})],
           ['sorted', dict(mark={i: 'ok' for i in range(6)}, st='sorted in one pass ✓')]])),
 ("Every element is touched once. O of n time, O of 1 space.", cx('O(n) time · O(1) space', 'O(n log n)', 'Dutch flag', 'lo, mid, hi pointers')),
 ('Comment NOTES, and I will send you five more two pointer questions.', cta('5 more two-pointer questions')),
]
NARRATION, NB = build(S, 'num', A)
