# Format test V2 · split-screen race. Pairs n(n-1)/2: n=5 -> 10, 5,000 -> 12,497,500, 50,000 -> 1,249,975,000.
# At 1,000,000 checks/s: 1,249,975,000 -> 1,250 s = 20.8 min; hash map 50,000 -> 0.05 s.
EP = dict(id='V2', short='Two Sum race', tail=1.2, bpm=124, drop_scenes=(5, 7), music_gain=1.0, duck=.35)
NARRATION = [
    'Same question, two methods. Let us race.',
    'Find two numbers in a list that add up to a target.',
    'Five numbers. Check every pair: ten checks. Hash map: five.',
    'Five thousand numbers. Every pair: twelve and a half million. Hash map: five thousand.',
    'Fifty thousand? One point two five billion, versus fifty thousand.',
    'At a million checks a second, that is twenty one minutes, versus a twentieth of a second.',
    'Why? The hash map remembers every number it has seen, so finding a partner is one lookup.',
    'Winner: hash map. O of n.',
    'Comment NOTES for five more questions with this pattern.',
]
