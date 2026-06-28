#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1k4jUO2XvOQ8f38sHRSSpOmy2joj1i6gQVL1PchMpp2c"
  "1oMDtF4UJUskq0lYDpaf5mFZBAOXfAUPNRLqSIryWqs2"
  "1eakAkZnufJZdRMyTzTvkqvSnfNhSm3KKhAm7Zz0I3Ns"
  "1HvpP7H4FkU6tYPZBBDQebqLfe9Mz5bj6HQ8IACTODhi"
  "1FzWnnlshr2odZsLuZbJsEYNujS5e7G0n4y1NBEoJy6U"
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
