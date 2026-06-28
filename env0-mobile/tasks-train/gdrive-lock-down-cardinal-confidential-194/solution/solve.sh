#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "19AySObe0vgmQCW5698y1p4U3ZElYbPZNiq2kN7qdhso"
  "1xxg0VLVgZ3KC1WBw53Z3hHbRGYvQooLgUGVaYJxAYpg"
  "1zlg7lpBgZQjpzugs81lkU22ILfJ1qabJtKvzxZVSlH8"
  "1WFFVFK78InL5WJbIlbq84nHKaW6aEexbPyD0Kasnt0e"
  "14mWVjsBxsrLpUOxA9tiJlRuvKzsy4oLAZ4hNkNvA0Nq"
)

for FID in "${FILE_IDS[@]}"; do
  PERMS=$(gws drive permissions list --params "{\"fileId\": \"$FID\"}")
  echo "$PERMS" | python3 -c "
import sys, json
data = json.load(sys.stdin)
internal = '$INTERNAL'
for p in data.get('permissions', []):
    if p.get('role') == 'owner':
        continue
    typ = p.get('type')
    email = p.get('emailAddress') or ''
    bad = (typ == 'anyone') or (typ == 'domain') or (typ == 'user' and email and not email.endswith(internal))
    if bad:
        print(p['id'])
" | while read -r PID; do
    gws drive permissions delete --params "{\"fileId\": \"$FID\", \"permissionId\": \"$PID\"}"
    echo "Revoked $PID on $FID"
  done
done

echo "Done. Locked down sensitive files."
