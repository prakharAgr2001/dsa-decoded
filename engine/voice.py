"""Voiceover post-processing (ffmpeg only). Output is always mono 48 kHz 16-bit WAV at vo/<ID>.wav.
  python3 -m engine.voice tts   S1E01 raw.wav [--fit 44]   # Speko/TTS output: trim silences, EQ, compress, -15 LUFS, atempo to fit
  python3 -m engine.voice clean S1E01 mine.m4a [--fit 44]  # own recording: denoise, EQ, de-ess, 2-stage comp, -14 LUFS
--fit N: if the speech is longer than N seconds, speed it up with atempo (max 1.15x) so the reel stays in 35-50 s."""
import os, re, subprocess, sys

TRIM = ('silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,'
        'areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.1,areverse,'
        'silenceremove=stop_periods=-1:stop_duration=0.32:stop_threshold=-45dB:stop_silence=0.22')   # cap gaps at ~0.22 s
TTS = 'highpass=f=80,equalizer=f=220:t=q:w=1:g=-1.5,equalizer=f=3200:t=q:w=1.2:g=2,acompressor=threshold=-20dB:ratio=3:attack=6:release=80:makeup=2'
CLEAN = ('highpass=f=75,afftdn=nf=-25,equalizer=f=250:t=q:w=1:g=-2,equalizer=f=3000:t=q:w=1.2:g=2.5,deesser=i=0.4,'
         'acompressor=threshold=-24dB:ratio=2.5:attack=15:release=120,acompressor=threshold=-14dB:ratio=4:attack=3:release=50:makeup=2')

def dur(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True)
    return float(r.stdout.strip())

def run(epid, src, chain, lufs, fit=None):
    os.makedirs('vo', exist_ok=True); os.makedirs('tmp', exist_ok=True)
    mid = f'tmp/{epid}_vo_mid.wav'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-ac', '1', '-ar', '48000', '-af', f'{TRIM},{chain}', mid], check=True)
    d = dur(mid); tempo = 1.0
    if fit and d > fit: tempo = min(1.15, d / fit)
    tail = f'atempo={tempo:.4f},' if tempo > 1.001 else ''
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mid, '-af', f'{tail}loudnorm=I={lufs}:TP=-1.5:LRA=9,aresample=48000',
                    '-ac', '1', '-ar', '48000', '-sample_fmt', 's16', f'vo/{epid}.wav'], check=True)
    print(f'vo/{epid}.wav  {d:.1f}s -> {dur(f"vo/{epid}.wav"):.1f}s (atempo {tempo:.3f}, {lufs} LUFS)')

if __name__ == '__main__':
    a = sys.argv[1:]; fit = None
    if '--fit' in a: i = a.index('--fit'); fit = float(a[i + 1]); del a[i:i + 2]
    mode, epid, src = a
    run(epid.upper(), src, TTS if mode == 'tts' else CLEAN, -15 if mode == 'tts' else -14, fit)
