"""One-command episode pipeline (notebook episodes).
  python3 -m engine.ep prep ID raw.wav 0,5200,8700,...   # raw TTS + scene-start ms (from Speko audio.transcribe word_timestamps) -> vo/ID.wav, anchors, sheet
  python3 -m engine.ep render ID [ID ...]   # out/ID_*.mp4 (sequential; run two shells for 2 cores)
TTS: Speko audio.synthesize, voice Fenrir, speed 1.2, text = `python3 -m engine.webreel text ID` (one paragraph per scene), instructions = VOICE.
Scene anchors: the N-1 longest pauses in the voice are the paragraph breaks; each is cut to GAP s, so pace stays fast and scenes start exactly."""
import json, re, subprocess, sys
import engine.webreel as W
VOICE = ("Young Indian male tech creator on Instagram, Indian English accent, warm, confident, energetic, conversational, punchy hook, "
         "clear teaching rhythm. Read digits in number lists one by one. Say 'O of n' clearly.")
GAP = .28
def sh(*a): return subprocess.run(a, capture_output=True, text=True)
def dur(p): return float(sh('ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p).stdout)
def prep(epid, raw, anchors_ms):
    """anchors_ms: raw-audio start (ms) of each scene's first word, from a word-timestamp transcription of the raw TTS."""
    ep, scenes = W.spec(epid); anc = [int(x) for x in anchors_ms.split(',')]; assert len(anc) == len(scenes), f'{epid}: {len(anc)} anchors for {len(scenes)} scenes'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-ac', '1', '-ar', '48000', '-af', 'atempo=1.15,atempo=1.15,highpass=f=80,equalizer=f=3200:t=q:w=1.2:g=2,'
                    'acompressor=threshold=-20dB:ratio=3:attack=6:release=80:makeup=2,loudnorm=I=-15:TP=-1.5:LRA=9', '-sample_fmt', 's16', f'vo/{epid}.wav'], check=True)
    json.dump([0.0] + [round(max(0, x / 1000 / 1.3225 - .06), 3) for x in anc[1:]], open(f'vo/{epid}.anchors.json', 'w'))
    print(f'{epid}: {dur(raw):.1f}s raw -> {dur(f"vo/{epid}.wav"):.1f}s')
    subprocess.run([sys.executable, '-m', 'engine.webreel', 'check', epid], check=True)
if __name__ == '__main__':
    cmd, a = sys.argv[1], sys.argv[2:]
    if cmd == 'prep': prep(a[0].upper(), a[1], a[2])
    if cmd == 'render':
        for e in a: subprocess.run([sys.executable, '-m', 'engine.webreel', 'render', e.upper()], check=True)
