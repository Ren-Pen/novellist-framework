#!/usr/bin/env python3
"""Tool runner — invoke a tool script using the project venv.

This is the cross-platform entry point. It is invoked as:

    python .claude/tools/run.py <tool-name> [args...]

The bootstrap interpreter (the one running this file) can be any
Python 3.x — it does not have to match the venv's version. This file
intentionally uses only basic Python so it boots on whatever the
system provides.

The actual tool script is run with the project venv's interpreter,
which is the one verified to be Python 3.9+ by setup.

Examples:
    python .claude/tools/run.py next_chapter_number
    python .claude/tools/run.py word_count book/chapters/001-foo.md
    python .claude/tools/run.py get_recent_chapters 2

Exit codes:
    0 on success
    1 if venv not initialized, tool not found, or bad usage
    (otherwise the exit code of the invoked tool)
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(here, "..", ".."))

    # Locate venv python (Windows vs POSIX path differ)
    if os.name == "nt":
        venv_python = os.path.join(project_root, ".venv", "Scripts", "python.exe")
    else:
        venv_python = os.path.join(project_root, ".venv", "bin", "python")

    if not os.path.isfile(venv_python):
        sys.stderr.write(
            "error: venv not initialized at {0}/.venv\n"
            "run setup first:\n"
            "  Unix/macOS/WSL:  .claude/tools/setup.sh\n"
            "  Windows native:  .claude\\tools\\setup.bat\n".format(project_root)
        )
        return 1

    if len(sys.argv) < 2:
        sys.stderr.write("usage: python {0} <tool-name> [args...]\n".format(sys.argv[0]))
        return 1

    tool_name = sys.argv[1]
    tool_args = sys.argv[2:]
    tool_path = os.path.join(here, tool_name + ".py")

    if not os.path.isfile(tool_path):
        sys.stderr.write("error: tool not found: {0}\n".format(tool_path))
        return 1

    # Run from project root so tools see consistent relative paths
    os.chdir(project_root)

    # Force UTF-8 for the child process to avoid Windows codepage
    # issues (cp932, cp936, gbk, etc.) when tools print Chinese
    # characters. PYTHONUTF8 enables UTF-8 mode in Python 3.7+;
    # PYTHONIOENCODING is a belt-and-suspenders fallback.
    child_env = os.environ.copy()
    child_env["PYTHONUTF8"] = "1"
    child_env["PYTHONIOENCODING"] = "utf-8"

    # os.execv would replace this process but doesn't exist cleanly on
    # Windows; use subprocess.call instead for portability.
    import subprocess
    return subprocess.call([venv_python, tool_path] + tool_args, env=child_env)


if __name__ == "__main__":
    sys.exit(main())
