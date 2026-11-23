from engine.nbspec import *
# Classic. Numbers: compute.py E09 ([0,3,0,5,7] -> [3,5,7,0,0])
EP = epd('S1E09', 'Move Zeroes', 'Two pointers', 'Easy', 'move-zeroes', hook='a write pointer')
A = [0, 3, 0, 5, 7]
S = [
 ('Easy question. But most people use an extra array, and lose the interviewer right there.', hook(big='In place!', sub='no extra array', at_co='easy', at_lpa='extra')),
 ('Move every zero to the end. Keep the other numbers in order. In place.', ques('move every zero to the end', 'keep the rest in order', note='in place, no copy')),
 ('Numbers: 0, 3, 0, 5, 7. After: 3, 5, 7, 0, 0.', ex(A, 'Numbers: 0, 3, 0, 5, 7.', big='→ 3  5  7  0  0', big_at='after')),
 ('Deleting each zero and shifting the rest left costs up to n squared moves. Rejected.',
  dict(h=dict(t='Brute force: delete + shift left', at=.05), lines=[L('each zero → shift everything after it', 'shifting', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: two pointers. A write pointer marks where the next non zero goes. The other one scans.',
  dict(lines=[L('w = next spot for a non-zero', 'write', 'blk', 60, b=True), L('i scans → non-zero? swap with w, w + 1', 'scans', 'red', 54)], ev=[['pointers', dict(ptr={'w': 0, 'i': 0})]])),
 ('Index 0 is zero, skip. 3 is not, swap it to the front. Index 2, zero, skip. 5, swap. 7, swap. Done: 3, 5, 7, 0, 0.',
  dict(ev=[['skip#1', dict(ptr={'i': 0, 'w': 0}, st='w = 0')], ['swap#1', dict(ptr={'i': 1, 'w': 1}, set={0: 3, 1: 0}, st='w = 1')], ['skip#2', dict(ptr={'i': 2})],
           ['5#1', dict(ptr={'i': 3, 'w': 2}, set={1: 5, 3: 0}, st='w = 2')], ['7#1', dict(ptr={'i': 4, 'w': 3}, set={2: 7, 4: 0}, st='w = 3')], ['done', dict(mark={0: 'ok', 1: 'ok', 2: 'ok'}, st='[3, 5, 7] then zeros ✓')]])),
 ("One pass, no extra array. That's O of n.", cx('O(n) time · O(1) space', 'O(n²)', 'Two pointers', 'one write pointer, one scan pointer')),
 ('Comment NOTES, and I will send you five more two pointer questions.', cta('5 more two-pointer questions')),
]
NARRATION, NB = build(S, 'num', A)
