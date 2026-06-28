#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1W21L03FfYXJp3PH2Tl8YJU7z2MzgPdhVTD2P3wAoiJ2"
  "1x1oMh1QjMFnuH8YQ2U5j0zfcVRULx4cdEjbHI8GK7jm"
  "131Aec8RIMn4Gj2LMpwuXcVJmRkWF5uKtE01Tl8S5MQX"
  "13ruec5XoRYnvvxRfgMJPMuuNutLi9vUukuk8LbBiAE1"
  "16FZyDnIUefzfStMH9kxdVr8nrxysA7o6m48WQVQAU89"
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
