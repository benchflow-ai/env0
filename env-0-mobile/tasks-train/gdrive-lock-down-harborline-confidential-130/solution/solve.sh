#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1tbM3kf3pxMZ4cgFfThJgj64QBxWABVlcuaK4bUbuZOY"
  "1CajyZ2dXZEkuUz3BpEYq1SrubigKUqWFqxFzxvNkTQX"
  "1CpW3FBAUXaKiZFRDiIbNwsgLi4RLjmfZ0lOJFV18Xbu"
  "1DWof1UNXZlqH4s59pm9qyqWL0voWkBSUx2QbrtTUtNX"
  "1I1dJG05XzJcGWheI0DdYQYAAywJzQHKgECBVRneo4Xb"
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
