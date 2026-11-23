# Sources (checked 2026-11-23):
# Goldman Sachs reports: LeetCode Discuss GS Analyst Hyd/Blr (Feb 2025) https://leetcode.com/discuss/interview-experience/6482400/
#                        LeetCode Discuss GS Analyst (Apr 2025) https://leetcode.com/discuss/post/6717915/my-interview-experience-at-goldman-sachs-q77z/
#                        Taro GS Software Engineer New Delhi (1 Aug 2025) https://www.jointaro.com/interviews/companies/goldman-sachs/experiences/software-engineer-new-delhi-august-1-2025-no-offer-negative-2361a6ac/
# Salary: GS Analyst, Engineering dept Rs 22.7-25.3 LPA (AmbitionBox via upGrad, 2026); Levels.fyi GS Analyst India Rs 26.9 L -> hook "25 lakh"
# Numbers (checked with node): heights [2,0,4,1,0,3] -> water 7 (bar1: 2, bar3: 2, bar4: 3).
#   two pointers: L0 lmax2 +0 | L1 +2 | R5 rmax3 +0 | R4 +3 | R3 +2 -> 7
#   brute force for n=5,000: each bar scans left (i+1) and right (n-i) -> n(n+1)... exact sum = 25,005,000 reads
EP = dict(id='S1E16', short='Trapping Rain Water', title='Trapping Rain Water', pattern='Two pointers', difficulty='Hard',
          official='https://leetcode.com/problems/trapping-rain-water/', company='Goldman Sachs', claim='asked', year=2025, lpa=25, role='Analyst',
          hook='move the shorter wall', cover_t=24.0, tail=0.8, bpm=108, drop_scenes=(5,), music_gain=.7, duck=.45)
NARRATION = [
    'Want a 25 lakh job at Goldman Sachs? This question keeps showing up in their interviews.',
    'Rain falls on these bars. How much water stays trapped?',
    'Heights: 2, 0, 4, 1, 0, 3. The answer is 7 units.',
    "Brute force: for every bar, scan left and right for the tallest wall. For 5,000 bars, that's 25 million steps. Rejected.",
    'The rule: water on a bar is the smaller of its two tallest walls, minus its own height.',
    'The trick: two pointers. Always move the side with the shorter wall, because its water is already decided.',
    'Left is shorter. Left max is 2. Bar one holds 2 minus 0. That is 2.',
    'Now right is shorter. Right max is 3. Bar four holds 3. Bar three holds 3 minus 1. That is 2.',
    'Total: 2 plus 3 plus 2. Seven units.',
    'One pass, no extra arrays. O of n time, O of 1 space.',
    "Comment NOTES, and I'll send you five more two pointer questions.",
]
