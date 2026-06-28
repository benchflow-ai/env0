#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1ttm9otHjiIiNdYryrybQPrfsRcuiaOivyOjDAJxe9mz"
  "1FUO7b6tU2epQitJ6ct5GuVid0Xg3TDHou6JUepZDjQO"
  "1b72D9jm5O3wGkD2Y44ceUOKiOpIPeeI021JA6xtLNkU"
  "1TSoCJanebQNBRnNaCN1jL1HkT5aVRKTLPHha78L3kc8"
  "1qiQUl0SYZ5QOklvqV0oIgK56BqMvduBWjACefnjBnZQ"
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
