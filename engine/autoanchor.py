"""Scene-start anchors (ms, raw audio) without transcription: pick N-1 pauses that best match each scene's share of the script."""
import re, subprocess, sys
def silences(wav, db=-35, d=0.12):
    out = subprocess.run(['ffmpeg', '-i', wav, '-af', f'silencedetect=noise={db}dB:d={d}', '-f', 'null', '-'], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', out)]; en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', out)]
    return list(zip(st, en))
def anchors(wav, lines, outro_s=None):
    sil = silences(wav); first = sil[0][1] if sil and sil[0][0] < .05 else 0.0
    last = sil[-1][0] if sil and sil[-1][1] > 0 else None
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', wav], capture_output=True, text=True).stdout)
    end = last if last and last > dur - 1.5 else dur
    tail = None
    if outro_s:  # fixed outro line: anchor it from the end, solve the rest
        g2 = [(s_, e_) for s_, e_ in sil if e_ < end - .5]
        tail = min(g2, key=lambda g: abs((end - g[1]) - outro_s)); end = tail[0]; lines = lines[:-1]
    w = [len(re.sub(r'[^a-z0-9]', '', l.lower())) + 6 for l in lines]; tot = sum(w)
    exp, c = [], 0
    for x in w[:-1]: c += x; exp.append(first + (end - first) * c / tot)
    gaps = [(s, e) for s, e in sil if s > first + .3 and e < end - .2]
    n, G = len(exp), len(gaps); INF = -1e9
    # dp[i][j]: best score assigning boundary i to gap j
    dp = [[INF] * G for _ in range(n)]; bk = [[-1] * G for _ in range(n)]
    sc = lambda i, j: (gaps[j][1] - gaps[j][0]) * 6 - abs((gaps[j][0] + gaps[j][1]) / 2 - exp[i]) * 1.2
    for j in range(G): dp[0][j] = sc(0, j)
    for i in range(1, n):
        best, bj = INF, -1
        for j in range(G):
            if j > 0 and dp[i - 1][j - 1] > best: best, bj = dp[i - 1][j - 1], j - 1
            if bj >= 0: dp[i][j] = best + sc(i, j); bk[i][j] = bj
    j = max(range(G), key=lambda k: dp[n - 1][k]); pick = [j]
    for i in range(n - 1, 0, -1): j = bk[i][j]; pick.append(j)
    pick.reverse()
    out = [0] + [int(gaps[k][1] * 1000) for k in pick]
    return out + ([int(tail[1] * 1000)] if tail else [])
if __name__ == '__main__':
    import importlib
    epid, wav = sys.argv[1], sys.argv[2]
    m = importlib.import_module(f'webreels.{epid.lower()}.spec')
    print(','.join(map(str, anchors(wav, m.NARRATION))))
