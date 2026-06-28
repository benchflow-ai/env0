#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1TobojdH3iqfXuBqNPPazYDrIG4sDrhzuo39YIIIzkwm"
  "1bquDQ9n58VoR2lgbPKFRrpbfMwOgjV7k0brL8IpPBXU"
  "1umfHjKJqFw6z3OliIsoVM1l1RdDvBQ08gQg8pA0Vhs0"
  "1NGjSIPjmOvQ0QT3MDuM4fxbYm0NfReRj8ZJGqvbYAy5"
  "1MK5U4FRlVEHJ3x1LocDLEvrvP8matYLpgUjddewyGv4"
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
