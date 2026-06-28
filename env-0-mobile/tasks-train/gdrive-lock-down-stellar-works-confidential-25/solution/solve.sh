#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1ZgbSw56vlB6gNjg101XG3klHvowE1Ln1g1RUktgGHZS"
  "1epG8DbVYWn6rY422gFV50KVN7iMFvCheAEFN1Zh230k"
  "1ZBN5FVnclSi5VafOOpwVHVmvMoBrpsK1nAyNl4MMd6E"
  "1EdY8NXTGm5YSEvBsn9bqERglwTTyTgqBvEkSW0rXYgg"
  "1K60AdwPa7HnQEczP7DFdmOSyK47AdxxwEWiopuY5tcO"
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
