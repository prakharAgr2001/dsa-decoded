from engine.nbspec import *
# Classic. Numbers: notes/traces/compute.py E05 ([3,1,3,3,2,3,1]: candidate 3, final count 1; 3 appears 4 of 7)
EP = epd('S1E05', 'Majority Element', 'Voting (Boyer-Moore)', 'Easy', 'majority-element', hook='votes cancel out')
A = [3, 1, 3, 3, 2, 3, 1]
S = [
 ('Interviewers love this one because the best answer uses zero extra memory.', hook(big='O(1) space', sub='the trick everyone forgets', at_co='zero', at_lpa='memory')),
 ('Find the number that appears more than half the time.', ques('find the number that appears', 'more than n/2 times')),
 ('Numbers: 3, 1, 3, 3, 2, 3, 1. 3 appears 4 times out of 7. Majority.', ex(A, 'Numbers: 3, 1, 3, 3, 2, 3, 1.', big='3 → 4 of 7 times', big_at='appears', ev=[['majority', dict(mark={0: 'ok', 2: 'ok', 3: 'ok', 5: 'ok'})]])),
 ('Counting with a hash map works, but it costs O of n extra space. The interviewer asks: can you do it in O of 1?',
  dict(h=dict(t='Hash map count: works, but…', at=.05), lines=[L('extra space O(n)', 'space', 'red', 60, strike='asks'), L('→ can you do it in O(1)?', 'asks', 'blk', 60)])),
 ('The trick: voting. Same number, count plus one. Different number, minus one. At zero, pick a new candidate.',
  dict(lines=[L('same → count + 1', 'same', 'grn', 60), L('different → count − 1', 'different', 'red', 60), L('count = 0 → new candidate', 'zero', 'blk', 60, b=True)])),
 ('3, count 1. 1 cancels it, zero. 3 again, count 1. 3, count 2. 2 cancels one. 3, back to 2. 1, down to 1. Candidate: 3.',
  dict(table=T(['num', 'candidate', 'count'], [[3, 3, 1], [1, 3, 0], [3, 3, 1], [3, 3, 2], [2, 3, 1], [3, 3, 2], [1, 3, 1]], [300, 300, 300], at=-1),
       ev=[[0.1, dict(ptr={'i': 0}, row=0, st='candidate = 3')], ['cancels#1', dict(ptr={'i': 1}, row=1)], ['again', dict(ptr={'i': 2}, row=2)], ['3#3', dict(ptr={'i': 3}, row=3)],
           ['cancels#2', dict(ptr={'i': 4}, row=4)], ['back', dict(ptr={'i': 5}, row=5)], ['down', dict(ptr={'i': 6}, row=6)], ['candidate', dict(st='candidate = [3] ✓', mark={0: 'ok', 2: 'ok', 3: 'ok', 5: 'ok'})]])),
 ("One pass, two variables. That's O of n time, O of 1 space.", cx('O(n) time · O(1) space', 'O(n) space (hash map)', 'Boyer-Moore', 'one pass, two variables')),
 ('Comment NOTES, and I will send you five more array tricks like this.', cta('5 more array tricks')),
]
NARRATION, NB = build(S, 'num', A)
