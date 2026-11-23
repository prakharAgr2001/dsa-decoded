from engine.nbspec import *
# ServiceNow: LeetCode (May 2025, IC2 Hyderabad) https://leetcode.com/discuss/interview-experience/6749919 ; also Tripadvisor (14 Oct 2026, LeetCode)
# Salary: Levels.fyi ServiceNow IC1 Rs 29.1 L - IC2 Rs 37.1 L -> 35. Numbers: compute.py E27 ('([]){}' -> valid)
EP = epd('S1E27', 'Valid Parentheses', 'Stack', 'Easy', 'valid-parentheses', 'ServiceNow', 'reported', 2025, 35, 'IC2', 'push opens, pop on close')
A = list('([]){}')
S = [
 ('Want a 35 lakh job at ServiceNow? This exact question came up in one of their recent interviews.', hook('ServiceNow', 35, 'IC2', 'reported', src='salary: Levels.fyi ServiceNow IC1-IC2')),
 ('Check if every bracket is closed in the right order.', ques('is every bracket closed', 'in the right order?')),
 ('Brackets: round, square, square, round, curly, curly. Valid.', ex(A, '', spoken=False, big='valid ✓', big_at='valid')),
 ('Counting brackets is not enough. Round open, square close, round close? Counts match, but the order is wrong.',
  dict(h=dict(t='Just count them?', at=.05), lines=[L('"( ] )" → counts look fine', 'counts', 'blk', 58), L('✗ order is wrong', 'wrong', 'red', 70)])),
 ('The trick: a stack. Push every opening bracket. On a closing bracket, the top must match. Pop it.',
  dict(stack=3, lines=[L('open → push', 'push', 'blue', 60), L('close → top must match → pop', 'match', 'red', 58)])),
 ('Push round. Push square. Square closes, matches, pop. Round closes, pop. Push curly. Curly closes, pop. Stack empty. Valid.',
  dict(stack=3, ev=[['round#1', dict(ptr={'i': 0}, push='(')], ['square#1', dict(ptr={'i': 1}, push='[')], ['pop#1', dict(ptr={'i': 2}, pop=1, mark={1: 'ok', 2: 'ok'})], ['pop#2', dict(ptr={'i': 3}, pop=1, mark={0: 'ok', 3: 'ok'})],
                     ['curly#1', dict(ptr={'i': 4}, push='{')], ['pop#3', dict(ptr={'i': 5}, pop=1, mark={4: 'ok', 5: 'ok'})], ['empty', dict(st='stack empty → valid ✓')]])),
 ('One pass, one stack. O of n.', cx('O(n) time · O(n) space', None, 'Stack', 'push opens, pop matching closes')),
 ('Comment NOTES, and I will send you five more stack questions.', cta('5 more stack questions')),
]
NARRATION, NB = build(S, 'char', A)
