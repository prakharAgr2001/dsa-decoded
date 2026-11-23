from engine.nbspec import *
# Google: LeetCode (10 Dec 2025, new grad) https://leetcode.com/discuss/interview-experience/7405521
# Salary: Levels.fyi Google L3 Bengaluru median Rs 40.7 L -> 40. Numbers: compute.py E21 ([1,2,1,2,1], k=3 -> 4)
EP = epd('S1E21', 'Subarray Sum Equals K', 'Prefix sum + hash map', 'Medium', 'subarray-sum-equals-k', 'Google', 'reported', 2025, 40, 'L3', 'count earlier prefixes')
A = [1, 2, 1, 2, 1]
S = [
 ('Want a 40 lakh job at Google? This exact question came up in one of their recent interviews.', hook('Google', 40, 'L3', 'reported', src='salary: Levels.fyi Google L3 Bengaluru median')),
 ('Count the groups of neighbours that add up to exactly 3.', ques('count groups of neighbours', 'that add up to exactly 3')),
 ('Numbers: 1, 2, 1, 2, 1. Groups: 1 2, 2 1, 1 2, 2 1. Answer 4.', ex(A, 'Numbers: 1, 2, 1, 2, 1.', big='→ 4 groups', big_at='answer')),
 ('Checking every start and end is O of n squared. Rejected.',
  dict(h=dict(t='Brute force: every start, every end', at=.05), lines=[L('n² ranges', 'every', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: keep a running total. If an earlier total equals running total minus 3, the part in between sums to 3.',
  dict(lines=[L('running − 3 seen before?', 'earlier', 'blk', 58, b=True), L('→ count += times seen', 'between', 'red', 58), L('seen = {0: 1} at the start', 'running', 'gry', 46)])),
 ('Totals: 1, need minus 2, none. 3, need 0, one. 4, need 1, one. 6, need 3, one. 7, need 4, one. Count: 4.',
  dict(table=T(['total', 'need', 'found', 'count'], [[1, -2, 0, 0], [3, 0, 1, 1], [4, 1, 1, 2], [6, 3, 1, 3], [7, 4, 1, 4]], [200, 200, 200, 200]),
       ev=[['none', dict(ptr={'i': 0}, row=0)], ['one#1', dict(ptr={'i': 1}, row=1)], ['one#2', dict(ptr={'i': 2}, row=2)], ['one#3', dict(ptr={'i': 3}, row=3)], ['one#4', dict(ptr={'i': 4}, row=4)], ['count', dict(st='count = [4]')]])),
 ('One pass with a hash map. O of n.', cx('O(n) time · O(n) space', 'O(n²)', 'Prefix sum + hash map', 'count of earlier totals')),
 ('Comment NOTES, and I will send you five more prefix sum questions.', cta('5 more prefix-sum questions')),
]
NARRATION, NB = build(S, 'num', A)
