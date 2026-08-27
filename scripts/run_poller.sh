#!/usr/bin/env bash
# Entry point: sources .env then runs the poller.
# Usage: run_poller.sh [--live] [--force-slot story|feed|reel]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# set -a: auto-exports everything .env defines, instead of a hand-kept
# whitelist -- a fixed `export VAR1 VAR2 ...` list here silently dropped
# DREIS_STORIES_DRIVE_FOLDER_ID (added to .env 2026-08-25) since nobody
# remembered to add it here too, causing a real KeyError crash mid-story
# (Facebook leg had already posted for real before the Instagram leg died).
# shellcheck disable=SC1091
set -a
source "$PROJECT_DIR/.env"
set +a

python3 "$SCRIPT_DIR/poller.py" "$@"
