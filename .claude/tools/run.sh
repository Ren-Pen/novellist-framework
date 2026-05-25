#!/usr/bin/env bash
# Tool runner — invoke a tool script using the project venv.
#
# Usage:
#   .claude/tools/run.sh <tool-name> [args...]
#
# Examples:
#   .claude/tools/run.sh next_chapter_number
#   .claude/tools/run.sh word_count book/chapters/001-foo.md
#   .claude/tools/run.sh get_recent_chapters 2
#
# The tool name is the script filename without .py extension.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VENV_PYTHON="$PROJECT_ROOT/.venv/bin/python"

if [[ ! -x "$VENV_PYTHON" ]]; then
  echo "error: venv not initialized at $PROJECT_ROOT/.venv" >&2
  echo "run: $SCRIPT_DIR/setup.sh" >&2
  exit 1
fi

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <tool-name> [args...]" >&2
  exit 1
fi

TOOL_NAME="$1"
shift

TOOL_PATH="$SCRIPT_DIR/${TOOL_NAME}.py"
if [[ ! -f "$TOOL_PATH" ]]; then
  echo "error: tool not found: $TOOL_PATH" >&2
  exit 1
fi

# cd to project root so tools see consistent relative paths (book/, etc.)
cd "$PROJECT_ROOT"
exec "$VENV_PYTHON" "$TOOL_PATH" "$@"
