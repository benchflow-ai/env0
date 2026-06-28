#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1nMIzJ1JBJ1rhrOjLfbYNdDwMh6UxcwUsEbwMNXFqNC6"
  "1dnpvprWB8Pmz14DdkDJhj073nji8iaRiJ6jtcY1U3WO"
  "1Q43gEYRWdVX31LVVgyOFiwWyySDdVhj4t62Nzj9k1H4"
  "1S8IU12JKwF94KjFuNO7maGDSahGIILGwLYZ6rgB9wJG"
  "1ujmuUvvX4oR2RRHwWSGjWjVIgu5fC9FLjIHVsa7dDXS"
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
