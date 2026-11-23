from engine.nbspec import *
# Classic. Numbers: compute.py E11 ([1,3,4,6,8,11] target 10: sums 12, 9, 11, 9, 10; pairs 5,000 -> 12,497,500)
EP = epd('S1E11', 'Two Sum II (sorted input)', 'Two pointers', 'Medium', 'two-sum-ii-input-array-is-sorted', hook='sorted means two pointers')
A = [1, 3, 4, 6, 8, 11]
S = [
 ("Two Sum's sorted cousin. If you reach for a hash map here, you missed the hint.", hook(big='Sorted = hint', sub='Two Sum II', at_co='sorted', at_lpa='hint')),
 ('The list is sorted. Find two numbers that add up to 10.', ques('the list is sorted.', 'find two that add up to 10')),
 ('Numbers: 1, 3, 4, 6, 8, 11. Answer: 4 and 6.', ex(A, 'Numbers: 1, 3, 4, 6, 8, 11.', big='4 + 6 = 10', big_at='answer', ev=[['answer', dict(mark={2: 'ok', 3: 'ok'})]])),
 ("Checking every pair would be 12 million checks for 5,000 numbers. Rejected.",
  dict(h=dict(t='Brute force: every pair', at=.05), lines=[L('n = 5,000 → [12,497,500] pairs', '5000', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: start at both ends. Too big, move the right pointer in. Too small, move the left pointer in.',
  dict(lines=[L('sum too big → R moves left', 'big', 'red', 60), L('sum too small → L moves right', 'small', 'blue', 60)], ev=[['ends', dict(ptr={'L': 0, 'R': 5})]])),
 ('1 plus 11 is 12, too big. 1 plus 8 is 9, too small. 3 plus 8, 11, too big. 3 plus 6, 9, too small. 4 plus 6. 10. Found it.',
  dict(table=T(['L', 'R', 'sum', 'move'], [[1, 11, 12, 'R ←'], [1, 8, 9, 'L →'], [3, 8, 11, 'R ←'], [3, 6, 9, 'L →'], [4, 6, 10, 'found ✓']], [180, 180, 220, 320]),
       ev=[[0.05, dict(ptr={'L': 0, 'R': 5})], ['12', dict(row=0)], ['8#1', dict(ptr={'R': 4})], ['9#1', dict(row=1)], ['3', dict(ptr={'L': 1})], ['11#2', dict(row=2)],
           ['6#1', dict(ptr={'R': 3})], ['9#2', dict(row=3)], ['4', dict(ptr={'L': 2})], ['10', dict(row=4, mark={2: 'ok', 3: 'ok'})]])),
 ("Each step throws away one number for good. O of n.", cx('O(n) time · O(1) space', 'O(n²)', 'Two pointers', 'each step rules out one number')),
 ('Comment NOTES, and I will send you five more two pointer questions.', cta('5 more two-pointer questions')),
]
NARRATION, NB = build(S, 'num', A)
