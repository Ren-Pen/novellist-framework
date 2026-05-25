#!/usr/bin/env bash
# Setup script — create the project's Python venv for tools/ scripts.
#
# Usage:
#   ./.claude/tools/setup.sh
#   ./.claude/tools/setup.sh --python=python3.11
#
# Idempotent: if .venv/ already exists, this script does nothing.
# Re-run to recreate? delete .venv/ first.

set -euo pipefail

# Locate project root (parent of .claude/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VENV_DIR="$PROJECT_ROOT/.venv"

# Default Python interpreter
PYTHON_BIN="python3"

# Parse --python= flag
for arg in "$@"; do
  case "$arg" in
    --python=*) PYTHON_BIN="${arg#--python=}" ;;
    *)          echo "unknown arg: $arg" >&2; exit 1 ;;
  esac
done

if [[ -d "$VENV_DIR" ]]; then
  echo "venv already exists at $VENV_DIR"
  echo "to recreate: rm -rf $VENV_DIR && $0"
  exit 0
fi

echo "creating venv at $VENV_DIR using $PYTHON_BIN"
"$PYTHON_BIN" -m venv "$VENV_DIR"

# Check Python version is >= 3.9 (tools use PEP 585 generics)
VERSION_OK=$("$VENV_DIR/bin/python" -c "import sys; print(sys.version_info >= (3, 9))")
if [[ "$VERSION_OK" != "True" ]]; then
  ACTUAL=$("$VENV_DIR/bin/python" --version)
  echo "error: tools/ scripts require Python 3.9+, got $ACTUAL" >&2
  echo "re-run with --python=python3.11 or similar" >&2
  rm -rf "$VENV_DIR"
  exit 1
fi

echo "venv ready. Python version:"
"$VENV_DIR/bin/python" --version
