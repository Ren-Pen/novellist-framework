# Novelist Framework

A Claude Code framework for writing long-form Chinese web fiction
(中文网文). Phase 1 — supports the core "write next chapter" workflow
with three subagents.

---

## What is this

A reusable framework that lives in a git repo. To write a novel:

1. Clone this framework into a directory (e.g., `~/work/my-novel/`).
2. **Initialize the Python venv for tools:**
   - Unix/macOS/WSL: `.claude/tools/setup.sh`
   - Windows: `.claude\tools\setup.bat`
   - Requires Python 3.9+. If your default `python3` is older, pass
     `--python=python3.11` (or similar).
3. Inside that directory, create a `book/` subdirectory which is the
   git repo for that specific novel's content.
4. Open Claude Code with that directory as cwd. The framework loads
   automatically via `.claude/`.
5. Use `/next` to write chapters. Use natural language ("continue the
   story", "下一章") to trigger the same workflow.

To write another novel: clone the framework again into a different
directory. Each novel gets its own clone (and its own `.venv/`).
Framework updates are pulled in via `git pull` per novel.

---

## Architecture

```
my-novel/                              ← framework clone, one per novel
├── .git/                              points to novelist-framework
├── .gitignore                         ignores book/
├── CLAUDE.md                          project memory loaded by Claude Code
├── README.md                          this file
├── .claude/
│   ├── skills/
│   │   └── write-next-chapter/
│   │       ├── SKILL.md               workflow orchestration
│   │       └── references/            workflow details
│   ├── agents/
│   │   ├── chapter-writer.md          writes prose
│   │   ├── deslop-pass.md             checks AI-slop, edits or rejects
│   │   └── continuity-keeper.md       updates bible after chapter
│   ├── commands/
│   │   └── next.md                    /next slash command
│   ├── tools/
│   │   ├── next_chapter_number.py
│   │   ├── word_count.py
│   │   ├── list_chapters.py
│   │   └── get_recent_chapters.py
│   └── docs/
│       ├── philosophy.md              what makes fiction land
│       ├── house-style.md             default voice
│       ├── emotion-formulas.md        emotion reference
│       ├── anti-slop.md               anti-AI-slop guide
│       └── templates/
│           ├── bible.md
│           ├── outline.md
│           └── chapter.md
└── book/                              the novel itself (separate git repo)
    ├── .git/                          points to the book's own remote
    ├── bible.md
    ├── outline.md
    ├── chapters/
    │   ├── 001-...md
    │   └── 002-...md
    ├── decisions.log
    └── reader-feedback.log
```

### Two git repos, one directory

The outer directory (`my-novel/`) is a clone of `novelist-framework`.
The `book/` subdirectory is its own independent git repo — that's where
the novel content lives. The framework's `.gitignore` excludes `book/`,
so the two repos don't see each other.

To `git pull` framework updates: run `git pull` at the outer level.
To `git commit` novel content: `cd book/ && git commit ...`.

---

## How the layers work

| Layer | What it does | Files |
|-------|--------------|-------|
| **Slash commands** | Explicit entry points | `.claude/commands/*.md` |
| **Skills** | Multi-step workflows | `.claude/skills/*/SKILL.md` |
| **Subagents** | Single-task specialists with isolated context | `.claude/agents/*.md` |
| **Tools** | Mechanical Python utilities | `.claude/tools/*.py` |
| **Docs** | Static writing knowledge | `.claude/docs/*.md` |

Each layer has one responsibility. The slash command triggers a skill,
the skill calls subagents in order, subagents read docs and use tools.
Knowledge doesn't migrate up the stack.

---

## Status

**Phase 1 — Core writing loop.** ✅ Done.

- `/next` writes the next chapter via chapter-writer → deslop-pass →
  continuity-keeper.
- The three subagents are isolated; each only reads its required docs.
- No "author state" simulation.
- No mandatory primary emotion per chapter.

**Phase 2 — Reader feedback.** Not implemented.

- `process-feedback` skill, `feedback-integrator` subagent.

**Phase 3 — Platform compliance.** Not implemented.

- `harmonize` skill, `platform-compliance` subagent, harmonization rules.

**Phase 4 — New novel bootstrap.** Not implemented.

- `start-new-novel` skill, `story-architect` subagent.

**Phase 5 — Status query.** Not implemented.

- `novel-status` skill.

---

## Comparison with the previous SKILL

This framework is the rewrite of an earlier `chinese-web-novel` skill.
What changed:

| Before | Now |
|--------|-----|
| One big SKILL.md (~600 lines) plus 8 subagents in `agents/` | Split into skills, subagents, docs, tools, commands |
| Subagents shared one context with the main flow | Each subagent has its own context window |
| Reference files mixed prevention and detection | `docs/` is reference only; subagents do detection |
| `chapter-planner` subagent with an 8-field planning sheet | Planning happens in the skill itself, 200-400 char brief |
| `author-state-keeper` simulated mood swings | Removed — produced parameterized fake unevenness |
| `anti-ai-slop.md` had §1-§7 with quantitative thresholds | `anti-slop.md` has the prevention rules + banned-word table + one critical pattern (time-reversal); no quantitative thresholds |
| Every chapter required a primary emotion | Primary emotion is optional in the brief |
| Hook type implicit | Hook type required in the brief |

The previous skill produced good chapters but had a systemic AI-uniform
texture — readers could feel "this is from a writing program" even
without identifying specific bad sentences. The rewrite targets that
texture by removing the rules that mechanically produced it.

---

## License

Personal project. Adjust to taste.
