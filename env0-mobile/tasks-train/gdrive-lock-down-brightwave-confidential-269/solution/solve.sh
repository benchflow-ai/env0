#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1SyM1oUfihK4pnzkZlInJ3f0pDlex39GJEsKMTnrG7xe"
  "1gqkbBS4xoFvo0vsr0WmkOPQD6xdHGV8bMftSW6XNPL3"
  "1ahE7wdJP1ocMJl3ZhGmcoeuxGyzEqtuPUvzSIK8s1AX"
  "11aOkJsx3BgE3IeGvccyJld3DSmHxWqDu6YrzE88sfdD"
  "1osnOgLok13QztewIlDnbZAQmnr9UUZOobAqrgtVwPRm"
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
