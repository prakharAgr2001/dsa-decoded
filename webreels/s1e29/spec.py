from engine.nbspec import *
# Goldman Sachs: Taro, Software Engineer Bengaluru (16 Jul 2025) https://www.jointaro.com/interviews/companies/goldman-sachs/experiences/software-engineer-bengaluru-july-16-2025-no-offer-positive-89301080
# Salary: AmbitionBox GS Analyst engineering Rs 22.7-25.3 L -> 25. Numbers: compute.py E29 ([4,2,6,1,3] -> [6,6,-1,3,-1])
EP = epd('S1E29', 'Next Greater Element', 'Monotonic stack', 'Medium', 'next-greater-element-ii', 'Goldman Sachs', 'reported', 2025, 25, 'Analyst', 'a stack of waiting numbers')
A = [4, 2, 6, 1, 3]
S = [
 ('Want a 25 lakh job at Goldman Sachs? This exact question came up in one of their recent interviews.', hook('Goldman Sachs', 25, 'Analyst', 'reported', src='salary: AmbitionBox range for Analyst')),
 ('For each number, find the next bigger number to its right. None? Minus 1.', ques('for each number: the next', 'BIGGER number to its right', note='none → −1')),
 ('Numbers: 4, 2, 6, 1, 3. Answer: 6, 6, minus 1, 3, minus 1.', ex(A, 'Numbers: 4, 2, 6, 1, 3.', big='→ [6, 6, −1, 3, −1]', big_at='answer')),
 ('Scanning right from every number is O of n squared. Rejected.',
  dict(h=dict(t='Brute force: scan right from each', at=.05), lines=[L('n numbers × n scans', 'scanning', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: a stack of numbers still waiting for an answer. A bigger number pops everyone smaller.',
  dict(stack=3, lines=[L('stack = numbers still waiting', 'waiting', 'blk', 58, b=True), L('bigger arrives → pop smaller, answer = it', 'pops', 'red', 50)])),
 ('Push 4. Push 2. 6 arrives: pop 2, answer 6. Pop 4, answer 6. Push 6. Push 1. 3 arrives: pop 1, answer 3. Push 3. Left over: minus 1.',
  dict(stack=3, ev=[['4#1', dict(ptr={'i': 0}, push=4)], ['2#1', dict(ptr={'i': 1}, push=2)], ['arrives#1', dict(ptr={'i': 2})], ['6#2', dict(pop=1, mark={1: 'ok'}, st='2 → 6')], ['6#3', dict(pop=1, mark={0: 'ok'}, st='4 → 6')],
                     ['push#3', dict(push=6)], ['1#1', dict(ptr={'i': 3}, push=1)], ['arrives#2', dict(ptr={'i': 4})], ['3#2', dict(pop=1, mark={3: 'ok'}, st='1 → 3')], ['3#3', dict(push=3)], ['over', dict(mark={2: 'bad', 4: 'bad'}, st='6, 3 → −1')]])),
 ('Each number is pushed once and popped once. O of n.', cx('O(n) time · O(n) space', 'O(n²)', 'Monotonic stack', 'stack stays decreasing')),
 ('Comment NOTES, and I will send you five more stack questions.', cta('5 more stack questions')),
]
NARRATION, NB = build(S, 'num', A)
