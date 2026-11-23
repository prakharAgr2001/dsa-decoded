from engine.nbspec import *
# Classic. Numbers: compute.py E20 ([3,1,4,1,5,9] prefix [0,3,4,8,9,14,23]; sum idx 1..4 = 14 - 3 = 11; 10,000 queries x 5,000 = 50,000,000)
EP = epd('S1E20', 'Range Sum Query', 'Prefix sum', 'Easy', 'range-sum-query-immutable', hook='one subtraction per query')
A = [3, 1, 4, 1, 5, 9]
S = [
 ('Prefix sums. One idea that unlocks a whole family of interview questions.', hook(big='Prefix sum', sub='one idea, many questions', at_co='prefix', at_lpa='family')),
 ('Answer many questions like: what is the sum from index 1 to index 4?', ques('many queries:', 'sum from index i to j?')),
 ('Numbers: 3, 1, 4, 1, 5, 9. Index 1 to 4: 1 plus 4 plus 1 plus 5. 11.', ex(A, 'Numbers: 3, 1, 4, 1, 5, 9.', big='sum(1..4) = 11', big_at='11', ev=[['index', dict(win=[1, 4, 'g'])]])),
 ('Adding up each range again: 10,000 queries on 5,000 numbers is 50 million additions. Rejected.',
  dict(h=dict(t='Brute force: add each range again', at=.05), lines=[L('10,000 × 5,000 = [50,000,000]', '10000', 'blk', 54), L('✗ TOO SLOW · O(n) per query', 'rejected', 'red', 66)])),
 ('The trick: build running totals once. 0, 3, 4, 8, 9, 14, 23.',
  dict(lines=[L('P[i] = sum before index i', 'running', 'blk', 58, b=True), L('P = [0, 3, 4, 8, 9, 14, 23]', 'once', 'grn', 56)])),
 ('Then any range is one subtraction. Index 1 to 4 is the total up to 4, which is 14, minus the total before 1, which is 3. 11.',
  dict(lines=[L('sum(i..j) = P[j+1] − P[i]', 'subtraction', 'blk', 58, box='blue'), L('= P[5] − P[1] = 14 − 3 = [11]', '14', 'red', 60, b=True)], ev=[['range', dict(win=[1, 4, 'g'])], ['11', dict(st='O(1) per query ✓')]])),
 ('O of n to build, then O of 1 per query.', cx('O(n) build · O(1) per query', 'O(n) per query', 'Prefix sum', 'running totals, then subtract')),
 ('Comment NOTES, and I will send you five more prefix sum questions.', cta('5 more prefix-sum questions')),
]
NARRATION, NB = build(S, 'num', A)
