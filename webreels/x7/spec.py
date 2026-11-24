from engine.iespec import *
# LeetCode Discuss, Palo Alto Networks (undated, India): https://leetcode.com/discuss/post/6775812/palo-alto-networks-interview-experience-rrahz/
EP = epd('X7', 'Palo Alto Networks interview', 'Interview experience', 'Medium', 'palo-alto-networks', hook='strong DSA, still rejected', cover_t=2.0)
S = [
 ("Palo Alto Networks. Strong in DSA, and still not selected. Here's what went wrong.", intro('Palo Alto Networks', 'Software Engineer · India', '3 rounds → [not selected]', 'red', at_co='palo', s=96)),
 ('Round 1, online test. DSA multiple choice questions, then two basic coding problems.',
  rnd('Round 1 · Online test', L('DSA multiple choice', 'multiple', 'blue', 66), L('2 basic coding problems', 'coding', 'blue', 64))),
 ('Round 2, DSA. Complexity, alternative approaches, and explaining your thinking out loud.',
  rnd('Round 2 · DSA', L('time + space complexity', 'complexity', 'blue', 62), L('other approaches', 'alternative', 'blue', 64), L('think out loud', 'explaining', 'blk', 66, b=True))),
 ('Round 3, core CS. Build data structures from scratch, hashing, browser internals, networks and operating systems.',
  rnd('Round 3 · Core CS', L('data structures from scratch', 'scratch', 'blue', 58), L('hashing + rehashing', 'hashing', 'blue', 62), L('browser internals', 'browser', 'blue', 62), L('networks + OS', 'networks', 'red', 66, b=True))),
 ('The feedback: strong in DSA, weak in networks and OS. Being a good coder alone was not enough.',
  rnd('The feedback', L('DSA ✓', 'strong', 'grn', 72, b=True), L('networks + OS ✗', 'weak', 'red', 72, b=True), L('coding alone is not enough', 'enough', 'blk', 60, b=True))),
 (OUTRO, outro()),
]
NARRATION, NB = make(S)
