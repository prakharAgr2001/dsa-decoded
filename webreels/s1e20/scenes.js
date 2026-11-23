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
// ---- nb: data-driven notebook explainer. An episode = NB {kind, arr, water?, scenes:[...]} (one scene per narration line). ----
// Scene keys: type ('hook'|'cta'|'cx'), vis (bool), draw [cue per element], h {t,at}, lines [{t,at,c,s,box,strike,circ,b}], big {t,at,c},
// table {cols, rows, w?}, ev [[cue, {ptr, mark, win, fill, arc, row, st, push, pop}]], reset, hook {...}, cta {t}, cx {time, space, brute, pattern}.
// Cues: 'word' | 'word#2' (n-th occurrence in the scene) | number (seconds into scene). Text markup: [x] = highlighter.
const BLUE = '#1f3fa8', RED = '#d0312d', GRN = '#1e8a4c', INK = '#262626';
const COL = { blue: BLUE, red: RED, grn: GRN, blk: INK, gry: '#8a8476' };
const PCOL = { L: RED, l: RED, i: RED, lo: RED, slow: RED, R: BLUE, r: BLUE, j: BLUE, hi: BLUE, fast: BLUE, mid: GRN, k: GRN, w: GRN };
const J = (s, k, a = 7) => (R(s * 7.31 + k) - .5) * a;
const rr = (x, y, w, h, s) => `M${x + J(s, 1)} ${y + J(s, 2)} L${x + w + J(s, 3)} ${y + J(s, 4)} L${x + w + J(s, 5)} ${y + h + J(s, 6)} L${x + J(s, 7)} ${y + h + J(s, 8)} L${x + J(s, 9) + 4} ${y + J(s, 10) - 5}`;
const ln = (x1, y1, x2, y2, s) => `M${x1} ${y1} Q${(x1 + x2) / 2 + J(s, 1, 6)} ${(y1 + y2) / 2 + J(s, 2, 6)} ${x2} ${y2}`;
const ell = (cx, cy, rx, ry, s) => { let d = ''; for (let k = 0; k <= 30; k++) { const a = -1.3 + k * (2 * Math.PI + .7) / 30, r = 1 + J(s, k, .09); d += (k ? 'L' : 'M') + (cx + rx * r * Math.cos(a)).toFixed(1) + ' ' + (cy + ry * r * Math.sin(a)).toFixed(1) + ' '; } return d; };
const arw = (x1, y1, x2, y2, h) => { const cx = (x1 + x2) / 2, cy = Math.min(y1, y2) - h, dx = x2 - cx, dy = y2 - cy, L = Math.hypot(dx, dy) || 1, ux = dx / L, uy = dy / L, a = 24;
  return `M${x1} ${y1} Q${cx} ${cy} ${x2} ${y2} M${x2} ${y2} L${x2 - a * (ux * .8 - uy * .55)} ${y2 - a * (uy * .8 + ux * .55)} M${x2} ${y2} L${x2 - a * (ux * .8 + uy * .55)} ${y2 - a * (uy * .8 - ux * .55)}`; };
const P = (id, d, col, w = 5) => `<path id="${id}" d="${d}" pathLength="1" stroke="${col}" stroke-width="${w}"/>`;
const MU = t => String(t).replace(/\[([^\]]+)\]/g, '<span class="hl">$1</span>');
const H = (id, x, y, sz, txt, cls = '') => `<div class="hw ${cls}" id="${id}" style="left:${x}px;top:${y}px;font-size:${sz}px">${MU(txt)}</div>`;
const HC = (id, y, sz, txt, cls = '') => `<div style="position:absolute;left:0;right:0;top:${y}px;text-align:center"><span class="hw ${cls}" id="${id}" style="position:relative;display:inline-block;font-size:${sz}px">${MU(txt)}</span></div>`;
function WRITE(S, id, at, dur = .5) { const e = S.$('#' + id); if (!e) return; if (at < 0) { e.style.opacity = 1; e.style.clipPath = 'none'; return; } const p = S.P(at, Math.max(.12, dur * .8), x => x);
  e.style.opacity = p > 0 ? 1 : 0; e.style.clipPath = `inset(-30px ${100 - 100 * p}% -30px -30px)`; if (S.on(at)) S.sfx(at, 'click'); }
function DRAW(S, id, at, dur = .4) { const e = S.$('#' + id); if (!e) return; if (at < 0) { e.style.strokeDashoffset = 0; return; } e.style.strokeDashoffset = 1 - S.P(at, dur * .8, eo); if (S.on(at)) S.sfx(at, 'swish'); }
function CUE(S, c, f = .3) { if (c === undefined || c === null) return S.dur * f; if (typeof c === 'number') return c; const m = String(c).split('#'); return TT(S, m[0], f, m[1] ? +m[1] : 1); }
// ---- geometry ----
function GEO(nb) {
  const n = nb.arr.length, g = {};
  if (nb.kind === 'bars') { const mx = Math.max(...nb.arr, ...(nb.arr.map((h, i) => h + ((nb.water || [])[i] || 0)))); g.U = Math.min(80, 300 / mx); g.bw = Math.min(120, Math.floor((860 - 20 * (n - 1)) / n)); g.gap = 20;
    g.x0 = (1080 - (n * g.bw + (n - 1) * g.gap)) / 2; g.base = 820; g.cx = i => g.x0 + i * (g.bw + g.gap) + g.bw / 2; g.ptrY = g.base + 64; g.below = g.base + 210; return g; }
  g.gap = 16; g.bw = Math.min(150, Math.floor((880 - g.gap * (n - 1)) / n)); g.bh = Math.min(130, g.bw + 10); g.x0 = (1080 - (n * g.bw + (n - 1) * g.gap)) / 2; g.y = 430;
  g.cx = i => g.x0 + i * (g.bw + g.gap) + g.bw / 2; g.fs = Math.min(66, g.bw * (nb.kind === 'char' ? .6 : .44)); g.ptrY = g.y + g.bh + 52; g.below = g.y + g.bh + 150; return g;
}
// ---- state carried across scenes ----
function APPLY(st, e) { const s = JSON.parse(JSON.stringify(st));
  if (e.ptr) for (const k in e.ptr) { if (e.ptr[k] === null) delete s.ptr[k]; else s.ptr[k] = e.ptr[k]; }
  if (e.mark) for (const k in e.mark) { if (e.mark[k] === null) delete s.mark[k]; else s.mark[k] = e.mark[k]; }
  if (e.win !== undefined) s.win = e.win; if (e.fill) e.fill.forEach(i => { if (!s.fill.includes(i)) s.fill.push(i); });
  if (e.set) for (const k in e.set) s.vals[k] = e.set[k];
  if (e.push !== undefined) s.stack.push(e.push); if (e.pop) for (let k = 0; k < e.pop; k++) s.stack.pop(); if (e.st !== undefined) s.st = e.st; return s; }
const EMPTY = () => ({ ptr: {}, mark: {}, win: null, fill: [], stack: [], st: '', vals: {} });
function NB_SCENES(nb) {
  const g = GEO(nb), starts = []; let st = EMPTY();
  nb.scenes.forEach(sc => { if (sc.reset) st = EMPTY(); starts.push(st); (sc.ev || []).forEach(([c, e]) => st = APPLY(st, e)); });
  return nb.scenes.map((sc, si) => SCENE(nb, g, sc, si, starts[si]));
}
function SCENE(nb, g, sc, si, st0) {
  const vis = sc.vis !== undefined ? sc.vis : !['hook', 'cta', 'cx'].includes(sc.type); let svg = '', html = '', y = vis ? g.below : 330;
  if (sc.type === 'hook') return HOOK(sc.hook);
  if (sc.type === 'cta') return CTA(sc.cta || {});
  if (sc.type === 'cx') return CX(sc.cx);
  if (sc.h) html += H('hd', 120, vis ? (nb.kind === 'bars' ? 250 : 300) : 330, sc.h.s || 56, sc.h.t, (sc.h.c || 'blk') + ' b');
  if (vis) { if (nb.kind === 'bars') nb.arr.forEach((h, i) => { const x = g.cx(i) - g.bw / 2, top = g.base - h * g.U;
        if (h) svg += P('bx' + i, rr(x, top, g.bw, h * g.U, 70 + i), INK, 5); html += `<div class="bfill" id="bf${i}" style="left:${x}px;top:${top}px;width:${g.bw}px;height:${h * g.U}px"></div>`;
        const w = (nb.water || [])[i] || 0; html += `<div class="wat" id="w${i}" style="left:${x + 4}px;top:${top - w * g.U}px;width:${g.bw - 8}px;height:${w * g.U}px"></div>`;
        html += `<div class="box" id="n${i}" style="left:${x}px;top:${g.base + 8}px;width:${g.bw}px;font-size:46px">${h}</div>`; });
      else nb.arr.forEach((v, i) => { const x = g.cx(i) - g.bw / 2; svg += P('bx' + i, rr(x, g.y, g.bw, g.bh, i + 1 + si * 3), INK, 4) + P('ok' + i, ell(g.cx(i), g.y + g.bh / 2, g.bw * .68, g.bh * .62, 11 + i), GRN, 6);
        html += `<div class="bg" id="bg${i}" style="left:${x + 4}px;top:${g.y + 4}px;width:${g.bw - 8}px;height:${g.bh - 8}px"></div><div class="box" id="n${i}" style="left:${x}px;top:${g.y + (g.bh - g.fs * 1.3) / 2}px;width:${g.bw}px;font-size:${g.fs}px">${v}</div>`
          + `<div class="idx" id="x${i}" style="left:${x}px;top:${g.y + g.bh + 2}px;width:${g.bw}px">${i}</div>`; });
    if (nb.kind === 'bars') svg += P('bs', ln(100, g.base, 990, g.base + 2, 79), INK, 6);
    else html += `<div class="frm" id="win"></div>`;
    Object.keys(PCOL).forEach(k => html += `<div class="ptr" id="p_${k}" style="color:${PCOL[k]};opacity:0">↑${k}</div>`);
    (sc.ev || []).forEach(([c, e], k) => { if (e.arc) { const [a, b, col] = e.arc, yy = nb.kind === 'bars' ? g.base - Math.max(nb.arr[a], nb.arr[b]) * g.U - 20 : g.y - 10;
      svg += P('arc' + k, arw(g.cx(a), yy, g.cx(b), yy, 50 + Math.abs(b - a) * 22), COL[col] || GRN, 5); } }); }
  if (sc.big) { html += HC('big', y, sc.big.s || 84, sc.big.t, (sc.big.c || 'grn') + ' b'); y += (sc.big.s || 84) * 1.5; }
  (sc.lines || []).forEach((L, k) => { const s = L.s || 56, w = Math.min(880, MU(L.t).replace(/<[^>]+>/g, '').length * s * .5 + 40);
    html += H('l' + k, 130, y, s, L.t, (L.c || 'blue') + (L.b ? ' b' : '')); if (L.box) svg += P('lb' + k, rr(115, y - 8, w, s * 1.5, 30 + k), COL[L.box] || BLUE, 5);
    if (L.strike) svg += P('ls' + k, ln(115, y + s * .62, 125 + w, y + s * .5, 40 + k), RED, 6); if (L.circ) svg += P('lc' + k, ell(120 + w / 2, y + s * .7, w / 2 + 30, s * .85, 50 + k), COL[L.circ] || GRN, 5); y += s * 1.45; });
  if (sc.table) { const T = sc.table, nc = T.cols.length, W = T.w || T.cols.map(() => 900 / nc), rh = T.rh || 66, ty = y + 10; let x = 120; const xs = W.map(w => { const a = x; x += w; return a; });
    svg += P('tb', rr(120, ty, 900, rh * (T.rows.length + 1), 91), INK, 4) + P('th', ln(120, ty + rh, 1020, ty + rh, 92), INK, 4) + xs.slice(1).map((xx, k) => P('tc' + k, ln(xx, ty, xx, ty + rh * (T.rows.length + 1), 93 + k), INK, 3)).join('');
    html += T.cols.map((c, k) => `<div class="cell blk" id="hd${k}" style="left:${xs[k]}px;top:${ty + 8}px;width:${W[k]}px;font-size:40px;font-weight:700">${c}</div>`).join('');
    T.rows.forEach((r, ri) => r.forEach((v, ci) => { const s = String(v), cls = /^(no|✗|false)$/i.test(s) ? 'red' : /^(yes|✓|true)|^\+[1-9]|^return/i.test(s) ? 'grn' : 'blu';
      html += `<div class="cell ${cls}" id="c${ri}_${ci}" style="left:${xs[ci]}px;top:${ty + rh * (ri + 1) + 6}px;width:${W[ci]}px;font-size:${Math.min(46, W[ci] / Math.max(2, s.length) * 1.7)}px">${s}</div>`; }));
    y = ty + rh * (T.rows.length + 1) + 30; }
  html += `<div class="st" id="st" style="top:${y}px"></div>`;
  if (sc.stack) html += `<div class="stk" id="stk" style="left:840px;top:${g.below + 10}px;height:${sc.stack * 70 + 20}px"></div>`;
  return { html: `<svg class="ink" viewBox="0 0 1080 1920">${svg}</svg>${html}`, draw(S) { DRAWSC(S, nb, g, sc, st0, vis); } };
}
function DRAWSC(S, nb, g, sc, st0, vis) {
  if (sc.h) WRITE(S, 'hd', CUE(S, sc.h.at, .02) - .1, .5);
  const evs = (sc.ev || []).map(([c, e]) => [CUE(S, c, .5) - .08, e]);
  let st = st0, prev = st0; const tEv = []; evs.forEach(([t, e], k) => { if (S.on(t)) { prev = st; st = APPLY(st, e); tEv.push([t, e, k]); } });
  if (vis) {
    nb.arr.forEach((v, i) => { const t = sc.draw ? CUE(S, sc.draw[i], .1 + i * .08) - .15 : -1; DRAW(S, 'bx' + i, t, .3); const on = t < 0 || S.on(t + .1); S.$('#n' + i).style.opacity = on ? 1 : 0;
      if (nb.kind === 'bars') S.$('#bf' + i).style.opacity = on ? 1 : 0; else S.$('#x' + i).style.opacity = on ? 1 : 0; });
    if (nb.kind === 'bars') { DRAW(S, 'bs', sc.draw ? .02 : -1, .3); nb.arr.forEach((h, i) => { const e = S.$('#w' + i); const k = tEv.find(([t, ev]) => ev.fill && ev.fill.includes(i)); const p = st0.fill.includes(i) ? 1 : k ? S.P(k[0], .45, eo) : 0;
        e.style.transform = `scaleY(${p})`; e.style.opacity = p > 0 ? 1 : 0; if (k && S.on(k[0])) S.sfx(k[0], 'swish'); }); }
    else nb.arr.forEach((v, i) => { const m = st.mark[i], bg = S.$('#bg' + i); const nv = st.vals[i] !== undefined ? st.vals[i] : v; if (S.$('#n' + i).textContent != String(nv)) S.$('#n' + i).textContent = nv; bg.style.opacity = m === 'bad' || m === 'hl' || m === 'on' ? 1 : 0;
        bg.style.background = m === 'bad' ? 'rgba(208,49,45,.22)' : m === 'on' ? 'rgba(30,138,76,.18)' : 'rgba(255,214,0,.55)'; S.$('#n' + i).style.opacity = m === 'dim' ? .3 : S.$('#n' + i).style.opacity;
        const k = tEv.find(([t, ev]) => ev.mark && ev.mark[i] === 'ok'); DRAW(S, 'ok' + i, m === 'ok' ? (st0.mark[i] === 'ok' ? -1 : k ? k[0] : -1) : 9e9, .35); if (m !== 'ok') S.$('#ok' + i).style.strokeDashoffset = 1; });
    // pointers: glide from previous index over .3 s
    const prevPos = k => { let p = st0.ptr[k]; for (const [t, e] of evs) { if (!S.on(t)) break; if (e.ptr && k in e.ptr) { if (S.t - t < .3 && p !== undefined && e.ptr[k] !== null) return p + (e.ptr[k] - p) * eio(clamp((S.t - t) / .3)); p = e.ptr[k]; } } return p; };
    const used = {}; Object.keys(PCOL).forEach(k => { const e = S.$('#p_' + k); const v = st.ptr[k]; if (v === undefined || v === null) { e.style.opacity = 0; return; } const pos = prevPos(k), slot = used[v] = (used[v] || 0) + 1;
      e.style.opacity = 1; e.style.left = g.cx(pos) + 'px'; e.style.top = (g.ptrY + (slot - 1) * 50) + 'px'; });
    const w = S.$('#win'); if (w) { if (st.win) { const [l, r, c] = st.win; w.style.opacity = 1; w.style.left = (g.cx(l) - g.bw / 2 - 12) + 'px'; w.style.width = ((r - l) * (g.bw + g.gap) + g.bw + 24) + 'px';
        w.style.top = (g.y - 14) + 'px'; w.style.height = (g.bh + 28) + 'px'; w.style.borderColor = c === 'r' ? RED : GRN; } else w.style.opacity = 0; }
    evs.forEach(([t, e], k) => { if (e.arc) DRAW(S, 'arc' + k, t, .45); });
  }
  if (sc.big) WRITE(S, 'big', CUE(S, sc.big.at, .5) - .1, .4);
  (sc.lines || []).forEach((L, k) => { const t = CUE(S, L.at, .05 + k * .2) - .12; WRITE(S, 'l' + k, t, L.d || Math.min(1.2, L.t.length * .03)); if (L.box) DRAW(S, 'lb' + k, CUE(S, L.box_at || L.at, .3) + .1, .35);
    if (L.strike) DRAW(S, 'ls' + k, CUE(S, L.strike, .8) - .1, .25); if (L.circ) DRAW(S, 'lc' + k, CUE(S, L.circ_at || L.at, .5) + .1, .35); });
  if (sc.table) { const T = sc.table, t0 = CUE(S, T.at, 0); DRAW(S, 'tb', T.at === -1 ? -1 : t0, .45); DRAW(S, 'th', T.at === -1 ? -1 : t0 + .25, .25); T.cols.slice(1).forEach((c, k) => DRAW(S, 'tc' + k, T.at === -1 ? -1 : t0 + .3 + k * .04, .25));
    T.cols.forEach((c, k) => S.$('#hd' + k).style.opacity = T.at === -1 || S.on(t0 + .35) ? 1 : 0);
    T.rows.forEach((r, ri) => { const pre = ri < (T.show || 0); const k = evs.find(([t, e]) => e.row === ri); r.forEach((v, ci) => { const e = S.$(`#c${ri}_${ci}`); if (pre) { e.style.opacity = 1; return; }
      if (!k) { e.style.opacity = 0; return; } const tt = k[0] + ci * .07, p = S.P(tt, .18, x => x); e.style.opacity = p > 0 ? 1 : 0; e.style.clipPath = `inset(-20px ${100 - 100 * p}% -20px -20px)`; if (S.on(tt) && ci === 0) S.sfx(tt, 'click'); }); }); }
  const se = S.$('#st'); if (se) { se.innerHTML = MU(st.st || ''); const k = [...tEv].reverse().find(([t, e]) => e.st !== undefined); if (k) { const p = S.P(k[0], .3, x => x); se.style.clipPath = `inset(-20px ${100 - 100 * p}% -20px -20px)`; } else se.style.clipPath = 'none'; }
  if (sc.stack) { const sk = S.$('#stk'); sk.innerHTML = st.stack.map((v, k) => `<div class="hw blu b" style="position:absolute;opacity:1;left:0;width:170px;text-align:center;bottom:${10 + k * 70}px;font-size:50px">${v}</div>`).join(''); }
}
function HOOK(h) {
  const cls = !h.co, lpa = h.lpa ? `₹${h.lpa} LPA` : '';
  const claim = cls ? 'A classic at product-company interviews' : h.claim === 'asked' ? `Asked in ${h.co} interviews · ${h.year}` : `Reported in ${/^[AEIOU]/.test(h.co) ? 'an' : 'a'} ${h.co} interview · ${h.year}`;
  return { html: `<div class="sticky" id="stc">${H('o1', 60, 50, 38, cls ? 'INTERVIEW CLASSIC' : 'OFFER LETTER', 'gry b')}${H('o2', 60, 110, h.role && (h.role + h.co).length > 22 ? 48 : 58, cls ? (h.sub || 'every product company') : `${h.role} · ${h.co} · India`, 'blk')}${H('o3', 60, 200, cls ? 130 : 190, cls ? (h.big || 'Top 50') : lpa, 'red mk')}</div>
    <svg class="ink" viewBox="0 0 1080 1920">${P('c0', ell(470, 640, 300, 125, 3), RED, 6) + P('u0', ln(150, 990, 1000, 984, 5), BLUE, 5)}</svg>
    ${H('a1', 150, 900, claim.length > 34 ? 46 : 56, claim, 'b')}${H('a2', 150, 1030, 62, '→ this exact question', 'red b')}${h.src ? H('a3', 150, 1140, 34, h.src, 'gry') : ''}`,
    draw(S) { const p = S.P(0, .35, back); S.$('#stc').style.opacity = clamp(p); S.$('#stc').style.translate = `0 ${60 * (1 - clamp(p))}px`; WRITE(S, 'o1', .05, .15); WRITE(S, 'o2', .1, .3);
      WRITE(S, 'o3', CUE(S, h.at_lpa || 'lakh', .15) - .25, .4); DRAW(S, 'c0', CUE(S, h.at_co || (h.co ? h.co.split(' ')[0] : 'classic'), .3), .4);
      WRITE(S, 'a1', CUE(S, 'question', .5) - .3, .6); DRAW(S, 'u0', CUE(S, 'question', .55) + .3, .3); WRITE(S, 'a2', S.dur * .82, .3); WRITE(S, 'a3', S.dur * .85, .25); } };
}
function CTA(c) {
  return { html: `<svg class="ink" viewBox="0 0 1080 1920">${P('nb', rr(250, 520, 580, 250, 61), RED, 7) + P('da', arw(540, 800, 545, 900, 0), BLUE, 5) + P('fu', ln(300, 1150, 780, 1146, 62), BLUE, 4)}</svg>
    ${HC('c1', 400, 80, 'Comment', 'blk b')}${HC('c2', 520, 230, 'NOTES', 'red mk')}${HC('c3', 930, 54, c.t || '5 more questions, same pattern', 'blu')}${HC('c4', 1010, 46, 'straight to your DMs', 'gry')}${HC('c5', 1080, 56, '', 'blu b')}`,
    draw(S) { S.$('#c5').textContent = 'follow ' + HANDLE; WRITE(S, 'c1', .02, .2); const tn = CUE(S, 'notes', .15) - .15; WRITE(S, 'c2', tn, .3); DRAW(S, 'nb', tn + .2, .35);
      DRAW(S, 'da', S.dur * .45, .25); WRITE(S, 'c3', S.dur * .45 + .1, .5); WRITE(S, 'c4', S.dur * .7, .25); WRITE(S, 'c5', S.dur - 1.2, .3); DRAW(S, 'fu', S.dur - .8, .25); } };
}
function CX(c) {
  return { html: `<svg class="ink" viewBox="0 0 1080 1920">${P('tbx', rr(115, 420, 860, 120, 52), GRN, 5) + P('st3', ln(120, 700, 700, 692, 53), RED, 6) + P('stp', rr(130, 840, 860, 160, 54), RED, 6)}</svg>
    ${H('t1', 145, 432, 70, c.time, 'grn b')}${H('t1b', 145, 560, 46, c.note || '', 'gry')}${H('t3', 130, 650, 58, c.brute ? 'Brute force: ' + c.brute : '', 'red')}
    <div style="position:absolute;left:130px;top:840px;width:860px;height:160px;transform:rotate(-4deg)">${H('pn', 26, 28, c.pattern.length > 14 ? 70 : 84, 'PATTERN: ' + c.pattern.toUpperCase(), 'red mk')}</div>`,
    draw(S) { WRITE(S, 't3', .05, .3); DRAW(S, 'st3', .35, .2); WRITE(S, 't1', CUE(S, 'o', .3) - .1, .5); DRAW(S, 'tbx', CUE(S, 'o', .3) + .4, .3); WRITE(S, 't1b', S.dur * .4, .35);
      const tz = Math.max(.6, S.dur - .9); DRAW(S, 'stp', tz, .25); WRITE(S, 'pn', tz + .05, .25); } };
}
// ---- end nb ----
const NB = {"kind": "num", "arr": [3, 1, 4, 1, 5, 9], "water": null, "scenes": [{"type": "hook", "hook": {"co": null, "lpa": null, "role": "SDE-1", "claim": "asked", "year": 2025, "src": null, "big": "Prefix sum", "sub": "one idea, many questions", "at_co": "prefix", "at_lpa": "family"}}, {"vis": false, "lines": [{"t": "Q. many queries:", "at": 0.05, "c": "red", "s": 66, "b": true}, {"t": "sum from index i to j?", "at": null, "c": "blue", "s": 62}]}, {"draw": ["3#1", "1#1", "4#1", "1#2", "5#1", "9#1"], "ev": [["index", {"win": [1, 4, "g"]}]], "big": {"t": "sum(1..4) = 11", "at": "11"}}, {"h": {"t": "Brute force: add each range again", "at": 0.05}, "lines": [{"t": "10,000 × 5,000 = [50,000,000]", "at": "10000", "c": "blk", "s": 54}, {"t": "✗ TOO SLOW · O(n) per query", "at": "rejected", "c": "red", "s": 66}]}, {"lines": [{"t": "P[i] = sum before index i", "at": "running", "c": "blk", "s": 58, "b": true}, {"t": "P = [0, 3, 4, 8, 9, 14, 23]", "at": "once", "c": "grn", "s": 56}]}, {"lines": [{"t": "sum(i..j) = P[j+1] − P[i]", "at": "subtraction", "c": "blk", "s": 58, "box": "blue"}, {"t": "= P[5] − P[1] = 14 − 3 = [11]", "at": "14", "c": "red", "s": 60, "b": true}], "ev": [["range", {"win": [1, 4, "g"]}], ["11", {"st": "O(1) per query ✓"}]]}, {"type": "cx", "cx": {"time": "O(n) build · O(1) per query", "brute": "O(n) per query", "pattern": "Prefix sum", "note": "running totals, then subtract"}}, {"type": "cta", "cta": {"t": "5 more prefix-sum questions"}}]};
const SCENES = NB_SCENES(NB);
