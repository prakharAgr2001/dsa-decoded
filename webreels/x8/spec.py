from engine.iespec import *
# LeetCode Discuss, Atlassian P40, Bangalore: https://leetcode.com/discuss/interview-experience/7196860
EP = epd('X8', 'Atlassian P40 interview', 'Interview experience', 'Medium', 'atlassian-p40', hook='5 rounds, offer', cover_t=2.0)
S = [
 ("Atlassian P40, Bangalore. Five rounds, and two of them are not technical at all. Here's what they asked.", intro('Atlassian', 'P40 · Bangalore', '5 rounds → [offer ✓]')),
 ('Round 1, low level design. Code a snake game where the snake grows only on every nth food.',
  rnd('Round 1 · Low-level design', L('code a snake game', 'snake', 'blk', 66, b=True), L('grows only on every nth food', 'grows', 'blue', 60), L('clean, extensible code', 'code', 'red', 60))),
 ('Round 2, DSA. Lowest common ancestor of any two leaves in an n-ary tree.',
  rnd('Round 2 · DSA', L('Lowest Common Ancestor', 'lowest', 'blue', 66), L('of any two leaves, n-ary tree', 'leaves', 'blue', 58))),
 ('Round 3, high level design. A home page of the most engaged documents, minus the ones you wrote or read.',
  rnd('Round 3 · High-level design', L('home page of top documents', 'home', 'blk', 60, b=True), L('skip the ones you wrote or read', 'minus', 'blue', 56))),
 ('Then values and the manager. A story for each Atlassian value, and a deep dive on your projects. Offer.',
  rnd('Rounds 4-5 · Values + manager', L('a story for each value', 'story', 'blue', 64), L('deep dive on your projects', 'deep', 'blue', 60), big=('OFFER ✓', 'offer'))),
 (OUTRO, outro()),
]
NARRATION, NB = make(S)
