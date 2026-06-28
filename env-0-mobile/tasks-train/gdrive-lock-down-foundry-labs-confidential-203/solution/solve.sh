#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1G2BLnNk97Yec38gc3kVftDKQqGhnPtN7inAHxNrASdL"
  "1zflEw2w9JjZAoPQY7DkVE7bqi0x7LSA0i1qkZJtI8bh"
  "10Ctr8ysowS9KzErUX6CtA6CSngkMKIFPgyYVtliR7EO"
  "1NLttIay2JvcwWDttm39DopkfgLQh5FVAEYkuWz2iHpx"
  "1HeYuMY0Cpo3ZVXvS5SommJNOcO6iL0q1sAHuEee00go"
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
