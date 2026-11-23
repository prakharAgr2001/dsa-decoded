from engine.nbspec import *
# Classic. Numbers: compute.py E24 ([1,3,5,4,2,6,1]: mids 4 (down), 3 (up), 5 (down) -> peak index 2)
EP = epd('S1E24', 'Find Peak Element', 'Binary search', 'Medium', 'find-peak-element', hook='walk uphill')
A = [1, 3, 5, 4, 2, 6, 1]
S = [
 ('Binary search on a list that is not even sorted. This one surprises people.', hook(big='Not sorted?', sub='still binary search', at_co='sorted', at_lpa='surprises')),
 ('Find any peak: a number bigger than both its neighbours. In log n time.', ques('find ANY peak:', 'bigger than both neighbours', note='in O(log n)')),
 ('Numbers: 1, 3, 5, 4, 2, 6, 1. Peaks: 5 and 6. Either is fine.', ex(A, 'Numbers: 1, 3, 5, 4, 2, 6, 1.', big='peaks: 5 or 6', big_at='peaks', ev=[['peaks', dict(mark={2: 'ok', 5: 'ok'})]])),
 ('A full scan works, but it is O of n. The interviewer asked for log n.',
  dict(h=dict(t='Linear scan', at=.05), lines=[L('check every neighbour pair → O(n)', 'scan', 'blk'), L('✗ asked for O(log n)', 'asked', 'red', 66)])),
 ('The trick: compare the middle with its right neighbour. Going uphill? A peak is on the right. Downhill? It is on the left.',
  dict(lines=[L('mid < mid+1 → uphill → go right', 'uphill', 'blue', 54), L('mid > mid+1 → downhill → go left', 'downhill', 'red', 54)], ev=[['middle', dict(ptr={'lo': 0, 'hi': 6}, mark={2: None, 5: None})]])),
 ('Middle is 4, next is 2. Downhill, go left. Middle is 3, next is 5. Uphill, go right. Middle is 5, next is 4. Downhill. Only 5 is left. Peak!',
  dict(table=T(['lo', 'hi', 'mid', 'vs next', 'go'], [[0, 6, 4, '> 2', 'left'], [0, 3, 3, '< 5', 'right'], [2, 3, 5, '> 4', 'left']], [140, 140, 160, 220, 200]),
       ev=[[0.05, dict(ptr={'lo': 0, 'hi': 6, 'mid': 3})], ['left#1', dict(row=0, ptr={'hi': 3, 'mid': 1})], ['right', dict(row=1, ptr={'lo': 2, 'mid': 2})], ['downhill#2', dict(row=2, ptr={'hi': 2})], ['peak', dict(mark={2: 'ok'}, st='peak at index [2]')]])),
 ('Half the list is gone every step. O of log n.', cx('O(log n) time · O(1) space', 'O(n)', 'Binary search', 'follow the uphill side')),
 ('Comment NOTES, and I will send you five more binary search questions.', cta('5 more binary-search questions')),
]
NARRATION, NB = build(S, 'num', A)
