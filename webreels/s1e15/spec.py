from engine.nbspec import *
# Microsoft: Taro, Software Engineer India (11 Nov 2025) https://www.jointaro.com/interviews/companies/microsoft/experiences/software-engineer-india-november-11-2025-declined-offer-positive-4cf9210f
# Salary: Microsoft SDE-1 Rs 31.9-35.2 LPA (AmbitionBox via upGrad) -> 33. Numbers: compute.py E15 ([-5,-2,0,1,3,4] -> only (-5,1,4); C(5000,3) = 20,820,835,000)
EP = epd('S1E15', '3Sum', 'Two pointers', 'Medium', '3sum', 'Microsoft', 'reported', 2025, 33, 'SDE-1', 'fix one, two-pointer the rest')
A = [-5, -2, 0, 1, 3, 4]
S = [
 ('Want a 33 lakh job at Microsoft? This exact question came up in one of their recent interviews.', hook('Microsoft', 33, 'SDE-1', 'reported', src='salary: AmbitionBox range for SDE-1')),
 ('Find three numbers that add up to zero.', ques('find three numbers', 'that add up to zero')),
 ('Numbers: minus 5, minus 2, 0, 1, 3, 4. Answer: minus 5, 1 and 4.', ex(A, '', spoken=False, big='−5 + 1 + 4 = 0', big_at='answer', ev=[['answer', dict(mark={0: 'ok', 3: 'ok', 5: 'ok'})]])),
 ('Trying every triple: for 5,000 numbers, that is over 20 billion triples. Rejected.',
  dict(h=dict(t='Brute force: every triple', at=.05), lines=[L('n = 5,000 → [20,820,835,000] triples', '5000', 'blk', 52), L('✗ TOO SLOW · O(n³)', 'rejected', 'red', 74)])),
 ('The trick: sort, fix one number, then run two pointers on the rest.',
  dict(lines=[L('1. sort the list', 'sort', 'blk', 58), L('2. fix nums[i]', 'fix', 'blk', 58), L('3. two pointers find −nums[i]', 'pointers', 'red', 58, b=True)])),
 ('Fix minus 5. Minus 2 plus 4 gives a total of minus 3. Too small, move left. 0 plus 4, minus 1. Still small, move left. 1 plus 4. Zero. Found one.',
  dict(table=T(['i', 'L', 'R', 'sum'], [[-5, -2, 4, -3], [-5, 0, 4, -1], [-5, 1, 4, '0 ✓']], [220, 220, 220, 240]),
       ev=[['fix', dict(ptr={'i': 0, 'L': 1, 'R': 5}, mark={0: 'hl'})], ['total', dict(row=0)], ['left#1', dict(ptr={'L': 2})], ['still', dict(row=1)], ['left#2', dict(ptr={'L': 3})], ['zero', dict(row=2)], ['found', dict(mark={0: 'ok', 3: 'ok', 5: 'ok'})]])),
 ('Fix minus 2, then 0. The pointers cross with no zero sum. Only one triple.',
  dict(ev=[['fix', dict(ptr={'i': 1, 'L': 2, 'R': 5}, mark={0: None, 3: None, 5: None, 1: 'hl'})], ['0', dict(ptr={'i': 2, 'L': 3, 'R': 5}, mark={1: None, 2: 'hl'})], ['only', dict(mark={2: None, 0: 'ok', 3: 'ok', 5: 'ok'}, st='triples = { [−5, 1, 4] }')]])),
 ("Sorting plus one pointer sweep per number. O of n squared.", cx('O(n²) time · O(1) extra', 'O(n³)', 'Two pointers', 'sort + fix one + two pointers')),
 ('Comment NOTES, and I will send you five more two pointer questions.', cta('5 more two-pointer questions')),
]
NARRATION, NB = build(S, 'num', A)
