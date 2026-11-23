"""Pre-push check: every queued item has its video and cover tracked in git (else Instagram gets a 404).
Usage: python3 -m publish.verify   (exit 1 on any problem)"""
import json, subprocess, sys
tracked = set(subprocess.run(['git', 'ls-files', 'videos', 'covers'], capture_output=True, text=True).stdout.split())
staged = set(subprocess.run(['git', 'diff', '--cached', '--name-only'], capture_output=True, text=True).stdout.split())
bad = [(e['id'], f) for e in json.load(open('publish/queue.json')) if not e.get('posted')
       for f in (e['video'], e['cover']) if f not in tracked | staged]
for i, f in bad: print(f'MISSING in git: {i} {f}')
print('verify:', 'FAIL' if bad else 'ok (all queued media tracked/staged)')
sys.exit(1 if bad else 0)
