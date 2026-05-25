---
name: write-next-chapter
description: Orchestrate writing the next chapter of the in-progress Chinese web novel. Use this skill whenever the user asks to write the next chapter, continue the story, write the next installment, or types `/next`. Triggers on phrases like "write the next chapter", "continue the story", "next chapter please", "继续", "下一章", "再写一章", and on any context where chapter N has been written and chapter N+1 should follow. This skill coordinates the chapter-writer, deslop-pass, and continuity-keeper subagents and handles error cases like rewrite loops and continuity contradictions.
---

# Write Next Chapter

This skill orchestrates the full workflow for writing one chapter:
gathering context → planning → writing → AI-slop check → continuity
update → delivery.

The skill itself does NOT write prose. It calls three subagents in
sequence and handles their interactions.

---

## Pre-flight check

Before starting, verify the working directory has:
- `book/bible.md`
- `book/outline.md`
- `book/chapters/` (may be empty for Chapter 1)

If `book/` does not exist or `bible.md` is missing, the user has not
started a novel. Tell them to run `/new-novel` first (or write the
bible manually), and stop.

---

## Workflow

### Step 1: Determine chapter number

```bash
python .claude/tools/next_chapter_number.py
```

This prints the next chapter number (e.g., `11`). Store it as `N`.

### Step 2: Gather context

Read these files yourself (the skill does this, NOT the subagents):

1. `book/bible.md` — full
2. `book/outline.md` — find the entry for chapter `N`
3. The last 2 chapters via:
   ```bash
   python .claude/tools/get_recent_chapters.py 2
   ```
4. `book/reader-feedback.log` if it exists — read last 5 entries
5. `book/decisions.log` if it exists — scan for binding decisions
   affecting upcoming events

For chapter 1, only steps 1-2 apply.

### Step 3: Compose a planning brief

Compose a 200-400 character brief in the format defined in
`references/planning-brief-format.md`. The brief MUST include:

- Chapter number and draft title
- Arc position
- What happens (2-3 sentences)
- Hook type (REQUIRED — from `.claude/docs/emotion-formulas.md` § 2)
- Foreshadow plant / payoff (if any)
- Avoid list (2-3 specific things)

The brief MAY include a primary emotion if one fits naturally. The
brief MUST NOT include a primary emotion just because the slot exists.
See `references/planning-brief-format.md` § "Optional fields" for
why this matters.

**The skill writes this brief in its own context. Do NOT spawn a
separate "planner" subagent.** Planning is light enough to live here.

### Step 4: Invoke `chapter-writer`

Use the Task tool to invoke the `chapter-writer` subagent. Pass it:
- The chapter number `N`
- The planning brief from Step 3

The subagent will read the bible itself, read recent chapters itself,
write the prose, and save to `book/chapters/{NNN}-{title}.md`.

It returns:
- The file path
- The chapter title
- One forward-framing sentence

### Step 5: Invoke `deslop-pass`

Use the Task tool to invoke the `deslop-pass` subagent. Pass it:
- The chapter path returned in Step 4

It returns a severity report. Handle the response:

- **Light or moderate:** chapter has been cleaned in place. Continue.
- **Severe (rewrite request):** see `references/error-handling.md`
  § Rewrite Loop.

### Step 6: Invoke `continuity-keeper`

Use the Task tool to invoke the `continuity-keeper` subagent. Pass it:
- The chapter path

It returns a diff report. Handle the response:

- **No contradictions:** continue.
- **Contradictions present:** STOP. Surface the contradictions to the
  user clearly and wait for direction. See
  `references/error-handling.md` § Contradictions.

### Step 7: Report to user

Show the user, in this order:

1. Chapter number and title: `第 N 章 <title>`
2. The full chapter text (read the file and display it)
3. ONE forward-framing sentence (from chapter-writer's return value)

See `references/reporting.md` for tone and format.

You MUST NOT ask the user how the chapter was. You MUST NOT offer to
revise. The reader will ask for changes if they want them. Constant
questioning breaks immersion.

---

## What this skill does NOT do

- Does NOT do platform-compliance export (separate skill, Phase 3)
- Does NOT do AI-slop detection itself (`deslop-pass` does)
- Does NOT modify story-bible itself (`continuity-keeper` does)
- Does NOT ask the user clarifying questions (the workflow is fully
  determined by the bible + outline)
- Does NOT run an "author state" simulation — the framework no longer
  models author mood/state. Variation comes from the chapter's own
  needs, not from a state machine.

---

## Reference files (read as needed)

- `references/planning-brief-format.md` — precise format of the brief
- `references/voice-continuity.md` — what to extract from recent chapters
- `references/error-handling.md` — rewrite loop, contradictions, max
  retries
- `references/reporting.md` — what to show the user, what NOT to show
