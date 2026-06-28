#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (foundrylabs.co).
INTERNAL="@foundrylabs.co"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1MhoBzFFi6Y1aUQSCgWlFOVKMvjr4bpg1CnpUVRN2ir9"
  "1RzGd6f9Zu7AWFten44l5SeqcQJdvvwgapCF0Z4HI9PZ"
  "10WhPk4j8xXVdCQX3Us2fXv5cG6Nfw8wgXmdonsuFOj3"
  "15TAAOpcgfnlm52dMwbj8qCFUnLdgpvDWtKCla9NrfXn"
  "12VRnVSiSqxmjHG2IPaiUL7xrh423bX72I5pCEQSJtvE"
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
