#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1w1eETbQsMQC65Kqtj8bTiW3iQSteM7sOpFHcGSORgKE"
  "1MoBosPAmZluB5VxBZnVeC5qLUsBkCqYkyKxBpoA8Kaq"
  "1MChjVFxP0DGeEwNAaKudnV4ocbI7PfmOlKDsE0RPl95"
  "1xhhu3iIzjMYOHTgOYbzhmWUX8luOedbijEJT769UGPe"
  "1rUDoP2tEq8nrVIeoLidlrvrAet2i5QTvTWHaSphtAjI"
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
