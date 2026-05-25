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
6. **Cross-platform.** A single entry point (`run.py`) handles both
   Unix and Windows. No platform-specific tool invocations leak into
   subagent or skill instructions.

## Setup (first time only)

The tools run in a project-local Python venv at `.venv/`. To create it:

**Unix / macOS / WSL:**
```bash
.claude/tools/setup.sh
# or explicitly pick an interpreter:
.claude/tools/setup.sh --python=python3.11
```

**Windows native (cmd / PowerShell):**
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

## Running tools — the single cross-platform entry point

All tools are invoked the same way on every platform:

```bash
python -X utf8 .claude/tools/run.py <tool-name> [args...]
```

The `-X utf8` flag enables Python's UTF-8 mode at interpreter startup,
forcing stdout/stderr to UTF-8 regardless of the system locale. **This
is REQUIRED on Windows in non-UTF-8 locales (cp932 for Japanese, cp936
for Simplified Chinese, etc.)** — without it, printing Chinese
characters to stdout will raise `UnicodeEncodeError` when Claude Code
runs the tool in its built-in shell.

On macOS / Linux this flag is harmless (the locale is usually already
UTF-8). It is kept in the command for consistency.

Examples:

```bash
python -X utf8 .claude/tools/run.py next_chapter_number
python -X utf8 .claude/tools/run.py word_count book/chapters/001-foo.md
python -X utf8 .claude/tools/run.py get_recent_chapters 2
python -X utf8 .claude/tools/run.py list_chapters
```

### Why this design

`run.py` is the bootstrap. It can be executed by any system Python 3.x
(no version pickiness, no PEP 585 syntax). Its only job is to:

1. Find the project venv (`.venv/bin/python` on Unix,
   `.venv\Scripts\python.exe` on Windows)
2. Forward the invocation to that interpreter

This means:
- Subagent and skill instructions write `python .claude/tools/run.py ...`
  ONCE. No "if Windows then run.bat else run.sh" branches anywhere.
- The version-sensitive logic (Python 3.9+ for PEP 585) lives in the
  venv. The bootstrap doesn't care.
- It works in WSL, Git Bash, native cmd, native PowerShell, and any
  POSIX shell, identically.

The only platform-specific files are `setup.sh` and `setup.bat`,
which exist purely because venv creation needs to invoke the right
interpreter on each platform. After setup, you never see another `.sh`
or `.bat`.

### Bootstrap Python requirement

The system `python` or `python3` command used to invoke `run.py` only
needs to be Python 3. Any 3.x works — `run.py` itself uses only
basic syntax compatible with 3.4+.

If your system's default `python` is Python 2, use `python3` instead:

```bash
python3 .claude/tools/run.py next_chapter_number
```

The `settings.json` allows both `python` and `python3` prefixes.

## Inventory

| Script | Purpose |
|--------|---------|
| `next_chapter_number.py` | Print the next chapter number based on `book/chapters/` contents |
| `word_count.py FILE` | Print Chinese character count of a chapter markdown file (excludes frontmatter) |
| `list_chapters.py` | Print a TSV table of all chapters with their metadata |
| `get_recent_chapters.py N` | Print the full text of the most recent N chapters |

All tools use only the Python 3 standard library — no `pip install`
needed beyond what the setup script creates.
