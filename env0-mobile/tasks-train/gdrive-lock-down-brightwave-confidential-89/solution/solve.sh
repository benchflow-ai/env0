#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1YGdQb9Cr33ly9XGXwAYXMQnhkMvOnDMVoitfoty6SRX"
  "12n0E6U5XpN2jdE2KMjhJ1fiYXpDMv7XqdLnG7wn7wqP"
  "1suuNA8FDRwxHfYd3KoUu6upgJ4TElPNmh2EaS1Ko1k9"
  "1ZfBj2N5rcyAL54FB6Tju3qpezLzbCTEddotu8sr4viP"
  "1g1gBBzLtGQIjIfEwGYVYBms5BMU0yliFFEOmHVyHb2s"
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
