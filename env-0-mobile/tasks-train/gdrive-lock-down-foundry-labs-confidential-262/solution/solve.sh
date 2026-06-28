#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "10mRUjK0Ug3KJF3ylIMHKveH4P0Hyf7OADmUsS9ibs5k"
  "1qtHrxfDpPu2ho3LJF7lFosm0nzhssYj4Z3ZMXz0Hdx2"
  "1APBRjjOEsg7AURHRIGi6unDITfV3uwyIGnYjDaaxNeb"
  "13JubBIsz8vN9bptiYgLzRjCnuK0k6H3mO57hJglT4aq"
  "1nXH4pZTivczurcWm9dNLSoEnAoy95Ba4NuoFEpeN9wn"
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
