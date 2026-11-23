# Sources (checked 2026-11-23):
# Amazon reports: Glassdoor AWS interview question "Two Sum + some variations" (29 Mar 2025) https://www.glassdoor.sg/Interview/Coding-Two-Sum-some-variations-QTN_8114209.htm
#                 Taro Amazon SDE2 Bengaluru (22 Sep 2025) https://www.jointaro.com/interviews/companies/amazon/experiences/software-engineer-ii-sde2-bengaluru-september-22-2025-accepted-offer-positive-770a13db
#                 Taro Amazon SDE intern Seattle (11 Jun 2025) https://www.jointaro.com/interviews/companies/amazon/experiences/sde-intern-seattle-wa-june-11-2025-no-offer-positive-d13c8ac3
# Salary: Amazon SDE-1 India 0-3 yrs Rs 14.5-30 L (AmbitionBox https://ambitionbox.com/salaries/amazon-salaries/sde-1-position);
#         public offer Apr 2025 base Rs 19.17 L + sign-on Rs 6.47 L (https://leetcode.com/discuss/post/6689833/) -> hook "28 lakh" inside range
# Numbers on screen: example [120,350,280,150,400] target 500 -> only pair (1,3) (checked with node);
#                    brute force pairs for n=5,000: 5000*4999/2 = 12,497,500
EP = dict(id='S1E01', short='Two Sum', title='Two Sum', pattern='Hashing', difficulty='Easy',
          official='https://leetcode.com/problems/two-sum/', company='Amazon', claim='asked', year=2025, lpa=28, role='SDE-1',
          hook='the one-pass hash map trick', cover_t=20.0, tail=1.2, bpm=116, drop_scenes=(4, 6), music_gain=1.0, duck=.35,
          asked=[dict(company='Amazon', role='SDE (AWS)', year=2025, source='Glassdoor', url='https://www.glassdoor.sg/Interview/Coding-Two-Sum-some-variations-QTN_8114209.htm'),
                 dict(company='Amazon', role='SDE-2, Bengaluru', year=2025, source='Taro', url='https://www.jointaro.com/interviews/companies/amazon/experiences/software-engineer-ii-sde2-bengaluru-september-22-2025-accepted-offer-positive-770a13db'),
                 dict(company='Amazon', role='SDE intern', year=2025, source='Taro', url='https://www.jointaro.com/interviews/companies/amazon/experiences/sde-intern-seattle-wa-june-11-2025-no-offer-positive-d13c8ac3')],
          similar=[dict(name='Contains Duplicate', url='https://leetcode.com/problems/contains-duplicate/', difficulty='Easy'),
                   dict(name='Two Sum II (sorted input)', url='https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/', difficulty='Medium'),
                   dict(name='Group Anagrams', url='https://leetcode.com/problems/group-anagrams/', difficulty='Medium', companies=['Adobe']),
                   dict(name='Subarray Sum Equals K', url='https://leetcode.com/problems/subarray-sum-equals-k/', difficulty='Medium', companies=['Google']),
                   dict(name='4Sum II', url='https://leetcode.com/problems/4sum-ii/', difficulty='Medium')])
NARRATION = [
    'Want a 28 lakh job at Amazon? This exact question keeps showing up in their interviews.',
    'Here it is: find two numbers in a list that add up to a target.',
    'Prices: 120, 350, 280, 150, 400. Target: 500. The answer? [[0.4]] 350 and 150.',
    "Most people check every pair. For 5,000 numbers, that's over 12 million checks. [[0.3]] Rejected.",
    'The trick? A hash map. For every number, ask: have I already seen my partner?',
    '120 needs 380. Not seen, save it. 350 needs 150. Save it. 280 needs 220. Save it.',
    'Now 150 needs 350. It is already in the map. [[0.4]] Done!',
    "One pass. That's O of n.",
    "Comment NOTES, and I'll send you five more questions with this exact pattern.",
]
