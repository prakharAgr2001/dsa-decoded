from engine.nbspec import *
# Classic. Numbers: compute.py E19 ([2,3,1,4,5,2], target 9 -> min length 2 (4+5))
EP = epd('S1E19', 'Minimum Size Subarray Sum', 'Sliding window', 'Medium', 'minimum-size-subarray-sum', hook='grow, then shrink while valid')
A = [2, 3, 1, 4, 5, 2]
S = [
 ('Sliding window, level two. The window now changes size.', hook(big='Level 2', sub='variable window', at_co='sliding', at_lpa='size')),
 ('Find the shortest group of neighbours with a sum of at least 9.', ques('shortest group of neighbours', 'with sum ≥ 9')),
 ('Numbers: 2, 3, 1, 4, 5, 2. Answer: 4 and 5. Length 2.', ex(A, 'Numbers: 2, 3, 1, 4, 5, 2.', big='4 + 5 = 9 → length 2', big_at='answer', ev=[['answer', dict(win=[3, 4, 'g'])]])),
 ('Trying every start and end is O of n squared. Rejected.',
  dict(h=dict(t='Brute force: every start, every end', at=.05), lines=[L('n² windows', 'every', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: grow the right side until the sum hits 9. Then shrink from the left while it stays at least 9.',
  dict(lines=[L('sum < 9 → grow right', 'grow', 'blue', 60), L('sum ≥ 9 → record, shrink left', 'shrink', 'red', 60, b=True)])),
 ('Grow to 10, length 4. Shrink to 8. Grow to 13, length 4. Shrink, 10, length 3. Shrink, 9, length 2. Shrink to 5. Grow to 7. Best: 2.',
  dict(ev=[[0.05, dict(ptr={'l': 0, 'r': 3}, win=[0, 3, 'g'], st='sum 10 · len 4')], ['8', dict(ptr={'l': 1}, win=[1, 3, 'r'], st='sum 8')], ['13', dict(ptr={'r': 4}, win=[1, 4, 'g'], st='sum 13 · len 4')],
           ['3#1', dict(ptr={'l': 2}, win=[2, 4, 'g'], st='sum 10 · len 3')], ['2#1', dict(ptr={'l': 3}, win=[3, 4, 'g'], st='sum 9 · len 2')], ['5', dict(ptr={'l': 4}, win=[4, 4, 'r'], st='sum 5')],
           ['7', dict(ptr={'r': 5}, win=[4, 5, 'r'], st='sum 7')], ['best', dict(win=[3, 4, 'g'], st='best = [2]')]])),
 ('Each number enters and leaves once. O of n.', cx('O(n) time · O(1) space', 'O(n²)', 'Sliding window', 'shrink while the sum is still ≥ target')),
 ('Comment NOTES, and I will send you five more sliding window questions.', cta('5 more sliding-window questions')),
]
NARRATION, NB = build(S, 'num', A)
