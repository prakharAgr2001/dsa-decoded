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
