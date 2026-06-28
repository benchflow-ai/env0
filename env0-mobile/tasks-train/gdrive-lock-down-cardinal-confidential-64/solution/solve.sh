#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1QvHKybBR54G2SuCKWIXu0Blp8sA77vwUdkj6bokJRNT"
  "1Pi7QmUikntiJL3DMaDPqEhvIx6uaGVYSPTmih9UdyOE"
  "1KaxZaKd0ifl0ivNsn7aETCKmXKyT0NTOD6FEQEWLMY8"
  "1lOg0lFdPhYLJXbfY4LU9DAf8xODgkCDELI5Qld5n3VS"
  "1ogfSLtBkx3YP4VFbg4AcHgm1zh2riIk1jbQqYq6FDsd"
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
