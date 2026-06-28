#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1VY9819NHdBki1fO4lHrMNqR4k1hCRsLtyDVNp3mKSam"
  "1SgP0NAXj1BJ2otjAuc9gM1WOv10yPogzAbkbystaZ2q"
  "1WCkKPOZhls3i2fJhqjru9U2wOizmyEY2qHpKjRQdx3b"
  "1cfIZhtnfVZIlOELJmPs5BntI90VJcJbCHQL7eLylj1x"
  "1eOSXinm647sIKtmSdR9H2vUS5xmv5FbjpQrkkUtxpbn"
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
