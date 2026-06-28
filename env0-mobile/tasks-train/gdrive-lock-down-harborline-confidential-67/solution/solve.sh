#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1gEaTDFwjXrvHi4LVHPkeCsVFOJ4yORQbcy90tWoFDMw"
  "10obootwOOo0KuLHSo9kErDL3LrNeX2RNV9DtCHSMz8C"
  "12mhxFi9OfyfOvDDytgPEBHAwV6254xzkTRTABpbv3Te"
  "1WuutuwXM6k5GLnlbt2OVCedodxCmJlH4he6H7PEtalc"
  "1HgJwsFMoCbYRXsT4GGQw3J5edgbFX3yj23LWmIqwSl7"
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
