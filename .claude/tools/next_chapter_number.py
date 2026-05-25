#!/usr/bin/env python3
"""Print the next chapter number based on book/chapters/ contents.

Counts files matching the pattern NNN-*.md directly in book/chapters/.
Subdirectories like _archive/ or _rejected/ are ignored.

Usage:
    python .claude/tools/run.py next_chapter_number

Output (stdout): a single integer, the next chapter number.
Exit code: 0 on success, 1 if book/chapters/ does not exist.
"""

import re
import sys

from pathlib import Path

# Force UTF-8 on stdout/stderr.
# On Windows the console may default to cp932/cp936/gbk, which cannot
# encode Chinese characters when not in those code pages.
# This is a no-op on Python < 3.7 (TextIOWrapper has no reconfigure).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

CHAPTER_DIR = Path("book/chapters")
PATTERN = re.compile(r"^(\d{3})-.+\.md$")


def main() -> int:
    if not CHAPTER_DIR.is_dir():
        print(f"error: {CHAPTER_DIR} does not exist", file=sys.stderr)
        return 1

    max_num = 0
    for entry in CHAPTER_DIR.iterdir():
        if not entry.is_file():
            continue
        match = PATTERN.match(entry.name)
        if match:
            num = int(match.group(1))
            if num > max_num:
                max_num = num

    print(max_num + 1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
