from engine.nbspec import *
# Classic. Numbers: compute.py E30 ([30,34,31,33,36,32] -> [1,3,1,1,0,0])
EP = epd('S1E30', 'Daily Temperatures', 'Monotonic stack', 'Medium', 'daily-temperatures', hook='stack of waiting days')
A = [30, 34, 31, 33, 36, 32]
S = [
 ('Same stack trick, new costume. If you know next greater element, you already know this.', hook(big='Same trick', sub='new costume', at_co='stack', at_lpa='costume')),
 ('For each day, how many days until a warmer one? None? Zero.', ques('days until a warmer day?', 'none → 0')),
 ('Temperatures: 30, 34, 31, 33, 36, 32. Answer: 1, 3, 1, 1, 0, 0.', ex(A, 'Temperatures: 30, 34, 31, 33, 36, 32.', big='→ [1, 3, 1, 1, 0, 0]', big_at='answer')),
 ('Scanning ahead from every day is O of n squared. Rejected.',
  dict(h=dict(t='Brute force: scan ahead from each day', at=.05), lines=[L('n days × n scans', 'scanning', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: a stack of days still waiting. A warmer day pops them, and the answer is the gap in days.',
  dict(stack=3, lines=[L('stack = days still waiting', 'waiting', 'blk', 58, b=True), L('warmer day → pop, answer = gap', 'gap', 'red', 54)])),
 ('Push 30. 34 pops it: 1 day. Push 34, push 31. 33 pops 31: 1 day. 36 pops 33: 1 day, and pops 34: 3 days. 36 and 32 never get warmer: 0.',
  dict(stack=3, ev=[['30', dict(ptr={'i': 0}, push=30)], ['pops#1', dict(ptr={'i': 1}, pop=1, mark={0: 'ok'}, st='30 → 1 day')], ['34#2', dict(push=34)], ['31#1', dict(ptr={'i': 2}, push=31)],
                     ['pops#2', dict(ptr={'i': 3}, pop=1, mark={2: 'ok'}, st='31 → 1 day')], ['day#2', dict(push=33)], ['pops#3', dict(ptr={'i': 4}, pop=1, mark={3: 'ok'}, st='33 → 1 day')],
                     ['pops#4', dict(pop=1, mark={1: 'ok'}, st='34 → 3 days')], ['days', dict(push=36)], ['never', dict(ptr={'i': 5}, mark={4: 'bad', 5: 'bad'}, st='36, 32 → 0')]])),
 ('Each day is pushed once and popped once. O of n.', cx('O(n) time · O(n) space', 'O(n²)', 'Monotonic stack', 'store indexes to get the gap')),
 ('Comment NOTES, and I will send you five more stack questions.', cta('5 more stack questions')),
]
NARRATION, NB = build(S, 'num', A)
