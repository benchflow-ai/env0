#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1fW2qLtg1NRYpZPiyEYu07ktMLHr0lUT012bNZ621vev"
  "1VscxIlTHK7Vfl3DKJ7ijuXdpXze5o4yQ14gob4XTxez"
  "1mhIrvGZglSfC6OONKISG4RX6fYHlxkfaBDYfTGFtp2I"
  "1vuucK96NBD2FpDJ3fEV6mSpl97kzwvh6OieM4COogfa"
  "1tzGVqqKP2PfZw7766dmbZAMRZCzRZyHgL3oay5flY9K"
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
