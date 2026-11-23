from engine.nbspec import *
# Classic (no recent company reports collected) -> classic hook. Numbers: [4,7,1,7,3] first repeat 7 at index 3; pairs n=5,000: 12,497,500.
EP = dict(id='S1E02', short='Contains Duplicate', title='Contains Duplicate', pattern='Hashing', difficulty='Easy', official='https://leetcode.com/problems/contains-duplicate/',
          company=None, claim=None, hook='the hash set check', cover_t=14.0, tail=.8, bpm=108, drop_scenes=(4,), music_gain=.7, duck=.45)
A = [4, 7, 1, 7, 3]
S = [
 ('This warm-up opens a lot of product company interviews. Get it wrong, and the round is over.', hook(big='Warm-up #1', sub='product-company favourite', at_co='warm')),
 ('Here it is: does this list contain any number twice?', ques('does any number', 'appear twice?')),
 ('Numbers: 4, 7, 1, 7, 3. Yes. 7 shows up twice.', ex(A, 'Numbers: 4, 7, 1, 7, 3.', big='yes → 7 appears twice', big_at='yes', ev=[['twice', dict(mark={1: 'ok', 3: 'ok'})]])),
 ("Most people compare every pair. For 5,000 numbers, that's 12 million comparisons. Rejected.",
  dict(h=dict(t='Brute force: compare every pair', at=0.05), ev=[['pair', dict(arc=[0, 1, 'blue'])], ['pair', dict(arc=[1, 3, 'blue'])]],
       lines=[L('n = 5,000 → [12,497,500] pairs', '5000', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 76)])),
 ('The trick: a hash set. Before adding a number, check if it is already inside.',
  dict(lines=[L('Trick: keep a [hash set]', 'trick', 'blk', 62, b=True), L('already in the set? → duplicate!', 'check', 'red', 58)], ev=[['set', dict(st='seen = { }')]])),
 ('4. Not seen, add it. 7, add. 1, add. Then 7 again. Already in the set. Duplicate!',
  dict(table=dict(cols=['i', 'num', 'in set?', 'action'], w=[120, 200, 260, 320], rows=[[0, 4, 'no', 'add'], [1, 7, 'no', 'add'], [2, 1, 'no', 'add'], [3, 7, 'yes', 'return true']], at=0),
       ev=[['4', dict(ptr={'i': 0}, row=0, st='seen = {4}')], ['7#1', dict(ptr={'i': 1}, row=1, st='seen = {4, 7}')], ['1', dict(ptr={'i': 2}, row=2, st='seen = {4, 7, 1}')],
           ['7#2', dict(ptr={'i': 3})], ['already', dict(row=3, mark={1: 'ok', 3: 'ok'}, st='seen = {4, [7], 1} → found 7')]])),
 ("One pass through the list. That's O of n.", cx('O(n) time · O(n) space', 'O(n²)', 'Hashing', 'one pass, one set lookup each')),
 ('Comment NOTES, and I will send you five more hashing questions.', cta('5 more hashing questions')),
]
NARRATION, NB = build(S, 'num', A)
