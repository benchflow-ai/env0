#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (greenfieldhq.com).
INTERNAL="@greenfieldhq.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1W6SWfXenI0j1KT3xnzIGd8BDozzcS9T8HjnewJA85JW"
  "1ML5149Xv6Y58YwzpbnG23ceTLsJhZPjwkGn9neNw5ni"
  "1bFf9TVAIW7B1DwaKqj0o6FCyRPO6dJhL3VUDruLxoi4"
  "1352DLVBsd8LwjCUQFx44mJLOAFEmOMtzB6Q0JAtbGcA"
  "17DR7BWodSfPFKg9yN14SSQUVZv543YJERviAxXiVPJt"
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
