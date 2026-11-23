// ---- story kit (shared by WR12+; copied into each scenes.js by webreels/_kit/build.sh) ----
const EMO = n => `<img src="../../brand/emoji/${n}.svg" style="width:1em;height:1em;vertical-align:-.12em">`;
const TT = (S, w, f = .3, n = 1) => { try { return S.T(w, n); } catch (e) { return S.dur * f; } };
const MK = (S, sel, at) => S.$(sel).style.setProperty('--m', S.P(at - .1, .35));
function POP(S, sel, at, snd = 'pop', from = .7) { const e = S.$(sel), p = S.P(at, .3, back); e.style.opacity = clamp(p); e.style.transform = `scale(${from + (1 - from) * clamp(p)})`; if (snd && S.on(at)) S.sfx(at, snd); return p; }
function STAMP(S, sel, at, rot = -8) { const e = S.$(sel), p = S.P(at, .22, back); e.style.opacity = clamp(p * 2); e.style.transform = `rotate(${rot}deg) scale(${1.6 - .6 * clamp(p)})`; if (S.on(at)) S.sfx(at, 'thud'); }
function TYPE(S, sel, txt, at, d) { const k = Math.floor(txt.length * S.P(at, d, x => x)); S.$(sel).innerHTML = txt.slice(0, k).replace(/</g, '&lt;') + (k < txt.length && S.on(at) ? '<span class="caret"></span>' : ''); if (S.on(at) && k < txt.length && Math.floor(S.t * 20) % 2) S.sfx(S.t, 'click'); }
function COUNT(S, sel, a, b, at, d, f = fmt, e = eio) { S.$(sel).textContent = f(a + (b - a) * S.P(at, d, e)); }
function SHAKE(S, sel, at, amp = 12, len = .6) { const k = S.on(at) ? Math.max(0, 1 - (S.t - at) / len) : 0; S.$(sel).style.translate = `${amp * k * Math.sin(S.t * 80)}px ${amp * .5 * k * Math.cos(S.t * 63)}px`; }
function IN(S, sel, at, dy = 60) { const e = S.$(sel), p = S.P(at, .35); e.style.opacity = p; e.style.transform = `translateY(${dy * (1 - p)}px)`; return p; }
const SWITCHES = (n, cols, w = 84) => `<div class="sws" style="width:${cols * (w + 18)}px">${'<span class="sw"></span>'.repeat(n)}</div>`;
function SETSW(S, on) { S.$$('.sw').forEach((s, i) => s.classList.toggle('on', i < on)); }
const WIN = (title, body, cls = '') => `<div class="win ${cls}"><div class="wt"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i><span>${title}</span></div><div class="wb">${body}</div></div>`;
// ---- end kit ----
// ---- dsa kit: number boxes, pointers, hash-map table, glow, karaoke ----
const A = [120, 350, 280, 150, 400], TG = 500, BW = 160, GAP = 14, X0 = 112;
const bx = i => X0 + i * (BW + GAP);
const ROW = (id, top, vals = A, pre = '') => `<div class="row" id="${id}" style="top:${top}px">${vals.map((v, i) => `<div class="b" style="left:${bx(i) - X0}px"><b>${pre}${v}</b><span>${i}</span></div>`).join('')}<div class="frame"></div></div>`;
function FRAME(S, id, l, r, col = 'var(--grn)', show = 1) { const f = S.$(`#${id} .frame`); f.style.left = (bx(l) - X0 - 10) + 'px'; f.style.width = ((r - l + 1) * (BW + GAP) - GAP + 20) + 'px'; f.style.borderColor = col; f.style.boxShadow = `0 0 40px ${col}`; f.style.opacity = show; }
function LITSET(S, id, set, cls = 'on') { S.$$(`#${id} .b`).forEach((b, i) => b.classList.toggle(cls, set.includes(i))); }
const PTR = (id, txt, col) => `<div class="pt" id="${id}" style="--c:${col}"><i></i>${txt}</div>`;
function PT(S, id, i, top) { const p = S.$('#' + id); p.style.left = (bx(i) + BW / 2 - 70) + 'px'; p.style.top = top + 'px'; }
function FLOAT(S, sel, amp = 6, sp = 2.2) { const e = S.$(sel); if (e) e.style.translate = `0 ${amp * Math.sin(S.abs * sp)}px`; }
const GL = (id, col) => `<div class="sglow" id="${id}" style="background:radial-gradient(60% 45% at 50% 45%,${col},transparent 70%)"></div>`;
function GLOW(S, id, at, len = 1.2) { const k = S.on(at) ? Math.max(0, 1 - (S.t - at) / len) : 0; S.$('#' + id).style.opacity = .55 * k; }
function WT(si) { const t0 = DATA.spans[si][0]; return DATA.words.filter(w => w[3] === si).map(w => w[1] - t0); }
function KARAOKE(S, sel, si, off = 0, dim = .22) { const ws = WT(si); S.$$(sel + ' w').forEach((e, k) => { const t = ws[k + off]; e.style.opacity = t !== undefined && S.t >= t - .05 ? 1 : dim; }); }
const WRAPW = txt => txt.split(' ').map(w => `<w>${w}</w>`).join(' ');
// ---- end dsa kit ----
// uses:dsa  V2 race: two lanes, counters computed in spec comments.
const LANES = (n, bf, hm) => `<div class="abs center" style="top:300px"><span class="nchip" id="nc">n = ${fmt(n)}</span></div>
 <div class="lane bad" style="top:440px"><div class="lh">CHECK EVERY PAIR</div><div class="lc" id="c1">0</div><div class="bar"><i id="b1"></i></div><div class="st" id="s1"></div></div>
 <div class="lane good" style="top:900px"><div class="lh">HASH MAP</div><div class="lc" id="c2">0</div><div class="bar"><i id="b2"></i></div><div class="st" id="s2"></div></div>`;
function RACE(S, bf, hm, t0, tb, th) {   // counts start at t0, hash finishes at th, brute visual finish tb (or never if null)
  const ph = S.P(t0, th - t0, x => x), pb = tb ? S.P(t0, tb - t0, x => x) : Math.min(.97, S.P(t0, S.dur - t0 + 6, x => x));
  S.$('#c2').textContent = fmt(hm * ph); S.$('#b2').style.width = 100 * ph + '%'; S.$('#c1').textContent = fmt(bf * pb); S.$('#b1').style.width = 100 * pb + '%';
  S.$('#s2').textContent = ph >= 1 ? 'DONE ✓' : ''; S.$('#s1').textContent = pb >= 1 ? 'DONE' : (S.on(th) ? 'still checking…' : '');
  if (S.on(th) && !S.on(th + .05)) S.sfx(th, 'ding'); }
const SCENES = [
 { html: `<div class="abs center kick" style="top:520px">two sum</div><div class="abs center h" style="top:600px;font-size:150px">THE <span class="mark" id="mk">RACE</span></div>
   <div class="abs center" style="top:900px"><span class="vs bad">every pair</span> <span class="vsx">vs</span> <span class="vs good">hash map</span></div>`,
  draw(S) { MK(S, '#mk', TT(S, 'race', .6) - .1); IN(S, '.vs.bad', .2); IN(S, '.vs.good', .4); }},
 { html: `<div class="qcard" id="qc">${WRAPW('Find two numbers in a list that add up to a target.')}</div>`, draw(S) { IN(S, '#qc', .05, 60); KARAOKE(S, '#qc', 1); }},
 { html: LANES(5), draw(S) { POP(S, '#nc', .05); RACE(S, 10, 5, TT(S, 'ten', .3) - .4, TT(S, 'ten', .3) + .2, TT(S, 'five', .8, 2)); }},
 { html: LANES(5000), draw(S) { POP(S, '#nc', .05); RACE(S, 12497500, 5000, .4, null, TT(S, 'thousand', .9, 2)); }},
 { html: LANES(50000), draw(S) { POP(S, '#nc', .05); RACE(S, 1249975000, 50000, .3, null, TT(S, 'versus', .7) + .4); SHAKE(S, '#c1', TT(S, 'billion', .5), 10); }},
 { html: `<div class="abs center lab" style="top:330px;font-size:40px">at 1,000,000 checks per second · n = 50,000</div>
   <div class="tcard bad" id="tA" style="top:470px"><span>every pair</span><b>20.8 min</b></div><div class="tcard good" id="tB" style="top:880px"><span>hash map</span><b>0.05 s</b></div>${GL('g5', 'rgba(61,220,132,.45)')}`,
  draw(S) { POP(S, '#tA', TT(S, 'minutes', .5) - .3, 'thud'); POP(S, '#tB', TT(S, 'second', .85, 2) - .3, 'ding'); GLOW(S, 'g5', TT(S, 'second', .85, 2) - .3); }},
 { html: `${ROW('rw', 380)}<div class="seen" style="top:640px"><h3>SEEN</h3>${[0, 1, 2].map(k => `<div class="kv" id="kv${k}"><b>${A[k]}</b><span>at</span><i>${k}</i></div>`).join('')}</div>
   <div class="abs center need" id="lk" style="top:1080px;opacity:0">150 → partner 350 → <b>found</b></div>`,
  draw(S) { const tr = TT(S, 'remembers', .3); [0, 1, 2].forEach(k => { const t = tr + k * .35; POP(S, '#kv' + k, t, 'pop'); LITSET(S, 'rw', [Math.min(3, Math.floor((S.t - tr) / .35))]); });
    const tl = TT(S, 'lookup', .85) - .2; S.$('#kv1').classList.toggle('hl', S.on(tl)); IN(S, '#lk', tl); if (S.on(tl)) LITSET(S, 'rw', [1, 3]); }},
 { html: `<div class="abs center kick" style="top:420px">winner</div><div class="abs center h" style="top:500px;font-size:130px">hash map</div><div class="abs center" id="on" style="top:760px;opacity:0"><span class="badge">O(n)</span></div>
   <div class="abs center lab" style="top:1100px;font-size:40px">every pair = O(n²)</div>${GL('g7', 'rgba(255,210,63,.4)')}`,
  draw(S) { POP(S, '#on', TT(S, 'o', .6) - .1, 'ding'); GLOW(S, 'g7', 0, 1.5); S.$('#on .badge').style.transform = `scale(${1 + .035 * Math.sin(S.t * 5)})`; }},
 { html: `<div class="abs center" style="top:480px"><span class="notes">NOTES</span></div><div class="abs center h2" style="top:790px">comment NOTES for 5 more<br>questions with this pattern</div><div class="abs center" style="top:1120px"><span class="pill" id="fl"></span></div>`,
  draw(S) { S.$('#fl').textContent = 'Follow ' + HANDLE; POP(S, '.notes', 0); }},
];
