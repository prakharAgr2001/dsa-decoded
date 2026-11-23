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
// T1 Trapping Rain Water, notebook style. Numbers in spec.py (checked with node).
const R0 = 0;
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
function WRITE(S, id, at, dur = .5) { const e = S.$('#' + id); if (at < 0) { e.style.opacity = 1; e.style.clipPath = 'none'; return; } const p = S.P(at, Math.max(.12, dur * .8), x => x);
  e.style.opacity = p > 0 ? 1 : 0; e.style.clipPath = `inset(-30px ${100 - 100 * p}% -30px -30px)`; if (S.on(at)) S.sfx(at, 'click'); }
function DRAW(S, id, at, dur = .4) { const e = S.$('#' + id); if (at < 0) { e.style.strokeDashoffset = 0; return; } e.style.strokeDashoffset = 1 - S.P(at, dur * .8, eo); if (S.on(at)) S.sfx(at, 'swish'); }

// ---- Trapping Rain Water: bars on squared paper ----
const HT = [2, 0, 4, 1, 0, 3], WT_ = [0, 2, 0, 2, 3, 0], U = 80, BW2 = 120, GX = 20, X0b = 130, BASE = 820;
const bxl = i => X0b + i * (BW2 + GX), btop = i => BASE - HT[i] * U;
const BARS_SVG = HT.map((h, i) => h ? P('br' + i, rr(bxl(i), btop(i), BW2, h * U, 70 + i), INK, 5) : '').join('') + P('bs', ln(100, BASE, 990, BASE + 2, 79), INK, 6);
const BARS_HTML = HT.map((h, i) => `<div class="bfill" id="bf${i}" style="left:${bxl(i)}px;top:${btop(i)}px;width:${BW2}px;height:${h * U}px"></div>
  <div class="wat" id="w${i}" style="left:${bxl(i) + 4}px;top:${btop(i) - WT_[i] * U}px;width:${BW2 - 8}px;height:${WT_[i] * U}px"></div>
  <div class="cell blk" id="hv${i}" style="left:${bxl(i)}px;top:${BASE + 10}px;width:${BW2}px;font-size:46px;font-weight:700">${h}</div>`).join('');
function BARS(S, at) { HT.forEach((h, i) => { if (h) DRAW(S, 'br' + i, at < 0 ? -1 : at + i * .08, .3); S.$('#bf' + i).style.opacity = at < 0 || S.on(at + i * .08 + .2) ? 1 : 0; }); DRAW(S, 'bs', at < 0 ? -1 : at, .3); }
function HV(S, times) { times.forEach((t, i) => { const e = S.$('#hv' + i); e.style.opacity = t < 0 || S.on(t) ? 1 : 0; }); }
function WATER(S, i, at, dur = .5) { const e = S.$('#w' + i); const p = at < 0 ? 1 : S.P(at, dur, eo); e.style.transform = `scaleY(${p})`; e.style.opacity = p > 0 ? 1 : 0; if (at >= 0 && S.on(at)) S.sfx(at, 'swish'); }
const PTRS = `<div class="hw red b" id="pl" style="top:${BASE + 70}px;font-size:54px;opacity:1">↑L</div><div class="hw b" id="pr" style="top:${BASE + 70}px;font-size:54px;opacity:1;color:${BLUE}">↑R</div>`;
function PLR(S, l, r) { S.$('#pl').style.left = (bxl(0) + 30 + l * (BW2 + GX)) + 'px'; S.$('#pr').style.left = (bxl(0) + 30 + r * (BW2 + GX)) + 'px'; }
const MX = `<div class="hw red" id="lm" style="left:130px;top:${BASE + 150}px;font-size:50px;opacity:1">leftMax = <b id="lmv">0</b></div><div class="hw" id="rm" style="left:600px;top:${BASE + 150}px;font-size:50px;opacity:1">rightMax = <b id="rmv">0</b></div>`;
// dry-run table
const TY2 = 1060, RH2 = 70, COLS2 = [[120, 120, 'move'], [240, 120, 'bar'], [360, 200, 'max'], [560, 220, 'water'], [780, 240, 'total']];
const ROWS2 = [['L', 0, 2, '+0', 0], ['L', 1, 2, '+2', 2], ['R', 5, 3, '+0', 2], ['R', 4, 3, '+3', 5], ['R', 3, 3, '+2', 7]];
const TAB2_SVG = P('tb', rr(120, TY2, 900, RH2 * 6, 91), INK, 4) + P('th', ln(120, TY2 + RH2, 1020, TY2 + RH2, 92), INK, 4) + [240, 360, 560, 780].map((x, k) => P('tc' + k, ln(x, TY2, x, TY2 + RH2 * 6, 93 + k), INK, 3)).join('');
const TAB2_HEAD = COLS2.map((c, k) => `<div class="cell blk" id="hd${k}" style="left:${c[0]}px;top:${TY2 + 10}px;width:${c[1]}px;font-size:40px;font-weight:700">${c[2]}</div>`).join('');
const TAB2_ROWS = ROWS2.map((r, ri) => r.map((v, ci) => `<div class="cell ${ci === 0 ? (v === 'L' ? 'red' : '') : ci === 3 && v !== '+0' ? 'grn' : 'blk'}" id="c${ri}${ci}" style="left:${COLS2[ci][0]}px;top:${TY2 + RH2 * (ri + 1) + 8}px;width:${COLS2[ci][1]}px;font-size:44px;${ci === 3 && v !== '+0' ? 'font-weight:700' : ''}">${v}</div>`).join('')).join('');
function TABLE2(S, at) { DRAW(S, 'tb', at, .45); DRAW(S, 'th', at < 0 ? -1 : at + .25, .25); [0, 1, 2, 3].forEach(k => DRAW(S, 'tc' + k, at < 0 ? -1 : at + .3 + k * .05, .25)); COLS2.forEach((c, k) => S.$('#hd' + k).style.opacity = at < 0 || S.on(at + .4) ? 1 : 0); }
function ROW2(S, ri, at) { for (let c = 0; c < 5; c++) CELL(S, ri, c, at < 0 ? -1 : at + c * .07); }
function CELL(S, r, c, at) { const e = S.$(`#c${r}${c}`); if (at < 0) { e.style.opacity = 1; e.style.clipPath = 'none'; return; } const p = S.P(at, .2, x => x); e.style.opacity = p > 0 ? 1 : 0; e.style.clipPath = `inset(-20px ${100 - 100 * p}% -20px -20px)`; if (S.on(at)) S.sfx(at, 'click'); }
const STATIC6 = [-1, -1, -1, -1, -1, -1];
const SCENES = [
 { // 0 hook
  html: `<div class="sticky" id="st">${H('o1', 60, 50, 38, 'OFFER LETTER', 'gry b')}${H('o2', 60, 110, 48, 'Analyst · Goldman Sachs · India', 'blk')}${H('o3', 60, 200, 190, '₹25 LPA', 'red mk')}</div>
   ${SVG(P('c0', ell(470, 640, 300, 125, 3), RED, 6) + P('u0', ln(150, 990, 1000, 984, 5), BLUE, 5))}
   ${H('a1', 150, 900, 46, 'Asked in Goldman Sachs interviews · 2025', 'b')}${H('a2', 150, 1030, 62, '→ this exact question', 'red b')}${H('a3', 150, 1140, 34, 'salary: AmbitionBox range for engineering analysts', 'gry')}`,
  draw(S) { const p = S.P(0, .35, back); S.$('#st').style.opacity = clamp(p); S.$('#st').style.translate = `0 ${60 * (1 - clamp(p))}px`;
    WRITE(S, 'o1', .05, .15); WRITE(S, 'o2', .1, .3); WRITE(S, 'o3', TT(S, 'lakh', .2) - .25, .4); DRAW(S, 'c0', TT(S, 'Goldman', .3), .4);
    WRITE(S, 'a1', TT(S, 'exact', .55) - .45, .6); DRAW(S, 'u0', TT(S, 'question', .65), .3); WRITE(S, 'a2', TT(S, 'interviews', .9) - .3, .3); WRITE(S, 'a3', TT(S, 'interviews', .9), .25); }},
 { // 1 question + empty bars + rain
  html: `${SVG(BARS_SVG + [0, 1, 2, 3, 4, 5, 6, 7, 8].map(k => P('rn' + k, ln(160 + k * 95, 260 + (k % 3) * 30, 140 + k * 95, 330 + (k % 3) * 30, 80 + k), BLUE, 4)).join(''))}${BARS_HTML}
   ${H('q0', 130, 940, 84, 'Q.', 'red b')}${H('q1', 230, 950, 60, 'How much rain water')}${H('q2', 130, 1040, 60, 'stays trapped between the bars?')}`,
  draw(S) { BARS(S, .02); HV(S, HT.map(() => -1)); for (let k = 0; k < 9; k++) { const t = (.1 + k * .13 + S.t * 1.3) % 1.4; const e = S.$('#rn' + k); e.style.strokeDashoffset = 0; e.style.translate = `${-20 * t}px ${200 * t}px`; e.style.opacity = t < 1.2 ? 1 : 0; }
    WRITE(S, 'q0', .1, .2); const th = TT(S, 'how', .55); WRITE(S, 'q1', th - .1, .6); WRITE(S, 'q2', th + .4, TT(S, 'trapped', .95) - th); }},
 { // 2 example: heights spoken, water fills, answer
  html: `${SVG(BARS_SVG + P('ae', ell(700, 1000, 230, 70, 9), GRN, 6))}${BARS_HTML}${H('ans', 520, 955, 80, '= 7 units', 'grn b')}${H('lb', 130, 960, 50, 'water:', 'blk')}`,
  draw(S) { BARS(S, -1); HV(S, HT.map((h, i) => TT(S, String(h), .1 + i * .1, [1, 1, 1, 1, 2, 1][i] ) - .15)); const ta = TT(S, '7', .8) - .2;
    [1, 3, 4].forEach((i, k) => WATER(S, i, ta - .3 + k * .12, .4)); WRITE(S, 'lb', ta - .3, .2); WRITE(S, 'ans', ta, .3); DRAW(S, 'ae', ta + .2, .35); }},
 { // 3 brute force: scan left + right for one bar, then the count
  html: `${SVG(BARS_SVG + P('sl', arw(bxl(3) + 60, btop(3) - 20, bxl(2) + 60, btop(2) - 20, 60), RED, 4) + P('sr', arw(bxl(3) + 60, btop(3) - 20, bxl(5) + 60, btop(5) - 20, 90), BLUE, 4)
     + P('sx', ln(110, 1100, 1000, 1060, 9), RED, 8) + P('sx2', rr(150, 1200, 760, 120, 17), RED, 5))}${BARS_HTML}
   ${H('bf', 130, 930, 48, 'Brute force: every bar scans both ways', 'blk b')}${H('m1', 130, 1020, 56, 'n = 5,000 → <span class="hl">25,005,000</span> reads', 'blk')}${H('rj', 180, 1218, 80, '✗ TOO SLOW · O(n²)', 'red mk')}`,
  draw(S) { BARS(S, -1); HV(S, STATIC6); const ts = TT(S, 'scan', .25); DRAW(S, 'sl', ts, .4); DRAW(S, 'sr', ts + .35, .45); WRITE(S, 'bf', .05, ts + .4);
    WRITE(S, 'm1', TT(S, '5000', .6) - .1, TT(S, 'million', .85) - TT(S, '5000', .6) + .2); const tr = TT(S, 'rejected', .95) - .1; DRAW(S, 'sx', tr, .2); WRITE(S, 'rj', tr - .1, .18); DRAW(S, 'sx2', tr + .1, .3); SHAKE(S, '#rj', tr, 8); }},
 { // 4 the rule, shown on bar 4 (walls 4 and 3 -> min 3 -> water 3)
  html: `${SVG(BARS_SVG + P('lv', ln(bxl(2), btop(5), bxl(5) + BW2, btop(5), 41), BLUE, 4) + P('fb', rr(120, 930, 880, 120, 42), BLUE, 5))}${BARS_HTML}
   ${H('fm', 145, 952, 48, 'water = min(leftMax, rightMax) − h', 'b')}${H('ex', 130, 1100, 52, 'bar 4: min(4, 3) − 0 = <b class="grn">3</b>', 'blk')}`,
  draw(S) { BARS(S, -1); HV(S, STATIC6); const tr = TT(S, 'smaller', .45); WRITE(S, 'fm', tr - .3, .6); DRAW(S, 'fb', tr + .2, .4); DRAW(S, 'lv', tr, .4); const tm = TT(S, 'minus', .8) - .1; WRITE(S, 'ex', tm, .5); WATER(S, 4, tm + .3, .4); }},
 { // 5 two pointers intro + table appears
  html: `${SVG(BARS_SVG + TAB2_SVG)}${BARS_HTML}${PTRS}${MX}${TAB2_HEAD}${TAB2_ROWS}${H('rl', 130, 200, 52, 'move the side with the <span class="hl">shorter wall</span>', 'blk b')}`,
  draw(S) { BARS(S, -1); HV(S, STATIC6); PLR(S, 0, 5); S.$('#pl').style.opacity = S.$('#pr').style.opacity = S.on(TT(S, 'pointers', .25) - .1) ? 1 : 0; S.$('#lm').style.opacity = S.$('#rm').style.opacity = S.on(TT(S, 'pointers', .25) + .2) ? 1 : 0;
    WRITE(S, 'rl', TT(S, 'move', .45) - .1, .6); TABLE2(S, TT(S, 'decided', .85) - .6); for (let r = 0; r < 5; r++) for (let c = 0; c < 5; c++) S.$(`#c${r}${c}`).style.opacity = 0; }},
 { // 6 left steps
  html: `${SVG(BARS_SVG + TAB2_SVG)}${BARS_HTML}${PTRS}${MX}${TAB2_HEAD}${TAB2_ROWS}`,
  draw(S) { BARS(S, -1); HV(S, STATIC6); TABLE2(S, -1); const t0 = TT(S, 'left', .1), t1 = TT(S, 'one', .55) - .1, t2 = TT(S, 'is', .9, 3);
    PLR(S, S.on(t1) ? 1 : 0, 5); S.$('#lmv').textContent = S.on(t0 + .3) ? 2 : 0; S.$('#rmv').textContent = 0; ROW2(S, 0, t0 + .2); ROW2(S, 1, t1); WATER(S, 1, t2 - .2, .45);
    for (let r = 2; r < 5; r++) for (let c = 0; c < 5; c++) S.$(`#c${r}${c}`).style.opacity = 0; }},
 { // 7 right steps
  html: `${SVG(BARS_SVG + TAB2_SVG)}${BARS_HTML}${PTRS}${MX}${TAB2_HEAD}${TAB2_ROWS}`,
  draw(S) { BARS(S, -1); HV(S, STATIC6); TABLE2(S, -1); WATER(S, 1, -1); ROW2(S, 0, -1); ROW2(S, 1, -1); S.$('#lmv').textContent = 2;
    const t0 = TT(S, 'right', .1), t4 = TT(S, 'four', .5) - .15, t3 = TT(S, 'three', .7) - .15; S.$('#rmv').textContent = S.on(t0 + .3) ? 3 : 0;
    const r = S.on(t3) ? 3 : S.on(t4) ? 4 : 5; PLR(S, 2, r); ROW2(S, 2, t0 + .25); ROW2(S, 3, t4); WATER(S, 4, t4 + .2, .45); ROW2(S, 4, t3); WATER(S, 3, TT(S, '2', .95, 1) - .2, .4); }},
 { // 8 total
  html: `${SVG(BARS_SVG + P('tc', rr(120, 940, 860, 130, 61), GRN, 6))}${BARS_HTML}${H('tt', 150, 950, 80, 'total = 2 + 3 + 2 = 7 ✓', 'grn b')}`,
  draw(S) { BARS(S, -1); HV(S, STATIC6); [1, 3, 4].forEach(i => WATER(S, i, -1)); const tt = TT(S, 'total', .1); WRITE(S, 'tt', tt, TT(S, 'seven', .7) - tt + .1); const ts = TT(S, 'seven', .7); DRAW(S, 'tc', ts, .35); if (S.on(ts)) S.sfx(ts, 'ding');
    [1, 3, 4].forEach((i, k) => { const e = S.$('#w' + i); e.style.boxShadow = S.on(TT(S, '2', .3) + k * .35 - .1) ? '0 0 0 5px #1e8a4c' : ''; }); }},
 { // 9 complexity + stamp
  html: `${SVG(P('tbx', rr(115, 420, 860, 120, 52), GRN, 5) + P('st3', ln(120, 700, 700, 692, 53), RED, 6) + P('stp', rr(130, 840, 860, 160, 54), RED, 6))}
   ${H('t1', 145, 432, 70, 'O(n) time · O(1) space', 'grn b')}${H('t1b', 145, 560, 46, 'one pass, no extra arrays', 'gry')}${H('t3', 130, 650, 60, 'Brute force: O(n²)', 'red')}
   <div style="position:absolute;left:130px;top:840px;width:860px;height:160px;transform:rotate(-4deg)">${H('pn', 26, 28, 74, 'PATTERN: TWO POINTERS', 'red mk')}</div>`,
  draw(S) { const tp = TT(S, 'pass', .15); WRITE(S, 't1b', tp - .1, .35); WRITE(S, 't3', .1, .3); DRAW(S, 'st3', .4, .2); const to = TT(S, 'o', .45) - .1; WRITE(S, 't1', to, TT(S, 'space', .95) - to); DRAW(S, 'tbx', TT(S, 'space', .95) - .1, .3);
    const tz = Math.min(S.dur - .6, TT(S, 'space', .95) + .1); DRAW(S, 'stp', tz, .25); WRITE(S, 'pn', tz + .05, .25); }},
 { // 10 CTA
  html: `${SVG(P('nb', rr(250, 520, 580, 250, 61), RED, 7) + P('da', arw(540, 800, 545, 900, 0), BLUE, 5) + P('fu', ln(300, 1150, 780, 1146, 62), BLUE, 4))}
   ${HC('c1', 400, 80, 'Comment', 'blk b')}${HC('c2', 520, 230, 'NOTES', 'red mk')}${HC('c3', 930, 56, '5 more two-pointer questions')}${HC('c4', 1010, 46, 'straight to your DMs', 'gry')}${HC('c5', 1080, 56, '', 'b')}`,
  draw(S) { S.$('#c5').textContent = 'follow ' + HANDLE; WRITE(S, 'c1', .02, .2); const tn = TT(S, 'notes', .15) - .15; WRITE(S, 'c2', tn, .3); DRAW(S, 'nb', tn + .2, .35);
    DRAW(S, 'da', TT(S, 'five', .5) - .1, .25); WRITE(S, 'c3', TT(S, 'five', .5), .5); WRITE(S, 'c4', TT(S, 'questions', .95) - .1, .25); WRITE(S, 'c5', S.dur - 1.2, .3); DRAW(S, 'fu', S.dur - .8, .25); }},
];
