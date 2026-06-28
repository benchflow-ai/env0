#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1MG3czN7O6IJk4Zuq4GtGn3TydCDcR28COn8Ieh8ESMP"
  "1ho9UOYX5fd5eUNrWhC5ArG3knH5TVRT7Kht3w89CQzO"
  "1gjcpM6CjcS9xdkd0jn2H7vHUsxl6qS9KE3mI0ZNLPaj"
  "1IfCrt3rUpQXxYWatHTZjdyEdIgMjyIlKapbHpTU2qXI"
  "1aN3WHAW5GeUHIe7GfE6LRhLdHAjoZuAD5Q07xRlCgpu"
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
