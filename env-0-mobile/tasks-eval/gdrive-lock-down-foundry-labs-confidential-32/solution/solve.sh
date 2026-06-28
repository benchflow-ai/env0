#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1dg9qTU7HAVrmMgwzCLcURMQil9g4hrgwqTwBSe4nDuz"
  "1q1pkFUl6azwqLtzvSTvUlRAjklfFgAaFX19yfEWgdtn"
  "1CIpaQA5uWG84TgD37yRWSEmCOTDQ3dOapTb5Gt3X1BO"
  "10z3TNzQsZ83iaY6NbGBXqcKatIM89vpYuLK11Q2EHYg"
  "1Fv6laHhOgAo8cnrnhfujbcZOnfMA2oGwOeeGJP5mwlu"
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
