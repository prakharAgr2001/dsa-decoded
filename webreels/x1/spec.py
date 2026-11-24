from engine.nbspec import *
# Interview-experience reel (not a DSA episode). Source: LeetCode Discuss, Flipkart UI Engineer 2, Bangalore, interviewed Jun 2025, offer Jul 2025
# https://leetcode.com/discuss/post/6909362/flipkart-ui-engineer-2-bangalore-july-20-6rlz/
EP = epd('X1', 'Flipkart UI Engineer 2 interview', 'Interview experience', 'Medium', 'flipkart-ui-engineer-2', hook='5 rounds, selected', cover_t=2.0)
H = lambda t: dict(t=t, at=.02, s=74, c='red')
S = [
 ("Flipkart UI Engineer 2. Five rounds, and this candidate got selected. Here's exactly what they asked.",
  dict(vis=False, y0=560, lines=[L('Flipkart', 'flipkart', 'blk', 130, b=True), L('UI Engineer 2', 'ui', 'blue', 95), L('5 rounds → [selected ✓]', 'rounds', 'grn', 66, b=True), L('here is exactly what they asked', 'exactly', 'red', 59)])),
 ('Round 1, machine coding. Build a chat app live, in 90 minutes, with about 15 candidates on the same call.',
  dict(vis=False, y0=520, h=H('Round 1 · Machine coding'), lines=[L('build a chat app, LIVE', 'chat', 'blk', 66, b=True), L('90 minutes', '90', 'red', 77), L('~15 candidates on the same call', '15', 'blue', 62)])),
 ('Round 2, they reviewed that code line by line. Functional versus class components, DOM performance, then write debounce live.',
  dict(vis=False, y0=520, h=H('Round 2 · Code review'), lines=[L('explain every line you wrote', 'line', 'blk', 66), L('functional vs class components', 'functional', 'blue', 62), L('DOM performance', 'dom', 'blue', 67), L('→ write debounce() live', 'debounce', 'red', 66, b=True)])),
 ('Round 3, DSA. Course Schedule, and a Merge Intervals variation.',
  dict(vis=False, y0=520, h=H('Round 3 · DSA'), lines=[L('Course Schedule', 'course', 'blk', 87, b=True), L('graph · topological sort', 'schedule', 'gry', 52), L('Merge Intervals (variation)', 'merge', 'blk', 66, b=True)])),
 ('Round 4, pure frontend. Shrink the build size, a local storage wrapper with expiry, async versus defer, and Promise dot race versus Promise dot any, with polyfills.',
  dict(vis=False, y0=520, h=H('Round 4 · Pure frontend'), lines=[L('shrink the build size', 'shrink', 'blue', 70), L('localStorage wrapper + expiry', 'local', 'blue', 64), L('async vs defer', 'async', 'blue', 70), L('Promise.race vs Promise.any', 'race', 'blk', 64, b=True), L('→ polyfills for both', 'polyfills', 'red', 75, b=True)])),
 ('Round 5, hiring manager. Past projects, teamwork, and how you think. No grilling.',
  dict(vis=False, y0=520, h=H('Round 5 · Hiring manager'), lines=[L('past projects', 'past', 'blue', 72), L('teamwork', 'teamwork', 'blue', 72), L('how you think', 'think', 'blue', 72)], big=dict(t='SELECTED ✓', at='grilling', c='grn'))),
 ('Comment NOTES, and I will send you all 13 frontend questions from round 4.', cta('all 13 round-4 questions')),
]
NARRATION, NB = build(S, 'char', ['F'])
