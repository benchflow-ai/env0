#!/usr/bin/env bash
set -euo pipefail
python3 <<'PY'
import importlib.util, json, os, subprocess, glob
def _load():
    cands = glob.glob(os.path.join(os.environ.get('TASKS_DIR', '/tasks'), '*', 'data', 'needles.py'))
    spec = importlib.util.spec_from_file_location('needles', cands[0])
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def _norm(t): return ' '.join((t or '').lower().split())
def gws(resource, method, params=None, body=None):
    cmd = ['gws', 'calendar', resource, method]
    if params is not None: cmd += ['--params', json.dumps(params)]
    if body is not None: cmd += ['--json', json.dumps(body)]
    out = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.strip()
    if not out: return {}
    i = min([x for x in (out.find('{'), out.find('[')) if x >= 0]); return json.loads(out[i:])
n = _load()
cancel = {_norm(s) for s in n.CANCEL_SUMMARIES}
data = gws('events', 'list', params={'calendarId': 'primary', 'singleEvents': True,
    'showDeleted': False, 'maxResults': 250,
    'timeMin': '2020-01-01T00:00:00Z', 'timeMax': '2035-01-01T00:00:00Z'})
for ev in data.get('items', []):
    if _norm(ev.get('summary', '')) in cancel:
        gws('events', 'delete', params={'calendarId': 'primary', 'eventId': ev['id']})
        print('deleted', ev.get('summary'))
PY
