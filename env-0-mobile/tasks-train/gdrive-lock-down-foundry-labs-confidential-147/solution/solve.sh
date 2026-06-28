#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1pLnN6Ovj2EWnyOz1yvXPOkki9I3apshj6cTrZZXDmMg"
  "1wnkEYZlRSZuiiQ4NGpS8xLzcuQ7lHe7Pjm7HZhZ62ql"
  "1fv6HMngUTBX9xvj9ZAo4DaArqwgEB6Syef96tSB7suz"
  "13JyyD8Sq2yquBT80ozBCP9ZNb7qv6Tw1BoT0yxe2BNH"
  "1TIkTsXpTILOXtE9qq05HBVJTX116RURqobLV2POVYAT"
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
