#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1OxpV9eiWqOZZuMLBR8eCY6h8sytLbhOfVoqvh6tgiYb"
  "1bj8viaAZRn8UWxerCguzZd61L6UBW2OfY7R6QBvo0qa"
  "15D9DYeVrZnCUJmrwWvLmjan5jMSFzbeXb0my191Jkhi"
  "1Q1xvzL0lPlWI5vCGmkawkZZp2uRPcU1kCm20mBLB0dV"
  "1z9SGBmYSbHJX7RB845sYVU9zWfTvcOwDyn5aNTFqu72"
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
