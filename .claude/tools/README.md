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

## Setup (first time only)

The tools run in a project-local Python venv at `.venv/`. To create it:

**Unix / macOS / WSL:**
```bash
.claude/tools/setup.sh
# or explicitly pick an interpreter:
.claude/tools/setup.sh --python=python3.11
```

**Windows:**
```cmd
.claude\tools\setup.bat
.claude\tools\setup.bat python3.11
```

The setup script:
- Creates `.venv/` at the project root
- Verifies Python is 3.9 or newer (tools use PEP 585 generics)
- Is idempotent — running again does nothing if `.venv/` already exists

To recreate the venv (e.g., changed Python version): delete `.venv/`
and re-run setup.

## Running tools

All tools are invoked through `run.sh` (Unix) or `run.bat` (Windows).
The runner uses the project venv and runs from the project root.

**Unix / macOS / WSL:**
```bash
.claude/tools/run.sh <tool-name> [args...]
```

**Windows:**
```cmd
.claude\tools\run.bat <tool-name> [args...]
```

Tool name is the script filename without `.py`. Examples:

```bash
.claude/tools/run.sh next_chapter_number
.claude/tools/run.sh word_count book/chapters/001-foo.md
.claude/tools/run.sh get_recent_chapters 2
.claude/tools/run.sh list_chapters
```

Subagent / skill docs use the Unix form. On Windows, Claude Code MAY
need to substitute `.claude\tools\run.bat` — but if you use WSL or
Git Bash, the Unix form works directly.

## Inventory

| Script | Purpose |
|--------|---------|
| `next_chapter_number.py` | Print the next chapter number based on `book/chapters/` contents |
| `word_count.py FILE` | Print Chinese character count of a chapter markdown file (excludes frontmatter) |
| `list_chapters.py` | Print a TSV table of all chapters with their metadata |
| `get_recent_chapters.py N` | Print the full text of the most recent N chapters |

All tools use only the Python 3 standard library — no `pip install`
needed beyond what the setup script creates.
