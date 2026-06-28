#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1YBL8B9XPB2x1WSdENmJb9IHW3hPnVNUUw9yyhdwMr6r"
  "1ehu6dGkVvPxpRWkh8TPcspjWYEMLALP9rVA9Irc3MTF"
  "1ZfMA0ogh1luK6uaZYC1EBoj7rW4YL2Fnkh2CceKsDEi"
  "1wYJX7A66A07msxFjV0ZUBG8c41WnJMmdICTPi0bxvTD"
  "1PTVzcoMxpKA4MbSUxoaQYCom9nav0YlylRCj8DR6PYc"
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
