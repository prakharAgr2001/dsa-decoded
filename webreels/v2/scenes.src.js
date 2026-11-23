// uses:dsa  V2 race: two lanes, counters computed in spec comments.
const LANES = (n, bf, hm) => `<div class="abs center" style="top:300px"><span class="nchip" id="nc">n = ${fmt(n)}</span></div>
 <div class="lane bad" style="top:440px"><div class="lh">CHECK EVERY PAIR</div><div class="lc" id="c1">0</div><div class="bar"><i id="b1"></i></div><div class="st" id="s1"></div></div>
 <div class="lane good" style="top:900px"><div class="lh">HASH MAP</div><div class="lc" id="c2">0</div><div class="bar"><i id="b2"></i></div><div class="st" id="s2"></div></div>`;
function RACE(S, bf, hm, t0, tb, th) {   // counts start at t0, hash finishes at th, brute visual finish tb (or never if null)
  const ph = S.P(t0, th - t0, x => x), pb = tb ? S.P(t0, tb - t0, x => x) : Math.min(.97, S.P(t0, S.dur - t0 + 6, x => x));
  S.$('#c2').textContent = fmt(hm * ph); S.$('#b2').style.width = 100 * ph + '%'; S.$('#c1').textContent = fmt(bf * pb); S.$('#b1').style.width = 100 * pb + '%';
  S.$('#s2').textContent = ph >= 1 ? 'DONE ✓' : ''; S.$('#s1').textContent = pb >= 1 ? 'DONE' : (S.on(th) ? 'still checking…' : '');
  if (S.on(th) && !S.on(th + .05)) S.sfx(th, 'ding'); }
const SCENES = [
 { html: `<div class="abs center kick" style="top:520px">two sum</div><div class="abs center h" style="top:600px;font-size:150px">THE <span class="mark" id="mk">RACE</span></div>
   <div class="abs center" style="top:900px"><span class="vs bad">every pair</span> <span class="vsx">vs</span> <span class="vs good">hash map</span></div>`,
  draw(S) { MK(S, '#mk', TT(S, 'race', .6) - .1); IN(S, '.vs.bad', .2); IN(S, '.vs.good', .4); }},
 { html: `<div class="qcard" id="qc">${WRAPW('Find two numbers in a list that add up to a target.')}</div>`, draw(S) { IN(S, '#qc', .05, 60); KARAOKE(S, '#qc', 1); }},
 { html: LANES(5), draw(S) { POP(S, '#nc', .05); RACE(S, 10, 5, TT(S, 'ten', .3) - .4, TT(S, 'ten', .3) + .2, TT(S, 'five', .8, 2)); }},
 { html: LANES(5000), draw(S) { POP(S, '#nc', .05); RACE(S, 12497500, 5000, .4, null, TT(S, 'thousand', .9, 2)); }},
 { html: LANES(50000), draw(S) { POP(S, '#nc', .05); RACE(S, 1249975000, 50000, .3, null, TT(S, 'versus', .7) + .4); SHAKE(S, '#c1', TT(S, 'billion', .5), 10); }},
 { html: `<div class="abs center lab" style="top:330px;font-size:40px">at 1,000,000 checks per second · n = 50,000</div>
   <div class="tcard bad" id="tA" style="top:470px"><span>every pair</span><b>20.8 min</b></div><div class="tcard good" id="tB" style="top:880px"><span>hash map</span><b>0.05 s</b></div>${GL('g5', 'rgba(61,220,132,.45)')}`,
  draw(S) { POP(S, '#tA', TT(S, 'minutes', .5) - .3, 'thud'); POP(S, '#tB', TT(S, 'second', .85, 2) - .3, 'ding'); GLOW(S, 'g5', TT(S, 'second', .85, 2) - .3); }},
 { html: `${ROW('rw', 380)}<div class="seen" style="top:640px"><h3>SEEN</h3>${[0, 1, 2].map(k => `<div class="kv" id="kv${k}"><b>${A[k]}</b><span>at</span><i>${k}</i></div>`).join('')}</div>
   <div class="abs center need" id="lk" style="top:1080px;opacity:0">150 → partner 350 → <b>found</b></div>`,
  draw(S) { const tr = TT(S, 'remembers', .3); [0, 1, 2].forEach(k => { const t = tr + k * .35; POP(S, '#kv' + k, t, 'pop'); LITSET(S, 'rw', [Math.min(3, Math.floor((S.t - tr) / .35))]); });
    const tl = TT(S, 'lookup', .85) - .2; S.$('#kv1').classList.toggle('hl', S.on(tl)); IN(S, '#lk', tl); if (S.on(tl)) LITSET(S, 'rw', [1, 3]); }},
 { html: `<div class="abs center kick" style="top:420px">winner</div><div class="abs center h" style="top:500px;font-size:130px">hash map</div><div class="abs center" id="on" style="top:760px;opacity:0"><span class="badge">O(n)</span></div>
   <div class="abs center lab" style="top:1100px;font-size:40px">every pair = O(n²)</div>${GL('g7', 'rgba(255,210,63,.4)')}`,
  draw(S) { POP(S, '#on', TT(S, 'o', .6) - .1, 'ding'); GLOW(S, 'g7', 0, 1.5); S.$('#on .badge').style.transform = `scale(${1 + .035 * Math.sin(S.t * 5)})`; }},
 { html: `<div class="abs center" style="top:480px"><span class="notes">NOTES</span></div><div class="abs center h2" style="top:790px">comment NOTES for 5 more<br>questions with this pattern</div><div class="abs center" style="top:1120px"><span class="pill" id="fl"></span></div>`,
  draw(S) { S.$('#fl').textContent = 'Follow ' + HANDLE; POP(S, '.notes', 0); }},
];
