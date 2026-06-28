#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1BIDeYJNilmJJMVpM9JpfJD0uazTR7JBqU8hLaDJmZlS"
  "1nXriWM2FNLWzgtC5lJ7X89h30gPwmQHIAWJ9YOK6qf0"
  "16X4gCBTeQJj2oP9Izdt9DSxevYsYRBhm42eD96SHzEu"
  "1ZtMiYI8FcDxE0iwFDKP9SEacBI4xK1bk6GHAitpejMS"
  "1vJQxHr3gD0fEJErv65f92ot4QSCif03cHztwFozQvaR"
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
