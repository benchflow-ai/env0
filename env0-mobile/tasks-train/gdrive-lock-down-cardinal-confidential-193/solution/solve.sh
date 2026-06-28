#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1AvecIVtpKyt0m0fdXYTgoNqWrPBTagOk6GVjSMT4Zs9"
  "1IedEzHprIrUvY8kUGmgrscab39mG9dvV9EskI2SyXP5"
  "1x0bGumJ8ZGl608T1JtUTr1AkJ2S9zTh0e8rNYIo3Pp5"
  "1w5KxYRXeU9ThAm08H38wg1wFamkLMak27I7TAMpQMNn"
  "1WA2RqmAJwt3ix9ErFVG12XnAUwCKqEDUzDM68eJLNhS"
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
