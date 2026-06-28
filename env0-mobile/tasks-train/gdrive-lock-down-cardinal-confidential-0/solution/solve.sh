#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "18rVjpVEDSlvs8ZEYDdHoGUbh0rUFoqePFNslfqBMJye"
  "13ju0wktsH5ZYv4JYNVuRhQ1x8UR9LxRqCdsmXXxNXGG"
  "1tW4q2BUMpk2RbvRHyYUOZufwTzR1vbWJHQWQzBz5vuz"
  "1IvlkvtLqdH7Jb2i7GXHocNdZyPdoL20hse2Kv3VpfbQ"
  "1vTDdAqLdjOJFeyvpK9SaexqZCGbYtHS6dGvftFDUhi2"
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
