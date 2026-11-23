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
// W1 notebook explainer: handwritten ink on squared paper; boxes/circles/arrows draw themselves; dry-run table like a teacher.
// Numbers: [120,350,280,150,400] target 500 -> only pair (1,3); 5,000 numbers -> 12,497,500 pairs (see spec.py).
const A = [120, 350, 280, 150, 400], BX = i => 150 + i * 170, BY = 430, BW = 150, BH = 130;
const BLUE = '#1f3fa8', RED = '#d0312d', GRN = '#1e8a4c', INK = '#262626';
const J = (s, k, a = 7) => (R(s * 7.31 + k) - .5) * a;
const rr = (x, y, w, h, s) => `M${x + J(s, 1)} ${y + J(s, 2)} L${x + w + J(s, 3)} ${y + J(s, 4)} L${x + w + J(s, 5)} ${y + h + J(s, 6)} L${x + J(s, 7)} ${y + h + J(s, 8)} L${x + J(s, 9) + 4} ${y + J(s, 10) - 5}`;
const ln = (x1, y1, x2, y2, s) => `M${x1} ${y1} Q${(x1 + x2) / 2 + J(s, 1, 6)} ${(y1 + y2) / 2 + J(s, 2, 6)} ${x2} ${y2}`;
const ell = (cx, cy, rx, ry, s) => { let d = ''; for (let k = 0; k <= 30; k++) { const a = -1.3 + k * (2 * Math.PI + .7) / 30, r = 1 + J(s, k, .09); d += (k ? 'L' : 'M') + (cx + rx * r * Math.cos(a)).toFixed(1) + ' ' + (cy + ry * r * Math.sin(a)).toFixed(1) + ' '; } return d; };
const arw = (x1, y1, x2, y2, h) => { const cx = (x1 + x2) / 2, cy = Math.min(y1, y2) - h, dx = x2 - cx, dy = y2 - cy, L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L, a = 24;
  return `M${x1} ${y1} Q${cx} ${cy} ${x2} ${y2} M${x2} ${y2} L${x2 - a * (ux * .8 - uy * .55)} ${y2 - a * (uy * .8 + ux * .55)} M${x2} ${y2} L${x2 - a * (ux * .8 + uy * .55)} ${y2 - a * (uy * .8 - ux * .55)}`; };
const P = (id, d, col, w = 5) => `<path id="${id}" d="${d}" pathLength="1" stroke="${col}" stroke-width="${w}"/>`;
const SVG = inner => `<svg class="ink" viewBox="0 0 1080 1920">${inner}</svg>`;
const H = (id, x, y, sz, txt, cls = '') => `<div class="hw ${cls}" id="${id}" style="left:${x}px;top:${y}px;font-size:${sz}px">${txt}</div>`;
const HC = (id, y, sz, txt, cls = '') => `<div style="position:absolute;left:0;right:0;top:${y}px;text-align:center"><span class="hw ${cls}" id="${id}" style="position:relative;display:inline-block;font-size:${sz}px">${txt}</span></div>`;
function WRITE(S, id, at, dur = .5) { const e = S.$('#' + id); if (at < 0) { e.style.opacity = 1; e.style.clipPath = 'none'; return; } const p = S.P(at, Math.max(.15, dur), x => x);
  e.style.opacity = p > 0 ? 1 : 0; e.style.clipPath = `inset(-30px ${100 - 100 * p}% -30px -30px)`; if (S.on(at)) S.sfx(at, 'click'); }
function DRAW(S, id, at, dur = .4) { const e = S.$('#' + id); if (at < 0) { e.style.strokeDashoffset = 0; return; } e.style.strokeDashoffset = 1 - S.P(at, dur, eo); if (S.on(at)) S.sfx(at, 'swish'); }
// array of boxes
const ARR_SVG = A.map((v, i) => P('bx' + i, rr(BX(i), BY, BW, BH, i + 1), INK, 4)).join('');
const ARR_HTML = A.map((v, i) => `<div class="cell blk b" id="n${i}" style="left:${BX(i)}px;top:${BY + 24}px;width:${BW}px;font-size:68px;font-weight:700">${v}</div><div class="cell gry" id="x${i}" style="left:${BX(i)}px;top:${BY + BH + 4}px;width:${BW}px;font-size:34px">${i}</div>`).join('');
function ARRAY(S, times) { times.forEach((t, i) => { DRAW(S, 'bx' + i, t, .3); const op = t < 0 || S.on(t + .12) ? 1 : 0; S.$('#n' + i).style.opacity = op; S.$('#x' + i).style.opacity = op; }); }
const STATIC = [-1, -1, -1, -1, -1];
// dry-run table
const TY = 720, RH = 90, COLS = [[120, 100, 'i'], [220, 190, 'num'], [410, 190, 'need'], [600, 180, 'seen?'], [780, 240, 'action']];
const ROWS = [[0, 120, 380, 'no', 'save'], [1, 350, 150, 'no', 'save'], [2, 280, 220, 'no', 'save'], [3, 150, 350, 'YES', 'return [1,3]']];
const RCLS = ['blk', 'blk', 'blk', '', ''];
const TAB_SVG = P('tb', rr(120, TY, 900, RH * 5, 31), INK, 4) + P('th', ln(120, TY + RH, 1020, TY + RH, 32), INK, 4) + [220, 410, 600, 780].map((x, k) => P('tc' + k, ln(x, TY, x, TY + RH * 5, 40 + k), INK, 3)).join('');
const TAB_HEAD = COLS.map((c, k) => `<div class="cell blk" id="hd${k}" style="left:${c[0]}px;top:${TY + 16}px;width:${c[1]}px;font-size:44px;font-weight:700">${c[2]}</div>`).join('');
const TAB_ROWS = n => ROWS.slice(0, n).map((r, ri) => r.map((v, ci) => { const cls = ci === 3 ? (v === 'YES' ? 'grn' : 'red') : ci === 4 ? (ri === 3 ? 'grn' : '') : RCLS[ci];
  return `<div class="cell ${cls}" id="c${ri}${ci}" style="left:${COLS[ci][0]}px;top:${TY + RH * (ri + 1) + 16}px;width:${COLS[ci][1]}px;font-size:${ci === 4 && ri === 3 ? 44 : 52}px;${ri === 3 && ci >= 3 ? 'font-weight:700' : ''}">${v}</div>`; }).join('')).join('');
function TABLE(S, at) { DRAW(S, 'tb', at, .5); DRAW(S, 'th', at < 0 ? -1 : at + .3, .3); [0, 1, 2, 3].forEach(k => DRAW(S, 'tc' + k, at < 0 ? -1 : at + .35 + k * .06, .3)); COLS.forEach((c, k) => S.$('#hd' + k).style.opacity = at < 0 || S.on(at + .5) ? 1 : 0); }
function CELL(S, r, c, at) { const e = S.$(`#c${r}${c}`); if (at < 0) { e.style.opacity = 1; e.style.clipPath = 'none'; return; } const p = S.P(at, .25, x => x); e.style.opacity = p > 0 ? 1 : 0; e.style.clipPath = `inset(-20px ${100 - 100 * p}% -20px -20px)`; if (S.on(at)) S.sfx(at, 'click'); }
const SEENL = `<div class="hw blk" id="sl" style="left:130px;top:${TY + RH * 5 + 40}px;font-size:58px;opacity:1">seen = { <span id="s0">120</span><span id="s1">, <span id="s1v">350</span></span><span id="s2">, 280</span> }</div>`;
const PTR = `<div class="hw red b" id="pt" style="top:600px;font-size:60px;opacity:1">↑ i</div>`;
function PT(S, f) { S.$('#pt').style.left = (BX(0) + 45 + f * 170) + 'px'; }
const SCENES = [
 { // 0 hook
  html: `<div class="sticky" id="st">${H('o1', 60, 50, 38, 'OFFER LETTER', 'gry b')}${H('o2', 60, 110, 60, 'SDE-1 · Amazon · India', 'blk')}${H('o3', 60, 200, 190, '₹28 LPA', 'red mk')}</div>
   ${SVG(P('c0', ell(470, 640, 300, 125, 3), RED, 6) + P('u0', ln(150, 990, 940, 984, 5), BLUE, 5))}
   ${H('a1', 150, 900, 56, 'Asked in Amazon interviews · 2025', 'b')}${H('a3', 150, 1060, 34, 'salary: AmbitionBox range for SDE-1', 'gry')}`,
  draw(S) { const p = S.P(0, .35, back); S.$('#st').style.opacity = clamp(p); S.$('#st').style.translate = `0 ${60 * (1 - clamp(p))}px`;
    WRITE(S, 'o1', .05, .15); WRITE(S, 'o2', .1, .25); WRITE(S, 'o3', TT(S, 'lakh', .1) - .25, .4); DRAW(S, 'c0', TT(S, 'Amazon', .25), .4);
    WRITE(S, 'a1', TT(S, 'question', .45) - .2, .6); DRAW(S, 'u0', TT(S, 'interviews', .85) - .2, .3); WRITE(S, 'a3', TT(S, 'interviews', .85), .3); }},
 { // 1 question + example in one
  html: `${SVG(ARR_SVG + P('u1', ln(130, 790, 900, 786, 7), RED, 6))}${H('l0', 130, 330, 56, 'nums =', 'blk')}${ARR_HTML}${H('q0', 130, 690, 72, 'Q. which two add up to 500?', 'red b')}`,
  draw(S) { WRITE(S, 'l0', .02, .2); ARRAY(S, A.map((v, i) => TT(S, String(v), .1 + i * .12) - .18)); const tw = TT(S, 'which', .75); WRITE(S, 'q0', tw - .15, TT(S, '500', .95) - tw + .25); DRAW(S, 'u1', TT(S, '500', .95) - .1, .3); }},
 { // 2 brute force
  html: `${SVG(ARR_SVG + [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]].map((p, k) => P('p' + k, arw(BX(p[0]) + 75, BY - 10, BX(p[1]) + 75, BY - 10, 30 + (p[1] - p[0]) * 26), BLUE, 3)).join('')
     + P('sx', ln(110, 880, 1000, 840, 9), RED, 8) + P('sx2', rr(150, 1010, 760, 120, 17), RED, 5))}${ARR_HTML}
   ${H('bf', 130, 660, 60, 'Brute force: check every pair', 'blk b')}${H('m1', 130, 760, 58, 'pairs = n(n−1) / 2')}${H('m2', 130, 850, 58, 'n = 5,000 → <span class="hl">12,497,500</span> checks', 'blk')}
   ${H('rj', 180, 1030, 80, '✗ TOO SLOW · O(n²)', 'red mk')}`,
  draw(S) { ARRAY(S, STATIC); const tp = TT(S, 'pair', .2); for (let k = 0; k < 10; k++) DRAW(S, 'p' + k, .03 + k * (tp + .4) / 10, .2);
    WRITE(S, 'bf', .03, tp + .1); WRITE(S, 'm1', TT(S, 'for', .35) - .2, .4); WRITE(S, 'm2', TT(S, '5000', .45) - .1, TT(S, 'million', .8) - TT(S, '5000', .45) + .2);
    const tr = TT(S, 'rejected', .95) - .1; DRAW(S, 'sx', tr, .2); WRITE(S, 'rj', tr, .25); DRAW(S, 'sx2', tr + .1, .3); SHAKE(S, '#rj', tr, 8); }},
 { // 3 the trick
  html: `${SVG(ARR_SVG + P('fb', rr(160, 770, 620, 110, 21), BLUE, 5))}${ARR_HTML}${H('id', 130, 660, 62, 'Trick: remember what you\'ve <span class="hl">seen</span>', 'blk b')}
   ${H('fm', 190, 782, 68, 'need = 500 − num', 'b')}${H('qq', 130, 930, 58, '“have I already seen need?”', 'red')}${H('s00', 130, 1060, 60, 'seen = { }', 'blk')}`,
  draw(S) { ARRAY(S, STATIC); WRITE(S, 'id', TT(S, 'trick', .1) - .1, .5); DRAW(S, 'fb', TT(S, 'number', .35) - .1, .35); WRITE(S, 'fm', TT(S, 'number', .35), .45);
    const ta = TT(S, 'ask', .45); WRITE(S, 'qq', ta - .1, TT(S, 'minus', .9) - ta + .2); WRITE(S, 's00', TT(S, 'it', .97) - .1, .25); }},
 { // 4 dry run rows 0-2
  html: `${SVG(ARR_SVG + TAB_SVG)}${ARR_HTML}${PTR}${TAB_HEAD}${TAB_ROWS(3)}${SEENL}`,
  draw(S) { ARRAY(S, STATIC); TABLE(S, 0); const ts = [TT(S, '120', .05), TT(S, '350', .38), TT(S, '280', .7)], sv = [1, 2, 3].map(n => TT(S, 'save', .25 + n * .25, n)), nd = [1, 2, 3].map(n => TT(S, 'needs', .1 + n * .3, n));
    let i = 0; ts.forEach((t, j) => { if (S.on(t - .15)) i = j; }); let f = i; if (i < 2) f = i + S.P(ts[i + 1] - .35, .25, eio); PT(S, f);
    for (let r = 0; r < 3; r++) { CELL(S, r, 0, ts[r] - .15); CELL(S, r, 1, ts[r] - .1); CELL(S, r, 2, nd[r] + .05); CELL(S, r, 3, nd[r] + .3); CELL(S, r, 4, sv[r] - .05); S.$('#s' + r).style.opacity = S.on(sv[r]) ? 1 : 0; } }},
 { // 5 the hit
  html: `${SVG(ARR_SVG + TAB_SVG + P('ar', arw(BX(3) + 75, BY - 10, BX(1) + 75, BY - 10, 120), GRN, 6) + P('ey', ell(690, TY + RH * 4 + 45, 80, 40, 23), GRN, 5))}${ARR_HTML}${PTR}${TAB_HEAD}${TAB_ROWS(4)}${SEENL}
   ${H('dn', 620, TY + RH * 5 + 120, 110, '✓ done!', 'grn mk')}`,
  draw(S) { ARRAY(S, STATIC); TABLE(S, -1); PT(S, 3); for (let r = 0; r < 3; r++) for (let c = 0; c < 5; c++) CELL(S, r, c, -1); [0, 1, 2].forEach(r => S.$('#s' + r).style.opacity = 1);
    CELL(S, 3, 0, .02); CELL(S, 3, 1, TT(S, '150', .1) - .1); CELL(S, 3, 2, TT(S, 'needs', .25) + .05); const ta = TT(S, 'already', .5) - .1;
    CELL(S, 3, 3, ta); DRAW(S, 'ey', ta + .1, .3); DRAW(S, 'ar', ta, .4); S.$('#s1v').classList.toggle('hl', S.on(ta)); CELL(S, 3, 4, TT(S, 'seen', .7));
    const td = TT(S, 'done', .9) - .1; WRITE(S, 'dn', td, .25); if (S.on(td)) S.sfx(td, 'ding'); }},
 { // 6 complexity + stamp
  html: `${SVG(P('tbx', rr(115, 420, 520, 120, 52), GRN, 5) + P('st3', ln(120, 700, 640, 692, 53), RED, 6) + P('stp', rr(150, 840, 820, 160, 54), RED, 6))}
   ${H('t1', 145, 430, 84, 'Time: O(n)', 'grn b')}${H('t1b', 660, 455, 46, '← one pass', 'gry')}${H('t3', 130, 650, 60, 'Brute force: O(n²)', 'red')}
   <div style="position:absolute;left:150px;top:840px;width:820px;height:160px;transform:rotate(-4deg)">${H('pn', 30, 22, 92, 'PATTERN: HASHING', 'red mk')}</div>`,
  draw(S) { const tp = TT(S, 'pass', .2); WRITE(S, 't1', 0, .3); DRAW(S, 'tbx', .25, .3); WRITE(S, 't1b', tp, .25); WRITE(S, 't3', .2, .3); DRAW(S, 'st3', .5, .2);
    const to = TT(S, 'o', .8) - .1; DRAW(S, 'stp', to, .25); WRITE(S, 'pn', to + .05, .25); }},
 { // 7 CTA
  html: `${SVG(P('nb', rr(250, 520, 580, 250, 61), RED, 7) + P('da', arw(540, 800, 545, 900, 0), BLUE, 5) + P('fu', ln(300, 1150, 780, 1146, 62), BLUE, 4))}
   ${HC('c1', 400, 80, 'Comment', 'blk b')}${HC('c2', 520, 230, 'NOTES', 'red mk')}${HC('c3', 930, 56, '5 variations of this question')}${HC('c4', 1010, 46, 'straight to your DMs', 'gry')}${HC('c5', 1080, 56, '', 'b')}`,
  draw(S) { S.$('#c5').textContent = 'follow ' + HANDLE; WRITE(S, 'c1', .02, .2); const tn = TT(S, 'notes', .15) - .15; WRITE(S, 'c2', tn, .3); DRAW(S, 'nb', tn + .2, .35);
    DRAW(S, 'da', TT(S, 'five', .45) - .1, .25); WRITE(S, 'c3', TT(S, 'five', .45), .5); WRITE(S, 'c4', TT(S, 'question', .9) - .1, .25); WRITE(S, 'c5', S.dur - 1.3, .3); DRAW(S, 'fu', S.dur - .9, .25); }},
];
