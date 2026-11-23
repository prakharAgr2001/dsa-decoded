"""Designed Instagram covers: blurred key frame, "₹28 LPA · AMAZON" pill, question name, hook.
Usage: python3 -m publish.covers S1E01 [S1E02 ...]   (needs out/<ID>_*.mp4)"""
import glob, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.lib import font, INK, YEL, RED, WHITE, GRN
from publish.episodes import load
from config import BRAND_TEXT

def wrap(text, f, maxw):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if f.getlength(t) <= maxw or not cur: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]

def cover(eid):
    ep = load(eid)
    src = glob.glob(f'out/{eid}_*.mp4')[0]; fr = f'tmp/{eid}_kf.jpg'; os.makedirs('tmp', exist_ok=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(ep.get('cover_t', 12)), '-i', src, '-frames:v', '1', fr], check=True)
    bg = Image.open(fr).convert('RGB').resize((1080, 1920)).filter(ImageFilter.GaussianBlur(16))
    im = ImageEnhance.Brightness(bg).enhance(.32); d = ImageDraw.Draw(im)
    pill = f"₹{ep['lpa']} LPA · {ep['company'].upper()}" if ep.get('company') else 'INTERVIEW CLASSIC'
    f = font('int', 46); tw = f.getlength(pill)
    d.rounded_rectangle((540 - tw / 2 - 40, 420, 540 + tw / 2 + 40, 510), 45, fill=GRN); d.text((540, 465), pill, font=f, fill=INK, anchor='mm')
    title = ep['title'].upper(); size = 150
    while size > 70:
        fo = font('osw', size); lines = wrap(title, fo, 880)
        if len(lines) <= 3: break
        size -= 8
    y = 580
    for i, l in enumerate(lines):
        w = fo.getlength(l); x0, x1 = 540 - w / 2 - 34, 540 + w / 2 + 34; sk = 6 if i % 2 == 0 else -5
        d.polygon([(x0, y - 4 + sk), (x1 + 8, y - 14), (x1, y + size - 14), (x0 + 6, y + size - 4 - sk)], fill=YEL)
        d.text((540, y + size // 2 - 6), l, font=fo, fill=INK, anchor='mm'); y += size + 16
    fh = font('int', 52)
    for l in wrap(ep['hook'], fh, 900): d.text((540, y + 70), l, font=fh, fill=WHITE, anchor='mm'); y += 66
    pt = f"{ep['pattern'].upper()} PATTERN"; fp = font('int', 38); pw = fp.getlength(pt)
    d.rounded_rectangle((540 - pw / 2 - 30, 1400, 540 + pw / 2 + 30, 1470), 16, outline=YEL, width=4); d.text((540, 1435), pt, font=fp, fill=YEL, anchor='mm')
    d.text((540, 1620), BRAND_TEXT, font=font('osw', 60), fill=YEL, anchor='mm')
    return im

if __name__ == '__main__':
    os.makedirs('covers', exist_ok=True)
    for eid in sys.argv[1:]:
        cover(eid.upper()).save(f'covers/{eid.upper()}.jpg', quality=92); print('covers/' + eid.upper() + '.jpg')
