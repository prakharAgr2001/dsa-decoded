# Sources (checked 2026-11-23):
# Amazon reports: Glassdoor AWS interview question "Two Sum + some variations" (29 Mar 2025) https://www.glassdoor.sg/Interview/Coding-Two-Sum-some-variations-QTN_8114209.htm
#                 Taro Amazon SDE2 Bengaluru (22 Sep 2025) https://www.jointaro.com/interviews/companies/amazon/experiences/software-engineer-ii-sde2-bengaluru-september-22-2025-accepted-offer-positive-770a13db
#                 Taro Amazon SDE intern Seattle (11 Jun 2025) https://www.jointaro.com/interviews/companies/amazon/experiences/sde-intern-seattle-wa-june-11-2025-no-offer-positive-d13c8ac3
# Salary: Amazon SDE-1 India 0-3 yrs Rs 14.5-30 L (AmbitionBox https://ambitionbox.com/salaries/amazon-salaries/sde-1-position);
#         public offer Apr 2025 base Rs 19.17 L + sign-on Rs 6.47 L (https://leetcode.com/discuss/post/6689833/) -> hook "28 lakh" inside range
# Numbers on screen: example [120,350,280,150,400] target 500 -> only pair (1,3) (checked with node);
#                    brute force pairs for n=5,000: 5000*4999/2 = 12,497,500
EP = dict(id='W2', short='Two Sum notebook 30s', tail=0.7, bpm=116, drop_scenes=(3,), music_gain=.7, duck=.45)
NARRATION = [
    '28 lakh at Amazon? This question keeps showing up in their interviews.',
    'Prices: 120, 350, 280, 150, 400. Which two add up to 500?',
    "Checking every pair? For 5,000 numbers, that's 12 million checks. Rejected.",
    'The trick: for each number, ask, have I already seen 500 minus it?',
    '120 needs 380. Save it. 350 needs 150. Save it. 280 needs 220. Save it.',
    '150 needs 350. Already seen. Done!',
    "One pass. That's O of n.",
    'Comment NOTES for five variations of this question.',
]
