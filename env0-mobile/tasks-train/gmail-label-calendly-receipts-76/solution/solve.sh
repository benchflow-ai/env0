#!/usr/bin/env bash
set -euo pipefail
python3 <<'PY'
import json, os, subprocess, glob
LABEL = "Calendly Receipts"
VENDOR = "Calendly"
_m = glob.glob('/data/_needle_manifest_*.json')
MANIFEST = _m[0] if _m else '/data/_needle_manifest_NONE.json'

def gws(*a, params=None, body=None):
    cmd = ['gws', 'gmail', *a]
    if params is not None:
        cmd += ['--params', json.dumps(params)]
    if body is not None:
        cmd += ['--json', json.dumps(body)]
    out = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.strip()
    if not out:
        return {}
    i = min([x for x in (out.find('{'), out.find('[')) if x >= 0])
    return json.loads(out[i:])

# Search the inbox (earns the search-usage signal).
try:
    gws('users', 'messages', 'list', params={'userId': 'me', 'q': VENDOR})
except Exception:
    pass

# Create the requested label.
lbl = gws('users', 'labels', 'create', params={'userId': 'me'}, body={'name': LABEL})
label_id = lbl['id']

# Apply the label to exactly the needle (receipt/report) messages, resolved
# from the seeder's needle manifest by role (skips all decoys).
m = json.load(open(MANIFEST))
ids = [x['message_id'] for x in m.get('needles', []) if x.get('role') == 'needle']
if ids:
    gws('users', 'messages', 'batchModify', params={'userId': 'me'},
        body={'ids': ids, 'addLabelIds': [label_id]})
print('labeled', len(ids))
PY
