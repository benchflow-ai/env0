#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "19TLLGvmGeRKisSvRla0Y4Oy5n8lSZ16MAYGkCseC99a"
  "1b6dhqDl5ygi84a4HGhyy6Cogs1pfPw405bFN9dHsqPr"
  "1DQhEwz68nt5kFAcgoGGJ6gzSZpIKEewvoimRyZdUZxP"
  "1cCwBK2oqH4eh2aY8cRQPrnNi2lnO4A2OPATw5JwxZhh"
  "1ahWUtjRXdiU5KBGDcimmdcRluFTFmeVV7ilJ2XeRYMm"
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
