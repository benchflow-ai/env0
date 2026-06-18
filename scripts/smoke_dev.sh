#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTROL="$ROOT/scripts/env0_control.py"
DB="$ROOT/.data/dev/data/gdrive.db"
ADMIN_DB="$(mktemp -u "/tmp/env0-gdrive-devhub-smoke.XXXXXX.db")"
ADMIN_PORT="$(python3 - <<'PY'
import socket

with socket.socket() as sock:
    sock.bind(("127.0.0.1", 0))
    print(sock.getsockname()[1])
PY
)"
TARGET_ID="1DraftArchiveTargetQ3PricingPlanAlpha000001"

log() {
  printf '\n==> %s\n' "$*"
}

log "unit tests"
python3 -m unittest "$ROOT/tests/test_env0_control.py"

log "control dry-runs"
python3 "$CONTROL" --dry-run start-default >/dev/null
python3 "$CONTROL" --dry-run start-task email-confidential-forward >/dev/null
python3 "$CONTROL" --dry-run start-default --devhub >/dev/null
python3 "$CONTROL" --dry-run start-task --devhub email-confidential-forward >/dev/null
python3 "$CONTROL" --dry-run seed-default mock-gmail >/dev/null
python3 "$CONTROL" --dry-run seed-task gdrive-archive-stale-drafts mock-gdrive >/dev/null
python3 "$CONTROL" --dry-run reset mock-gmail >/dev/null
python3 "$CONTROL" --dry-run snapshot smoke mock-gmail >/dev/null
python3 "$CONTROL" --dry-run restore smoke mock-gmail >/dev/null
python3 "$ROOT/devhub/app.py" --render-once >/dev/null

log "real task-aware seed"
python3 "$CONTROL" seed-task gdrive-archive-stale-drafts mock-gdrive

log "verify seeded needle"
python3 - "$DB" "$TARGET_ID" <<'PY'
import sqlite3
import sys

db_path, target_id = sys.argv[1:3]
con = sqlite3.connect(db_path)
try:
    count = con.execute(
        "select count(*) from files where id = ?",
        (target_id,),
    ).fetchone()[0]
finally:
    con.close()

if count != 1:
    raise SystemExit(f"expected one seeded target file {target_id}, found {count}")
print(f"seeded target file: {target_id}")
PY

log "devhub admin task seed path"
rm -f "$ADMIN_DB" "$ADMIN_DB-shm" "$ADMIN_DB-wal"
(
  cd "$ROOT/packages/environments/mock-gdrive"
  uv run mock-gdrive --db "$ADMIN_DB" seed --scenario default >/tmp/env0-gdrive-devhub-seed.log
)
(
  cd "$ROOT/packages/environments/mock-gdrive"
  TASKS_DIR="$ROOT/example_tasks" uv run mock-gdrive --db "$ADMIN_DB" serve --host 127.0.0.1 --port "$ADMIN_PORT" --no-mcp >/tmp/env0-gdrive-devhub-serve.log 2>&1
) &
SERVER_PID=$!
cleanup_server() {
  pkill -TERM -P "$SERVER_PID" 2>/dev/null || true
  kill "$SERVER_PID" 2>/dev/null || true
  wait "$SERVER_PID" 2>/dev/null || true
  rm -f "$ADMIN_DB" "$ADMIN_DB-shm" "$ADMIN_DB-wal"
}
trap cleanup_server EXIT
python3 - "$ADMIN_PORT" <<'PY'
import sys
import time
import urllib.request

port = sys.argv[1]
health = f"http://127.0.0.1:{port}/health"
for _ in range(40):
    try:
        with urllib.request.urlopen(health, timeout=1) as response:
            if response.status < 500:
                break
    except Exception:
        time.sleep(0.25)
else:
    raise SystemExit("mock-gdrive did not become healthy")

for path in ("/dev/dashboard", "/dev/db-viewer", "/dev/api-explorer"):
    with urllib.request.urlopen(f"http://127.0.0.1:{port}{path}", timeout=5) as response:
        body = response.read().decode("utf-8")
    if "Drive" not in body:
        raise SystemExit(f"{path} did not render Drive shell")
    print(f"{path} ok")

request = urllib.request.Request(
    f"http://127.0.0.1:{port}/_admin/seed?task_name=gdrive-archive-stale-drafts",
    method="POST",
)
with urllib.request.urlopen(request, timeout=15) as response:
    body = response.read().decode("utf-8")
print(body)
PY
python3 - "$ADMIN_DB" "$TARGET_ID" <<'PY'
import sqlite3
import sys

db_path, target_id = sys.argv[1:3]
con = sqlite3.connect(db_path)
try:
    count = con.execute(
        "select count(*) from files where id = ?",
        (target_id,),
    ).fetchone()[0]
finally:
    con.close()

if count != 1:
    raise SystemExit(f"expected one admin-seeded target file {target_id}, found {count}")
print(f"admin seed target file: {target_id}")
PY
cleanup_server
trap - EXIT

log "ok"
