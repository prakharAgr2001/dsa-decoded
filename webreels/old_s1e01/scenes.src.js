// S1E01 Two Sum (hashing). Company/salary sources are in spec.py. No logos. Numbers: only pair (1,3) sums to 500; 5000*4999/2 = 12,497,500.
const A = [120, 350, 280, 150, 400], TG = 500, BW = 160, GAP = 14, X0 = 112;
const bx = i => X0 + i * (BW + GAP);
const ROW = (id, top) => `<div class="row" id="${id}" style="top:${top}px">${A.map((v, i) => `<div class="b" style="left:${bx(i) - X0}px"><b>${v}</b><span>${i}</span></div>`).join('')}<div class="frame"></div></div>`;
function FRAME(S, id, l, r, col = 'var(--grn)', show = 1) { const f = S.$(`#${id} .frame`); f.style.left = (bx(l) - X0 - 10) + 'px'; f.style.width = ((r - l + 1) * (BW + GAP) - GAP + 20) + 'px'; f.style.borderColor = col; f.style.boxShadow = `0 0 40px ${col}`; f.style.opacity = show; }
function LITSET(S, id, set, cls = 'on') { S.$$(`#${id} .b`).forEach((b, i) => b.classList.toggle(cls, set.includes(i))); }
const PTR = (id, txt, col) => `<div class="pt" id="${id}" style="--c:${col}"><i></i>${txt}</div>`;
function PT(S, id, i, top) { const p = S.$('#' + id); p.style.left = (bx(i) + BW / 2 - 70) + 'px'; p.style.top = top + 'px'; }
function FLOAT(S, sel, amp = 6, sp = 2.2) { const e = S.$(sel); if (e) e.style.translate = `0 ${amp * Math.sin(S.abs * sp)}px`; }
const GL = (id, col) => `<div class="sglow" id="${id}" style="background:radial-gradient(60% 45% at 50% 45%,${col},transparent 70%)"></div>`;
function GLOW(S, id, at, len = 1.2) { const k = S.on(at) ? Math.max(0, 1 - (S.t - at) / len) : 0; S.$('#' + id).style.opacity = .55 * k; }
function KARAOKE(S, sel, si, off) { const ws = DATA.words.filter(w => w[3] === si), t0 = DATA.spans[si][0];
  S.$$(sel + ' w').forEach((e, k) => { const w = ws[k + off]; const on = w && S.t >= w[1] - t0 - .05; e.style.opacity = on ? 1 : .22; }); }
const SEEN = (n) => `<div class="seen"><h3>SEEN (value → index)</h3>${[0, 1, 2].map(k => `<div class="kv" id="kv${k}"><b>${A[k]}</b><span>at</span><i>${k}</i></div>`).slice(0, n).join('')}</div>`;
const SCENES = [
 { // 0 hook
  html: `<div class="offer" id="of"><div class="ok">OFFER</div><div class="role">Software Development Engineer I</div><div class="co">Amazon · India</div><div class="ctc"><span id="ct">₹0</span><small> LPA total comp</small></div></div>
   <div class="abs center" id="ch" style="top:1020px;opacity:0"><span class="tag">ASKED IN AMAZON INTERVIEWS · 2025</span></div>
   <div class="abs center h2" id="q" style="top:1130px;opacity:0">this <span class="mark" id="mk">exact question</span></div>
   <div class="abs center lab" style="top:1330px;font-size:22px">salary: AmbitionBox range for SDE-1 · illustration</div>`,
  draw(S) { const p = S.P(0, .5, back); S.$('#of').style.transform = `translateY(${120 * (1 - clamp(p))}px) rotate(${-3 + 3 * clamp(p)}deg)`; S.$('#of').style.opacity = clamp(p);
    COUNT(S, '#ct', 0, 28, .2, .9, v => '₹' + Math.round(v)); if (S.on(1.1)) S.sfx(1.1, 'ding'); POP(S, '#ch', TT(S, 'Amazon', .25) + .3, 'pop'); IN(S, '#q', TT(S, 'exact', .5) - .2); MK(S, '#mk', TT(S, 'question', .6)); }},
 { // 1 question
  html: `<div class="abs center kick" style="top:420px">the question</div><div class="qcard" id="qc"><w>Find</w> <b><w>two</w> <w>numbers</w></b> <w>in</w> <w>a</w> <w>list</w><br><w>that</w> <b><w>add</w> <w>up</w> <w>to</w> <w>a</w> <w>target</w></b>.</div>`,
  draw(S) { IN(S, '#qc', .05, 60); KARAOKE(S, '#qc', 1, 3); }},
 { // 2 example
  html: `<div class="abs center kick" style="top:440px">prices</div>${ROW('r2', 560)}<div class="abs center" id="tg" style="top:800px;opacity:0"><span class="tgt">TARGET ₹500</span></div>
   <div class="abs center big" id="an" style="top:950px;font-size:120px;color:var(--grn);opacity:0">350 + 150 = 500</div>`,
  draw(S) { S.$$('#r2 .b').forEach((b, i) => { const p = S.P(TT(S, String(A[i]), .1 + i * .05) - .1, .3, back); b.style.opacity = clamp(p); b.style.transform = `translateY(${40 * (1 - clamp(p))}px)`; });
    POP(S, '#tg', TT(S, '500', .45) - .1, 'pop'); const a1 = TT(S, '350', .7, 2), a2 = TT(S, '150', .85, 2); const set = [];
    if (S.on(a1 - .1)) set.push(1); if (S.on(a2 - .1)) set.push(3); LITSET(S, 'r2', set); POP(S, '#an', a2, 'ding'); FLOAT(S, '#r2', 5); }},
 { // 3 trap
  html: `${ROW('r3', 520)}<div class="abs center big" id="ck" style="top:820px;font-size:130px;color:var(--red)">0</div><div class="abs center lab" style="top:990px;font-size:40px">pairs to check for 5,000 numbers</div>
   <div class="stamp" id="rj" style="left:250px;top:1110px;font-size:110px">REJECTED</div>${GL('g3', 'rgba(255,59,59,.55)')}`,
  draw(S) { const k = Math.floor(S.t * 8), pairs = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], pr = pairs[k % 10]; LITSET(S, 'r3', pr, 'bad'); if (k !== this.k) { S.sfx(S.t, 'tick'); this.k = k; }
    const tr = TT(S, 'Rejected', .9); COUNT(S, '#ck', 0, 12497500, .3, TT(S, 'million', .6) - .1, v => fmt(v), x => x * x * x); STAMP(S, '#rj', tr); GLOW(S, 'g3', tr); SHAKE(S, '#r3', tr, 16); SHAKE(S, '#ck', tr, 10); if (S.t > tr) LITSET(S, 'r3', []); }},
 { // 4 insight intro
  html: `<div class="abs center h" style="top:360px;font-size:110px"><span class="mark" id="mk">Hash map</span></div>${ROW('r4', 600)}
   <div class="abs center h2" id="qq" style="top:880px;opacity:0">"have I already seen<br>my <span style="color:var(--yel)">partner</span>?"</div>
   <div class="abs center need" id="pf" style="top:1120px;opacity:0">partner = <b>500 − number</b></div>`,
  draw(S) { MK(S, '#mk', TT(S, 'hash', .3)); IN(S, '#qq', TT(S, 'question', .6) - .1); IN(S, '#pf', TT(S, 'partner', .85) - .1); S.$$('#r4 .b').forEach((b, i) => b.style.translate = `0 ${8 * Math.sin(S.t * 3 - i * .7)}px`); }},
 { // 5 walk: 120, 350, 280 -> save
  html: `${ROW('r5', 420)}${PTR('pi', 'i', '#4c9dff')}${[0, 1, 2].map(k => `<div class="fly" id="fy${k}">${A[k]}</div>`).join('')}<div class="abs center need" id="nd" style="top:720px"></div><div class="abs center x" id="ns" style="top:830px;opacity:0">✗ not seen</div>${SEEN(3)}`,
  draw(S) { const ts = [TT(S, '120', .05), TT(S, '350', .35), TT(S, '280', .68)], sv = [1, 2, 3].map(n => TT(S, 'save', .25 + n * .25, n));
    let i = 0; ts.forEach((t, j) => { if (S.on(t - .1)) i = j; }); let pf = i; if (i < 2) pf = i + S.P(ts[i + 1] - .45, .35, eio); PT(S, 'pi', pf, 590); LITSET(S, 'r5', [i]);
    [0, 1, 2].forEach(k => { const f = S.$('#fy' + k), q = S.P(sv[k] - .4, .38, eio), x0 = bx(k) + BW / 2, y0 = 495, x1 = 540, y1 = 1111 + 94 * k;
      f.style.opacity = q > 0 && q < 1 ? 1 : 0; f.style.left = (x0 + (x1 - x0) * q - 70) + 'px'; f.style.top = (y0 + (y1 - y0) * q - 90 * Math.sin(q * Math.PI) - 40) + 'px'; if (S.on(sv[k] - .4)) S.sfx(sv[k] - .4, 'swish'); });
    S.$('#nd').innerHTML = `${A[i]} needs <b>${TG - A[i]}</b>`; if (i !== this.i) { S.sfx(S.t, 'click'); this.i = i; }
    const saved = sv.filter(t => S.on(t - .05)).length; S.$('#ns').style.opacity = saved <= i ? 1 : 0;
    [0, 1, 2].forEach(k => { const p = S.P(sv[k] - .05, .3, back); S.$('#kv' + k).style.opacity = clamp(p); S.$('#kv' + k).style.transform = `translateX(${60 * (1 - clamp(p))}px)`; if (S.on(sv[k] - .05)) S.sfx(sv[k] - .05, 'pop'); }); }},
 { // 6 hit
  html: `${ROW('r6', 420)}${PTR('pi6', 'i', '#4c9dff')}<svg class="abs" width="1080" height="700" style="left:0;top:0"><path id="arc" d="" stroke="#ffd23f" stroke-width="7" fill="none" stroke-dasharray="16 10"/></svg>
   <div class="abs center need" id="nd6" style="top:720px">150 needs <b>350</b></div><div class="abs center" id="fd" style="top:830px;opacity:0"><span class="tgt" style="font-size:52px">FOUND · [1, 3]</span></div>${SEEN(3)}${GL('g6', 'rgba(61,220,132,.5)')}`,
  draw(S) { PT(S, 'pi6', 3, 590); GLOW(S, 'g6', TT(S, 'done', .85) - .1, 1.5); SHAKE(S, '#fd', TT(S, 'done', .85) - .1, 10); const ta = TT(S, 'already', .3), td = TT(S, 'done', .85);
    const hit = S.on(ta - .1); S.$('#kv1').classList.toggle('hl', hit); [0, 1, 2].forEach(k => S.$('#kv' + k).style.opacity = 1); if (S.on(ta - .1)) S.sfx(ta - .1, 'ding');
    LITSET(S, 'r6', hit ? [1, 3] : [3]); const p = S.P(TT(S, 'index', .6) - .2, .5, eio);
    S.$('#arc').setAttribute('d', p > 0 ? `M${bx(3) + 80} 410 Q${(bx(1) + bx(3)) / 2 + 80} ${410 - 200 * p} ${bx(3) + 80 - (bx(3) - bx(1)) * p} 410` : ''); POP(S, '#fd', td - .1, 'thud'); }},
 { // 8 payoff
  html: `${ROW('r8', 420)}<div class="abs center lab" id="tc" style="top:620px;font-size:44px">lookups: 0</div><div class="abs center" id="on" style="top:760px;opacity:0"><span class="badge">O(n)</span></div>
   <div class="stamp g" id="pn" style="left:200px;top:1160px;font-size:76px">HASHING PATTERN</div>`,
  draw(S) { const n = Math.min(4, Math.floor(4 * S.P(.05, TT(S, 'lookup', .4), x => x) + .001)); LITSET(S, 'r8', [0, 1, 2, 3].slice(0, n)); S.$('#tc').textContent = `lookups: ${n} (stopped at the answer)`; if (n !== this.n) { S.sfx(S.t, 'click'); this.n = n; }
    POP(S, '#on', TT(S, 'o', .7) - .1, 'ding'); S.$('#on .badge').style.transform = `scale(${1 + .035 * Math.sin(S.t * 5)})`; STAMP(S, '#pn', TT(S, 'o', .7) + .45, -6); }},
 { // 9 CTA
  html: `<div class="abs center kick" style="top:420px">want 5 more like this?</div><div class="abs center" style="top:520px"><span class="notes">NOTES</span></div><div class="abs center h2" style="top:830px">comment NOTES for 5 more<br>questions with this pattern</div>
   <div class="abs center" style="top:1160px"><span class="pill" id="fl"></span></div>`,
  draw(S) { S.$('#fl').textContent = 'Follow ' + HANDLE; POP(S, '.notes', 0, 'pop'); S.$('.notes').style.transform += ` scale(${1 + .03 * Math.sin(S.t * 6)})`; }},
];
