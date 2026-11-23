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
// uses:dsa  V4 quiz: countdown ring during the 3 s silence, A/B/C option cards, reveal.
const RING = `<svg class="ring" width="420" height="420" viewBox="0 0 420 420"><circle cx="210" cy="210" r="180" stroke="#2a2a31" stroke-width="26" fill="none"/><circle id="rg" cx="210" cy="210" r="180" stroke="#ffd23f" stroke-width="26" fill="none" stroke-linecap="round" transform="rotate(-90 210 210)" stroke-dasharray="1131" stroke-dashoffset="0"/></svg><div class="rn" id="rn">3</div>`;
const OPT = (k, t, cls = '') => `<div class="opt ${cls}" id="o${k}"><span>${'ABC'[k]}</span>${t}</div>`;
const OPTS = `${OPT(0, 'check every pair')}${OPT(1, 'sort first')}${OPT(2, 'a hash map')}`;
const SCENES = [
 { html: `<div class="abs center kick" style="top:470px">amazon interview quiz</div><div class="abs center h" style="top:560px;font-size:140px">beat the <span class="mark" id="mk">clock</span></div>
   <div class="abs center" style="top:900px">${EMO('alarm-clock').replace('1em', '220px').replace('1em', '220px')}</div>`,
  draw(S) { MK(S, '#mk', TT(S, 'clock', .6) - .1); S.$('img').style.transform = `rotate(${8 * Math.sin(S.t * 18)}deg)`; }},
 { html: `<div class="abs center h2" id="qq" style="top:380px">which two add up to <span style="color:var(--grn)">500</span>?</div>${ROW('rw', 640)}`,
  draw(S) { IN(S, '#qq', .05); S.$$('#rw .b').forEach((b, i) => { const t = TT(S, String(A[i]), .5 + i * .08) - .15; const q = S.P(t, .3, back); b.style.opacity = clamp(q); b.style.transform = `scale(${.7 + .3 * clamp(q)})`; if (S.on(t)) S.sfx(t, 'pop'); }); }},
 { html: `${ROW('rw', 380)}<div class="abs" style="left:330px;top:700px">${RING}</div>`,
  draw(S) { const g = TT(S, 'go', .25) + .3, left = clamp(1 - (S.t - g) / 3); S.$('#rg').setAttribute('stroke-dashoffset', 1131 * (1 - left)); S.$('#rn').textContent = Math.max(1, Math.ceil(3 * left));
    const k = Math.floor((S.t - g)); if (S.on(g) && k !== this.k && k < 3) { S.sfx(S.t, 'tick'); this.k = k; } S.$('#rg').setAttribute('stroke', left < .34 ? '#ff3b3b' : '#ffd23f'); FLOAT(S, '#rw', 5); }},
 { html: `${ROW('rw', 380)}<div class="abs center big" id="an" style="top:680px;font-size:120px;color:var(--grn);opacity:0">350 + 150 ✓</div><div class="abs center h2" id="rq" style="top:1000px;opacity:0">now the <span style="color:var(--yel)">real</span> question…</div>${GL('g3', 'rgba(61,220,132,.4)')}`,
  draw(S) { LITSET(S, 'rw', [1, 3]); POP(S, '#an', .05, 'ding'); GLOW(S, 'g3', .05); IN(S, '#rq', TT(S, 'real', .7) - .2); }},
 { html: `<div class="abs center h2" style="top:330px">fastest way to find them?</div><div class="opts">${OPTS}</div>`,
  draw(S) { [0, 1, 2].forEach(k => { const t = TT(S, ['every', 'sort', 'hash'][k], .4 + k * .15) - .2; const q = S.P(t, .35, back); const e = S.$('#o' + k); e.style.opacity = clamp(q); e.style.transform = `translateX(${120 * (1 - clamp(q))}px)`; if (S.on(t)) S.sfx(t, 'swish'); }); }},
 { html: `<div class="opts" style="top:300px">${OPT(0, 'check every pair', 'dim')}${OPT(1, 'sort first', 'dim')}${OPT(2, 'a hash map', 'win')}</div>
   <div class="abs center need" id="ex" style="top:1000px;opacity:0">save each · partner = 1 lookup</div><div class="abs center" id="on" style="top:1120px;opacity:0"><span class="badge" style="font-size:130px">O(n)</span></div>${GL('g5', 'rgba(61,220,132,.45)')}`,
  draw(S) { [0, 1, 2].forEach(k => S.$('#o' + k).style.opacity = 1); const tr = TT(S, 'right', .2); GLOW(S, 'g5', tr); SHAKE(S, '#o2', tr, 10); if (S.on(tr)) S.sfx(tr, 'ding'); IN(S, '#ex', TT(S, 'save', .4) - .1); POP(S, '#on', TT(S, 'o', .85) - .1, 'pop'); }},
 { html: `<div class="cmp"><div class="cr"><span>A · every pair</span><b class="r">O(n²)</b></div><div class="cr"><span>B · sort first</span><b class="y">O(n log n)</b></div><div class="cr"><span>C · hash map</span><b class="g">O(n)</b></div></div>`,
  draw(S) { S.$$('.cr').forEach((e, k) => IN(S, '.cr:nth-child(' + (k + 1) + ')', [TT(S, 'pair', .2), TT(S, 'sorting', .6), TT(S, 'log', .9) + .35][k] - .15, 30)); }},
 { html: `<div class="abs center h2" style="top:400px">comment <span style="color:var(--yel)">A, B or C</span></div><div class="abs center" style="top:600px"><span class="notes">NOTES</span></div>
   <div class="abs center h2" style="top:900px">for 5 more quizzes</div><div class="abs center" style="top:1120px"><span class="pill" id="fl"></span></div>`,
  draw(S) { S.$('#fl').textContent = 'Follow ' + HANDLE; POP(S, '.notes', TT(S, 'notes', .6) - .1); }},
];
