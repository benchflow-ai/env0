#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1rZ2PM3ZriIhHBXM4Vm3HufWSghgEcKyXGe1fOUqvNmt"
  "15eujJyIcIAyvbLnzXuzzPiE8I8vACMUkebzQplDHvFn"
  "1RZJoMA64qnQiAxcSXVioa9tx2Afx8iOBr8mjfIFmimg"
  "1N6V3P5uDHzcsKy1Bay01VWstAozAUuot2SHyZ9NVua3"
  "1YzsQ4fN8QJYeaYlsD8BAWMxcx9fRyhgyKhISZD9g9UP"
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
