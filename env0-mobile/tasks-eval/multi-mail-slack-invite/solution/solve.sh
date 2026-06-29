#!/usr/bin/env bash
# Oracle solution for multi-mail-slack-invite.
#
# Strategy:
#   1. Create three SkillsBench difficulty channels.
#   2. For each contributor, look up their Slack user by (canonical) email
#      and invite them to every channel matching their tasks' difficulty.
#
# Difficulty thresholds:
#   easy   → estimated time < 100 min
#   medium → 100 ≤ estimated time < 500 min
#   hard   → estimated time ≥ 500 min
#
# Note: contributors with tasks in multiple buckets appear in multiple channels.

set -euo pipefail

GMAIL="${GMAIL_URL:-http://localhost:9001}"
BASE="${SLACK_URL:-http://localhost:9002}"
BOT="Authorization: Bearer ${SLACK_BOT_TOKEN:-mock-bot-token}"
WS="X-Mock-Slack-Workspace: workspace_001"

# ---------------------------------------------------------------------------
# 0. Read all SkillsBench emails from Gmail (satisfies Gmail scoring component)
# ---------------------------------------------------------------------------
echo "==> Reading SkillsBench contributor emails from Gmail..."
MSG_IDS=$(curl -sf \
  "$GMAIL/gmail/v1/users/me/messages?q=subject%3A%5BSkillsBench%5D&maxResults=100" \
  | python3 -c "import sys,json; [print(m['id']) for m in json.load(sys.stdin).get('messages',[])]")

for mid in $MSG_IDS; do
  curl -sf "$GMAIL/gmail/v1/users/me/messages/$mid" > /dev/null
done
echo "    read $(echo "$MSG_IDS" | grep -c .) email(s)"

# ---------------------------------------------------------------------------
# Helper: create a channel and return its ID
# ---------------------------------------------------------------------------
create_channel() {
  curl -sf -X POST -H "$BOT" -H "$WS" -H "Content-Type: application/json" \
    "$BASE/api/conversations.create" \
    -d "{\"name\": \"$1\"}" \
    | python3 -c "import sys,json; print(json.load(sys.stdin).get('channel',{}).get('id',''))"
}

# ---------------------------------------------------------------------------
# Helper: look up a Slack user ID by email
# ---------------------------------------------------------------------------
lookup_user() {
  local encoded
  encoded=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote('$1'))")
  curl -sf -H "$BOT" -H "$WS" \
    "$BASE/api/users.lookupByEmail?email=$encoded" \
    | python3 -c "import sys,json; print(json.load(sys.stdin).get('user',{}).get('id',''))"
}

# ---------------------------------------------------------------------------
# Helper: invite a contributor (by email) to a channel
# ---------------------------------------------------------------------------
invite_contributor() {
  local email="$1"
  local ch_id="$2"
  local uid
  uid=$(lookup_user "$email")
  if [ -n "$uid" ]; then
    curl -sf -X POST -H "$BOT" -H "$WS" -H "Content-Type: application/json" \
      "$BASE/api/conversations.invite" \
      -d "{\"channel\": \"$ch_id\", \"users\": \"$uid\"}" > /dev/null
    echo "    invited $email → $ch_id"
  else
    echo "    WARNING: user not found for $email"
  fi
}

# ---------------------------------------------------------------------------
# 1. Create the three difficulty channels
# ---------------------------------------------------------------------------
echo "==> Creating SkillsBench channels..."
EASY_ID=$(create_channel   "skillsbench_task_easy")
MEDIUM_ID=$(create_channel "skillsbench_task_medium")
HARD_ID=$(create_channel   "skillsbench_task_hard")
echo "    easy:   $EASY_ID"
echo "    medium: $MEDIUM_ID"
echo "    hard:   $HARD_ID"

# ---------------------------------------------------------------------------
# 2. Invite contributors
#    Each contributor is invited to every channel where they have tasks.
#    Source: answer_easy.csv / answer_medium.csv / answer_hard.csv
# ---------------------------------------------------------------------------

echo "==> Inviting easy   (< 100 min) contributors..."
invite_contributor "marcushill@gmail.com"              "$EASY_ID"  # Marcus Hill
invite_contributor "alex.thompson@gmail.com"           "$EASY_ID"  # Alex Thompson
invite_contributor "kevin.brown91@gmail.com"           "$EASY_ID"  # Kevin Brown
invite_contributor "chris.taylor@gmail.com"            "$EASY_ID"  # Chris Taylor
invite_contributor "sophia.johnson@gmail.com"          "$EASY_ID"  # Sophia Johnson
invite_contributor "laura.williams@gmail.com"          "$EASY_ID"  # Laura Williams
invite_contributor "sam.cohen@gmail.com"               "$EASY_ID"  # Sam Cohen
invite_contributor "eric.foster@gmail.com"             "$EASY_ID"  # Eric Foster
invite_contributor "brianha@stanford.edu"              "$EASY_ID"  # Brian Harrison
invite_contributor "nwatson@gmail.com"                 "$EASY_ID"  # Nicole Watson
invite_contributor "adavis169@gmail.com"               "$EASY_ID"  # Amy Davis
invite_contributor "frank.stevens@oxford.ac.uk"        "$EASY_ID"  # Frank Stevens
invite_contributor "lchen@company.ai"                  "$EASY_ID"  # Lisa Chen
invite_contributor "jwhite0227@gmail.com"              "$EASY_ID"  # Jennifer White
invite_contributor "pgreen@outlook.com"                "$EASY_ID"  # Patrick Green
invite_contributor "akim.cs@gmail.com"                 "$EASY_ID"  # Andrew Kim
invite_contributor "mthompson@ucsd.edu"                "$EASY_ID"  # Mark Thompson
invite_contributor "afoster@duke.edu"                  "$EASY_ID"  # Amanda Foster
invite_contributor "pzhang@bu.edu"                     "$EASY_ID"  # Paul Zhang
invite_contributor "ivan.lee@columbia.edu"             "$EASY_ID"  # Ivan Lee
invite_contributor "olivia.martinez@gmail.com"         "$EASY_ID"  # Olivia Martinez
invite_contributor "derek.wu@mit.edu"                  "$EASY_ID"  # Derek Wu
invite_contributor "carlos.rivera@gatech.edu"          "$EASY_ID"  # Carlos Rivera

echo "==> Inviting medium (100–500 min) contributors..."
invite_contributor "alex.thompson@gmail.com"           "$MEDIUM_ID"  # Alex Thompson
invite_contributor "michael.chen88@gmail.com"          "$MEDIUM_ID"  # Michael Chen
invite_contributor "david.park@gmail.com"              "$MEDIUM_ID"  # David Park
invite_contributor "james.wilson@gmail.com"            "$MEDIUM_ID"  # James Wilson
invite_contributor "emily.rodriguez@gmail.com"         "$MEDIUM_ID"  # Emily Rodriguez
invite_contributor "sophia.johnson@gmail.com"          "$MEDIUM_ID"  # Sophia Johnson
invite_contributor "tsmith@gmail.com"                  "$MEDIUM_ID"  # Tom Smith
invite_contributor "nclark.dev@gmail.com"              "$MEDIUM_ID"  # Nathan Clark
invite_contributor "peter.jackson@rutgers.edu"         "$MEDIUM_ID"  # Peter Jackson
invite_contributor "eric.foster@gmail.com"             "$MEDIUM_ID"  # Eric Foster
invite_contributor "clanderson19@gmail.com"            "$MEDIUM_ID"  # Claire Anderson
invite_contributor "brianha@stanford.edu"              "$MEDIUM_ID"  # Brian Harrison
invite_contributor "adavis169@gmail.com"               "$MEDIUM_ID"  # Amy Davis
invite_contributor "smoore@gmail.com"                  "$MEDIUM_ID"  # Sandra Moore
invite_contributor "akim.cs@gmail.com"                 "$MEDIUM_ID"  # Andrew Kim
invite_contributor "tina.chang@gmail.com"              "$MEDIUM_ID"  # Tina Chang
invite_contributor "jreed@usc.edu"                     "$MEDIUM_ID"  # Jason Reed
invite_contributor "pzhang@bu.edu"                     "$MEDIUM_ID"  # Paul Zhang
invite_contributor "ivan.lee@columbia.edu"             "$MEDIUM_ID"  # Ivan Lee
invite_contributor "olivia.martinez@gmail.com"         "$MEDIUM_ID"  # Olivia Martinez
invite_contributor "hannah.park@gmail.com"             "$MEDIUM_ID"  # Hannah Park

echo "==> Inviting hard   (> 500 min) contributors..."
invite_contributor "ryan.martinez@gmail.com"           "$HARD_ID"  # Ryan Martinez
invite_contributor "daniel.lee@gmail.com"              "$HARD_ID"  # Daniel Lee
invite_contributor "sam.cohen@gmail.com"               "$HARD_ID"  # Sam Cohen
invite_contributor "peter.jackson@rutgers.edu"         "$HARD_ID"  # Peter Jackson
invite_contributor "eric.foster@gmail.com"             "$HARD_ID"  # Eric Foster
invite_contributor "vincent.miller.9701@gmail.com"     "$HARD_ID"  # Vincent Miller
invite_contributor "robert.chen111@gmail.com"          "$HARD_ID"  # Robert Chen
invite_contributor "pzhang@bu.edu"                     "$HARD_ID"  # Paul Zhang
invite_contributor "rkim@andrew.cmu.edu"               "$HARD_ID"  # Rachel Kim
invite_contributor "carlos.rivera@gatech.edu"          "$HARD_ID"  # Carlos Rivera

echo "==> Done."
