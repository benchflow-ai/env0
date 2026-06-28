#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1idvVk8pEz41GGeRJsyNurgS3zF0yOgOXqDSzzz3XaCj"
  "110Mu79kgoZEtG0suSLV0wOZSS0Hcx8HFpBLL3pmUkGm"
  "1rCQK6zspfegBGQxOQHds8mUwYxFRoLtqAs2Ob4vDlCe"
  "1xBpPR7erTsaDMwvQxvROqgr4R9ZbdXcEiQnk0OSg2Xd"
  "1fow92OAaDfQS3llo5eWatSHKJSDlMl2PpNFtz9la7bB"
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
