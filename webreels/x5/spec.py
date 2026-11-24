from engine.iespec import *
# LeetCode Discuss, Goldman Sachs Analyst, Bengaluru, Sep-Oct 2024: https://leetcode.com/discuss/interview-experience/6053956/
EP = epd('X5', 'Goldman Sachs Analyst interview', 'Interview experience', 'Medium', 'goldman-sachs-analyst', hook='6 rounds, offer', cover_t=2.0)
S = [
 ("Goldman Sachs analyst, Bengaluru. Six rounds, one stumble, and still an offer. Here's what they asked.", intro('Goldman Sachs', 'Analyst · Bengaluru', '6 rounds → [offer ✓]', s=110)),
 ('Round 1, an online test, one easy and one medium. Round 2, CoderPad. Fraction to recurring decimal, and trapping rain water in constant space.',
  rnd('Rounds 1-2 · OA + CoderPad', L('1 easy + 1 medium', 'easy', 'blue', 64), L('Fraction to Recurring Decimal', 'fraction', 'blue', 58), L('Trapping Rain Water, O(1) space', 'trapping', 'blk', 58, b=True))),
 ('Superday, data structures. Pairs of songs divisible by 60, and median of two sorted arrays. The optimal version failed some tests.',
  rnd('Round 3 · Data structures', L('Pairs of Songs, total ÷ 60', 'pairs', 'blue', 60), L('Median of Two Sorted Arrays', 'median', 'blue', 60), L('✗ optimal version failed tests', 'failed', 'red', 58, b=True))),
 ('Engineering practices. Sliding window maximum, threads and deadlocks, and a theater booking system with no double booking.',
  rnd('Round 4 · Engineering practices', L('Sliding Window Maximum', 'sliding', 'blue', 62), L('threads, deadlocks, semaphores', 'threads', 'blue', 58), L('theatre booking, no double-booking', 'theater', 'blk', 54, b=True))),
 ('Design round. Highest average from a marks table, Java comparators, and syncing records through Kafka when timestamps arrive out of order.',
  rnd('Round 5 · Design + architecture', L('highest average from marks', 'highest', 'blue', 60), L('Comparator vs Comparable', 'comparators', 'blue', 60), L('Kafka + out-of-order timestamps', 'kafka', 'blk', 56, b=True))),
 ('Hiring manager, about 20 minutes. Why leave, why Goldman. Offer two weeks later.',
  rnd('Round 6 · Hiring manager', L('why leave? why GS?', 'why', 'blue', 66), big=('OFFER ✓', 'offer'))),
 (OUTRO, outro()),
]
NARRATION, NB = make(S)
