#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1Ia12VAbIDHzzYYVLGsa7ztBinoLg9ZN9Pmy0jsSSzcc"
  "14u6LBykSFtSRjGnmIAzQGXdT3XxqKn0GwFCwkPtnd2x"
  "1fYn5nvjCrUrJyYsE9Ddmqoy0FVmhZxtYrQOFW7z6R4i"
  "1LgzXW9KATcdcKtg4tiztk1XLMzHynjWv4BiGVlxcdWj"
  "13NCz7IxVxL52pP9ELkEvbND9pd676BEt8uiJCNa8W4z"
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
