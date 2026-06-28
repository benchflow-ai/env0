#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1RhKk6MDodHNxBbUg86QJyin3yrEZMS6SSqZeflcJWwP"
  "1E2C7wU2lrCXrMw77faIZZ7h6ACRq3SIWlPxqcfb5PVp"
  "1E0c4CAdwmAQBHzsuZSZK0ma4YO4ePMKMEBHfSdcUS02"
  "1WdQ3CYtLp6O8ITd0wRjb4GK5kAcI9q1WAlkqUapLcak"
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
