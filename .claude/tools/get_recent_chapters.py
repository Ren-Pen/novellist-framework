#!/usr/bin/env python3
"""Print the full text of the most recent N chapters.

Reads chapter files from book/chapters/, sorts by chapter number
(descending), and emits the most recent N. Each chapter is preceded
by a separator line for easy visual scanning.

Usage:
    python .claude/tools/run.py get_recent_chapters 2

Argument:
    N    number of recent chapters to emit (must be positive integer)

Output (stdout): the full text of the N most recent chapters, each
preceded by:

    === CHAPTER N: <title> ===

Exit code: 0 on success, 1 on error.
"""

import re
import sys
from pathlib import Path

CHAPTER_DIR = Path("book/chapters")
PATTERN = re.compile(r"^(\d{3})-.+\.md$")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: get_recent_chapters.py N", file=sys.stderr)
        return 1

    try:
        n = int(argv[1])
        if n < 1:
            raise ValueError
    except ValueError:
        print(f"error: N must be a positive integer (got {argv[1]!r})",
              file=sys.stderr)
        return 1

    if not CHAPTER_DIR.is_dir():
        print(f"error: {CHAPTER_DIR} does not exist", file=sys.stderr)
        return 1

    # Collect (chapter_number, path) tuples
    chapters: list[tuple[int, Path]] = []
    for entry in CHAPTER_DIR.iterdir():
        if not entry.is_file():
            continue
        match = PATTERN.match(entry.name)
        if match:
            chapters.append((int(match.group(1)), entry))

    # Sort descending by number, take top N
    chapters.sort(key=lambda x: x[0], reverse=True)
    recent = chapters[:n]

    # Emit in chronological order (oldest of the recent N first)
    recent.sort(key=lambda x: x[0])

    for num, path in recent:
        # Extract title from filename: NNN-title.md → title
        title = path.stem.split("-", 1)[1] if "-" in path.stem else path.stem
        print(f"=== CHAPTER {num}: {title} ===")
        print(path.read_text(encoding="utf-8"))
        print()  # blank line between chapters

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
