from engine.nbspec import *
# Classic. Numbers: compute.py E12 ([1,1,2,3,3,3,4] -> k = 4)
EP = epd('S1E12', 'Remove Duplicates from Sorted Array', 'Two pointers', 'Easy', 'remove-duplicates-from-sorted-array', hook='slow and fast pointers')
A = [1, 1, 2, 3, 3, 3, 4]
S = [
 ('A favourite opener at product companies. Looks trivial. Most people use extra space and fail.', hook(big='In place!', sub='opener question', at_co='favourite', at_lpa='trivial')),
 ('The list is sorted. Remove duplicates in place, and return how many unique numbers remain.', ques('sorted: keep one of each,', 'in place → return the count')),
 ('Numbers: 1, 1, 2, 3, 3, 3, 4. Unique: 1, 2, 3, 4. Answer 4.', ex(A, 'Numbers: 1, 1, 2, 3, 3, 3, 4.', big='→ 1 2 3 4 · k = 4', big_at='unique')),
 ("Deleting each duplicate shifts everything after it. That's O of n squared. Rejected.",
  dict(h=dict(t='Brute force: delete + shift', at=.05), lines=[L('every delete shifts the rest', 'shifts', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: slow and fast pointers. Fast scans. When it finds a new number, slow moves up and copies it.',
  dict(lines=[L('fast scans every number', 'fast', 'blk', 60, b=True), L('new value → slow + 1, copy it', 'new', 'red', 58)], ev=[['pointers', dict(ptr={'slow': 0, 'fast': 1})]])),
 ('Fast finds 1 again, skip. 2 is new, copy it to slot 1. 3 is new, slot 2. 3, 3, skip. 4 is new, slot 3. Answer: 4.',
  dict(ev=[[0.05, dict(ptr={'slow': 0, 'fast': 1})], ['2#1', dict(ptr={'fast': 2, 'slow': 1}, set={1: 2}, st='k = 2')], ['3#1', dict(ptr={'fast': 3, 'slow': 2}, set={2: 3}, st='k = 3')],
           ['skip#2', dict(ptr={'fast': 5})], ['4#1', dict(ptr={'fast': 6, 'slow': 3}, set={3: 4}, st='k = 4')], ['answer', dict(mark={0: 'ok', 1: 'ok', 2: 'ok', 3: 'ok'}, st='k = [4] → [1, 2, 3, 4]')]])),
 ("One pass, no extra array. O of n.", cx('O(n) time · O(1) space', 'O(n²)', 'Two pointers', 'slow writes, fast reads')),
 ('Comment NOTES, and I will send you five more two pointer questions.', cta('5 more two-pointer questions')),
]
NARRATION, NB = build(S, 'num', A)
