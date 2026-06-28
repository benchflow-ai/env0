#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1LgguEoHBahZGqN0oSQuqRRIgrSX7vjXGF6c0F8kCcKf"
  "1sJKwyGp3v3epiOy4MadRroYSD9WTf0cfvgSh9vpD1l3"
  "1XKttQob2ulTT8zUnwnaA95TbjCwKRdWb8MyLzUcuBDR"
  "14y9jPznO9oC2sPGjTXZkmNE8nA74w22N9xHhgoa4nQo"
  "1QLWJXkaxVGcS7FOXfIblDQn0wu6RESqy1UICcR4zOls"
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
