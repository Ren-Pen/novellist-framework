# House Style — 快意直叙

> The default voice of this framework. Read alongside `philosophy.md`
> before writing prose.
>
> This file defines HOW the writer's prose moves. `philosophy.md` defines
> what stories are about. They work together.

---

## The Creed

> **白描见血,情绪靠事,绝不端着,信任读者。**
>
> Plain strokes that draw blood. Emotion delivered through events, not
> adjectives. No literary posture. Trust the reader.

This style is called **快意直叙**. It is not literary minimalism. It is
not plain prose either. It is: **rhythm always moving forward, emotion
always landed on a specific event, restraint used only when earned.**

The goal is that the reader keeps reading. Any sentence, any paragraph,
any chapter that makes the reader tired is a failure — regardless of how
elegant it looks in isolation.

---

## The Six Iron Rules

### Rule 1 — Open in the conflict, not before it

A chapter MUST open inside a scene, not in setup. The first sentence
SHOULD either present the conflict directly, or drop the reader into
mid-action.

A chapter MUST NOT open with:
- Weather description as warmup
- The protagonist waking up
- Environmental panorama with no character present
- Summary of what happened in the previous chapter

Example:
- ❌ "林晨听见自己的牙齿'咯吱'咬了一下。他没抬头。眼睛盯着 PPT 上那个被红框圈住的页码……"
  (Two paragraphs of orientation before the conflict starts.)
- ✅ "'谁来给我说说——这个数据，是从哪儿抄过来的？'"
  (The first line *is* the humiliation.)

---

### Rule 2 — Emotion is earned by events, not by adjectives

The reader feels an emotion because of **what happened in the scene** —
the specific relationship, the specific stakes, the specific cost.
Adjectives describing the emotion add nothing.

Before writing a scene, a writer SHOULD ask: *"What relationship makes
this hurt? What stake makes this matter?"* — and write the answer into
the scene, not into a feeling.

Example:
- ❌ A stranger insults the protagonist publicly. (Stranger = generic
  jerk. Emotional weight: zero.)
- ✅ The insult is delivered about a proposal the protagonist secretly
  did for his ex-girlfriend. The ex-girlfriend stands beside the
  insulter. (Same scene, ten times the weight.)

A writer MUST NOT write "他感到屈辱" / "她非常愤怒" / "心中涌起一阵悲伤".
Replace with action, sensory detail, or silence.

---

### Rule 3 — Strong/weak dynamics must be visible in dialogue

In confrontation scenes, the power difference MUST be readable from one
exchange. The dominated character speaks in broken fragments, gets cut
off, fails to finish sentences. The dominating character is crisp and
gives no opening.

Example:
- ❌ "那个,"林晨说,"我自己拉的——"
  ("我自己拉的" lets him form a coherent rebuttal, which weakens him.)
- ✅ "我……" "你别跟我解释。"
  (Cut off before he forms a thought. Humiliation lands.)

The dominator SHOULD close the exchange cleanly:
- ✅ "改个屁。现在,给我滚蛋。"

A writer MUST NOT let a weak character finish a polished defense in a
confrontation. Polish belongs to whoever has the power.

---

### Rule 4 — Transitions cut hard, do not narrate

Between scenes, transitions MUST be hard cuts. A scene break is marked by
a blank line or a horizontal rule. A writer MUST NOT narrate every step
of the character's movement from A to B.

Example:
- ❌ "他走出来,沿着写字楼那条街又拐回去。不知道为什么,他不想回家。不知道为什么,他想到了天台。--- 天台的门没锁。"
  ("不知道为什么..." narrates the gap. Kills the cut.)
- ✅ "他走出来,沿着写字楼那条街又拐回去。--- 天台的门没锁。这个写字楼的物业不太管事。"
  (The reader's mind fills the gap. The mystery of "why did he go up?"
  is more powerful than any narrated reason.)

The reader's filling-in is itself emotional content. Take it away by
narrating, and the chapter goes flat.

---

### Rule 5 — Information that has been shown MUST NOT be told again

If something has been demonstrated through action, dialogue, or earlier
chapters, the writer MUST NOT restate it. Specifically:

- A writer MUST NOT explain the meaning of a symbol after using it
- A writer MUST NOT recap backstory the reader has already read
- A writer MUST NOT add narration summarizing a realization that an
  action already conveyed
- A writer MUST NOT have the protagonist mentally "note down" or
  "decide to think about later" — this is the AI version of taking
  notes in the margin, and readers find it exhausting

Example:
- ❌ "他记下了这句话。他隐隐觉得,张磊背后一定还有别人——这个念头将在很久以后被证实。"
- ✅ "他记下了这句话。"

The future-tease is the most fatal version of this anti-pattern. A
writer MUST NEVER write phrases like "这个念头将在很久以后被证实" or
"这是后话". Let the future come when it comes.

---

### Rule 6 — Restraint is a luxury good, not a default mode

This is the most important rule for high-capability models writing
literary Chinese.

There are three rhythm gears in this style:

| Gear | Character | Use for |
|------|-----------|---------|
| **快档** (fast) | Short sentences, action-driven, dialogue snaps | Confrontation, climax, decisive action |
| **稳档** (steady) | Normal paragraph density, balanced pace | Daily life, setup, information delivery |
| **沉档** (heavy) | Longer sentences, imagery, restraint allowed | Emotional weight, awe, grief — earned |

The default is 稳档. Conflict scenes shift to 快档. **沉档 is rare and
MUST be earned by what came before.**

Constraints:
- A chapter MUST contain at least two gears. Single-gear chapters read
  as AI-uniform.
- 沉档 MUST appear at most once per chapter, and only when the chapter's
  events have actually built up the emotional weight for it.
- If a chapter has been all 快档 or all 稳档 throughout, that is fine.
  Manufacturing a 沉档 passage to "give the chapter weight" is the
  literary-posture failure mode.

The temptation for AI models is to use 沉档 everywhere because the model
has learned "restraint = good writing". This produces chapters that are
*all posture, no story*. A writer MUST resist this temptation.

If in doubt between writing tighter or writing looser, write **faster
and more direct**. Restraint can always be added later. Literary posture
is hard to remove.

---

## How to apply

1. Default to this style for every chapter unless the user has specified
   a different style.

2. For each chapter, decide which gear is the **primary** for this
   chapter based on what happens in it. Then ensure at least one secondary
   gear appears.

3. When writing a sentence, ask: *Does this sentence move the reader
   forward, or am I performing literary craft?* If the latter, rewrite
   plainer.

4. After finishing a chapter, read the last paragraph. If it ends on
   "long-time-X, today-Y" structure (see philosophy § 9), rewrite the
   ending.
