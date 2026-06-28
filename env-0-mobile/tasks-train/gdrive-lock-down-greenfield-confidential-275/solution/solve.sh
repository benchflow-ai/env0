#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1prGNs5j9RaVd4UedZLbnRxhOrY24bvez5aMe00Bu5bU"
  "1Zj6uDkSvMuX2Ap8bBrdzb4VOwuSi65UrStzUhQDy2vs"
  "1uE24KN4GJlx1PBVIJDTsnm06mYQlQigN2zD422Tkq4r"
  "1aF4r3RoRqYmHQUvXl4nYXbtOzOpvi28oYJEcB5Ozqim"
  "1otImzv3l2BQW7ybs6xf0JADsfXHlBNGPxE8VK3awwUj"
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
