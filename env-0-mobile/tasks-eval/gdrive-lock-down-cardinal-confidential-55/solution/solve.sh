#!/usr/bin/env bash
set -euo pipefail

# Revoke the oversharing permission on each sensitive file. We resolve the
# offending permission per file: any "anyone" share, or any user share whose
# email is outside the internal domain (cardinaldata.com).
INTERNAL="@cardinaldata.com"

# Sensitive file ids (baked at seed time).
FILE_IDS=(
  "1TvbfU56IChEFcU8rtVhqHTg9uTD1P7XP4nMiG3tz6s2"
  "1yPDg9mAAX5sO3IDA3c4M3VuiFhoopOvC0obAIatVRIS"
  "14uROq97Sptvddu9ocGtZGJaW27fc69l6108hj4gt6hJ"
  "17MUN9UpsDLoX55rnXi0M7g9jZCgMXxIf2JTDzL7p148"
  "1nbZuaQ6EufPO551SrfhaDmEnSriQUqbHS3pxjncFHvd"
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
