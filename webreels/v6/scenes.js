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
// uses:dsa  V6 kinetic v2: hook -> trap (real count) -> rule -> concrete aha -> payoff -> variations CTA.
const LN = ['Amazon. 28 lakh package. And this question keeps coming up.', 'Find two numbers that add up to 500.', 'Most people check every pair. Five thousand numbers? Twelve million checks. Rejected.',
  "The trick: don't search. Remember.", 'At 150, ask one thing: have I seen 350? Yes. Done.', 'One pass. O of n.', 'Comment NOTES. I will DM you five variations of this question.'];
const VAR = [['Contains Duplicate', 'Easy'], ['Two Sum II · sorted input', 'Medium'], ['Group Anagrams', 'Medium'], ['Subarray Sum Equals K', 'Medium'], ['4Sum II', 'Medium']];
const KEY = /^(amazon|28|lakh|500|every|pair|twelve|million|rejected|search|remember|150|350|yes|done|pass|o|n|notes|five|variations)$/i;
const BG = ['#0c0c0e', '#0c0c0e', '#0c0c0e', '#ffd23f', '#0c0c0e', '#3ddc84', '#0c0c0e'], FG = ['#f4f1ea', '#f4f1ea', '#f4f1ea', '#0c0c0e', '#f4f1ea', '#0c0c0e', '#f4f1ea'];
const SZ = [100, 120, 80, 170, 96, 200, 76];
const EXTRA = si => [
  `<div class="offer2" id="of"><div class="ok">OFFER</div><div class="o2r">SDE-1 · Amazon · India</div><div class="o2c"><span id="ct">₹0</span> LPA</div></div><div class="abs center" id="tgc" style="top:1380px;opacity:0"><span class="tag">ASKED IN AMAZON INTERVIEWS · 2025</span></div>`,
  `${ROW('rw', 900)}<div class="abs center" id="tg" style="top:1130px;opacity:0"><span class="tgt">TARGET 500</span></div>`,
  `${ROW('rw', 980)}<div class="abs center big" id="ck" style="top:1190px;font-size:120px;color:var(--red)">0</div><div class="abs center lab" style="top:1330px;font-size:34px">pairs for 5,000 numbers</div>`,
  `<div class="abs center" style="top:1260px;font:700 44px Roboto;color:#0c0c0e;opacity:.75" id="sub">keep a set of every number you've seen</div>`,
  `${ROW('rw', 860)}${PTR('pi', 'i', '#4c9dff')}<div class="seenrow"><b>SEEN</b>${[0, 1, 2].map(k => `<span class="sc" id="sc${k}">${A[k]}</span>`).join('')}</div>${GL('g4', 'rgba(61,220,132,.5)')}`,
  `<div class="abs center lab" style="top:1180px;font-size:44px;color:#0c0c0e">every pair = O(n²) · this = O(n)</div>`,
  `<div class="vlist" style="top:700px">${VAR.map((v, k) => `<div class="vr" id="vr${k}"><span>${k + 1}</span>${v[0]}<i class="${v[1]}">${v[1]}</i></div>`).join('')}<div class="vlock">in your DMs · comment NOTES</div></div><div class="abs center" style="top:1440px"><span class="pill" id="fl" style="font-size:34px"></span></div>`][si];
const SCENES = LN.map((ln, si) => ({ noCap: true,
  html: `<div class="field" style="background:${BG[si]}"></div><div class="kt" style="font-size:${SZ[si]}px;color:${FG[si]};--kc:${BG[si] === '#0c0c0e' ? '#ffd23f' : '#b00b1e'}">${ln.split(' ').map(w => `<span class="kw ${KEY.test(w.replace(/[^a-z0-9]/gi, '')) ? 'k' : ''}">${w}</span>`).join(' ')}</div>${EXTRA(si)}`,
  draw(S) { const ws = WT(si); S.$$('.kw').forEach((e, k) => { const t = ws[k] ?? 0; const q = S.P(t - .06, .18, back); e.style.opacity = clamp(q * 1.5); e.style.transform = `scale(${1.8 - .8 * clamp(q)}) rotate(${(k % 2 ? 1 : -1) * 3 * (1 - clamp(q))}deg)`; if (S.on(t - .06) && e.classList.contains('k')) S.sfx(t - .06, 'thud'); });
    S.el.querySelector('.field').style.transform = `scale(${1 + .02 * Math.sin(S.abs * 128 / 60 * Math.PI)})`;
    if (si === 0) { const p = S.P(.05, .45, back); S.$('#of').style.opacity = clamp(p); S.$('#of').style.transform = `translateY(${80 * (1 - clamp(p))}px)`; COUNT(S, '#ct', 0, 28, .4, .7, v => '₹' + Math.round(v)); if (S.on(1.1)) S.sfx(1.1, 'ding'); POP(S, '#tgc', ws[5] - .05, 'pop'); }
    if (si === 1) { S.$$('#rw .b').forEach((b, i) => { const q = S.P(.1 + i * .07, .3, back); b.style.opacity = clamp(q); }); POP(S, '#tg', ws[7] - .1, 'pop'); }
    if (si === 2) { const k = Math.floor(S.t * 8), pr = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]][k % 10]; const tr = ws[11]; LITSET(S, 'rw', S.t < tr ? pr : [], 'bad');
      COUNT(S, '#ck', 0, 12497500, ws[5] - .1, ws[9] - ws[5] + .2, v => fmt(v), x => x * x); SHAKE(S, '#ck', tr, 14); if (S.on(tr - .06)) { S.$('#ck').style.textDecoration = 'line-through'; } }
    if (si === 3) IN(S, '#sub', ws[5] + .1, 20);
    if (si === 4) { [0, 1, 2].forEach(k => S.$('#sc' + k).style.opacity = 1); PT(S, 'pi', 3, 1030); LITSET(S, 'rw', S.on(ws[9] - .1) ? [1, 3] : [3]); const ty = ws[9] - .1;
      S.$('#sc1').classList.toggle('hl', S.on(ty)); GLOW(S, 'g4', ty, 1.4); if (S.on(ty)) S.sfx(ty, 'ding'); SHAKE(S, '#sc1', ty, 10); }
    if (si === 6) { S.$('#fl').textContent = 'Follow ' + HANDLE; VAR.forEach((_, k) => { const t = (ws[5] ?? .8) - .2 + k * .16; const q = S.P(t, .3, back); const e = S.$('#vr' + k); e.style.opacity = clamp(q); e.style.transform = `translateX(${140 * (1 - clamp(q))}px)`; if (S.on(t)) S.sfx(t, 'swish'); }); }
  }}));
