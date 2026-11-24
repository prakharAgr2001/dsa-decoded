from engine.iespec import *
# LeetCode Discuss, Intuit SDE-2, Jun 2025: https://leetcode.com/discuss/interview-experience/6991433
EP = epd('X6', 'Intuit SDE-2 interview', 'Interview experience', 'Medium', 'intuit-sde-2', hook='craft demo, offer', cover_t=2.0)
S = [
 ("Intuit SDE 2, with only two years of experience. Five rounds, and an offer. Here's what they asked.", intro('Intuit', 'SDE-2 · 2 years exp', '5 rounds → [offer ✓]')),
 ('Round 1, the eliminator. Count paths through a grid of ones, then GenAI questions, and write a prompt that returns only JSON.',
  rnd('Round 1 · Eliminator', L('count grid paths through 1s', 'paths', 'blue', 60), L('how do you use GenAI?', 'genai', 'blue', 62), L('→ prompt that returns only JSON', 'prompt', 'red', 58, b=True))),
 ('Round 2, the craft demo, 90 minutes. Add a REST API to a Java project, with tests, after 15 minutes of design questions.',
  rnd('Round 2 · Craft demo', L('15 min of design questions first', 'design', 'red', 56), L('add a REST API to a Java repo', 'rest', 'blk', 58, b=True), L('with unit tests', 'tests', 'blue', 64))),
 ('Round 3, problem solving. Balanced brackets with a stack, then scaling, rate limiters, and the thundering herd.',
  rnd('Round 3 · Problem solving', L('balanced brackets (stack)', 'brackets', 'blue', 62), L('scaling + rate limiters', 'scaling', 'blue', 62), L('thundering herd', 'thundering', 'blk', 66, b=True))),
 ('Then a team member chat and the hiring manager. Offer, which they declined for remote work.',
  rnd('Rounds 4-5 · Team + HM', L('team member chat', 'team', 'blue', 64), L('hiring manager', 'hiring', 'blue', 64), big=('OFFER ✓', 'offer'))),
 (OUTRO, outro()),
]
NARRATION, NB = make(S)
