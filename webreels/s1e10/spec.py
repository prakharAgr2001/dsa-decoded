from engine.nbspec import *
# Classic. Numbers: compute.py E10 ('topspot': t/t, o/o, p/p match; meet at index 3)
EP = epd('S1E10', 'Valid Palindrome', 'Two pointers', 'Easy', 'valid-palindrome', hook='one pointer at each end')
A = list('topspot')
S = [
 ('Interviewers use this to check one thing: can you think in two pointers?', hook(big='2 pointers', sub='warm-up round', at_co='interviewers', at_lpa='two')),
 ('Does this text read the same forwards and backwards, ignoring spaces?', ques('same forwards and backwards?', 'ignore spaces and case')),
 ('Text: top spot. Without the space, t o p s p o t. Yes, a palindrome.', ex(A, '', spoken=False, big='yes ✓ palindrome', big_at='yes')),
 ('The easy way: build a reversed copy and compare. It works, but it uses extra memory. The interviewer wants O of 1.',
  dict(h=dict(t='Easy way: reverse a copy', at=.05), lines=[L('reversed copy → O(n) extra space', 'copy', 'red', strike='memory'), L('→ do it in O(1) space', 'wants', 'blk', 60)])),
 ('The trick: one pointer at each end. Compare, then move both inward.',
  dict(lines=[L('L at the start, R at the end', 'pointer', 'blk', 60, b=True), L('match → move both inward', 'compare', 'red', 58)], ev=[['end', dict(ptr={'L': 0, 'R': 6})]])),
 ('t and t, match. o and o, match. p and p, match. They meet at s. Palindrome!',
  dict(table=T(['L', 'R', 'match?'], [['t', 't', 'yes'], ['o', 'o', 'yes'], ['p', 'p', 'yes']], [300, 300, 300]),
       ev=[[0.05, dict(ptr={'L': 0, 'R': 6})], ['match#1', dict(row=0, mark={0: 'ok', 6: 'ok'})], ['o#1', dict(ptr={'L': 1, 'R': 5})], ['match#2', dict(row=1, mark={1: 'ok', 5: 'ok'})],
           ['p#1', dict(ptr={'L': 2, 'R': 4})], ['match#3', dict(row=2, mark={2: 'ok', 4: 'ok'})], ['meet', dict(ptr={'L': 3, 'R': 3}, mark={3: 'hl'})], ['palindrome', dict(st='valid palindrome ✓')]])),
 ("One pass from both ends, no copy. O of n time, O of 1 space.", cx('O(n) time · O(1) space', 'O(n) space (copy)', 'Two pointers', 'move inward from both ends')),
 ('Comment NOTES, and I will send you five more two pointer questions.', cta('5 more two-pointer questions')),
]
NARRATION, NB = build(S, 'char', A)
