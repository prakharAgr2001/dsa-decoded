"""Release rendered episodes: cover + upload-ready video for every out/SxEyy_*.mp4 not yet in videos/, then queue + site.
Usage: python3 -m publish.release [S1]      Then verify + commit (see CLAUDE.md)."""
import glob, os, subprocess, sys
want = [a.upper() for a in sys.argv[1:]]
eps = sorted({os.path.basename(p).split('_')[0] for p in glob.glob('out/S*E*_*.mp4')})
eps = [e for e in eps if not os.path.exists(f'videos/{e}.mp4') and (not want or any(e.startswith(w + 'E') for w in want))]
print('new episodes:', eps or 'none')
if eps:
    subprocess.run([sys.executable, '-m', 'publish.covers', *eps], check=True)
    subprocess.run([sys.executable, '-m', 'publish.prep_videos', *eps], check=True)
subprocess.run([sys.executable, '-m', 'publish.build_queue'], check=True)
subprocess.run([sys.executable, '-m', 'publish.build_site'], check=True)
print('Next: git add videos covers publish/queue.json site && python3 -m publish.verify && commit, pull --rebase, push')
