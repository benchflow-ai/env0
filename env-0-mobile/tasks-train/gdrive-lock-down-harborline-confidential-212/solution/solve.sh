#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1LYeYqi8FjcF71x1j8btA2AvDyuShIHfyZbxJJEwfQhv"
  "1vz6M8pwJGdYjusUSnsprwh2WC0IH5TXJ0U7CbOW97U2"
  "1JSOHIXwDsji73acsCxnqQOZxclBSxIFBpzZGDjc3SKu"
  "13AF7KYNtdMOhwiNR8Dm7GE85sKVQ2X5MhdRiXz1U8Dd"
  "1ip6IHrCamqONznsJxpv7GXK9puFHFhoj6OUeTm0Opyz"
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
