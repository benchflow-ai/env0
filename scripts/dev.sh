#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTROL="$ROOT/scripts/env0_control.py"

usage() {
  cat <<'EOF'
Usage:
  dev.sh
  dev.sh task <name>

Internal control contract:
  scripts/env0_control.py --dry-run start-default [--devhub]
  scripts/env0_control.py --dry-run start-task [--devhub] <name>
  scripts/env0_control.py seed-default [service...]
  scripts/env0_control.py seed-task <name> [service...]
  scripts/env0_control.py reset [service...]
  scripts/env0_control.py snapshot <name> [service...]
  scripts/env0_control.py restore <name> [service...]
EOF
}

if [[ $# -eq 0 ]]; then
  exec python3 "$CONTROL" start-default --devhub
fi

case "${1:-}" in
  task)
    if [[ $# -ne 2 ]]; then
      usage >&2
      exit 2
    fi
    exec python3 "$CONTROL" start-task --devhub "$2"
    ;;
  -h|--help|help)
    usage
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac
