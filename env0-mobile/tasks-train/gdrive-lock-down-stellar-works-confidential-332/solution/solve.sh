#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1PmQUDvrPOYU0Suv7GV6NsW3PVQ3uGI086nYvKKQT1pX"
  "1SF6oggpqoZ3tihlT7XT4nXHlKhD9mvaS7U58p15XAMf"
  "14MwFmgdqsyM5GwWFcBaAiFaR3WWpcgGcv1w2MGtsMRQ"
  "1qboSfh12u7rttAy500fn5Y6Pdaq6W9nKmcQRDEqfnEQ"
  "1GVwTJzdgraAWzRZJneU4JPi8fXE3cagnXNmc4pi1v67"
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
