#!/usr/bin/env bash
# Unified fixture capture + conformance validation for all env0 environments.
#
# Thin orchestrator that calls each environment's capture_fixtures.py and
# conformance tests, then generates a combined parity report.
#
# Usage:
#   scripts/capture-and-validate.sh              # validate only (uses existing fixtures)
#   scripts/capture-and-validate.sh --capture     # re-capture fixtures then validate
#   scripts/capture-and-validate.sh --report      # just print the parity report
#
# Prerequisites for --capture:
#   Google (Gmail, GCal, GDocs, GDrive):
#     Place OAuth token at packages/environments/mock-{gmail,gcal,gdoc,gdrive}/scripts/token.json
#     Run each env's auth script first: python scripts/gmail_auth.py (etc.)
#
#   Slack:
#     Place tokens at packages/environments/mock-slack/scripts/slack_token.json
#     Run: python scripts/slack_auth.py
#
# Output:
#   .local/parity-report.json   — machine-readable parity report
#   stdout                      — human-readable summary

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPORT_DIR="$REPO_ROOT/.local"
REPORT_FILE="$REPORT_DIR/parity-report.json"
DO_CAPTURE=false
REPORT_ONLY=false
export REPO_ROOT REPORT_FILE

for arg in "$@"; do
    case "$arg" in
        --capture) DO_CAPTURE=true ;;
        --report)  REPORT_ONLY=true ;;
        --help|-h)
            echo "Usage: $0 [--capture] [--report]"
            echo "  --capture   Re-capture fixtures from real APIs before validating"
            echo "  --report    Only print the parity report (skip tests)"
            exit 0
            ;;
    esac
done

ENVS=(mock-gmail mock-gcal mock-gdoc mock-gdrive mock-slack)
ENV_DIRS=()
for env in "${ENVS[@]}"; do
    ENV_DIRS+=("$REPO_ROOT/packages/environments/$env")
done

mkdir -p "$REPORT_DIR"

# ─── Colors ──────────────────────────────────────────────────────────────
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m'

# ─── Phase 1: Capture (optional) ────────────────────────────────────────
if $DO_CAPTURE; then
    echo "═══════════════════════════════════════"
    echo "  Phase 1: Capturing real API fixtures"
    echo "═══════════════════════════════════════"
    echo ""

    for i in "${!ENVS[@]}"; do
        env="${ENVS[$i]}"
        dir="${ENV_DIRS[$i]}"
        capture_script="$dir/scripts/capture_fixtures.py"

        if [ ! -f "$capture_script" ]; then
            echo -e "  ${YELLOW}SKIP${NC} $env — no capture script"
            continue
        fi

        echo -n "  Capturing $env... "

        # Check for credentials (env-local scripts/ or shared secrets/)
        has_creds=false
        if [[ "$env" == "mock-slack" ]]; then
            if [ -f "$dir/scripts/slack_token.json" ]; then
                has_creds=true
            elif [ -f "$REPO_ROOT/secrets/slack_token.json" ]; then
                ln -sf "$REPO_ROOT/secrets/slack_token.json" "$dir/scripts/slack_token.json"
                has_creds=true
            fi
        else
            if [ -f "$dir/scripts/token.json" ]; then
                has_creds=true
            elif [ -f "$REPO_ROOT/secrets/token.json" ]; then
                # Symlink shared credentials + token into env scripts dir
                [ -f "$REPO_ROOT/secrets/credentials.json" ] && ln -sf "$REPO_ROOT/secrets/credentials.json" "$dir/scripts/credentials.json"
                ln -sf "$REPO_ROOT/secrets/token.json" "$dir/scripts/token.json"
                has_creds=true
            fi
        fi

        if ! $has_creds; then
            echo -e "${YELLOW}SKIP${NC} (no credentials)"
            continue
        fi

        if (cd "$dir" && uv run --extra dev python scripts/capture_fixtures.py) > /tmp/capture-$env.log 2>&1; then
            fixture_count=$(find "$dir/tests/fixtures/real_"* -name "*.json" ! -name "_*" 2>/dev/null | wc -l)
            echo -e "${GREEN}OK${NC} ($fixture_count fixtures)"
        else
            echo -e "${RED}FAIL${NC} (see /tmp/capture-$env.log)"
        fi
    done
    echo ""
fi

# ─── Phase 2: Check fixture ↔ test coverage ─────────────────────────────
COVERAGE_FAIL=false
if ! $REPORT_ONLY; then
    echo "═══════════════════════════════════════"
    echo "  Phase 2: Fixture ↔ test coverage"
    echo "═══════════════════════════════════════"
    echo ""

    for i in "${!ENVS[@]}"; do
        env="${ENVS[$i]}"
        dir="${ENV_DIRS[$i]}"

        # Find fixture directory
        fixture_dir=$(find "$dir/tests/fixtures" -maxdepth 1 -name "real_*" -type d 2>/dev/null | head -1)
        test_file="$dir/tests/test_conformance.py"

        if [ -z "$fixture_dir" ] || [ ! -f "$test_file" ]; then
            echo -e "  ${YELLOW}SKIP${NC} $env (no fixtures or conformance tests)"
            continue
        fi

        # Check each fixture is referenced in test files (conformance + golden fixtures)
        # Look in all test_*.py files since some envs split across multiple files
        untested=""
        total=0
        covered=0
        for f in "$fixture_dir"/*.json; do
            fname=$(basename "$f")
            [ "$fname" = "_capture_metadata.json" ] && continue
            total=$((total + 1))
            # Check for filename with or without .json extension
            fname_no_ext="${fname%.json}"
            if grep -rq "$fname" "$dir/tests/"*.py 2>/dev/null || \
               grep -rq "\"$fname_no_ext\"" "$dir/tests/"*.py 2>/dev/null; then
                covered=$((covered + 1))
            else
                untested="$untested $fname"
            fi
        done

        if [ -n "$untested" ]; then
            echo -e "  ${RED}GAP${NC}  $env ($covered/$total covered)"
            echo "        Untested fixtures:"
            for f in $untested; do
                echo "          - $f"
            done
            echo ""
            echo "        → Follow the API validation playbook to add conformance tests"
            echo "          for these fixtures, then re-run this script."
            COVERAGE_FAIL=true
        else
            echo -e "  ${GREEN}OK${NC}   $env ($covered/$total fixtures covered)"
        fi
    done
    echo ""

    if $COVERAGE_FAIL; then
        echo -e "${RED}Fixture coverage gaps found. Add conformance tests before proceeding.${NC}"
        echo "See: docs/api-validation-playbook.md"
        echo ""
        # Continue to report phase but note the gap
    fi
fi

# ─── Phase 3: Run conformance tests ─────────────────────────────────────
if ! $REPORT_ONLY; then
    echo "═══════════════════════════════════════"
    echo "  Phase 3: Running conformance tests"
    echo "═══════════════════════════════════════"
    echo ""

    declare -A TEST_RESULTS
    for i in "${!ENVS[@]}"; do
        env="${ENVS[$i]}"
        dir="${ENV_DIRS[$i]}"

        echo -n "  Testing $env... "

        if [ ! -f "$dir/tests/test_conformance.py" ]; then
            echo -e "${YELLOW}SKIP${NC} (no conformance tests)"
            TEST_RESULTS[$env]="skip"
            continue
        fi

        # Run conformance tests, capture output
        if (cd "$dir" && uv run --extra dev pytest tests/test_conformance.py -v --tb=short) > /tmp/test-$env.log 2>&1; then
            passed=$(grep -c "PASSED" /tmp/test-$env.log 2>/dev/null || echo 0)
            echo -e "${GREEN}PASS${NC} ($passed tests)"
            TEST_RESULTS[$env]="pass:$passed"
        else
            passed=$(grep -c "PASSED" /tmp/test-$env.log 2>/dev/null || echo 0)
            failed=$(grep -c "FAILED" /tmp/test-$env.log 2>/dev/null || echo 0)
            echo -e "${RED}FAIL${NC} ($passed passed, $failed failed — see /tmp/test-$env.log)"
            TEST_RESULTS[$env]="fail:$passed:$failed"
        fi
    done
    echo ""
fi

# ─── Phase 4: Generate parity report ────────────────────────────────────
echo "═══════════════════════════════════════"
echo "  Phase 4: Parity Report"
echo "═══════════════════════════════════════"
echo ""

# Build JSON report
python3 << 'PYEOF'
import json
import os
from datetime import datetime, timezone
from pathlib import Path

repo = Path(os.environ.get("REPO_ROOT", "."))
envs = ["mock-gmail", "mock-gcal", "mock-gdoc", "mock-gdrive", "mock-slack"]

report = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "environments": {},
}

for env in envs:
    env_dir = repo / "packages" / "environments" / env
    fixtures_parent = env_dir / "tests" / "fixtures"

    # Find real fixtures dir
    real_dirs = list(fixtures_parent.glob("real_*"))
    real_dir = real_dirs[0] if real_dirs else None

    # Count fixtures
    fixture_count = 0
    if real_dir and real_dir.exists():
        fixture_count = len([f for f in real_dir.glob("*.json") if not f.name.startswith("_")])

    # Read capture metadata
    capture_date = None
    capture_account = None
    metadata_file = real_dir / "_capture_metadata.json" if real_dir else None
    if metadata_file and metadata_file.exists():
        try:
            meta = json.loads(metadata_file.read_text())
            capture_date = meta.get("captured_at", meta.get("capture_date"))
            capture_account = meta.get("account", meta.get("workspace"))
        except Exception:
            pass

    # Read mock coverage (flat list under "endpoints" key)
    coverage_file = fixtures_parent / "mock_coverage.json"
    endpoints_total = 0
    endpoints_implemented = 0
    endpoints_with_fixtures = 0
    endpoints_with_tests = 0
    if coverage_file.exists():
        try:
            cov = json.loads(coverage_file.read_text())
            for ep in cov.get("endpoints", []):
                endpoints_total += 1
                if ep.get("implemented"):
                    endpoints_implemented += 1
                if ep.get("fixture"):
                    endpoints_with_fixtures += 1
                if ep.get("tests"):
                    endpoints_with_tests += 1
        except Exception:
            pass

    # Read API spec for total real endpoints
    spec_files = list(fixtures_parent.glob("*_api_spec.json"))
    real_endpoint_count = 0
    if spec_files:
        try:
            spec = json.loads(spec_files[0].read_text())
            # Check for total_endpoints field first
            if "total_endpoints" in spec:
                real_endpoint_count = spec["total_endpoints"]
            elif isinstance(spec.get("resources"), dict):
                # resources is {name: {endpoints: [...]}} or {name: [...]}
                for resource_name, resource_data in spec["resources"].items():
                    if isinstance(resource_data, dict):
                        real_endpoint_count += len(resource_data.get("endpoints", []))
                    elif isinstance(resource_data, list):
                        real_endpoint_count += len(resource_data)
            elif isinstance(spec.get("resources"), list):
                for resource in spec["resources"]:
                    real_endpoint_count += len(resource.get("endpoints", []))
        except Exception:
            pass

    # Check conformance test exists
    has_conformance = (env_dir / "tests" / "test_conformance.py").exists()

    # Freshness
    days_old = None
    if capture_date:
        try:
            captured = datetime.fromisoformat(capture_date.replace("Z", "+00:00"))
            days_old = (datetime.now(timezone.utc) - captured).days
        except Exception:
            pass

    report["environments"][env] = {
        "fixtures": fixture_count,
        "capture_date": capture_date,
        "capture_account": capture_account,
        "days_since_capture": days_old,
        "fresh": days_old is not None and days_old < 30,
        "real_endpoints": real_endpoint_count,
        "mock_endpoints_implemented": endpoints_implemented,
        "mock_endpoints_with_fixtures": endpoints_with_fixtures,
        "mock_endpoints_with_tests": endpoints_with_tests,
        "has_conformance_tests": has_conformance,
        "coverage_pct": round(100 * endpoints_implemented / real_endpoint_count, 1) if real_endpoint_count else 0,
        "fixture_pct": round(100 * endpoints_with_fixtures / endpoints_implemented, 1) if endpoints_implemented else 0,
    }

# Print human-readable summary
print(f"{'Env':<16} {'Fixtures':>8} {'Captured':>12} {'Fresh':>6} {'Implemented':>13} {'Coverage':>9} {'Fixture%':>9}")
print("─" * 80)
for env, info in report["environments"].items():
    fresh = "✅" if info["fresh"] else ("⚠️" if info["days_since_capture"] else "❌")
    impl = f"{info['mock_endpoints_implemented']}/{info['real_endpoints']}" if info['real_endpoints'] else "?"
    print(f"{env:<16} {info['fixtures']:>8} {(info['capture_date'] or 'never')[:10]:>12} {fresh:>6} {impl:>13} {info['coverage_pct']:>8.1f}% {info['fixture_pct']:>8.1f}%")

print()

# Gaps
print("Gaps:")
for env, info in report["environments"].items():
    gaps = []
    if not info["fresh"]:
        gaps.append(f"fixtures stale ({info['days_since_capture'] or '?'}d old)")
    if info["fixture_pct"] < 70:
        gaps.append(f"only {info['fixture_pct']:.0f}% of implemented endpoints have fixtures")
    if info["coverage_pct"] < 60:
        gaps.append(f"only {info['coverage_pct']:.0f}% of real endpoints implemented")
    if gaps:
        print(f"  {env}: {'; '.join(gaps)}")

# Save JSON
report_path = Path(os.environ.get("REPORT_FILE", ".local/parity-report.json"))
report_path.parent.mkdir(parents=True, exist_ok=True)
report_path.write_text(json.dumps(report, indent=2) + "\n")
print(f"\nReport saved to: {report_path}")
PYEOF

echo ""
echo "═══════════════════════════════════════"
echo "  Done"
echo "═══════════════════════════════════════"
