#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1it241GxgldmFlild9X0oXrpnJtRZTJCeq3ivGTz5ya9"
  "1tciZP3A6u8bJGeLDizgpf1rIneWHi67HUnC3dMMjpRu"
  "13n7ut8RGnhdL82sc8GEYAbvzBzQhomqY2j0kfJyvaJo"
  "1mtUZLf124xdxVFHx26nFv1b7iPVCiPQKQdODQqAheQc"
  "1Kroem6r5B99KP7CBZjKche5dQUr0ios6htXd0CwRWkl"
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
