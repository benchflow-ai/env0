#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1PK2CHRQqnmoqQ0csENNQfy6VxAkZRdPbcyL5leo48aQ"
  "1sE4KLDmm7q5WTSBWA9yYf3pGEhI0AEjC64N9X1z5vNS"
  "1AOw5p5yVFQlhxphcfjXDz00G2HIrqr6fyLIoFhuRlcK"
  "16ez573BuQcyLWU6PX7RlSL0izezoesQdckyFtslBbsh"
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
