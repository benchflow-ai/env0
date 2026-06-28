#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1EwqsdT8HPDFQ8JB9C0zKeiaR1QShdZrsNnDEZ9dzm2s"
  "1qFJI6vjj3156uQ0pOk7U78JbPL1TU6D91hs81FnwL1Y"
  "1tixs7fDQwnOpCLl12RcECv1cNVu7T6FF24Ayl2NzfuD"
  "1sKoZSMLl2IvnGsHUveZAyp2xyVcHY0jGEJQRD6gYr2P"
  "1EsvpoSwFqu2TIIczuhG49hH1ZDYsCbGUZa6ACna63FU"
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
