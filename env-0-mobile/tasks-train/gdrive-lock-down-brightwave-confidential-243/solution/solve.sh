#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (brightwave.io).
INTERNAL="@brightwave.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1XzmVKyXNrr8bm6WBi086dKdkAX02dSmwmAnVF6PQAe6"
  "1fqGCNtvziMoZSvmLvaNxadJQ1CCfLJ4a7z5j3KgGLd4"
  "1xmpje0JCxs0RrA3nJeVYQo3QHrY6v4FeJx88s9FaWuw"
  "1Go8n8VR0qZ873cSCCudM4cJIjbnR5FVtly6k4jk3ZRJ"
  "1Roxm0aSePbuWmsK4M3yAURl24RhR3FJkcB5xUjZK3F1"
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
