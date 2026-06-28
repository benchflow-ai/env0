#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1zLYgHRXH9S7QM3lEofoE3c3EfZUNmSNeMFDQL24KXXX"
  "1ZNKU5hTbT6tyUUnukfstLzQyMikyK2cDZpUzJuqUS56"
  "1P032mgKE3d7RlnPyVdbEZCa9fQ1neotBMpJuQUWM9qE"
  "1g2TQ50gShtZsJ40gG2FJco652TNBsLt2DWacnVRuWFD"
  "1FvhRSo2UMECzPm7tbCzClNYJFWTXJtcxk4hRyKcuztL"
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
