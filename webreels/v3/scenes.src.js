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
