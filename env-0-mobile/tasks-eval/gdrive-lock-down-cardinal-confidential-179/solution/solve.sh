#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1qJEc1YNM8T4wZwkMF1YVKY6DN6ApNLSIhAJEqZBJoIE"
  "1ttinqOj2rPbVV4jNoOgGqZzvwm0DxPnxIWRY9OUHDxG"
  "1zHGvxTUyFlQRgHw1ugwKBgANKHVZgcCVk4ufY5fKP3k"
  "1soJuxAjm9Npcfrnr2vIvUwkSXpPv1WWMJb87BNi712K"
  "1atPyNHQKFNpGnMQesScWqQ1qP7NHkMJ2UKIG7AxK65i"
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
