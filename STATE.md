# State

- 2026-11-23: repo set up (engine + kit copied from frontend-decoded, publish scripts, post-reel workflow, site builder).
- 2026-11-24: Season 1 rendered, all 30 reels (30-45 s, notebook look). videos/ + covers/ + publish/queue.json built (30 waiting).
  E01 = W3 look, E16 = T1; the rest are NB specs (engine/nbspec.py -> webreels/_kit/nb.js).
  Per-episode flow: spec.py -> Speko TTS (Fenrir 1.2) -> transcribe (word_timestamps) for scene starts -> python3 -m engine.ep prep ID raw.wav anchors -> python3 -m engine.cuecheck ID -> queue.
- Next: notes pages (notes/eps/s1eNN.md + .js, EP asked/similar lists) and site; push once the GitHub repo is reachable; IG secrets for @tech.explained.dsa.

## Open decisions
- Instagram handle: @tech.explained.dsa (decided; separate page).
- Posting slot: provisional 18:47 IST + backup 19:27 IST (cron 17 13 / 57 13 UTC).
- Netlify project name / URL (config.py SITE_URL).

## Seasons
- S1 ₹10-15 LPA patterns (arrays, hashing, two pointers, sliding window, prefix sums, binary search, stack)
- S2 ₹20-30 LPA (monotonic stack, intervals, heaps/top-K, linked lists, greedy, backtracking)
- S3 ₹30-50 LPA (trees, BFS/DFS, topo sort, Dijkstra, union-find, tries)
- S4 ₹50 LPA+ (DP)

## Analogies used (don't reuse for a different concept)
- (none yet)
