#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1T1GOFdvVYaOWE0L2PcJid95oNE8j1Br5Uqip9HjLHTa"
  "1IomeR0DAtjgRkZpvATgYtOEl4M8gZtVz7SWIQTbyybd"
  "1MOXrrPRj5fueYwz91uPzLyrcZYuIawTjhBpDLthwCv7"
  "1Pdq9P91GKtPJiJlDVxjWI6Wz5yTpn6ndXlbF1jmDOBN"
  "1LZyBZOYIC50uiE50cByLjEyvvqSJsmmq8DpMTyeAxcL"
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
