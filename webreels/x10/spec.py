from engine.iespec import *
# LeetCode Discuss, Uber SDE-1 (L3), Bangalore, May 2025: https://leetcode.com/discuss/post/6725593/
EP = epd('X10', 'Uber SDE-1 (L3) interview', 'Interview experience', 'Medium', 'uber-l3', hook='4 rounds, offer', cover_t=2.0)
S = [
 ("Uber SDE 1, level 3, Bangalore. Four rounds, and an offer. Here's what they asked.", intro('Uber', 'SDE-1 (L3) · Bangalore', '4 rounds → [offer ✓]')),
 ('Round 1, online test. Four problems, three solved fully.',
  rnd('Round 1 · Online test', L('4 problems', 'four', 'blue', 70), L('3 fully solved', 'three', 'grn', 70, b=True))),
 ("Round 2, DSA. From a rider log, count how many riders visited each three city sequence in order. Then, the data doesn't fit in memory.",
  rnd('Round 2 · DSA', L('rider log → city triplets', 'rider', 'blk', 62, b=True), L('count riders per ordered triplet', 'count', 'blue', 56), L("follow-up: doesn't fit in memory", 'memory', 'red', 56))),
 ('Round 3, design coding. Add an employee under a manager, and count everyone under a manager.',
  rnd('Round 3 · Design coding', L('add employee under manager', 'add', 'blue', 60), L('headcount under a manager', 'count', 'blue', 60))),
 ('Round 4, the engineering manager. Conflict, disagreeing with your manager, pressure, and why Uber. Offer.',
  rnd('Round 4 · Engineering manager', L('team conflict', 'conflict', 'blue', 64), L('disagree with your manager', 'disagreeing', 'blue', 60), L('delivering under pressure', 'pressure', 'blue', 60), big=('OFFER ✓', 'offer'))),
 (OUTRO, outro()),
]
NARRATION, NB = make(S)
