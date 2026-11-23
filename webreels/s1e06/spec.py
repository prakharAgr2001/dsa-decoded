from engine.nbspec import *
# Google: Code360 off-campus interview (4 Nov 2025) https://www.naukri.com/code360/interview-experiences/google-com/interview-experience-off-campus-nov-2025
# Salary: Levels.fyi Google L3 Greater Bengaluru median Rs 40.7 L -> 40. Numbers: compute.py E06 ([9,4,7,2,8,5] -> 6; pairs 5,000 days = 12,497,500)
EP = epd('S1E06', 'Best Time to Buy and Sell Stock', 'Running minimum', 'Easy', 'best-time-to-buy-and-sell-stock', 'Google', 'reported', 2025, 40, 'SWE L3', 'track the cheapest day')
A = [9, 4, 7, 2, 8, 5]
S = [
 ('Want a 40 lakh job at Google? This exact question came up in one of their recent interviews.', hook('Google', 40, 'SWE L3', 'reported', src='salary: Levels.fyi L3 Bengaluru median')),
 ('Buy one day, sell a later day. What is the most profit you can make?', ques('buy once, sell later', 'max profit?')),
 ('Prices: 9, 4, 7, 2, 8, 5. Buy at 2, sell at 8. Profit 6.', ex(A, 'Prices: 9, 4, 7, 2, 8, 5.', big='buy 2 → sell 8 = 6', big_at='buy', ev=[['buy', dict(mark={3: 'ok'})], ['sell', dict(mark={4: 'ok'}, arc=[3, 4, 'grn'])]])),
 ("Brute force tries every buy and sell pair. For 5,000 days, that's 12 million pairs. Rejected.",
  dict(h=dict(t='Brute force: every buy/sell pair', at=.05), lines=[L('5,000 days → [12,497,500] pairs', '5000', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ('The trick: walk once. Remember the cheapest price so far. Each day, profit is today minus that minimum.',
  dict(lines=[L('Trick: remember the [cheapest so far]', 'trick', 'blk', 60, b=True), L('profit = today − min so far', 'profit', 'red', 60, box='red')])),
 ('9, min 9. 4, new min. 7, profit 3. 2, new min. 8, profit 6, best so far. 5, profit 3. Answer: 6.',
  dict(table=T(['price', 'min so far', 'profit', 'best'], [[9, 9, 0, 0], [4, 4, 0, 0], [7, 4, '+3', 3], [2, 2, 0, 3], [8, 2, '+6', 6], [5, 2, '+3', 6]], [200, 260, 220, 220]),
       ev=[['9', dict(ptr={'i': 0}, row=0)], ['4', dict(ptr={'i': 1}, row=1)], ['7', dict(ptr={'i': 2}, row=2)], ['2', dict(ptr={'i': 3}, row=3, mark={3: 'hl'})],
           ['8', dict(ptr={'i': 4}, row=4, arc=[3, 4, 'grn'])], ['5', dict(ptr={'i': 5}, row=5)], ['answer', dict(st='answer = [6]', mark={3: 'ok', 4: 'ok'})]])),
 ("One pass, two numbers to remember. That's O of n.", cx('O(n) time · O(1) space', 'O(n²)', 'Running minimum', 'one pass, two variables')),
 ('Comment NOTES, and I will send you five more questions with this trick.', cta('5 more questions, same trick')),
]
NARRATION, NB = build(S, 'num', A)
