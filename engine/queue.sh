#!/bin/sh
# render worker: takes IDs from tmp/queue.txt (one per line), renders each once. Run two workers for 2 cores.
cd "$(dirname "$0")/.." ; touch tmp/queue.txt tmp/done.txt
while true; do
  id=$( (flock 9; next=$(grep -vxF -f tmp/done.txt -f tmp/taken.txt tmp/queue.txt 2>/dev/null | head -1); [ -n "$next" ] && echo "$next" >> tmp/taken.txt; echo "$next") 9>tmp/queue.lock )
  if [ -z "$id" ]; then sleep 5; continue; fi
  python3 -m engine.webreel render "$id" >> tmp/render.log 2>&1 && echo "$id" >> tmp/done.txt || echo "FAIL $id" >> tmp/render.log
done
