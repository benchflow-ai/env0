#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1qqER4T5qgNBLl5zJrzYXkm9I5Pwbs7DFEtKQ7QFW7Ow"
  "1kIn5zt74s9yc3t6DEJ3lhZUUOYG1cQOUC2FTfXoQ0Nx"
  "1pIGJUFjmPsem0VsewP8BzVpIgkSehYOdzejPCgqlmVw"
  "1kJghoNoBTjih31FW4vT4dppTsvjsmdq0maWQ4DvdwEJ"
  "1sRyQReGIR9gcpkSO35L4NroTzwJNpQQr0wodSGc7zAT"
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
