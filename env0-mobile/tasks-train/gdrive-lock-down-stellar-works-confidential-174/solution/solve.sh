#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (stellarworks.io).
INTERNAL="@stellarworks.io"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1tcyenm7TmWbMpvAIkcRLyKdPNFgqBBuqGXLX0WTNUwj"
  "1IcRIHs9TJWnRKOD5KvufowKbXWCVIzenR6m4G5sDTX7"
  "11MjsyEaMGOv4De4WGOD2xVuHvWjADqC0araYFRNghLZ"
  "11ZAzKVVAgWbKesKlovHTz4OXotJDKveoJAuERbMMXJS"
  "1FlhZZTdvnTR7E1sLm62I4v4PwBFHdZ96Q8WdLPR9adm"
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
