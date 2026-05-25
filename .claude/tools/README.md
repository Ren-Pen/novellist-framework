# Tools — Helper Scripts for the Novel-Writing Workflow

> Stateless utility scripts. Each script does one mechanical job.
> Subagents and skills call these instead of writing ad-hoc bash.

## Design Principles

1. **Stateless.** Inputs come from command-line arguments. No script
   reads hidden config files.
2. **Single responsibility.** One script = one job. No flags that
   change fundamental behavior.
3. **Unix conventions.** Output goes to stdout, errors to stderr,
   exit code 0 = success, nonzero = error.
4. **No judgment.** Tools do mechanical operations. Judgment (e.g.,
   "is this AI-slop?") belongs to subagents.
5. **No side effects** unless explicitly named. Read-only scripts MUST
   NOT write anywhere.

## Inventory

| Script | Purpose |
|--------|---------|
| `next_chapter_number.py` | Print the next chapter number based on `book/chapters/` contents |
| `word_count.py FILE` | Print Chinese character count of a chapter markdown file (excludes frontmatter) |
| `list_chapters.py` | Print a table of all chapters with their metadata |
| `get_recent_chapters.py N` | Print the full text of the most recent N chapters |

## Running

All scripts assume the working directory is the framework root (where
`.claude/` and `book/` live). They are invoked as:

```bash
python .claude/tools/<script>.py [args]
```

Scripts use only the Python 3 standard library — no `pip install` needed.
