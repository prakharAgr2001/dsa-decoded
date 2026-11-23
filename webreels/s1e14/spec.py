from engine.nbspec import *
# Classic. Numbers: compute.py E14 ([3,7,2,6,4,8]: areas 15, 28, 6, 12, 4 -> 28 = brute max; pairs 5,000 -> 12,497,500)
EP = epd('S1E14', 'Container With Most Water', 'Two pointers', 'Medium', 'container-with-most-water', hook='move the shorter wall')
A = [3, 7, 2, 6, 4, 8]
S = [
 ('This one looks like geometry. It is actually a two pointer greedy trick.', hook(big='Greedy', sub='max water', at_co='geometry', at_lpa='greedy')),
 ('Pick two walls. Water between them is width times the shorter wall. Find the maximum.', ques('pick two walls:', 'area = width × shorter wall')),
 ('Walls: 3, 7, 2, 6, 4, 8. Best: walls 7 and 8, width 4. Area 28.', ex(A, 'Walls: 3, 7, 2, 6, 4, 8.', big='4 × 7 = 28', big_at='area', ev=[['best', dict(mark={1: 'ok', 5: 'ok'})]])),
 ("Every pair of walls is 12 million pairs for 5,000 walls. Rejected.",
  dict(h=dict(t='Brute force: every pair of walls', at=.05), lines=[L('n = 5,000 → [12,497,500] pairs', '5000', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: start with the widest pair. Always move the shorter wall inward, because the short wall limits the water.',
  dict(lines=[L('start widest: L = 0, R = end', 'widest', 'blk', 58), L('move the SHORTER wall inward', 'move', 'red', 60, b=True)], ev=[['widest', dict(ptr={'L': 0, 'R': 5})]])),
 ('3 and 8: width 5, area 15. Move the 3. 7 and 8: width 4, area 28. Move the 7. 2 and 8: area 6. 6 and 8: 12. 4 and 8: 4. Best stays 28.',
  dict(table=T(['L', 'R', 'width', 'area', 'best'], [[3, 8, 5, 15, 15], [7, 8, 4, 28, 28], [2, 8, 3, 6, 28], [6, 8, 2, 12, 28], [4, 8, 1, 4, 28]], [150, 150, 200, 200, 200]),
       ev=[[0.05, dict(ptr={'L': 0, 'R': 5})], ['15', dict(row=0)], ['move#1', dict(ptr={'L': 1})], ['28#1', dict(row=1)], ['move#2', dict(ptr={'L': 2})], ['6#1', dict(row=2)],
           ['6#2', dict(ptr={'L': 3})], ['12', dict(row=3)], ['4#2', dict(ptr={'L': 4})], ['4#3', dict(row=4)], ['stays', dict(mark={1: 'ok', 5: 'ok'}, st='best = [28]')]])),
 ("Each step drops one wall for good. O of n.", cx('O(n) time · O(1) space', 'O(n²)', 'Two pointers', 'greedy: the shorter wall moves')),
 ('Comment NOTES, and I will send you five more two pointer questions.', cta('5 more two-pointer questions')),
]
NARRATION, NB = build(S, 'num', A)
