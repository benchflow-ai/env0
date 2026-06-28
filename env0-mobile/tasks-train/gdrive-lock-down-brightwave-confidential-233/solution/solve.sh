#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1w9N4GrSd2gJyZdufwkFbAGjpH5YOsarbD3jOGY1RkQq"
  "1K6r7oFqvSXZNZgjigPvaVtYiFB0CzfHFQ1Kdc2dznHi"
  "1kMNb6UCLuds7Db54zS242Rb8rEWSdubbFlDGU9BKD4R"
  "1RENvroJ4Hac8HtJPEHOiWoVAslD5cSOEjcN9cXyB4VN"
  "1sCoflje92QAbTxqRaNZL64Ce9LPVIGatIIRnRBSBUCF"
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
