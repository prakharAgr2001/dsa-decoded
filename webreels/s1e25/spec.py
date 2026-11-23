from engine.nbspec import *
# Amazon: Taro (1 Apr 2025) https://www.jointaro.com/interviews/companies/amazon/experiences/software-development-engineer-sde-bangalore-rural-april-1-2025-no-offer-neutral-a87159ec/ ; LeetCode (Apr 2026, SDE-1) https://leetcode.com/discuss/post/8014509/
# Salary: AmbitionBox Amazon SDE-1 0-3 yrs Rs 14.5-30 L -> 28. Numbers: compute.py E25 ([15,18,22,3,6,9,12] t=6: mids 3, 9, 6 -> index 4)
EP = epd('S1E25', 'Search in Rotated Sorted Array', 'Binary search', 'Medium', 'search-in-rotated-sorted-array', 'Amazon', 'asked', 2026, 28, 'SDE-1', 'one half is always sorted')
A = [15, 18, 22, 3, 6, 9, 12]
S = [
 ('Want a 28 lakh job at Amazon? This exact question keeps showing up in their interviews.', hook('Amazon', 28, 'SDE-1', 'asked', 2026, src='salary: AmbitionBox range for SDE-1')),
 ('A sorted list was rotated. Find 6 in log n time.', ques('sorted list, then rotated.', 'find 6 in O(log n)')),
 ('Numbers: 15, 18, 22, 3, 6, 9, 12. 6 is at index 4.', ex(A, 'Numbers: 15, 18, 22, 3, 6, 9, 12.', big='→ index 4', big_at='index')),
 ('A full scan is O of n. And normal binary search breaks, because the list is not fully sorted.',
  dict(h=dict(t='The obvious answers', at=.05), lines=[L('scan → O(n)', 'scan', 'red'), L('plain binary search → wrong half', 'breaks', 'red')])),
 ('The trick: cut at the middle. One half is always sorted. Check if 6 is inside that sorted half.',
  dict(lines=[L('one half is ALWAYS sorted', 'always', 'blk', 60, b=True), L('target inside it? go there. else other half', 'inside', 'grn', 50)], ev=[['middle', dict(ptr={'lo': 0, 'hi': 6})]])),
 ('Middle is 3. The right half, 3 to 12, is sorted, and 6 is inside. Go right. Middle is 9. Left half, 6 to 9, is sorted, 6 is inside. Go left. Found 6 at index 4.',
  dict(ev=[[0.05, dict(ptr={'lo': 0, 'hi': 6, 'mid': 3})], ['sorted#1', dict(win=[3, 6, 'g'])], ['right#2', dict(ptr={'lo': 4, 'mid': 5}, win=None)], ['9#2', dict(win=[4, 5, 'g'])], ['left#2', dict(ptr={'hi': 4, 'mid': 4}, win=None)], ['found', dict(mark={4: 'ok'}, st='index [4] ✓')]])),
 ('Half the list is gone every step. O of log n.', cx('O(log n) time · O(1) space', 'O(n)', 'Binary search', 'find the sorted half first')),
 ('Comment NOTES, and I will send you five more binary search questions.', cta('5 more binary-search questions')),
]
NARRATION, NB = build(S, 'num', A)
