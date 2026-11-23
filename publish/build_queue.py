"""publish/queue.json: one entry per videos/<ID>.mp4, in season order. Captions are generated from the episode EP dict.
Keeps posted status, media ids and any manual `hold: true` of existing entries. EP['hold']=True also holds."""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from publish.episodes import load, key
from config import IG_HANDLE, HASHTAGS

def caption(ep):
    first = f"{ep['company']} asked this 👀" if ep.get('company') else 'A classic interview question 👀'
    return (f"{first}\n{ep['title']}, the {ep['pattern']} way.\n"
            f"💬 Comment NOTES for 5 more {ep['pattern']} questions\n"
            f"📤 Send this to a friend with an interview this week\nFollow @{IG_HANDLE}\n\n{HASHTAGS}")

if __name__ == '__main__':
    old = {e['id']: e for e in json.load(open('publish/queue.json'))} if os.path.exists('publish/queue.json') else {}
    out = []
    for eid in sorted((os.path.basename(p)[:-4] for p in glob.glob('videos/S*E*.mp4')), key=key):
        ep = load(eid); e = old.get(eid, {'id': eid, 'posted': False})
        e.update(video=f'videos/{eid}.mp4', cover=f'covers/{eid}.jpg', caption=caption(ep))
        if ep.get('hold'): e['hold'] = True
        out.append(e)
    json.dump(out, open('publish/queue.json', 'w'), indent=1, ensure_ascii=False)
    print(len(out), 'entries,', sum(not e['posted'] and not e.get('hold') for e in out), 'waiting')
