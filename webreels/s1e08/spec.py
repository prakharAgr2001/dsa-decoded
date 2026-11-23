from engine.nbspec import *
# Microsoft: Glassdoor (1 Aug 2026) https://www.glassdoor.com/Interview/Microsoft-Interview-E1651-RVW105023468.htm ; Glassdoor (14 Nov 2025) https://www.glassdoor.ca/Interview/Microsoft-Interview-E1651-RVW101276731.htm
# Salary: Microsoft SDE-1 Rs 31.9-35.2 LPA (AmbitionBox via upGrad, Apr 2026) -> 33. Numbers: compute.py E08 (left [1,2,6,24], right [60,20,5,1], answer [60,40,30,24]; 5000*4999 = 24,995,000)
EP = epd('S1E08', 'Product of Array Except Self', 'Prefix products', 'Medium', 'product-of-array-except-self', 'Microsoft', 'asked', 2026, 33, 'SDE-1', 'left × right, no division')
A = [2, 3, 4, 5]
S = [
 ('Want a 33 lakh job at Microsoft? This exact question keeps showing up in their interviews.', hook('Microsoft', 33, 'SDE-1', 'asked', 2026, src='salary: AmbitionBox range for SDE-1')),
 ('For every position, return the product of all the other numbers. No division allowed.', ques('each slot = product of', 'all the OTHER numbers', note='no division allowed')),
 ('Numbers: 2, 3, 4, 5. Answer: 60, 40, 30, 24.', ex(A, 'Numbers: 2, 3, 4, 5.', big='→ [60, 40, 30, 24]', big_at='answer')),
 ("Brute force multiplies everything else for each slot. For 5,000 numbers, that's 25 million multiplications. Rejected.",
  dict(h=dict(t='Brute force: re-multiply for every slot', at=.05), lines=[L('n = 5,000 → [24,995,000] multiplications', '5000', 'blk', 52), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: the answer is everything on the left, times everything on the right.',
  dict(lines=[L('answer[i] = left[i] × right[i]', 'answer', 'blk', 60, b=True, box='blue'), L('left = product before i', 'left', 'red'), L('right = product after i', 'right', 'blue')])),
 ('Left pass. Nothing before index 0, so 1. Then 2. Then 2 times 3, 6. Then 6 times 4, 24.',
  dict(h=dict(t='pass 1: left → right', at=.02), ev=[['nothing', dict(ptr={'i': 0}, st='left = [1]')], ['2#1', dict(ptr={'i': 1}, st='left = [1, 2]')], ['6#1', dict(ptr={'i': 2}, st='left = [1, 2, 6]')], ['24', dict(ptr={'i': 3}, st='left = [1, 2, 6, 24]')]])),
 ('Right pass, from the end. 1. Then 5. Then 5 times 4, 20. Then 20 times 3, 60.',
  dict(h=dict(t='pass 2: right → left', at=.02), ev=[['end', dict(ptr={'i': 3}, st='right = [_, _, _, 1]')], ['5#1', dict(ptr={'i': 2}, st='right = [_, _, 5, 1]')], ['20#1', dict(ptr={'i': 1}, st='right = [_, 20, 5, 1]')], ['60', dict(ptr={'i': 0}, st='right = [60, 20, 5, 1]')]])),
 ('Multiply them. 1 times 60, 60. 2 times 20, 40. 6 times 5, 30. 24 times 1, 24.',
  dict(table=T(['i', 'left', 'right', 'answer'], [[0, 1, 60, 60], [1, 2, 20, 40], [2, 6, 5, 30], [3, 24, 1, 24]], [140, 240, 240, 280]),
       ev=[['times#1', dict(ptr={'i': 0}, row=0, mark={0: 'ok'})], ['times#2', dict(ptr={'i': 1}, row=1, mark={1: 'ok'})], ['times#3', dict(ptr={'i': 2}, row=2, mark={2: 'ok'})], ['times#4', dict(ptr={'i': 3}, row=3, mark={3: 'ok'})]])),
 ("Two passes, no division. That's O of n.", cx('O(n) time · O(1) extra space', 'O(n²)', 'Prefix products', 'output array not counted')),
 ('Comment NOTES, and I will send you five more prefix questions.', cta('5 more prefix questions')),
]
NARRATION, NB = build(S, 'num', A)
