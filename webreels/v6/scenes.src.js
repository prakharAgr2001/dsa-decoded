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
