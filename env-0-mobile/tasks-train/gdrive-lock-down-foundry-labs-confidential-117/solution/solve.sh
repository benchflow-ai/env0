#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "109lxNPAhtDFHQz74UnodrjYUDNQLByR81ggB0r0fXeO"
  "19k4oYMkUF1TRR0MHr6bECR4ElS8k7hrtF8Bhy4CCOlF"
  "1xMTSkru5CMPcDgRBEEKHgkMQ3kph8uWAJzd6eKL4xOL"
  "1dJckIJO2sNIMQfcylgJJYwF4lwutXX65lGR5MhKTYeB"
  "1s3jEdvcA7K2tUyhBU2jx9q7NotrUC17VUoHPB8TZPII"
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
