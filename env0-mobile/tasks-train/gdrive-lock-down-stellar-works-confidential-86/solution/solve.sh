#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1uX2w7ExrOUkNyumHc38bV3aU4kZfdNnPvxGLe1ye7ZT"
  "18NnrpUmMUiC7QENnxnXBKh6g9tWGu0wewwoMQ0bLC2k"
  "1UD0X40mrt1k6pBU22ex6Prdt18laCdrZVqAcLKcLDOd"
  "1AmWKA2jab9ZWbGyGOyKXSkFbDQySIigCJc683qJJC2s"
  "1AbePcrkYNBxy0Ku92WIMfr6nDuzHy0IMPEA51K139aD"
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
