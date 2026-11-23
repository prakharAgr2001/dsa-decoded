# Format V5 kinetic, script v2. Sources: see webreels/s1e01/spec.py (Amazon asked 2025; SDE-1 Rs 14.5-30 L -> 28).
# Numbers: [120,350,280,150,400] target 500 -> only pair 350+150; 5,000 numbers -> 5000*4999/2 = 12,497,500 pairs.
EP = dict(id='V6', short='Two Sum 20s script v2', tail=1.4, bpm=128, drop_scenes=(3, 4), music_gain=1.1, duck=.3)
NARRATION = [
    'Amazon. 28 lakh package. And this question keeps coming up.',
    'Find two numbers that add up to 500.',
    'Most people check every pair. Five thousand numbers? Twelve million checks. Rejected.',
    "The trick: don't search. Remember.",
    'At 150, ask one thing: have I seen 350? Yes. Done.',
    'One pass. O of n.',
    'Comment NOTES. I will DM you five variations of this question.',
]
