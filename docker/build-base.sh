#!/usr/bin/env bash
# Build and optionally push the shared base image.
#
# Usage:
#   ./docker/build-base.sh          # build version + latest tags
#   ./docker/build-base.sh --push   # build + push both tags
set -euo pipefail

REPO="${REPO:-ghcr.io/benchflow-ai/env0}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VERSION_FILE="${VERSION_FILE:-$ROOT_DIR/VERSION}"
DEFAULT_VERSION_TAG="$(tr -d '[:space:]' < "$VERSION_FILE")"
VERSION_TAG="${VERSION_TAG:-$DEFAULT_VERSION_TAG}"
LATEST_TAG="${LATEST_TAG:-latest}"
TAGS=("$VERSION_TAG")

if [[ -z "$VERSION_TAG" ]]; then
    echo "ERROR: empty version tag from $VERSION_FILE" >&2
    exit 1
fi

if [[ -n "$LATEST_TAG" && "$LATEST_TAG" != "$VERSION_TAG" ]]; then
    TAGS+=("$LATEST_TAG")
fi

echo "==> Generating Dockerfile.base from template + config.toml"
python3 "$SCRIPT_DIR/generate_dockerfile.py"

BUILD_TAG_ARGS=()
for tag in "${TAGS[@]}"; do
    BUILD_TAG_ARGS+=("-t" "$REPO:$tag")
done

echo "==> Building base image: ${TAGS[*]/#/$REPO:}"
docker build "${BUILD_TAG_ARGS[@]}" \
    -f "$SCRIPT_DIR/Dockerfile.base" "$ROOT_DIR"

echo "==> Built: ${TAGS[*]/#/$REPO:}"

if [[ "${1:-}" == "--push" ]]; then
    for tag in "${TAGS[@]}"; do
        echo "==> Pushing $REPO:$tag"
        docker push "$REPO:$tag"
    done
    echo "==> Done."
fi
