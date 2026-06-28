#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1BM1hmBRtA87r7y1SYADilfFMRFw0RSMuLVQHFGZjtLr"
  "1rA1634NagmfD7cmKTzrj5YKJWfAZgp1hEFmQc7ygIMd"
  "10MAtPJfiYKChduZ6nl9mznmcmWc8SLAjgDBHwTYcJzR"
  "1WP7z25hvH3xLWugikC8KkQyWamA0cFXw0jNwAS38CE9"
  "1wf4YolzU2bPKqC6T1qyCP38wt6tnpDJJEndy2lkZRL9"
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
