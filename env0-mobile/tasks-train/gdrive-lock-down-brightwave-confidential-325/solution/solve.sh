#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1OnX5eqevM95pDtyEmTRRzHWFRwlgL1TLpLQKvO1HFlI"
  "1oGlv3aO0D3Zfd8lpfx8oAvzEWf9jLCyYjq9JLyuBgfk"
  "1QPz4qTUscPrUHeJJZ89E3eNTyFJdr24nDDZUcfw8NRX"
  "1zfymy8vDwOmGLFeeEBOKXsyDx9cYjhoT4FRyuo1aVjD"
  "1KS52RD6s86RuSss9Iek8npRU2tKIw8dKtFOwbKGRCGO"
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
