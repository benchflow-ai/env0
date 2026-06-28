#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1mJrhyP5izCwhPcZ0TDmLosfbOzVJUzOdKEWGR3XtzTI"
  "1VDSHZltFu4unnQg5DngENPlMv9dspDnECTYUjWHnvw7"
  "1FBPUDGLuoyh7D4OI6bLxMs5QngLdiL07DtqSrc9v8JJ"
  "1PCYy3e0SxaBXzaK6Hl6IINsjfUMWWDY6ULmJHR6m5JZ"
  "1JUGFeC8cF1xY7V5IfyfOlbPVD6THL5IH1ag7gepfTPV"
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
