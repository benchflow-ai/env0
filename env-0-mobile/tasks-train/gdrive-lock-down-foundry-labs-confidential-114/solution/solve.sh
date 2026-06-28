#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1AknakkTXKBwC8uw4iq18nmsQLrzWCzcavidHDhaFHxo"
  "1Gf41sxYrCLzSLDZt24xdLCeGfvKW3RawyVAdXXG8Bvh"
  "1OGNWbwDZlR33fN4VuDALZrnAZ1LPmK2cs4S3hBfp7s6"
  "1A9Lqf1F94IVQhAPcuhlV3FQnzsfECmpoht1HDwF5k5p"
  "1ieSg89TJyYNlq6SP0QJ7keUdbCle5DNBFGw6dUvNYpc"
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
