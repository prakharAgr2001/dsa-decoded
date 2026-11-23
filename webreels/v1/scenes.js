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
// uses:dsa  V1 interview roleplay: live chat bubbles (karaoke) + whiteboard. No captions (bubbles are the captions).
const WHO = ['I', 'C', 'I', 'C', 'I', 'C', 'I', 'C', 'C'];
const TX = ['Amazon interview, round one. Find two numbers in this list that add up to 500.', "Easy. I'll check every pair.", "With five thousand numbers? That's twelve million pairs. Faster, please.",
  "Okay. I'll walk the list once, and remember every number I've seen.", 'And how does that help?', "Each number's partner is 500 minus it. If the partner is already saved, I'm done. One lookup.",
  'Complexity?', 'O of n. One pass.', "Comment NOTES, and I'll send you five more questions like this."];
const TILES = `<div class="tiles"><div class="tile2" id="tI"><div class="av">I</div><div><b>Interviewer</b><small>SDE-1 · Round 1</small></div></div><div class="tile2" id="tC"><div class="av you">Y</div><div><b>You</b><small>candidate</small></div></div></div>`;
const BUB = (k, live) => `<div class="bub ${WHO[k] === 'C' ? 'me' : ''}" ${live ? 'id="live"' : ''}>${live ? WRAPW(TX[k]) : TX[k]}</div>`;
const BOARD = si => {
  if (si === 0 || si === 1) return `<div class="board">${ROW('rw', 150)}<div class="abs center" id="tg" style="top:360px"><span class="tgt">TARGET 500</span></div></div>`;
  if (si === 2) return `<div class="board"><div class="abs center big" id="ck" style="top:120px;font-size:120px;color:var(--red)">0</div><div class="abs center lab" style="top:270px;font-size:36px">pairs for 5,000 numbers</div><div class="stamp" id="rj" style="left:300px;top:340px;font-size:70px">TOO SLOW</div></div>`;
  if (si <= 4) return `<div class="board">${ROW('rw', 150)}${PTR('pi', 'i', '#4c9dff')}</div>`;
  if (si <= 6) return `<div class="board">${ROW('rw', 60)}<div class="mini">${[0, 1, 2].map(k => `<span class="mk" id="m${k}">${A[k]}</span>`).join('')}</div><div class="abs center" id="fd" style="top:420px;opacity:0"><span class="tgt">150 + 350 = 500 ✓</span></div></div>`;
  if (si === 7) return `<div class="board"><div class="abs center" id="on" style="top:120px;opacity:0"><span class="badge">O(n)</span></div></div>`;
  return `<div class="board"><div class="abs center" style="top:110px"><span class="notes">NOTES</span></div><div class="abs center" style="top:380px"><span class="pill" id="fl"></span></div></div>`;
};
const SCENES = TX.map((_, si) => ({ noCap: true,
  html: `${TILES}${BOARD(si)}<div class="chat">${[si - 2, si - 1].filter(k => k >= 0).map(k => BUB(k, false)).join('')}${BUB(si, true)}</div>`,
  draw(S) {
    const sp = WHO[si]; const talk = .5 + .5 * Math.abs(Math.sin(S.t * 9));
    S.$('#tI').style.boxShadow = sp === 'I' ? `0 0 0 ${4 + 4 * talk}px var(--blue)` : ''; S.$('#tC').style.boxShadow = sp === 'C' ? `0 0 0 ${4 + 4 * talk}px var(--yel)` : '';
    const lv = S.$('#live'), p = S.P(0, .3, back); lv.style.opacity = clamp(p); lv.style.transform = `translateY(${30 * (1 - clamp(p))}px)`; KARAOKE(S, '#live', si, 0, .15);
    if (si === 0) { S.$$('#rw .b').forEach((b, i) => { const q = S.P(TT(S, 'list', .5) + i * .06 - .2, .3, back); b.style.opacity = clamp(q); }); POP(S, '#tg', TT(S, '500', .8) - .1); }
    if (si === 1) { const k = Math.floor(S.t * 7), pr = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3]][k % 8]; LITSET(S, 'rw', pr, 'bad'); }
    if (si === 2) { const tm = TT(S, 'million', .6); COUNT(S, '#ck', 0, 12497500, .1, tm, v => fmt(v), x => x * x); STAMP(S, '#rj', TT(S, 'faster', .8)); }
    if (si === 3) { const t0 = TT(S, 'walk', .3), t1 = TT(S, 'seen', .9); const f = clamp((S.t - t0) / (t1 - t0)) * 4; PT(S, 'pi', f, 330); LITSET(S, 'rw', [Math.round(f)]); }
    if (si === 4) { PT(S, 'pi', 0, 330); FLOAT(S, '#rw', 6); }
    if (si === 5 || si === 6) { const done = si === 6; [0, 1, 2].forEach(k => { const t = done ? -1 : TT(S, 'saved', .5) - .6 + k * .2; POP(S, '#m' + k, t, done ? null : 'pop'); });
      const tf = done ? -1 : TT(S, 'lookup', .9) - .2; S.$('#m1').classList.toggle('hl', S.on(tf)); LITSET(S, 'rw', S.on(tf) ? [1, 3] : [3]); POP(S, '#fd', tf, done ? null : 'ding'); }
    if (si === 7) { POP(S, '#on', .1, 'ding'); S.$('#on .badge').style.transform = `scale(${1 + .035 * Math.sin(S.t * 5)})`; }
    if (si === 8) { S.$('#fl').textContent = 'Follow ' + HANDLE; S.$('.notes').style.transform = `scale(${1 + .03 * Math.sin(S.t * 6)})`; }
  }}));
