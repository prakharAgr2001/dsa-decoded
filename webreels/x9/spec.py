from engine.iespec import *
# LeetCode Discuss, PhonePe SDE-2 Backend, posted Sep 2026: https://leetcode.com/discuss/post/8547106/phonepe-sde-2-backend-interview-experien-vcqt/
EP = epd('X9', 'PhonePe SDE-2 interview', 'Interview experience', 'Medium', 'phonepe-sde-2', hook='4 good rounds, still rejected', cover_t=2.0)
S = [
 ("PhonePe SDE 2. Every round felt good, and still rejected. Here's what they asked.", intro('PhonePe', 'SDE-2 · Backend', '4 rounds → [rejected]', 'red')),
 ('Round 1, a take home to do app with no AI allowed, then a code review on every design choice.',
  rnd('Round 1 · Machine coding', L('take-home to-do app', 'take', 'blk', 64, b=True), L('no AI allowed', 'ai', 'red', 64), L('review: every design choice', 'review', 'blue', 58))),
 ('Round 2, DSA. Two medium problems hidden inside stories, one on graphs and one on sets.',
  rnd('Round 2 · DSA', L('2 mediums inside stories', 'stories', 'blk', 62, b=True), L('graphs', 'graphs', 'blue', 66), L('sets', 'sets', 'blue', 66))),
 ('Round 3, design Shazam. Turn audio into something you can match, store it, and scale it.',
  rnd('Round 3 · High-level design', L('→ design Shazam', 'shazam', 'red', 70, b=True), L('audio → something matchable', 'audio', 'blue', 58), L('storage + scale', 'store', 'blue', 64))),
 ('Round 4, hiring manager for over an hour. Production incidents, on call, and CI CD. Rejected days later, with no feedback.',
  rnd('Round 4 · Hiring manager', L('production incidents', 'production', 'blue', 62), L('on-call + CI/CD', 'call', 'blue', 62), big=('REJECTED', 'rejected', 'red'))),
 (OUTRO, outro()),
]
NARRATION, NB = make(S)
