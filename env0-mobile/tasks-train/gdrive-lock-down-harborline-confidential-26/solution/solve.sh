#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1L7m8LUlUmtwLxSWzvOmXCtS65jvJOwOgf7Cm7Rbb3e3"
  "1D0Zs7z6Cn9ai1R2bW9ho504P4iRQYZyXNa3ZzpWicVs"
  "1bA1HrfL2rZU3kHQVO3XEtyHRVYEtl9QGi0tplThIya8"
  "1Vf5gcLXbCQkkrtTQvuVqlzMoJ2CF5B2mBPpEvI1HBok"
  "1sSldaXHzhqat76NukamP4rsIxk5Zbi0roLem4KhI8Lg"
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
