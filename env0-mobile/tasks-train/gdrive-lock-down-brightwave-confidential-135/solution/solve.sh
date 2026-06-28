#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1GpR7ywvKu8Nthiuyk1VmlLxMHE2Q4nHIXoZxcZ77tIJ"
  "1miv3Buqi0uMpyr32JakUIEfFlfDfa6wxhyas0BebnCp"
  "1EAs4jejYIR8Pe91oPO1zEkScgr8xDSnMhIQKXbcItV3"
  "1a3zM8jLEORRtJ30ry0OrWbVO4aZijcdmx6mypYSK2e8"
  "1F1U2xKOCliLwLQm1mexMT7N3yekC0bDsGGdVyFtNJhh"
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
