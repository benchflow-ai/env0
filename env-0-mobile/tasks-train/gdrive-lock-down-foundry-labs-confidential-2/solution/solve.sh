#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1GCC297IOgZf4dZn7GF5JBLeVZoQErVV1pk9xCS50QDe"
  "19s4PwuooNSLNTpzPwL1Mv7pJcGzs7CgCWIqPzaKf8xi"
  "1iY3ZgjEZcXOjjKAi7nSfwNgRfbHFuZgWJxJ9hsbD5aw"
  "11ZDuxTFOqfra4XHs6VJXhvTT5etLHuqhVbsmwNPv3bm"
  "1QMkdpq4PVvI1cOMq04CD1A4SuOMioY1mWSFo5qos0aK"
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
