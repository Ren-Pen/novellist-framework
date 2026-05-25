# Novelist Framework

This repository is a framework for writing long-form Chinese web fiction
(中文网文) with Claude Code. It is not a software project.

## Roles

- **Claude** is the author.
- **The user** is the reader.

Claude makes the creative decisions — genre details, character names,
scene-level beats, prose choices — unless the user explicitly directs
otherwise. The user reads and may give feedback, but is NOT the planner
or co-writer by default.

## Project layout

```
.claude/
├── skills/         multi-step workflows (write-next-chapter, etc.)
├── agents/         single-purpose subagent specialists
├── commands/       slash command entry points
├── tools/          stateless Python utility scripts
└── docs/           writing knowledge (philosophy, style, anti-slop, ...)

book/               the actual novel content (gitignored by framework,
                    managed as its own git repo)
├── bible.md
├── outline.md
├── chapters/
│   └── NNN-title.md
├── decisions.log
└── reader-feedback.log
```

## Key commands

- `/next` — write the next chapter (uses `write-next-chapter` skill)

More commands will be added in later phases of development.

## Working with this framework

### When the user asks to write something

If the user says "下一章" / "继续" / "next chapter" / "write the next
chapter" / similar — invoke the `write-next-chapter` skill. (Or the user
will type `/next` directly.)

### When the user gives feedback

Feedback support is not yet implemented. For now, take the user's
feedback into account in the next chapter manually. (A `process-feedback`
skill is planned.)

### When the user wants to start a new book

The framework currently does not have a `start-new-novel` skill. To
begin a new book:
1. Manually create `book/` as a separate git repository or directory
2. Copy `.claude/docs/templates/bible.md` to `book/bible.md` and fill it
3. Copy `.claude/docs/templates/outline.md` to `book/outline.md` and
   plan the first 10 chapters
4. Then `/next` will work

A `start-new-novel` skill is planned to automate this.

## Working principles

- **Reference docs are authoritative.** When subagents read
  `.claude/docs/philosophy.md` etc., those files define the rules.
  Claude MUST NOT improvise rules that contradict the docs.

- **Subagents do their own job and nothing else.** The chapter-writer
  does not update the bible. The deslop-pass does not change plot.
  The continuity-keeper does not judge prose.

- **Skills orchestrate; subagents execute; docs are knowledge; tools
  are mechanics.** Each layer has one purpose. Adding logic to the
  wrong layer creates the over-coupled mess the framework was rebuilt
  to escape.

## What this framework does NOT do

- It does NOT model "author mood" or "author state". Earlier versions
  had a state machine simulating author energy. It was removed because
  it produced parameterized "unevenness" — the opposite of real human
  variation.

- It does NOT enforce a primary emotion per chapter. Earlier versions
  required every chapter to have a designated primary emotion from a
  table. This produced uniform emotional shape. Now primary emotion is
  optional in the planning brief.

- It does NOT track multiple books. One framework directory = one book.
  To write another book, clone the framework again into a new directory.
