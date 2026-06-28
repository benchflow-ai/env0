#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1tKhPASU79znzxQSzAshj4Y4stXQPFbNlkvc0OKLBP40"
  "17gH1QuZJyIbx0wAgw42WrAXpmnzi2zbRNRfx2e8tnwF"
  "1HrfES6tJY2x1muZIoy2M010cYNB9t4bdsZsZQ1JKZB1"
  "1eCJjXjee4Ggd5vMR7123qVoPg7Rj8ioRQWgQ4LL3KV7"
  "1Jfg7INUJzj6T4Y3687jehyBbTLpEZZ41hTkFiEMK17J"
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
