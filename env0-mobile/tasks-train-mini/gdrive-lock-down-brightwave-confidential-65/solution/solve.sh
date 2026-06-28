#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1lfhvEg40hPFSQnRmVbGNCy4dcUQmGjT5AXhMHKHlptI"
  "15qTPY2t9Lmnr2BQFXCyl7V0cJSZOBvtMQtiPfm27oNh"
  "1J9zs1ESNYJmj1bgPBpmgp8HPPWpv4A0DhOmXn6w3ObY"
  "1bvmODwVtoPOeQo1pZ1cQgF1C8HSX6XAIrjQrKsf1LAR"
  "1Kj8XzAvqn2MkHiaO7rIbGoAJsP5CNvMOUJEKqwD8Yl1"
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
