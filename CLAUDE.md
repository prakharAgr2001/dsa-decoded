# DSA Decoded · production repo

Vox-style 9:16 reels (35-50 s) that teach one DSA interview question each, auto-posted daily to Instagram, plus a notes site.
No personal name anywhere (reels, covers, captions, URLs, site). Branding lives in `config.py`.
Read `STATE.md` first (where we are), then only the files for the episodes you are working on.
The engine and kit were copied from frontend-decoded (`webreels/sample_dsa02/` is the reference look). Do not rebuild them.

## Episode files
- `webreels/sXeYY/spec.py` - source comments (every URL + date), `EP` dict, `NARRATION` (one line per scene).
  EP keys: id, short, title, pattern, difficulty, official, company (or None), claim ('asked' | 'reported' | None), year, lpa, role,
  hook (cover subtitle), cover_t (key-frame second), asked=[{company, role, year, source, url}], similar=[{name, url, difficulty, companies}] (5, easiest first),
  tail, bpm, drop_scenes, optional hold=True.
- `webreels/sXeYY/scenes.src.js` + `style.src.css` - scenes; the kit (`webreels/_kit/`) is prepended automatically on check/render.
- `notes/eps/sxeyy.md` - `## Problem`, `## Example`, `## Pattern`, `## Key points`, `## Interview answer` (a `>` quote), `## Analogy`, `## Common traps`, `## Complexity`.
- `notes/eps/sxeyy.js` - plain JavaScript (no TypeScript) solution + 3+ tests incl. edge cases, printed with console.log. The site build runs it with node and shows the real output.

## Reel format (match sample_dsa02)
1. HOOK 0-4 s: "Want a <X> lakh job at <Company>? This exact question keeps showing up in their interviews." Offer card (role · company · ₹X LPA, plain text, no logos/brand colours) + tag "ASKED IN <COMPANY> INTERVIEWS · <YEAR>" (or "REPORTED IN A <COMPANY> INTERVIEW").
2. QUESTION 4-9 s: one line in OUR words on a card. Never copy LeetCode/GfG text.
3. EXAMPLE 9-13 s: our own small example in boxes, answer revealed.
4. TRAP 13-18 s: brute force + a REAL computed count -> REJECTED stamp.
5. INSIGHT 18-38 s: pattern animated step by step on the example, synced to words (labelled pointers, glowing window, red on conflict, arcs, live side table). One Indian analogy if it helps.
6. PAYOFF 38-42 s: complexity badge + pattern name stamp.
7. CTA last 3-4 s: big NOTES card, "Comment NOTES for 5 more questions with this pattern" + follow line (`HANDLE` in JS).
No code in the reel. Every number on screen is computed (in JS or a checked comment), never invented.

## Sourcing rules (strict)
- Company claims from recent (last 2 years) interview experiences: LeetCode Discuss, GfG interview experiences, Naukri Code360, Glassdoor, Taro. Read individual pages only; no scrapers or bulk downloads.
  2+ independent reports -> "Asked in <Company> interviews (<year>)"; 1 -> "Reported in a <Company> interview"; 0 -> no company, "a classic at product-company interviews".
- Salary: real range for that role/level (AmbitionBox / Levels.fyi / public offer posts); hook uses a round number inside the range. No fake exact numbers, no guarantees.
- Every source URL + date as comments at the top of spec.py. Never on screen.
- Prefer questions reported at 3+ companies. Across a season no company is in more than ~30% of hooks.

## Make an episode
1. `python3 -m engine.webreel text SxEyy` -> exact TTS text.
2. Voice: Speko `audio.synthesize`, provider google-tts, voice "Fenrir", speed ~1.2, instructions "Young Indian male tech creator on Instagram, Indian English accent, warm, confident, energetic, conversational, punchy hook, clear teaching rhythm."
   (ElevenLabs "Kaanha" id kNgdRSecKh7LrZA0cR8g via Speko if the account has credit.) Then `python3 -m engine.voice tts SxEyy raw.wav --fit 46` -> vo/SxEyy.wav.
   Own recordings: `python3 -m engine.voice clean SxEyy file --fit 46`.
3. `python3 -m engine.webreel check SxEyy` -> tmp/SxEyy_sheet.jpg. Fix overlaps.
4. `python3 -m engine.webreel render SxEyy` -> out/SxEyy_<slug>.mp4 (background, several in a queue).
5. `python3 -m publish.release S1` -> covers/, videos/, publish/queue.json, site/.
6. `git add videos covers publish/queue.json site notes webreels && python3 -m publish.verify` (every queued item must have videos/<id>.mp4 + covers/<id>.jpg tracked).

## Posting (GitHub Actions, .github/workflows/post-reel.yml)
- Media URLs pinned to GITHUB_SHA; missing video/cover -> skipped, not failed; `hold: true` keeps an item from auto-posting.
- Instagram processing errors retried 3x with a fresh container. Normal reels, share_to_feed true (trial only on request).
- Cron on off-peak minutes + backup 40 min later + SKIP_IF_POSTED_WITHIN_H. Never 11:31 or 13:17 IST if the same account as frontend-decoded.
- Manual run: `gh api repos/prakharAgr2001/dsa-decoded/actions/workflows/post-reel.yml/dispatches -f ref=main -f 'inputs[episode]=S1E01'` (not `gh workflow run`).
- IG_TOKEN / IG_USER_ID secrets are set by the owner. Never ask for tokens, never set secrets.

## Git
- Before every push: `git pull --rebase origin main`, then `git -c push.negotiate=true push`.
- `vo/`, `out/`, `tmp/` are git-ignored.
- Site: Netlify, publish dir `site`, auto-deploy on push. Keep the hidden Medium card (`notes/links.json`). No emojis, no "TL;DR" on the site.
