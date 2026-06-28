#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1vCdnR2gLYEuNIyUpzAsMF4ZdlcEgkfIomOU9L2N4dXG"
  "1jow31JUmgqCpWo3aQiWXsqCMvOMNZVM3g8VE8mAOyv3"
  "1RuCKtGauY8leALFAsnYXwDEHmVADpBVhHKq4vFFW0je"
  "1XMEZKqtOFcG8tek4Fi8wU95e6wdKvblyrkqxD0tDkFo"
  "1STVa68IbH5tlAhN6ykdJaN0dLKnPr4VAh57JmJgtxfU"
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
