"""Static notes site -> site/ (Netlify publishes site/, no build step; regenerate locally and commit).
site/index.html            search every question (name, pattern, company, s1e5)
site/sXeYY/index.html      one page per episode: Notes tab + Cheat-sheet tab
site/patterns/<slug>/      one page per pattern     site/companies/<slug>/   one page per company ("Comment AMAZON" DMs)
Sources per episode: webreels/sXeYY/spec.py (EP metadata), notes/eps/sXeYY.md (prose), notes/eps/sXeYY.js (solution + tests).
The .js is run with node at build time; its stdout is cached in notes/eps/sXeYY.out.txt (--no-run reuses the cache, e.g. in CI).
Usage: python3 -m publish.build_site [--no-run]"""
import html, json, os, re, shutil, subprocess, sys
import markdown
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from publish.episodes import all_eps, slug, claim_line
from config import IG_URL, IG_HANDLE, BRAND_TEXT

E = html.escape
CSS = open(os.path.join(os.path.dirname(__file__), 'site.css')).read()
SEASONS = {1: '₹10-15 LPA patterns', 2: '₹20-30 LPA patterns', 3: '₹30-50 LPA patterns', 4: '₹50 LPA+ patterns'}
LINKS = json.load(open('notes/links.json')) if os.path.exists('notes/links.json') else {}
REELS = {e['id']: e.get('permalink') for e in json.load(open('publish/queue.json'))} if os.path.exists('publish/queue.json') else {}
ORDER = ['Problem', 'Example', 'Pattern', 'Key points', 'Interview answer', 'Analogy', 'Solution', 'Common traps', 'Complexity']

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#F5F2EA">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono&family=Oswald:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css"></head><body><div class="wrap">
<div class="top"><a class="logo" href="{root}">""" + BRAND_TEXT.replace(', ', ', <b>') + """</b></a><a class="follow" href=\"""" + IG_URL + """\">Follow on Instagram</a></div>"""
FOOT = '<footer>One interview question, one pattern, one reel a day · <a href="' + IG_URL + '">@' + IG_HANDLE + '</a></footer></div>{js}</body></html>'

TABS_JS = '''<script>
document.querySelectorAll('.tabs button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.tabs button').forEach(x=>x.classList.toggle('on',x===b));
  document.querySelectorAll('.pane').forEach(p=>p.classList.toggle('on',p.id===b.dataset.p));history.replaceState(null,'',b.dataset.p==='sheet'?'#cheatsheet':location.pathname)});
if(location.hash==='#cheatsheet')document.querySelector('[data-p=sheet]').click();
</script>'''

def md(text):
    return markdown.markdown(text, extensions=['tables', 'fenced_code', 'codehilite'], extension_configs={'codehilite': {'guess_lang': False, 'css_class': 'hl-code'}})

def sections(eid):
    p = f'notes/eps/{eid.lower()}.md'
    if not os.path.exists(p): return {}
    parts = re.split(r'^## (.+)$', open(p).read(), flags=re.M)
    return {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts), 2)}

def solution(eid, run):
    js, cache = f'notes/eps/{eid.lower()}.js', f'notes/eps/{eid.lower()}.out.txt'
    if not os.path.exists(js): return None, None
    if run:
        r = subprocess.run(['node', js], capture_output=True, text=True, timeout=30)
        if r.returncode: sys.exit(f'{js} failed:\n{r.stderr}')
        open(cache, 'w').write(r.stdout)
    return open(js).read(), (open(cache).read() if os.path.exists(cache) else '')

def medium_card(eid=None):
    art = (LINKS.get('episodes') or {}).get(eid) if eid else None
    prof = LINKS.get('medium_profile')
    if art: return f'<a class="medium" href="{E(art)}" target="_blank" rel="noopener"><b>Go deeper on Medium</b><span>Follow-ups and variations of this question →</span></a>'
    if prof: return f'<a class="medium" href="{E(prof)}" target="_blank" rel="noopener"><b>Interview prep on Medium</b><span>DSA interview questions, explained step by step →</span></a>'
    return ''

def diff(d): return f'<span class="diff {E(d)}">{E(d)}</span>'

def asked_table(ep):
    rows = ep.get('asked') or []
    if not rows: return '<p>No verified company reports yet. A classic at product-company interviews.</p>'
    h = '<table><tr><th>Company</th><th>Role</th><th>Year</th><th>Source</th></tr>'
    for r in rows:
        h += f'<tr><td><a href="../companies/{slug(r["company"])}/">{E(r["company"])}</a></td><td>{E(r.get("role", ""))}</td><td>{E(str(r.get("year", "")))}</td><td><a href="{E(r["url"])}" target="_blank" rel="noopener nofollow">{E(r.get("source", "link"))}</a></td></tr>'
    return h + '</table>'

def similar_table(ep, root='../'):
    rows = ep.get('similar') or []
    h = '<table><tr><th>#</th><th>Question</th><th>Level</th><th>Reported at</th></tr>'
    for i, r in enumerate(rows, 1):
        cos = ', '.join(r.get('companies') or []) or '-'
        h += f'<tr><td>{i}</td><td><a href="{E(r["url"])}" target="_blank" rel="noopener">{E(r["name"])}</a></td><td>{diff(r["difficulty"])}</td><td>{E(cos)}</td></tr>'
    return h + '</table>'

def ep_page(ep, sec, code, out, prev, nxt):
    eid = ep['id']; body = ''
    for name in ORDER:
        if name == 'Solution':
            if code:
                body += '<h2 id="solution">Solution (JavaScript)</h2>' + md(f'```js\n{code.strip()}\n```')
                body += f'<p class="src">Real output, run with node:</p><div class="out">{E(out.strip())}</div>'
            continue
        if name in sec:
            sid = slug(name)
            body += f'<h2 id="{sid}">{E(name)}</h2>' + md(sec[name])
    body += '<h2 id="where-asked">Where it\'s been asked</h2>' + asked_table(ep)
    body += f'<h2 id="similar">5 more {E(ep["pattern"])} questions</h2><p class="src">Easiest to hardest.</p>' + similar_table(ep)
    sheet = f'<h2>{E(ep["title"])}</h2><p><b>Pattern:</b> {E(ep["pattern"])}</p>'
    for name in ('Key points', 'Complexity', 'Interview answer'):
        if name in sec: sheet += f'<h3>{E(name)}</h3>' + md(sec[name])
    sheet += '<h3>Practice next</h3><ol>' + ''.join(f'<li><a href="{E(r["url"])}">{E(r["name"])}</a> ({E(r["difficulty"])})</li>' for r in ep.get('similar') or []) + '</ol>'
    reel = f'<a class="reel" href="{REELS[eid]}" target="_blank" rel="noopener">Watch the reel</a>' if REELS.get(eid) else ''
    s, e = int(eid[1:eid.index('E')]), int(eid[eid.index('E') + 1:])
    nav = lambda x, lab, cls='': f'<a class="{cls}" href="../{x["id"].lower()}/"><small>{lab}</small>{E(x["title"])}</a>' if x else '<span></span>'
    p = HEAD.format(title=f'{ep["title"]} · {ep["pattern"]} · {BRAND_TEXT}', desc=E(claim_line(ep) + '. ' + ep['title'] + ', the ' + ep['pattern'] + ' way, with JavaScript solution.'), root='../')
    p += f'''<span class="pill">Season {s} · Episode {e}</span>
<h1><span class="hl">{E(ep["title"])}</span></h1>
<div class="meta">{reel}<a class="pat" href="../patterns/{slug(ep["pattern"])}/">{E(ep["pattern"])}</a>{diff(ep["difficulty"])}<span class="claim">{E(claim_line(ep))}</span><a href="{E(ep["official"])}" target="_blank" rel="noopener">Official problem ↗</a></div>
<div class="tabs"><button class="on" data-p="deep">Notes</button><button data-p="sheet">Cheat sheet</button></div>
<div class="pane on" id="deep"><div class="deep">{body}</div>{medium_card(eid)}</div>
<div class="pane" id="sheet"><div class="sheet">{sheet}</div><div class="bar"><button class="btn" onclick="print()">Print / save as PDF</button></div></div>
<div class="bar"><a class="btn" href="../">All questions</a><button class="btn" onclick="navigator.share?navigator.share({{title:document.title,url:location.href}}):navigator.clipboard.writeText(location.href).then(()=>this.textContent='Link copied')">Share</button></div>
<div class="nav">{nav(prev, "← PREVIOUS")}{nav(nxt, "NEXT →", "r")}</div>
<div class="cta">One interview question a day, as a 45-second reel: <a href="{IG_URL}">follow @{IG_HANDLE}</a></div>'''
    return p + FOOT.format(js=TABS_JS)

def list_page(title, lead, items, root='../../', extra=''):
    p = HEAD.format(title=f'{title} · {BRAND_TEXT}', desc=E(lead), root=root) + f'<h1><span class="hl">{E(title)}</span></h1><p class="lead">{E(lead)}</p>'
    for ep in items:
        p += f'<a class="item" href="{root}{ep["id"].lower()}/"><span class="n">{ep["id"]}</span><span><span class="t">{E(ep["title"])}</span><span class="snip">{E(ep["pattern"])} · {E(claim_line(ep))}</span></span></a>'
    return p + extra + f'<div class="bar"><a class="btn" href="{root}">All questions</a></div>' + FOOT.format(js='')

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(text)

APP_JS = r"""<script>
const D=__DATA__;const q=document.getElementById('q'),list=document.getElementById('list');
const norm=s=>s.toLowerCase().replace(/[^a-z0-9 ]+/g,' ').replace(/\s+/g,' ').trim();const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
D.forEach(d=>d.k=norm([d.id,d.title,d.pattern,d.cos.join(' '),d.text].join(' ')));
function render(){const v=q.value.trim();let r=D;const m=v.match(/^\s*s?(\d+)\s*[ e.x]\s*(\d+)\s*$/i);
 if(m)r=D.filter(d=>d.s==+m[1]&&d.e==+m[2]);else if(v){const w=norm(v).split(' ');r=D.filter(d=>w.every(x=>d.k.includes(x)))}
 list.innerHTML=r.length?r.map(d=>`<a class="item" href="${d.id.toLowerCase()}/"><span class="n">${d.id}</span><span><span class="t">${esc(d.title)}</span><span class="snip">${esc(d.pattern)} · ${esc(d.claim)}</span></span></a>`).join(''):'<div class="empty">Nothing found. Try <b>two pointers</b>, <b>amazon</b> or <b>s1e3</b>.</div>'}
q.oninput=render;document.querySelectorAll('.hint code').forEach(c=>c.onclick=()=>{q.value=c.textContent;render()});render();
</script>"""

def build(run=True):
    eps = all_eps()
    shutil.rmtree('site', ignore_errors=True); os.makedirs('site'); write('site/style.css', CSS)
    pats, cos = {}, {}
    for i, ep in enumerate(eps):
        sec = sections(ep['id']); code, out = solution(ep['id'], run)
        same = lambda x: x and x['id'][:x['id'].index('E')] == ep['id'][:ep['id'].index('E')]
        prev = eps[i - 1] if i and same(eps[i - 1]) else None; nxt = eps[i + 1] if i + 1 < len(eps) and same(eps[i + 1]) else None
        write(f'site/{ep["id"].lower()}/index.html', ep_page(ep, sec, code, out, prev, nxt))
        ep['_text'] = ' '.join(re.sub(r'[#*`>|_-]', ' ', sec.get(k, '')) for k in ('Problem', 'Pattern', 'Key points'))[:600]
        pats.setdefault(ep['pattern'], []).append(ep)
        for r in ep.get('asked') or []: cos.setdefault(r['company'], {})[ep['id']] = ep
    for name, items in pats.items():
        sim = {}
        for ep in items:
            for r in ep.get('similar') or []: sim.setdefault(r['name'], r)
        extra = '<h2>Practice list</h2>' + similar_table({'similar': sorted(sim.values(), key=lambda r: ['Easy', 'Medium', 'Hard'].index(r['difficulty']))}) if sim else ''
        write(f'site/patterns/{slug(name)}/index.html', list_page(f'{name} pattern', f'Every {name} question in the series, with notes and JavaScript solutions.', items, extra=extra))
    for name, d in cos.items():
        write(f'site/companies/{slug(name)}/index.html', list_page(f'{name} interview questions', f'Questions with public {name} interview reports (sources on each page).', list(d.values())))
    data = [dict(id=e['id'], s=int(e['id'][1:e['id'].index('E')]), e=int(e['id'][e['id'].index('E') + 1:]), title=e['title'], pattern=e['pattern'],
                 claim=claim_line(e), cos=[r['company'] for r in e.get('asked') or []], text=e['_text']) for e in eps]
    grid = lambda d, base: '<div class="grid">' + ''.join(f'<a href="{base}/{slug(k)}/">{E(k)}<small>{len(v)} question{"s" * (len(v) != 1)}</small></a>' for k, v in sorted(d.items())) + '</div>'
    idx = HEAD.format(title=f'{BRAND_TEXT} · DSA interview questions, one pattern at a time', desc='Notes, JavaScript solutions and practice lists for every reel.', root='')
    idx += f'''<h1>Crack the <span class="hl">pattern</span>, not the question</h1>
<p class="lead">{len(eps)} interview questions with notes, a JavaScript solution and 5 more to practise. Search by name, pattern or company.</p>
<div class="search"><input id="q" type="search" placeholder="two pointers · amazon · s1e3" autocomplete="off" aria-label="Search">
<div class="hint">Try <code>sliding window</code> <code>amazon</code> <code>s1e1</code></div></div><div id="list"></div>
<div class="group"><h2>Patterns</h2>{grid(pats, "patterns")}</div><div class="group"><h2>Companies</h2>{grid({k: list(v) for k, v in cos.items()}, "companies")}</div>{medium_card()}'''
    write('site/index.html', idx + FOOT.format(js=APP_JS.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))))
    write('site/404.html', HEAD.format(title='Not found', desc='', root='/') + '<h1><span class="hl">Not found</span></h1><p><a class="btn" href="/">All questions</a></p>' + FOOT.format(js=''))
    json.dump(data, open('site/notes.json', 'w'), ensure_ascii=False)
    print(f'site/: {len(eps)} episodes, {len(pats)} patterns, {len(cos)} companies')

if __name__ == '__main__':
    build(run='--no-run' not in sys.argv)
