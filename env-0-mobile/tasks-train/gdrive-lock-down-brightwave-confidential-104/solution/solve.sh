#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "19j3OsIAd1QPGqMiBffymeU96cz29BkmjKAp10VrbBIG"
  "1jqdedmgOYZoykD6hGVVKM1GSU0RLt2m4v24YQisyayG"
  "1YKjXurKfUv1IEjBaO0EyZxQuxJIRt2Hg8W10WIc6O6q"
  "1Ov4rHiQdlyH5Esc8qR7bEaA9xIVFA3d3sJLsgOyJkAQ"
  "1hSd2DdRIO0n0x5oKHCLAjyqRBcEhBmojUKYfofzWVQc"
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
