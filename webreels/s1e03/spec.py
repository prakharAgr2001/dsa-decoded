from engine.nbspec import *
# Adobe: Glassdoor "group words that are anagrams" (3 Feb 2025) https://www.glassdoor.co.in/Interview/Javascript-coding-question-how-to-group-words-that-are-anagrams-example-abc-bca-cab-QTN_7960490.htm
# Salary: Adobe MTS-1 Rs 15-40.4 L (AmbitionBox https://ambitionbox.com/salaries/adobe-salaries/member-technical-staff-1) -> 30. Numbers: notes/traces/compute.py E03 (10,000 words -> 49,995,000 pairs)
EP = epd('S1E03', 'Group Anagrams', 'Hashing', 'Medium', 'group-anagrams', 'Adobe', 'reported', 2025, 30, 'MTS-1', 'sorted letters = the key')
A = ['pat', 'tap', 'art', 'rat', 'apt', 'tar']
S = [
 ('Want a 30 lakh job at Adobe? This exact question came up in one of their recent interviews.', hook('Adobe', 30, 'MTS-1', 'reported', src='salary: AmbitionBox range for MTS-1')),
 ('Group the words that are anagrams: same letters, different order.', ques('group the anagrams', 'same letters, different order')),
 ('Words: pat, tap, art, rat, apt, tar. Two groups: pat, tap, apt. And art, rat, tar.', ex(A, 'pat, tap, art, rat, apt, tar.', ev=[['groups', dict(mark={0: 'hl', 1: 'hl', 4: 'hl'})], ['art#2', dict(mark={2: 'on', 3: 'on', 5: 'on'})]])),
 ("Comparing every pair of words? For 10,000 words, that's almost 50 million comparisons. Rejected.",
  dict(h=dict(t='Brute force: compare every pair', at=.05), lines=[L('10,000 words → [49,995,000] pairs', '10000', 'blk'), L('✗ TOO SLOW · O(n²·k)', 'rejected', 'red', 74)])),
 ("The trick: sort each word's letters. Anagrams get the same key.",
  dict(lines=[L('Trick: [sorted letters] = key', 'trick', 'blk', 62, b=True), L('tap → a p t     rat → a r t', 'anagrams', 'red', 58)], ev=[['key', dict(st='map = { }')]])),
 ('pat sorts to A P T. tap, also A P T. art sorts to A R T. rat, A R T again. apt joins A P T. tar joins A R T.',
  dict(table=T(['word', 'sorted key', 'group'], [['pat', 'apt', '1'], ['tap', 'apt', '1'], ['art', 'art', '2'], ['rat', 'art', '2'], ['apt', 'apt', '1'], ['tar', 'art', '2']], [260, 340, 300]),
       ev=[['pat', dict(ptr={'i': 0}, row=0, mark={0: 'hl'}, st='apt: [pat]')], ['tap', dict(ptr={'i': 1}, row=1, mark={1: 'hl'}, st='apt: [pat, tap]')],
           ['art', dict(ptr={'i': 2}, row=2, mark={2: 'on'}, st='apt: [pat, tap] · art: [art]')], ['rat', dict(ptr={'i': 3}, row=3, mark={3: 'on'}, st='apt: [pat, tap] · art: [art, rat]')],
           ['apt', dict(ptr={'i': 4}, row=4, mark={4: 'hl'}, st='apt: [pat, tap, apt] · art: [art, rat]')], ['tar', dict(ptr={'i': 5}, row=5, mark={5: 'on'}, st='apt: [pat, tap, apt] · art: [art, rat, tar]')]])),
 ("One pass. Each word sorted once. That's O of n times k log k.", cx('O(n · k log k) time', 'O(n²·k)', 'Hashing', 'k = letters per word')),
 ('Comment NOTES, and I will send you five more hashing questions.', cta('5 more hashing questions')),
]
NARRATION, NB = build(S, 'char', A)
