#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1lXCEy5AXGBbWxRmcjtVEHI9pcKTSp6m3tz6Nu4hS2bZ"
  "1jyqlaAVGvmyVgLmLT9csKLNHpXEabSMLG7xyHP099Ng"
  "1qf3zI2L1C2vEuOKBr6ivj2rYhxd9AKQuLMEUl2aRIef"
  "1V5okOo507TR8pun3zpgEnE4Wyc1uLTj0a8yT6WNLWpe"
  "1bPvMvLY6rnb25a3u5wtTTPUc0pdH4duf2zoHIp42GDF"
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
