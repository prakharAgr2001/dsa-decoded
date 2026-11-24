from engine.iespec import *
# LeetCode Discuss, Zomato SDE-1 (UI), Jun 2025: https://leetcode.com/discuss/post/8359475/zomato-sde-1-ui-interview-experience-by-84krj/
EP = epd('X3', 'Zomato SDE-1 UI interview', 'Interview experience', 'Medium', 'zomato-sde-1-ui', hook='strong hire, every round', cover_t=2.0)
S = [
 ("Zomato SDE 1, frontend. Three rounds, and a strong hire in every one. Here's what they asked.", intro('Zomato', 'SDE-1 · Frontend (UI)', '3 rounds → [strong hire ✓]')),
 ('Round 1, UI and machine coding. The event loop, React reconciliation, output questions, browser internals, and rendering performance.',
  rnd('Round 1 · UI + machine coding', L('event loop', 'event', 'blue', 66), L('React reconciliation', 'reconciliation', 'blue', 64), L('"what does this print?"', 'output', 'blk', 60), L('browser internals', 'browser', 'blue', 64), L('rendering performance', 'rendering', 'blue', 64))),
 ('Round 2, about 90 minutes. Polyfills, React internals, then design Google Calendar.',
  rnd('Round 2 · UI + system design', L('polyfills', 'polyfills', 'blue', 70), L('React internals', 'internals', 'blue', 70), L('→ design Google Calendar', 'calendar', 'red', 66, b=True))),
 ('Round 3, onsite with the VP of technology. Why Zomato, your goals, and are you ready for the ownership. Selected.',
  rnd('Round 3 · VP of Technology', L('why Zomato?', 'why', 'blue', 66), L('your career goals', 'goals', 'blue', 66), L('ready for the ownership?', 'ownership', 'blk', 64, b=True), big=('SELECTED ✓', 'selected'))),
 (OUTRO, outro()),
]
NARRATION, NB = make(S)
