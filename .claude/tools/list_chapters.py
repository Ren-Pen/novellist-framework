#!/usr/bin/env python3
"""List all chapters with their metadata as a TSV table.

Reads YAML frontmatter from each NNN-*.md file in book/chapters/.
Output is a tab-separated table on stdout for easy parsing.

Columns:
    number   chapter_number from frontmatter
    title    chapter_title from frontmatter
    words    word_count from frontmatter
    emotion  emotional_target from frontmatter
    hook     hook_type from frontmatter
    file     filename

Usage:
    python .claude/tools/run.py list_chapters

Exit code: 0 on success, 1 if book/chapters/ does not exist.
"""

import re
import sys
from pathlib import Path

CHAPTER_DIR = Path("book/chapters")
PATTERN = re.compile(r"^(\d{3})-.+\.md$")


def parse_frontmatter(text: str) -> dict[str, str]:
    """Minimal YAML frontmatter parser. Returns key-value strings."""
    result: dict[str, str] = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return result

    for line in lines[1:]:
        if line.strip() == "---":
            break
        # Simple key: value parsing; doesn't handle lists or nesting,
        # which is fine for the chapter frontmatter we use.
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            # Strip surrounding quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            result[key] = value
    return result


def main() -> int:
    if not CHAPTER_DIR.is_dir():
        print(f"error: {CHAPTER_DIR} does not exist", file=sys.stderr)
        return 1

    rows: list[dict[str, str]] = []
    for entry in sorted(CHAPTER_DIR.iterdir()):
        if not entry.is_file() or not PATTERN.match(entry.name):
            continue
        meta = parse_frontmatter(entry.read_text(encoding="utf-8"))
        rows.append({
            "number": meta.get("chapter_number", ""),
            "title": meta.get("chapter_title", ""),
            "words": meta.get("word_count", ""),
            "emotion": meta.get("emotional_target", ""),
            "hook": meta.get("hook_type", ""),
            "file": entry.name,
        })

    # Print header + rows as TSV
    headers = ["number", "title", "words", "emotion", "hook", "file"]
    print("\t".join(headers))
    for row in rows:
        print("\t".join(row[h] for h in headers))

    return 0


if __name__ == "__main__":
    sys.exit(main())
