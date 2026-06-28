#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1C83FWfOAAO1LpMA7iziW67RzvJ2HbUYyIack9tVUmMp"
  "1txeI7wluOXJ0Jf9beWnXwa0EknYlZyRKpVc1uwSNeBj"
  "1pZNI9CnXHK5gli3ZnoZoQJ3fAfemwg836XXyXagqTs1"
  "1aJpA1ryT6Qdq1eZXJHawcIIfB7ItlQJjt1bFhYLWetz"
  "1P7Zjt5h37MBXdQK92KcubrMbxfCA6bzyughBAsyd8RP"
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
