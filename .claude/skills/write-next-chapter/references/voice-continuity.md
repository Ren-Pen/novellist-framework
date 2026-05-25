# Voice Continuity

When the skill reads the last 2 chapters (via
`python .claude/tools/get_recent_chapters.py 2`), the purpose is voice
continuity — making sure chapter N+1 sounds like it was written by the
same person who wrote chapter N.

This is NOT the same as plot continuity, which is `continuity-keeper`'s
job after the chapter is written.

---

## What to extract from recent chapters

When the skill reads the recent chapters as part of context gathering,
it MUST notice:

1. **Sentence rhythm** — were the last 2 chapters mostly short
   sentences, mostly long, or mixed? Match the general feel; vary
   deliberately.

2. **Recent vocabulary choices** — what specific words has the writer
   used a lot? If chapter 9 had "搁这儿胡想啥呢" once, chapter 10 had
   the same construction once — chapter 11 should NOT use it again.
   Recurring phrases lose their charge.

3. **Recent imagery** — what sensory anchors appeared? If chapter 9
   was "海风 + 柴油味" and chapter 10 was also "海风 + 柴油味",
   chapter 11 SHOULD shift to a different sensory anchor.

4. **Character voice samples** — when a returning character speaks,
   they MUST sound like the same person. If 王心怡 was characterized
   by "细烟 + 转身 + 软软的语气", that combination is her signature.

5. **What hooks have been used recently** — see emotion-formulas § 2.
   The same hook type MUST NOT appear in three consecutive chapters.

---

## What NOT to copy from recent chapters

A writer SHOULD vary:

- **Setting** — don't open three consecutive chapters in the same place
- **Time of day** — don't have three consecutive openings at dusk
- **Weather** — don't have three consecutive chapters with rain
- **Scene structure** — don't have three consecutive chapters of
  "scene A → scene B → final hook"
- **Emotional climax position** — don't have three consecutive chapters
  where the emotional peak is in the same act
- **Specific sentence patterns** — see anti-slop § 3 for the
  time-reversal pattern in particular

---

## A simple test

After reading the recent 2 chapters, the skill SHOULD be able to
answer:

1. What did chapter N-1 end on?
2. What did chapter N-2 end on?
3. What is one thing chapter N+1 must NOT repeat from chapter N-1?

If any of these can't be answered, re-read the recent chapters more
carefully.
