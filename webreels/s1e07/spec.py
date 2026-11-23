from engine.nbspec import *
# Amazon: Code360 Amazon intern OA (26 Sep 2025) https://www.naukri.com/code360/interview-experiences/amazon/amazon-interview-experience-by-mohit-vohra-off-campus-sep-2025
#         Glassdoor Amazon SDE intern OA (Apr 2026) https://www.glassdoor.com/Interview/Amazon-Interview-E6036-RVW104097638.htm ; LeetCode Amazon SDE-1 (Apr 2026, circular variant) https://leetcode.com/discuss/post/8014509/
# Salary: AmbitionBox Amazon SDE-1 0-3 yrs Rs 14.5-30 L -> 28. Numbers: compute.py E07 ([2,-4,3,-1,4,-6,2] -> 6; subarrays n=5,000: 12,502,500)
EP = epd('S1E07', 'Maximum Subarray', "Kadane's algorithm", 'Medium', 'maximum-subarray', 'Amazon', 'asked', 2026, 28, 'SDE-1', 'extend or restart')
A = [2, -4, 3, -1, 4, -6, 2]
S = [
 ('Want a 28 lakh job at Amazon? This exact question keeps showing up in their interviews.', hook('Amazon', 28, 'SDE-1', 'asked', 2026, src='salary: AmbitionBox range for SDE-1')),
 ('Find the contiguous part of the list with the biggest sum.', ques('the contiguous part', 'with the biggest sum')),
 ('Numbers: 2, minus 4, 3, minus 1, 4, minus 6, 2. Best is 3, minus 1, 4. Sum 6.', ex(A, '2 -4 3 -1 4 -6 2', spoken=False, big='3 − 1 + 4 = 6', big_at='best', ev=[['best', dict(win=[2, 4, 'g'])]])),
 ("Brute force adds up every subarray. For 5,000 numbers, that's 12 and a half million of them. Rejected.",
  dict(h=dict(t='Brute force: sum every subarray', at=.05), lines=[L('n = 5,000 → [12,502,500] subarrays', '5000', 'blk'), L('✗ TOO SLOW · O(n²)', 'rejected', 'red', 74)])),
 ("The trick: at each number, decide. Extend the running sum, or restart from here. Keep whichever is bigger.",
  dict(lines=[L("Kadane: cur = max(x, cur + x)", 'trick', 'blk', 60, b=True, box='blue'), L('negative past? → restart', 'restart', 'red', 58)])),
 ('2. Minus 4 drops it to minus 2. 3 beats extending, restart at 3. Minus 1, 2. 4 pushes it to 6. Minus 6, 0. 2, 2. Best stays 6.',
  dict(table=T(['x', 'cur', 'best'], [[2, 2, 2], [-4, -2, 2], [3, 3, 3], [-1, 2, 3], [4, 6, 6], [-6, 0, 6], [2, 2, 6]], [300, 300, 300]),
       ev=[[0.1, dict(ptr={'i': 0}, row=0, win=[0, 0, 'g'])], ['4#1', dict(ptr={'i': 1}, row=1, win=[0, 1, 'r'])], ['3', dict(ptr={'i': 2}, row=2, win=[2, 2, 'g'])], ['1', dict(ptr={'i': 3}, row=3, win=[2, 3, 'g'])],
           ['4#2', dict(ptr={'i': 4}, row=4, win=[2, 4, 'g'])], ['6#2', dict(ptr={'i': 5}, row=5, win=[2, 5, 'r'])], ['2#4', dict(ptr={'i': 6}, row=6)], ['best', dict(win=[2, 4, 'g'], st='best = [6] (index 2 to 4)')]])),
 ("One pass. That's O of n.", cx('O(n) time · O(1) space', 'O(n²)', "Kadane", 'extend or restart at every number')),
 ('Comment NOTES, and I will send you five more subarray questions.', cta('5 more subarray questions')),
]
NARRATION, NB = build(S, 'num', A)
