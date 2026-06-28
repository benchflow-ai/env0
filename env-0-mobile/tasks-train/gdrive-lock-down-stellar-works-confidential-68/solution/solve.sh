#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1fScjNpOMewt3xabJnV762sSuBPbpQx6utX7F19vHoeG"
  "1IQNMkH7WDDa0fLfMJoLRp34UDdk4BkYBzDYAoShd0X2"
  "1tb7vDOhyk8BNyK6W4qBSw4FnGKuuMhD1TJJAWscqjjB"
  "1Vv3I1jSG4GCG6p1j4mj6p7zuMILv2WAZDLNlP8kUIrp"
  "1DVWK2c5WvbXQPFYeuBdiDBgHxKLpXGbxpGDRTqzprzO"
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
