#!/bin/sh
# gws wrapper: routes gws service names to canonical MOCK_*_URL env vars.
#
# Each `gws <service> ...` invocation targets one service. This wrapper maps
# the gws service name to the correct canonical env var, checks the explicit
# health endpoint, then sets GOOGLE_WORKSPACE_CLI_API_BASE_URL for that call.
#
# Mapping:
#   gws gmail    -> MOCK_GMAIL_URL    -> http://localhost:9001
#   gws calendar -> MOCK_GCAL_URL     -> http://localhost:9002
#   gws docs     -> MOCK_GDOC_URL     -> http://localhost:9004
#   gws drive    -> MOCK_GDRIVE_URL   -> http://localhost:9003
#   gws slack    -> MOCK_SLACK_URL    -> http://localhost:9005
# Falls through to GOOGLE_WORKSPACE_CLI_API_BASE_URL if no per-service var is set.

BUNDLED_CACHE_DIR="${GWS_DISCOVERY_CACHE_DIR:-/opt/env0/gws-discovery-cache}"

SERVICE="$1"

if [ -n "$SERVICE" ]; then
    case "$SERVICE" in
        gmail) VAR="MOCK_GMAIL_URL"; DISCOVERY_CACHE="gmail_v1.json" ;;
        calendar) VAR="MOCK_GCAL_URL"; DISCOVERY_CACHE="calendar_v3.json" ;;
        docs) VAR="MOCK_GDOC_URL"; DISCOVERY_CACHE="docs_v1.json" ;;
        drive) VAR="MOCK_GDRIVE_URL"; DISCOVERY_CACHE="drive_v3.json" ;;
        slack) VAR="MOCK_SLACK_URL"; DISCOVERY_CACHE="" ;;
        *) VAR="" ;;
    esac

    if [ -n "$VAR" ]; then
        eval URL="\$$VAR"
    else
        URL=""
    fi
    if [ -n "${DISCOVERY_CACHE:-}" ] && [ -f "$BUNDLED_CACHE_DIR/$DISCOVERY_CACHE" ]; then
        HOME_DIR="${HOME:-/tmp}"
        CONFIG_DIR="${GOOGLE_WORKSPACE_CLI_CONFIG_DIR:-$HOME_DIR/.config/gws}"
        mkdir -p "$CONFIG_DIR/cache"
        cp "$BUNDLED_CACHE_DIR/$DISCOVERY_CACHE" "$CONFIG_DIR/cache/$DISCOVERY_CACHE"
        # gws treats discovery cache entries older than 24h as stale.
        touch "$CONFIG_DIR/cache/$DISCOVERY_CACHE" 2>/dev/null || true
    fi

    if [ -n "$URL" ]; then
        HEALTH_URL="${URL%/}/health"
        if ! curl -sf --max-time 1 -o /dev/null "$HEALTH_URL" 2>/dev/null; then
            echo "error: $SERVICE service is not running at ${URL}." >&2
            exit 1
        fi
        export GOOGLE_WORKSPACE_CLI_API_BASE_URL="$URL"
    fi
fi

exec gws-bin "$@"
