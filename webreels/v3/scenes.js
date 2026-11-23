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
// uses:dsa  V3 POV shop: product tiles + paper notebook (the hash map) + cart.
const IT = [['MUG', 120], ['T-SHIRT', 350], ['BOOK', 280], ['CAP', 150], ['WATCH', 400]];
const SHELF = (id, top) => `<div class="shelf" id="${id}" style="top:${top}px">${IT.map((x, i) => `<div class="prod" id="${id}p${i}"><small>${x[0]}</small><b>₹${x[1]}</b></div>`).join('')}<div class="plank"></div></div>`;
const NOTE = n => `<div class="note"><h3>my notebook</h3>${[0, 1, 2].slice(0, n).map(k => `<div class="nl" id="nl${k}">₹${IT[k][1]}</div>`).join('')}</div>`;
function PICK(S, id, i) { S.$$(`#${id} .prod`).forEach((p, k) => { p.classList.toggle('pk', k === i); p.style.translate = k === i ? `0 ${-24 - 6 * Math.sin(S.t * 6)}px` : '0 0'; }); }
function STEP(S, i, nn) {  // scene for item i: pick, "need", write notebook line nn-1
  PICK(S, 'sh', i); S.$('#nd').innerHTML = `need <b>₹${TG - IT[i][1]}</b>`; IN(S, '#nd', TT(S, 'need', .3) - .1, 20);
  for (let k = 0; k < nn; k++) { const e = S.$('#nl' + k); if (k < nn - 1) { e.style.opacity = 1; continue; } const tw = TT(S, 'write', .7) - .1; const q = S.P(tw, .5, x => x);
    e.style.opacity = q > 0 ? 1 : 0; e.style.clipPath = `inset(0 ${100 - 100 * q}% 0 0)`; if (S.on(tw)) S.sfx(tw, 'click'); } }
const SCENES = [
 { html: `<div class="gift" id="gc"><small>GIFT CARD</small><b>₹500</b><span>valid on exactly 2 items</span></div><div class="abs center h2" id="ct" style="top:1120px;opacity:0">catch: <span style="color:var(--yel)">exactly two</span> items</div>`,
  draw(S) { const p = S.P(0, .6, back); S.$('#gc').style.transform = `rotate(${-8 + 6 * clamp(p)}deg) scale(${.6 + .4 * clamp(p)})`; S.$('#gc').style.opacity = clamp(p); if (S.on(.2)) S.sfx(.2, 'ding'); IN(S, '#ct', TT(S, 'catch', .5) - .1); }},
 { html: `<div class="abs center kick" style="top:380px">the shelf</div>${SHELF('sh', 520)}`,
  draw(S) { IT.forEach((x, i) => { const t = TT(S, String(x[1]), .2 + i * .14) - .15; POP(S, '#shp' + i, t, 'pop'); }); }},
 { html: `${SHELF('sh', 380)}<div class="abs center need" id="nd" style="top:760px"></div>${NOTE(1)}`, draw(S) { STEP(S, 0, 1); }},
 { html: `${SHELF('sh', 380)}<div class="abs center need" id="nd" style="top:760px"></div>${NOTE(2)}`, draw(S) { STEP(S, 1, 2); }},
 { html: `${SHELF('sh', 380)}<div class="abs center need" id="nd" style="top:760px"></div>${NOTE(3)}`, draw(S) { STEP(S, 2, 3); }},
 { html: `${SHELF('sh', 380)}<div class="abs center need" id="nd" style="top:760px">need <b>₹350</b></div>${NOTE(3)}<div class="cart" id="ca">CHECKOUT · ₹350 + ₹150 = ₹500 ✓</div>${GL('g5', 'rgba(61,220,132,.45)')}`,
  draw(S) { PICK(S, 'sh', 3); [0, 1, 2].forEach(k => S.$('#nl' + k).style.opacity = 1); const tc = TT(S, 'there', .6) - .1; S.$('#nl1').classList.toggle('hl', S.on(tc)); if (S.on(tc)) S.sfx(tc, 'ding');
    const tk = TT(S, 'checkout', .85) - .1; POP(S, '#ca', tk, 'thud'); GLOW(S, 'g5', tk, 1.5); if (S.on(tk)) { S.$('#shp1').classList.add('pk'); } }},
 { html: `${NOTE(3)}<div class="abs center h" id="hm" style="top:420px;font-size:110px;opacity:0">notebook = <span class="mark" id="mk">hash map</span></div>
   <div class="abs center" id="on" style="top:1340px;opacity:0"><span class="badge" style="font-size:120px;padding:16px 50px">O(n)</span></div>`,
  draw(S) { [0, 1, 2].forEach(k => S.$('#nl' + k).style.opacity = 1); IN(S, '#hm', .05); MK(S, '#mk', TT(S, 'hash', .3)); POP(S, '#on', TT(S, 'o', .8) - .1, 'ding'); }},
 { html: `<div class="abs center" style="top:430px"><span class="tag">ASKED IN AMAZON INTERVIEWS · 2025</span></div><div class="abs center" style="top:600px"><span class="notes">NOTES</span></div>
   <div class="abs center h2" style="top:900px">comment NOTES for 5 more</div><div class="abs center" style="top:1120px"><span class="pill" id="fl"></span></div>`,
  draw(S) { S.$('#fl').textContent = 'Follow ' + HANDLE; POP(S, '.notes', TT(S, 'notes', .6) - .1); }},
];
