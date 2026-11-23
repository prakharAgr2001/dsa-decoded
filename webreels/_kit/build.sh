#!/bin/sh
# usage: sh webreels/_kit/build.sh wr12   -> prepends the kit to webreels/wr12/{scenes.src.js,style.src.css}
# scenes that start with "// uses:dsa" also get _kit/dsa.js (shared array/map helpers)
d=$(dirname "$0"); r=$d/../$1
if head -1 $r/scenes.src.js | grep -q "uses:dsa"; then cat $d/story.js $d/dsa.js $r/scenes.src.js > $r/scenes.js; else cat $d/story.js $r/scenes.src.js > $r/scenes.js; fi
cat $d/story.css $r/style.src.css > $r/style.css
