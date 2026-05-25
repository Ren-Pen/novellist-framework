#!/usr/bin/env python3
"""Print the next chapter number based on book/chapters/ contents.

Counts files matching the pattern NNN-*.md directly in book/chapters/.
Subdirectories like _archive/ or _rejected/ are ignored.

Usage:
    python .claude/tools/next_chapter_number.py

Output (stdout): a single integer, the next chapter number.
Exit code: 0 on success, 1 if book/chapters/ does not exist.
"""

import re
import sys
from pathlib import Path

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
