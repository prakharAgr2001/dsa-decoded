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
// uses:dsa  V5 kinetic type: each spoken word slams in; key words yellow; alternating colour fields; beat flashes.
const LN = ['Two Sum. In twenty seconds. Go.', 'Every number has a partner: target minus number.', 'Walk the list once.', 'Partner already seen? Done.', 'Not seen? Save the number. Move on.', 'One pass. O of n.', 'Comment NOTES for five more.'];
const KEY = /^(sum|twenty|go|partner|target|minus|once|seen|done|save|move|pass|o|n|notes)$/i;
const BG = ['#0c0c0e', '#ffd23f', '#0c0c0e', '#3ddc84', '#0c0c0e', '#ffd23f', '#0c0c0e'], FG = ['#f4f1ea', '#0c0c0e', '#f4f1ea', '#0c0c0e', '#f4f1ea', '#0c0c0e', '#f4f1ea'];
const SCENES = LN.map((ln, si) => ({ noCap: true,
  html: `<div class="field" style="background:${BG[si]}"></div><div class="kt" style="color:${FG[si]};--kc:${BG[si] === "#0c0c0e" ? "#ffd23f" : "#b00b1e"}">${ln.split(' ').map(w => `<span class="kw ${KEY.test(w.replace(/[^a-z]/gi, '')) ? 'k' : ''}">${w}</span>`).join(' ')}</div>
    ${si === 2 ? ROW('rw', 1200) : ''}${si === 3 ? `<div class="abs center" id="ck" style="top:1250px">${EMO('check-mark-button').replace('1em', '240px').replace('1em', '240px')}</div>` : ''}
    ${si === 6 ? '<div class="abs center" style="top:1250px"><span class="pill" id="fl" style="font-size:40px"></span></div>' : ''}`,
  draw(S) { const ws = WT(si); S.$$('.kw').forEach((e, k) => { const t = ws[k] ?? 0; const q = S.P(t - .06, .18, back); e.style.opacity = clamp(q * 1.5); e.style.transform = `scale(${1.8 - .8 * clamp(q)}) rotate(${(k % 2 ? 1 : -1) * 3 * (1 - clamp(q))}deg)`; if (S.on(t - .06) && e.classList.contains('k')) S.sfx(t - .06, 'thud'); });
    S.el.querySelector('.field').style.transform = `scale(${1 + .02 * Math.sin(S.abs * 128 / 60 * Math.PI)})`;
    if (si === 2) { const t0 = ws[0], f = clamp((S.t - t0) / (S.dur - t0 - .2)); LITSET(S, 'rw', [0, 1, 2, 3, 4].filter(i => i <= f * 4.99)); }
    if (si === 3) POP(S, '#ck', ws[3] - .05, 'ding');
    if (si === 6) S.$('#fl').textContent = 'Follow ' + HANDLE; }}));
