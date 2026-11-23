from engine.nbspec import *
# Uber: Code360 (Oct 2025) https://www.naukri.com/code360/interview-experiences/uber/uber-interview-experience-by-vaidya-dandriyal-off-campus-oct-2025
# Salary: Levels.fyi Uber SWE I India Rs 35.7 L -> 35. Numbers: compute.py E18 ('chaichai' -> 4)
EP = epd('S1E18', 'Longest Substring Without Repeating Characters', 'Sliding window', 'Medium', 'longest-substring-without-repeating-characters', 'Uber', 'reported', 2025, 35, 'SWE I', 'grow right, shrink left')
A = list('chaichai')
S = [
 ('Want a 35 lakh job at Uber? This exact question came up in one of their recent interviews.', hook('Uber', 35, 'SWE I', 'reported', src='salary: Levels.fyi Uber SWE I India')),
 ('Find the longest stretch of text with no repeated letter.', ques('longest stretch of text', 'with no repeated letter')),
 ('Text: chai chai. Longest: c h a i. Length 4.', ex(A, '', spoken=False, big='longest = "chai" → 4', big_at='longest', ev=[['longest', dict(win=[0, 3, 'g'])]])),
 ('Checking every substring is n squared substrings, each checked again. Too slow.',
  dict(h=dict(t='Brute force: every substring', at=.05), lines=[L('n² substrings × a repeat check', 'every', 'blk'), L('✗ TOO SLOW', 'slow', 'red', 74)])),
 ('The trick: a sliding window. Grow the right side. On a repeat, shrink from the left.',
  dict(lines=[L('r grows the window', 'grow', 'blue', 60), L('repeat → l moves past it', 'repeat', 'red', 60, b=True)], ev=[['window', dict(ptr={'l': 0, 'r': 0}, win=[0, 0, 'g'])]])),
 ('c, h, a, i. Length 4. Next c is a repeat, left moves up. Same for h, a, i. The window never beats 4.',
  dict(ev=[[0.05, dict(ptr={'l': 0, 'r': 0}, win=[0, 0, 'g'], st='len 1')], ['h', dict(ptr={'r': 1}, win=[0, 1, 'g'], st='len 2')], ['a', dict(ptr={'r': 2}, win=[0, 2, 'g'], st='len 3')], ['i', dict(ptr={'r': 3}, win=[0, 3, 'g'], st='len 4')],
           ['repeat', dict(ptr={'r': 4}, win=[0, 4, 'r'], mark={0: 'bad'})], ['up', dict(ptr={'l': 1}, win=[1, 4, 'g'], mark={0: None}, st='len 4')], ['same', dict(ptr={'l': 4, 'r': 7}, win=[4, 7, 'g'])], ['never', dict(st='best = [4]')]])),
 ('Each letter enters and leaves the window once. O of n.', cx('O(n) time · O(k) space', 'O(n²)', 'Sliding window', 'map: letter → last index')),
 ('Comment NOTES, and I will send you five more sliding window questions.', cta('5 more sliding-window questions')),
]
NARRATION, NB = build(S, 'char', A)
