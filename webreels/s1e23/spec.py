from engine.nbspec import *
# Classic. Numbers: compute.py E23 ([5,7,7,8,8,8,10] t=8: first 3, last 5)
EP = epd('S1E23', 'Find First and Last Position', 'Binary search', 'Medium', 'find-first-and-last-position-of-element-in-sorted-array', hook='keep searching after a match')
A = [5, 7, 7, 8, 8, 8, 10]
S = [
 ('Binary search with a twist. Finding the number is not enough.', hook(big='Don’t stop', sub='at the first match', at_co='twist', at_lpa='enough')),
 ('Find the first and the last position of 8.', ques('find the FIRST and LAST', 'position of 8')),
 ('Numbers: 5, 7, 7, 8, 8, 8, 10. First 8 at index 3. Last at 5.', ex(A, 'Numbers: 5, 7, 7, 8, 8, 8, 10.', big='→ [3, 5]', big_at='first#1')),
 ('Find one 8, then walk outward? If every number is 8, that is O of n again.',
  dict(h=dict(t='Find one, then walk', at=.05), lines=[L('[8, 8, 8, 8, …] → walk all of it', 'every', 'blk'), L('✗ O(n) worst case', 'again', 'red', 70)])),
 ('The trick: on a match, save it and keep going. Go left for the first, right for the last.',
  dict(lines=[L('match → save it, keep searching', 'save', 'blk', 58, b=True), L('first: hi = mid − 1', 'left', 'red', 56), L('last: lo = mid + 1', 'right', 'blue', 56)])),
 ('First: middle is 8, save 3, go left. 7, go right. 7, go right. First is 3. Last: 8, save 3, go right. 8, save 5. 10, go left. Last is 5.',
  dict(ev=[[0.05, dict(ptr={'lo': 0, 'hi': 6, 'mid': 3})], ['save#1', dict(mark={3: 'ok'}, st='first = 3')], ['7#1', dict(ptr={'hi': 2, 'mid': 1})], ['7#2', dict(ptr={'lo': 2, 'mid': 2})], ['first#2', dict(ptr={'lo': 3, 'hi': 2, 'mid': None}, st='first = [3]')],
           ['last', dict(ptr={'lo': 0, 'hi': 6, 'mid': 3})], ['save#3', dict(ptr={'lo': 4, 'mid': 5}, mark={5: 'ok'}, st='last = 5')], ['10', dict(ptr={'lo': 6, 'mid': 6})], ['last#2', dict(ptr={'hi': 5, 'mid': None}, st='[3, 5] ✓')]])),
 ('Two binary searches. O of log n.', cx('O(log n) time · O(1) space', 'O(n)', 'Binary search', 'on match: save and keep going')),
 ('Comment NOTES, and I will send you five more binary search questions.', cta('5 more binary-search questions')),
]
NARRATION, NB = build(S, 'num', A)
