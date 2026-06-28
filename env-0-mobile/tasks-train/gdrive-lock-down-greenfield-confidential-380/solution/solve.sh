#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1PoQKUt8CWj0MvOUN5LVPaz2CMoQpoyypdYu1k2kWrD7"
  "1wlga0jtl9CB3p6EpOqxq7RwxQmXm4vSa7tgzgBcPiAC"
  "1jZwjwSwZJaRYNcmQwkpfH5UJAZ0ps2OGQgU9fXATAdW"
  "1Yrh0ckBhSb6T77xPI5pc112Zv1e8wI5n1zCUkU4YqJT"
  "1kPkTyh4yMSv3TTBkzEHNwYrO2cqe51DRQ2rpwUFr50v"
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
