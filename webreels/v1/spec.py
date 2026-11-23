# Format test V1 · interview roleplay (two voices). Same sources as webreels/s1e01/spec.py. 5000*4999/2 = 12,497,500.
EP = dict(id='V1', short='Two Sum interview roleplay', tail=1.2, bpm=100, drop_scenes=(5,), music_gain=.8, duck=.4)
WHO = ['I', 'C', 'I', 'C', 'I', 'C', 'I', 'C', 'C']   # I = interviewer (Kore), C = candidate (Fenrir)
NARRATION = [
    'Amazon interview, round one. Find two numbers in this list that add up to 500.',
    "Easy. I'll check every pair.",
    "With five thousand numbers? That's twelve million pairs. Faster, please.",
    "Okay. I'll walk the list once, and remember every number I've seen.",
    'And how does that help?',
    "Each number's partner is 500 minus it. If the partner is already saved, I'm done. One lookup.",
    'Complexity?',
    'O of n. One pass.',
    "Comment NOTES, and I'll send you five more questions like this.",
]
