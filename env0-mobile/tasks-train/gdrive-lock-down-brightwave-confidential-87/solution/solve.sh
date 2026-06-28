#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1kQlU9G6MmqTpgkFhTdqMfFWphr3TX6T8xvbexfkWlZr"
  "1vfEKUSVUIadOWyEd8uetVGZtAICm4EzavbvMHY03pY0"
  "1TYPEiSW9GnJ1TRZ2o4uoxS6K5M6fLtaNxqF1whZ3PPB"
  "1T448oCjRqOxVthazUEdzdJLUxZ1LQTdW5ApKW3Dol14"
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
