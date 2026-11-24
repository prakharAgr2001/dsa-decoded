from engine.iespec import *
# LeetCode Discuss, Angel One SDE-2, 23 Sep 2026: https://leetcode.com/discuss/post/8535545/interview-experience-sde2-angel-one-by-t-lpfz/
EP = epd('X4', 'Angel One SDE-2 interview', 'Interview experience', 'Medium', 'angel-one-sde-2', hook='3 rounds, offer', cover_t=2.0)
S = [
 ("Angel One SDE 2. Three rounds, and an offer of 29 lakh fixed. Here's what they asked.", intro('Angel One', 'SDE-2 · Backend', '3 rounds → [₹29 L fixed ✓]', at_co='angel')),
 ('Round 1, DSA. Koko eating bananas, longest palindromic substring, and decoding a digit string into letters with DP. All three solved.',
  rnd('Round 1 · DSA', L('Koko Eating Bananas', 'koko', 'blue', 64), L('Longest Palindromic Substring', 'palindromic', 'blue', 58), L('decode digits → A-Z (DP)', 'decoding', 'blue', 62), L('3 / 3 solved ✓', 'solved', 'grn', 66, b=True))),
 ('Round 2, high level design for over an hour. Design a payment service: transactions, Kafka, bank failures, and retries.',
  rnd('Round 2 · High-level design', L('design a payment service', 'payment', 'blk', 64, b=True), L('DB transactions', 'transactions', 'blue', 62), L('Kafka streams', 'kafka', 'blue', 62), L('bank failures + retries', 'bank', 'red', 62))),
 ('Round 3, everything else. A system design, a books and authors database, and a parking lot. Selected.',
  rnd('Round 3 · System + DB + LLD', L('a system design', 'system', 'blue', 64), L('DB: books + authors store', 'books', 'blue', 62), L('LLD: parking lot', 'parking', 'blue', 64), big=('SELECTED ✓', 'selected'))),
 (OUTRO, outro()),
]
NARRATION, NB = make(S)
