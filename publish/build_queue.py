"""publish/queue.json: one entry per videos/<ID>.mp4, in season order. Captions are generated from the episode EP dict.
Keeps posted status, media ids and any manual `hold: true` of existing entries. EP['hold']=True also holds."""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from publish.episodes import load, key
from config import IG_HANDLE, HASHTAGS

AI_TAGS = '#ai #aitools #github #opensource #claudecode #mcp #developer #coding #programming #techreels'

def ai_caption(ep):
    from engine.aitools import T
    repo, name, stars, sc, find = T[int(ep['id'][1:]) - 1]
    return (f"{name}: {sc[0][0]}\n\nRepo: github.com/{repo}\n"
            f"Save this for later and follow @{IG_HANDLE} for more AI tools\n\n{AI_TAGS}")

def ie_caption(ep):
    return (f"{ep['title']}: every round, from a real LeetCode Discuss post.\n"
            f"Follow @{IG_HANDLE} for more real interview breakdowns\n\n{HASHTAGS}")

def caption(ep):
    first = f"{ep['company']} asked this 👀" if ep.get('company') else 'A classic interview question 👀'
    return (f"{first}\n{ep['title']}, the {ep['pattern']} way.\n"
            f"💬 Comment NOTES for 5 more {ep['pattern']} questions\n"
            f"📤 Send this to a friend with an interview this week\nFollow @{IG_HANDLE}\n\n{HASHTAGS}")

if __name__ == '__main__':
    old = {e['id']: e for e in json.load(open('publish/queue.json'))} if os.path.exists('publish/queue.json') else {}
    out = []
    ids = sorted((os.path.basename(p)[:-4] for p in glob.glob('videos/S*E*.mp4')), key=key)
    ies = sorted((os.path.basename(p)[:-4] for p in glob.glob('videos/X*.mp4')), key=lambda x: int(x[1:]))
    # interview-experience reels (X*) go right after whatever is already posted, ahead of unposted episodes
    ais = sorted((os.path.basename(p)[:-4] for p in glob.glob('videos/Y*.mp4')), key=lambda x: int(x[1:]))
    posted = [i for i in ids if old.get(i, {}).get('posted')]
    for eid in posted + ies + ais + [i for i in ids if i not in posted]:
        ep = load(eid); e = old.get(eid, {'id': eid, 'posted': False})
        e.update(video=f'videos/{eid}.mp4', cover=f'covers/{eid}.jpg', caption=ai_caption(ep) if eid.startswith('Y') else ie_caption(ep) if eid.startswith('X') else caption(ep))
        if ep.get('hold'): e['hold'] = True
        out.append(e)
    json.dump(out, open('publish/queue.json', 'w'), indent=1, ensure_ascii=False)
    print(len(out), 'entries,', sum(not e['posted'] and not e.get('hold') for e in out), 'waiting')
