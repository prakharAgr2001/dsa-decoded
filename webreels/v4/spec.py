# Format test V4 · quiz with countdown. Only pair summing to 500: 350 + 150 (checked).
EP = dict(id='V4', short='Two Sum quiz', tail=1.2, bpm=112, drop_scenes=(3,), music_gain=.9, duck=.4)
NARRATION = [
    'Amazon interview quiz. Can you beat the clock?',
    'Which two prices add up to 500? 120, 350, 280, 150, 400.',
    'Three seconds. Go! [[3]]',
    '350 and 150. Easy part done. Now the real question.',
    'What is the fastest way to find them? A: check every pair. B: sort first. C: a hash map.',
    'If you said C, you are right. Save each number, and look up its partner in one step. That is O of n.',
    'Every pair is O of n squared. Sorting is n log n.',
    'Comment your answer, and comment NOTES for five more quizzes like this.',
]
