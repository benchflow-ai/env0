#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1QW4MqVI7Zbs1YnNHP5hmxJdgIj7WPYZqEfMjHx7lRQt"
  "14PKMlncvZ6jIbhRfiGzfdyTX1gXUNJDThhMMyfwdgvj"
  "1dtgQmJ6FtlZTNZ5hT2BzgZvwlHW06YzFfHaC1Yxlacy"
  "1dORHFObzlDREhBUT3DHVdugWn7vQzD08iUqbNtjbkxp"
  "1nQWlXlxgN6pt8NTa9f4drHPnNvXnGc9hG0aE8luhbEU"
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
