#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "17SPtv8NWmvaznIpinNKVa3kJf48FuxdhqafyZ6yryh6"
  "1FfAshrc49l1te16S07nPxLg36yoYqGH39jAEmafp7IV"
  "1Crv2pxYWYRzUo7UO5y3BXpXcL1mNteQXDK3FBoddcK1"
  "12kyFQBq2YPS0cg2Sqq2JtTLaG3Unv9TpB03PCyT9abg"
  "1XbGh1S4QvOnDRw1YRSiUTkc1IpE27rRe92qE9Ufhdx8"
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
