#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1RXo5b1zyXziFAZQr4f7dmCvuuXwXXpUFhs2hioICB4O"
  "1FOoNO1mTIjXpNf2gVD9exqqfQqZSlwEAbqT1QFrHL5j"
  "1tYv81MoN1X9weMOtQAN3hDzvtGKyARtEfIqghw2bW5k"
  "1M16YcfDaONZp5EPYSWjaJyPJLL5PuKkiU7K5VLUXwVS"
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
