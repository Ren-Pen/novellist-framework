#!/usr/bin/env python3
"""Print the Chinese character count of a chapter markdown file.

Excludes YAML frontmatter (the block between two `---` lines at file start)
and the leading `# 第N章 标题` heading line.

Counts only CJK ideographs (U+4E00 to U+9FFF and adjacent CJK ranges).
Punctuation and whitespace are not counted. This matches the convention
used in Chinese web fiction platforms (字数 / 中文字符).

Usage:
    python .claude/tools/run.py word_count book/chapters/001-foo.md

Output (stdout): a single integer, the Chinese character count.
Exit code: 0 on success, 1 on error (file missing, etc.).
"""

import sys
from pathlib import Path


def is_cjk(char: str) -> bool:
    """True if char is a CJK ideograph."""
    code = ord(char)
    return (
        0x4E00 <= code <= 0x9FFF      # CJK Unified Ideographs
        or 0x3400 <= code <= 0x4DBF   # Extension A
        or 0x20000 <= code <= 0x2A6DF # Extension B
        or 0xF900 <= code <= 0xFAFF   # Compatibility Ideographs
    )


def strip_frontmatter_and_heading(text: str) -> str:
    """Remove YAML frontmatter and the first heading line."""
    lines = text.splitlines()
    i = 0

    # Skip frontmatter
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1  # past the closing ---

    # Skip blank lines after frontmatter
    while i < len(lines) and not lines[i].strip():
        i += 1

    # Skip the first H1 heading if present
    if i < len(lines) and lines[i].startswith("#"):
        i += 1

    return "\n".join(lines[i:])


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: word_count.py FILE", file=sys.stderr)
        return 1

    path = Path(argv[1])
    if not path.is_file():
        print(f"error: {path} not found", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    body = strip_frontmatter_and_heading(text)
    count = sum(1 for ch in body if is_cjk(ch))
    print(count)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
