from engine.iespec import *
# LeetCode Discuss, Swiggy SDE-1, posted 12 Mar 2026: https://leetcode.com/discuss/post/7642548/swiggy-sde-1-interview-experience-by-ano-4lnc/
EP = epd('X2', 'Swiggy SDE-1 interview', 'Interview experience', 'Medium', 'swiggy-sde-1', hook='4 rounds, joined', cover_t=2.0)
S = [
 ("Swiggy SDE 1. Four rounds in about three weeks, and this candidate joined. Here's what they asked.", intro('Swiggy', 'SDE-1', '4 rounds → [joined ✓]')),
 ('Round 1, online test. Three DSA problems, two medium and one hard, and only Java or Go allowed.',
  rnd('Round 1 · Online test', L('3 DSA problems', 'three', 'blk', 72, b=True), L('2 medium + 1 hard', 'medium', 'red', 68), L('Java or Go only', 'java', 'blue', 62))),
 ('Round 2, a third party interviewer. Fully running code for a bit manipulation problem and a merge intervals variation, then 20 rapid fire Java questions.',
  rnd('Round 2 · DSA + Java', L('code must actually run', 'running', 'red', 62, b=True), L('bit manipulation', 'bit', 'blue', 66), L('Merge Intervals variation', 'merge', 'blue', 62), L('~20 Java questions: OOP, JVM, GC', 'java', 'blk', 54))),
 ('Round 3, low level design. Assign drivers to orders, with VIP orders and driver ratings. Design it, code it, dry run it.',
  rnd('Round 3 · Low-level design', L('assign drivers to orders', 'assign', 'blk', 64, b=True), L('VIP orders + driver ratings', 'vip', 'blue', 60), L('→ design, code, dry run', 'design#2', 'red', 64, b=True))),
 ('Round 4, hiring manager. About 20 minutes on your experience, interests and team fit. Offer, and they joined.',
  rnd('Round 4 · Hiring manager', L('your experience', 'experience', 'blue', 66), L('your interests', 'interests', 'blue', 66), L('team fit', 'team', 'blue', 66), big=('OFFER ✓', 'offer'))),
 (OUTRO, outro()),
]
NARRATION, NB = make(S)
