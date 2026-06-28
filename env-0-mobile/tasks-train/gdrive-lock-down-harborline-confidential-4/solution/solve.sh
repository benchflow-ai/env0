#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (harborline.com).
INTERNAL="@harborline.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1LA1ipW0xd5uWggfpqNKenURXQMGAUeT8SJaEo379NdR"
  "1rDCLjVEj8vFIhCjTUhEkDIdW19cTk2u3bMHjBcb97m6"
  "1YwK3vFQq1q9Uex8YXoocTm9CJ0qK9lm8MdXPgpGqyzS"
  "1j28dPkLmDY9r3hVIrj27INrnIo3qLRTHazkSRgPWn8K"
  "1ijn8DfNLn8lOnY6GaXCKwdqU51fMoJy7p004EMjTWwS"
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
