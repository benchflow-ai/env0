#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1FwhIFHxJsEBKqqYYYheIFASDXGsHj7Ez5h1ofBzlChD"
  "19ZRQpGXC6G1HOdgrQPaYRDi2ue24stq5rYxMD0eMU2O"
  "1JpXgX3rD7qAJl0C6HE4GXXPQ72LyIl6gMWEuSUccNLg"
  "1FSzPo04rkLp5hQPOnfkJepOCUbuN4WayjIpe8MzAXZ8"
  "1ArMOmFodjxXeTgsnWEn2NwPkqBzgSprt1Eq0hYJpjsL"
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
