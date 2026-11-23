from engine.nbspec import *
# Classic. Numbers: notes/traces/compute.py E04 ([8,4,200,7,5,6,1] -> 5; n*n for 5,000 = 25,000,000)
EP = epd('S1E04', 'Longest Consecutive Sequence', 'Hashing', 'Medium', 'longest-consecutive-sequence', hook='only start at a sequence start')
A = [8, 4, 200, 7, 5, 6, 1]
S = [
 ("Sorting is the obvious answer here. And it's exactly what the interviewer doesn't want.", hook(big='No sorting!', sub='O(n) or it fails', at_co='sorting', at_lpa='sorting')),
 ('Find the longest run of consecutive numbers, in any order, in one pass.', ques('longest run of consecutive', 'numbers, in O(n)')),
 ('Numbers: 8, 4, 200, 7, 5, 6, 1. The run is 4, 5, 6, 7, 8. Length 5.', ex(A, 'Numbers: 8, 4, 200, 7, 5, 6, 1.', big='4 5 6 7 8 → length 5', big_at='run', ev=[['run', dict(mark={0: 'ok', 1: 'ok', 3: 'ok', 4: 'ok', 5: 'ok'})]])),
 ("Brute force: for every number, scan the list for the next one, again and again. That's 25 million steps for 5,000 numbers. Rejected.",
  dict(h=dict(t='Brute force: scan for x+1 each time', at=.05), lines=[L('5,000 × 5,000 = [25,000,000] scans', '25', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: put everything in a set. Only start counting at a number whose smaller neighbour is missing.',
  dict(lines=[L('Trick: [hash set] for O(1) lookups', 'trick', 'blk', 60, b=True), L('start only if x − 1 is NOT in the set', 'only', 'red', 56)], ev=[['set', dict(st='set = {8, 4, 200, 7, 5, 6, 1}')]])),
 ('8? 7 is in the set, skip. 4? 3 is missing, so start: 5, 6, 7, 8. Length 5. 200 starts a run of 1.',
  dict(table=T(['num', 'x−1 in set?', 'start?', 'length'], [[8, 'yes', 'no', '-'], [4, 'no', 'yes', 5], [200, 'no', 'yes', 1]], [180, 280, 200, 240]),
       ev=[['8', dict(ptr={'i': 0}, row=0)], ['4#1', dict(ptr={'i': 1}, row=1)], ['length', dict(mark={1: 'ok', 4: 'ok', 5: 'ok', 3: 'ok', 0: 'ok'}, st='best = 5')], ['200', dict(ptr={'i': 2}, row=2)]])),
 ("7, 5 and 6 aren't starts. 1 starts a run of 1. Best is 5, and every number was touched at most twice.",
  dict(table=dict(cols=['num', 'x−1 in set?', 'start?', 'length'], w=[180, 280, 200, 240], rows=[[7, 'yes', 'no', '-'], [5, 'yes', 'no', '-'], [6, 'yes', 'no', '-'], [1, 'no', 'yes', 1]], at=0),
       ev=[['7', dict(ptr={'i': 3}, row=0)], ['5', dict(ptr={'i': 4}, row=1)], ['6', dict(ptr={'i': 5}, row=2)], ['1', dict(ptr={'i': 6}, row=3)], ['best', dict(st='best = [5]')]])),
 ("That's O of n.", cx('O(n) time · O(n) space', 'O(n²)', 'Hashing', 'each number visited at most twice')),
 ('Comment NOTES, and I will send you five more hashing questions.', cta('5 more hashing questions')),
]
NARRATION, NB = build(S, 'num', A)
