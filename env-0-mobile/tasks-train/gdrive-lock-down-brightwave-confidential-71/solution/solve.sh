#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1qRRznVRJV2gihBcPP7iVo1BpkavFiTusERbpxFvtdTP"
  "1nnCYc6u8x1edrLOggQipg9iqbJbbhoOJh63NaMQV4vn"
  "1gg1uBBmFJ9Hg8VFMAxUHrJ7qx5G7uSMRm6pCDaRhpMb"
  "1KAaia4pbofivQFJng42IqxxwoZCqWnkf2efwkLfKJJh"
  "1Fpn2tY73E3KHI6CZOwzvIXW40xZ8gQizZKYyTbsjw85"
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
