#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1DR5L1BuiDgTi1LLKkw4050TMpxPU56AyOZZLtfyjWi8"
  "1dTij5S7uU5ODDSSbzH1cSRDjsSatmc7nxyf6VSiame2"
  "1Ethz8WQ0na46ymfHt0Hi67Z1wCDd4DPgYxQjgr6Znc5"
  "14hDysr4sKjzD7JqVFW6qdQ5c0HZ1QNiEyeYk1ddW2Lz"
  "1im278w4uHCgRUocMfUQlRFUlA4dpM7i4ZIIHoP40SbN"
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
