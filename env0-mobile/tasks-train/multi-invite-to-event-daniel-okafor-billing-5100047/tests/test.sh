#!/usr/bin/env bash
# Fetch state/diff/action_log from the environment and run evaluate.py
set -euo pipefail

GCAL="${CALENDAR_URL:-http://localhost:9003}"
GMAIL="${GMAIL_URL:-http://localhost:9001}"
LOGS_DIR="${LOGS_DIR:-/logs/verifier}"
mkdir -p "$LOGS_DIR"

curl -s "$GCAL/_admin/state" > /tmp/final_state.json
curl -s "$GCAL/_admin/diff" > /tmp/diff.json

# Merge action logs from all involved services
curl -s "$GCAL/_admin/action_log" > /tmp/al_gcal.json
curl -s "$GMAIL/_admin/action_log" > /tmp/al_gmail.json
python3 -c "
import json
paths = ['/tmp/al_gcal.json', '/tmp/al_gmail.json']
merged = []
for p in paths:
    d = json.load(open(p))
    entries = d.get('entries', d) if isinstance(d, dict) else d
    merged.extend(entries)
json.dump({'entries': merged}, open('/tmp/action_log.json','w'))
"

python3 "$(dirname "$0")/evaluate.py" \
  --state /tmp/final_state.json \
  --diff /tmp/diff.json \
  --action-log /tmp/action_log.json \
  --output "$LOGS_DIR/reward.json"

cat "$LOGS_DIR/reward.json"
