#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1KIXpdTbGNsE5DijMlDbzpIf8qDAfzHiDYJduBhAMM2p"
  "1txNCRi8ElnpGCx0DmyW5Cur8JGgD15wjgtogfRFFwlG"
  "17wab0ZO6FCmncmAz17nhLt614MczWeEzyBAdS2hKTgt"
  "14vmwiAPaG5cuTJepRzom2fcrgmItlMpdXS2N11h4fPD"
  "1xMzgIBnXvUoHcc8zS2FPyWwU797dqYnKvfSKqPQjv31"
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
