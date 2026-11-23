"""Exact word timings for a voiceover from a transcription with word timestamps (e.g. Speko audio.transcribe word_timestamps=true).
  python3 -m engine.words ID transcript.json [--scale 1.3225] [--offset 0]
transcript.json = the transcription result ({"words": [{"text", "start_ms", "end_ms"}, ...]}) of the RAW voice file.
--scale: the atempo applied when making vo/ID.wav from that raw file (times are divided by it); --offset: seconds trimmed from the start.
Writes vo/ID.words.json: one [start, end] per script word (engine.build uses it instead of silence-based estimates).
Script words that the transcript spells differently (7 vs seven, 2, 0, 4 vs 204) are matched by sequence alignment; gaps are spread evenly."""
import difflib, json, re, sys, importlib
import engine.build as B
import engine.webreel as WR

NUM = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}
def norm(w):
    w = re.sub(r"[^a-z0-9']", '', w.lower().replace(',', ''))
    return NUM.get(w, w)

def main(epid, tpath, scale=1.0, offset=0.0):
    B.load = WR.spec
    ep, scenes = B.load(epid)
    words = [w['w'] for w in B.parse(scenes)[0]]
    T = json.load(open(tpath))['words']
    tw = [norm(w['text']) for w in T]; sw = [norm(w) for w in words]
    t = lambda ms: max(0.0, ms / 1000 / scale - offset)
    out = [None] * len(sw)
    for a, b, n in difflib.SequenceMatcher(None, sw, tw, autojunk=False).get_matching_blocks():
        for k in range(n): out[a + k] = [t(T[b + k]['start_ms']), t(T[b + k]['end_ms'])]
    # fill unmatched runs evenly between the neighbouring matched words
    i = 0
    while i < len(out):
        if out[i] is not None: i += 1; continue
        j = i
        while j < len(out) and out[j] is None: j += 1
        lo = out[i - 1][1] if i else 0.0
        hi = out[j][0] if j < len(out) else lo + .3 * (j - i)
        step = (hi - lo) / (j - i)
        for k in range(i, j): out[k] = [lo + step * (k - i), lo + step * (k - i + 1) - .02]
        print(f'  filled {j - i} word(s): {" ".join(words[i:j])}  ({lo:.2f}-{hi:.2f}s)')
        i = j
    json.dump([[round(a, 3), round(b, 3)] for a, b in out], open(f'vo/{epid}.words.json', 'w'))
    print(f'vo/{epid}.words.json: {len(out)} words')

if __name__ == '__main__':
    a = sys.argv[1:]; kw = {}
    for flag in ('--scale', '--offset'):
        if flag in a: i = a.index(flag); kw[flag[2:]] = float(a[i + 1]); del a[i:i + 2]
    main(a[0].upper(), a[1], **kw)
