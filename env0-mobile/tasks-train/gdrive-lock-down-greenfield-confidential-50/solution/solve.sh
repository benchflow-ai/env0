#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1x60zynNTICzz2jO5cGwBOALYjiQvLSIh5MYldRE385R"
  "1LaFDVOcYGjwQA90x8tTmOUmycFvebTqqPODuTHDvW4X"
  "19vIuChSAlwZYnervtUp2g79Zp7DHAgQevESGSHk2QKQ"
  "12HIJgYwu2lgbtDyvfgD8KUYBORtJhma6N5aDtd4E1xL"
  "1kEMPo25ixEL9UqK8fiEd4zG26dtPziX2OhULx377ZYb"
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
