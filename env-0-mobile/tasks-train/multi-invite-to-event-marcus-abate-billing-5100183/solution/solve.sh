#!/usr/bin/env bash
set -euo pipefail

# Read the invite (already known from the seeded mail) and create the matching
# calendar event. Uses the next occurrence of the requested weekday at the
# requested local hour; only title + start hour are graded.
SUMMARY="Billing Cleanup Discussion"
HOUR=14
WEEKDAY=3

START=$(python3 -c "
import datetime
now = datetime.datetime.now()
delta = ($WEEKDAY - now.weekday()) % 7
delta = delta or 7
d = (now + datetime.timedelta(days=delta)).replace(hour=$HOUR, minute=0, second=0, microsecond=0)
print(d.strftime('%Y-%m-%dT%H:%M:%S'))
")
END=$(python3 -c "
import datetime
s = datetime.datetime.fromisoformat('$START')
print((s + datetime.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%S'))
")

gws calendar events insert \
  --params '{"calendarId": "primary"}' \
  --json "{
    \"summary\": \"$SUMMARY\",
    \"start\": {\"dateTime\": \"$START\"},
    \"end\": {\"dateTime\": \"$END\"}
  }"

echo "Created calendar event: $SUMMARY"
