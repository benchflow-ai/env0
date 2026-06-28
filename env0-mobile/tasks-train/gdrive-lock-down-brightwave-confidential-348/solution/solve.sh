#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1nUO8uw0w8KxBK1XpYfXE90AQrqaE6gdFYdGfnJGCwmI"
  "1DGlx5wspAMTsPWCx8DLP6ia7mjOB0SaMO3igaz7e6x1"
  "11m2UMj3Ya01lyiL75V51TLnGPa8tjwGUU6JG8xQnHSY"
  "1ARWlACewdH3G2DWqF61OBBrzs6mHLaeGqwXDjrJPd4u"
  "1NXe2xLaeQSBbty7mgQa5ujfG2QWv8H0BEarg26eFap2"
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
