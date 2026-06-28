#!/usr/bin/env bash
# Oracle: revoke the over-permissioned app for user1 via the admin API,
# leaving every other connected app untouched.
set -euo pipefail

AUTH="${AUTH_URL:-http://localhost:9000}"
USER="user1"
TARGET="formfiller-1100003"

echo "== Inspect connected apps =="
curl -s "$AUTH/_admin/clients?user_id=$USER" || true
echo

echo "== Revoke every scope held by $TARGET =="
for scope in gmail.full drive.full; do
  curl -s -X POST "$AUTH/_admin/revoke_scope" \
    -H 'Content-Type: application/json' \
    -d "{\"user_id\": \"$USER\", \"client_id\": \"$TARGET\", \"scope\": \"$scope\"}"
  echo
done

echo "Revoked all access for $TARGET on user $USER."
