#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1YVXlJXd33FWBPGn0U29pwr7lnyLKohfdjojPChetHh9"
  "1fcplPT3YpeHSpx72FTPg3C0drpnDBAhqglHOrPb5k9T"
  "1Q29rm2p7UwJ392E4cBWqN8HsiYJeZLngMgJ8wJi6nQn"
  "1iZbVsycN0sgmixr7BRwyCf4mj8VGKXoaSIADLBxmaxt"
  "1ndOY3gjDUUqULSfop5IIUvkt8rxffkl3IWPflHL0Tbr"
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
