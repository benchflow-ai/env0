#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1LkYOLwSb3uaN7XSA1FUckiMBq4RS1hF91151tGq5tlE"
  "1OhpF0iyaRpxvGvZDne0lNeGet4FfdJm28eLhDfx46N1"
  "1S8rosyOYT7TVXUqVF1inLvN2cbUl3VDkV8GlVIYCSYt"
  "1xXYG9pjSKiFkR5lQ0u0Sv4UlUnLUfD6h8milGjB7Vzw"
  "16zwZdIg2j3lXqdXG67CPyTbxTxtmeFUmqdujd4CkSpy"
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
