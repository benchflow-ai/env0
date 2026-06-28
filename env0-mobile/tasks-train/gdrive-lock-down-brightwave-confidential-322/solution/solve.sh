#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1RMVo2SuBfzc6plAgSYEgZXGyEeRj8tPF3i2Orn68eXB"
  "1VwcGr5SECFhdnf3zhT2MzLQsaKy2xwZZYwza8P8TLXQ"
  "1Tt59nH0Tz8aIxal5bnt2WBCfN7SEd4t1TZW8Nnmua6e"
  "1u67tmBvnEvf4rnyFD14X775wXKYZGBwLfDJzY8gihYN"
  "126VC42SrPONY5raVPHno0r4pnQ1IvucnUSBOtxIQUYg"
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
