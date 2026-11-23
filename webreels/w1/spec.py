# Sources (checked 2026-11-23):
# Amazon reports: Glassdoor AWS interview question "Two Sum + some variations" (29 Mar 2025) https://www.glassdoor.sg/Interview/Coding-Two-Sum-some-variations-QTN_8114209.htm
#                 Taro Amazon SDE2 Bengaluru (22 Sep 2025) https://www.jointaro.com/interviews/companies/amazon/experiences/software-engineer-ii-sde2-bengaluru-september-22-2025-accepted-offer-positive-770a13db
#                 Taro Amazon SDE intern Seattle (11 Jun 2025) https://www.jointaro.com/interviews/companies/amazon/experiences/sde-intern-seattle-wa-june-11-2025-no-offer-positive-d13c8ac3
# Salary: Amazon SDE-1 India 0-3 yrs Rs 14.5-30 L (AmbitionBox https://ambitionbox.com/salaries/amazon-salaries/sde-1-position);
#         public offer Apr 2025 base Rs 19.17 L + sign-on Rs 6.47 L (https://leetcode.com/discuss/post/6689833/) -> hook "28 lakh" inside range
# Numbers on screen: example [120,350,280,150,400] target 500 -> only pair (1,3) (checked with node);
#                    brute force pairs for n=5,000: 5000*4999/2 = 12,497,500
EP = dict(id='W1', short='Two Sum notebook', tail=1.0, bpm=108, drop_scenes=(4,), music_gain=.7, duck=.45)
NARRATION = [
    'Want a 28 lakh job at Amazon? This exact question keeps showing up in their interviews.',
    'Here it is: find two numbers in a list that add up to a target.',
    'Prices: 120, 350, 280, 150, 400. Target: 500. The answer? 350 and 150.',
    "Most people check every pair. For 5,000 numbers, that's over 12 million checks. Rejected.",
    'The trick? A hash map. For every number, ask one question: have I already seen my partner?',
    '120 needs 380. Not seen. Save it. 350 needs 150. Not seen. Save it. 280 needs 220. Save it.',
    'Now 150 needs 350. Already in the map, at index one. Done!',
    'Like the register at your society gate: one look, and you know who came in.',
    "One pass, one lookup per number. That's O of n.",
    "Comment NOTES, and I'll send you five more questions with this exact pattern.",
]
