from engine.nbspec import *
# Classic. Numbers: compute.py E22 ([2,5,8,12,16,23,38,56] t=16: mids 12, 23, 16; 1,000,000 items -> 20 steps)
EP = epd('S1E22', 'Binary Search', 'Binary search', 'Easy', 'binary-search', hook='halve the range every step')
A = [2, 5, 8, 12, 16, 23, 38, 56]
S = [
 ('Binary search looks easy. Most people still get the loop wrong in the interview.', hook(big='lo ≤ hi', sub='get the loop right', at_co='binary', at_lpa='loop')),
 ('The list is sorted. Find the position of 16.', ques('sorted list:', 'find the position of 16')),
 ('Numbers: 2, 5, 8, 12, 16, 23, 38, 56. 16 is at index 4.', ex(A, 'Numbers: 2, 5, 8, 12, 16, 23, 38, 56.', big='→ index 4', big_at='index')),
 ('Scanning one by one is O of n. For a million numbers, a million checks.',
  dict(h=dict(t='Linear scan', at=.05), lines=[L('1,000,000 numbers → 1,000,000 checks', 'million#1', 'blk', 52), L('✗ O(n)', 'checks', 'red', 74)])),
 ('The trick: check the middle. Too small, drop the left half. Too big, drop the right half.',
  dict(lines=[L('mid < target → lo = mid + 1', 'small', 'red', 56), L('mid > target → hi = mid − 1', 'big', 'blue', 56)], ev=[['middle', dict(ptr={'lo': 0, 'hi': 7})]])),
 ('Middle is 12, too small. Search the right half. Middle is 23, too big. Now only 16 is left. Found at index 4.',
  dict(table=T(['lo', 'hi', 'mid', 'value'], [[0, 7, 3, 12], [4, 7, 5, 23], [4, 4, 4, '16 ✓']], [180, 180, 180, 240]),
       ev=[[0.05, dict(ptr={'lo': 0, 'hi': 7, 'mid': 3})], ['12', dict(row=0)], ['right', dict(ptr={'lo': 4, 'mid': 5})], ['23', dict(row=1)], ['only', dict(ptr={'hi': 4, 'mid': 4})], ['found', dict(row=2, mark={4: 'ok'})]])),
 ('Halving every step: a million numbers takes just 20 steps. O of log n.', cx('O(log n) time · O(1) space', 'O(n)', 'Binary search', '1,000,000 → 20 steps')),
 ('Comment NOTES, and I will send you five more binary search questions.', cta('5 more binary-search questions')),
]
NARRATION, NB = build(S, 'num', A)
