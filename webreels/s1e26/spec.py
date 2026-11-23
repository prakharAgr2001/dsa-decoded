from engine.nbspec import *
# Flipkart: Glassdoor (Apr 2025, SDE intern) https://www.glassdoor.ca/Interview/Flipkart-Interview-E300494-RVW99627426.htm ; also Swiggy (Dec 2024) https://www.naukri.com/code360/interview-experiences/swiggy/interview-experience-dec-2024-exp-0-2-years
# Salary: Levels.fyi Flipkart SDE 1 avg Rs 22.4 L -> 22. Numbers: compute.py E26 (piles [4,9,6,12], h=8: speed 6 -> 6h, 3 -> 11h, 5 -> 8h, 4 -> 9h; answer 5)
EP = epd('S1E26', 'Koko Eating Bananas', 'Binary search on answer', 'Medium', 'koko-eating-bananas', 'Flipkart', 'reported', 2025, 22, 'SDE-1', 'binary search the speed')
A = [4, 9, 6, 12]
S = [
 ('Want a 22 lakh job at Flipkart? This exact question came up in one of their recent interviews.', hook('Flipkart', 22, 'SDE-1', 'reported', src='salary: Levels.fyi Flipkart SDE 1 average')),
 ('Koko eats bananas from piles, one pile per hour at most. Find the slowest speed that finishes in 8 hours.', ques('slowest eating speed', 'that finishes in 8 hours', note='one pile per hour, at most')),
 ('Piles: 4, 9, 6, 12. Answer: 5 bananas per hour.', ex(A, 'Piles: 4, 9, 6, 12.', big='speed = 5', big_at='answer')),
 ('Trying every speed from 1 up to 12 works, but the speed can go up to a billion. Rejected.',
  dict(h=dict(t='Brute force: try every speed', at=.05), lines=[L('speeds 1 … max pile', 'every', 'blk'), L('✗ max pile can be 10⁹', 'billion', 'red', 62)])),
 ('The trick: binary search the speed. Fast enough? Try slower. Too slow? Try faster.',
  dict(lines=[L('hours(speed) ≤ 8 → try slower', 'enough', 'grn', 56), L('hours(speed) > 8 → try faster', 'faster', 'red', 56), L('hours = Σ ceil(pile / speed)', 'speed#1', 'gry', 46)])),
 ('Speed 6: 6 hours, fine. Speed 3: 11 hours, too slow. Speed 5: 8 hours, fine. Speed 4: 9 hours, too slow. So 5.',
  dict(table=T(['speed', 'hours', 'ok?'], [[6, '1+2+1+2 = 6', 'yes'], [3, '2+3+2+4 = 11', 'no'], [5, '1+2+2+3 = 8', 'yes'], [4, '1+3+2+3 = 9', 'no']], [180, 440, 160]),
       ev=[['6#2', dict(row=0)], ['11', dict(row=1)], ['8#1', dict(row=2)], ['9', dict(row=3)], ['so', dict(st='slowest speed = [5]')]])),
 ('Log of the max pile steps, each checking every pile. O of n log m.', cx('O(n log m) time · O(1) space', 'O(n·m)', 'Binary search on answer', 'm = biggest pile')),
 ('Comment NOTES, and I will send you five more binary search questions.', cta('5 more binary-search questions')),
]
NARRATION, NB = build(S, 'num', A)
