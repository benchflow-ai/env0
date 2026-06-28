#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1hZYE6K198Nx9NW7ELoTn1GMhMHjO9w4MBwAKftPOZOa"
  "1Cw4rBKX5xWFu8gjlUjGSulhPtTzAQyRcQMeaEYC9YHT"
  "15sFiXOge5gVTbxPVxV5L2m6zJHfdSSVq3NPjgaM2ET3"
  "1WGSpcUf8KSuiIrJaw1kX39DSjRA0xgLjwF39a44mu0G"
  "1RuNMvb67tnLxq4bfsPGH8pis4CDFC3GNuRoqs1mAUcu"
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
