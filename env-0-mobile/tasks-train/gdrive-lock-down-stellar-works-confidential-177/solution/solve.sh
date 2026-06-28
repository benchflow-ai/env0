#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1jCEpGahctuOtyRbOg1VT7krg5HdMeHSkpheE3EcQ7ej"
  "1LAdBAdncZMIMsaDQJ9xw7ULYUCg0FWVPXRqlccKMFiA"
  "1QGqxd1YiCACEbxx9PaxE7NkZ2WapNNTNg1MH5rxAJsd"
  "196Atp3fFbjVYCznzhEBVaS2csNDJwgOIRFW0sgBwQAH"
  "1Zu5VpSnZMoFT0pFlDxgeQv0Ayy4QFyfUHzBDYGBl7OA"
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
