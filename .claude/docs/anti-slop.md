# Anti-Slop Guide

> Read this before writing prose. The goal is not to write "correctly" —
> it is to write in a way that does not feel machine-assembled.
>
> Keywords MUST, MUST NOT, SHOULD, SHOULD NOT, MAY follow RFC 2119.

---

## § 1 — The Core Belief

> **AI writes prose that is not bad — it is too good. Too smooth, too
> symmetric, too explanatory. The problem is not errors. The problem
> is uniform polish.**

Real human writing has rough edges. Spoken-language fragments. Jumps in
logic. Things left half-said. AI default-writes everything flat, even,
and explanatory. The work of avoiding AI slop is not "fix mistakes" — it
is "introduce real human texture".

---

## § 2 — The Ten Prevention Rules (write with these in mind)

### Rule 1 — Replace abstract emotion words with concrete actions
- ❌ 他感到一丝紧张
- ✅ 他的手指在裤缝上蹭了一下

### Rule 2 — No facial-expression templates (the worst Claude habit)
A writer MUST NOT write:
- 眼中闪过一丝 X
- 嘴角勾起一抹 X
- 眉头微皱
- 心中涌起一股 X
- 脸色 X (in narration)

Replace with: specific action, observed-from-outside description, or
nothing.

### Rule 3 — No literary-classical filler
A writer MUST NOT write 仿佛 / 犹如 / 宛若 / 一般 in default narration.
Use 像 if needed, or describe directly. Default-delete: 缓缓 / 微微 /
轻轻 / 淡淡 / 不禁. 90% of these can be removed with no loss. 深吸一口气
SHOULD be deleted in most contexts.

### Rule 4 — No judgment fillers
A writer MUST NOT write 不容置疑 / 显而易见 / 毫无疑问 / 不可否认.
Show the fact directly. The reader judges.

### Rule 5 — No summary or epiphany (the most AI-shaped move)
A writer MUST NOT write:
- 他终于明白...
- 她这才意识到...
- 此刻,他...
- 原来一切都是...
- 这一刻,他...

When the chapter ends, **do not have the character mentally summarize
what just happened**. The reader summarizes. Your job is to stop typing.

### Rule 6 — No 3+ parallel sentences
Three or more consecutive sentences with the same opening pattern, the
same length, or the same rhetorical structure → cut to one.

### Rule 7 — Vary paragraph length
A chapter MUST NOT have every paragraph the same size (e.g., all 4-6
sentences). Use 1-sentence paragraphs at moments of impact. Use longer
paragraphs in scene-setting. Uniform paragraph density = AI shape.

### Rule 8 — Minimize dialogue tags
Default-delete 他说道 / 她问道 / etc. where context is clear. Use action
beats instead.

### Rule 9 — Refuse vague-mystery language
A writer MUST NOT use 神色复杂 / 莫名的情绪 / 说不清的感觉 / 不知道为什么.
Either show the specific emotion, or leave the space blank.

### Rule 10 — No ending epiphany or sigh
The final sentence of a chapter MUST NOT be:
- 他想... / 他知道... / 他明白...
- 这一刻... / 在那一刻...
- A character realizing something internally with no external event

The ending MUST be a concrete action, image, line of dialogue, or
unresolved beat. See `emotion-formulas.md` § 2 for the six hook types.

---

## § 3 — The Time-Reversal Sentence Pattern (CRITICAL)

This is the most insidious AI-slop pattern in Chinese literary prose,
because it is structurally encouraged by the very things that make
fiction work (emotional engineering uses long-buildup + short-reversal
at the *story* level).

**The pattern:**
```
[Time anchor: 两年了 / 那时候 / 从前 / 搁两年前]
[Reversal: 今天 / 头一回 / 现在 / 这回]
[Short payoff sentence, often a single state]
```

Examples to recognize:
- 两年了。她头一回在他面前，把一句使唤的话咽了回去。
- 那时候这片灯，是别人的。
- 搁两年前，光是"你不一样了"这一句，他能感动得不行。
- 报的仇，到手了。可这会儿，他心里那块地方，空的。

**Why this is fatal:** Each instance individually lands. By the 3rd-4th
use in a novel, readers unconsciously identify the formula. The 10th
time it appears, the chapter feels "AI-written" even though the reader
cannot point to a single bad sentence.

**Constraints:**
- A chapter MUST NOT contain more than **one** time-reversal payoff in
  this exact structure.
- This pattern MUST NOT be used as a chapter ending. (See Rule 10.)
- If a writer wants to convey "things have changed", they SHOULD do it
  through *action* (the character does something they couldn't do
  before, with no narrated comparison) rather than this sentence
  pattern.

Better alternative — show change through behavior:
- ❌ "搁两年前，她一句话他就改口说行。今天他说了'下午有事'。"
- ✅ "'下午有事。'他说。" (Let the absence of the old "行" be the change.)

---

## § 4 — Banned Word Reference Table

For mechanical word-level scanning. Listed by category.

### 4.1 Tier-1 banned (replace on sight, with no exception except whitelist)

**情态类:** 仿佛 / 好像 / 犹如 / 宛若 / 一丝 / 一抹 / 些许 / 几分 / 隐约
**动作类:** 深吸一口气 / 缓缓 / 不禁 / 微微 / 轻轻 / 淡淡
**表情类:** 眼中闪过 / 嘴角勾起 / 眉头微皱 / 眉眼低垂 / 瞳孔微缩 / 脸色一变 / 面色复杂
**心理类:** 心中一动 / 心头一震 / 心下了然 / 心中暗道 / 心底泛起 / 不由得 / 心中涌起 / 莫名地
**判断类:** 不容置疑 / 不易察觉 / 显而易见 / 毫无疑问 / 不可否认 / 说不清道不明
**升华类:** 这一刻 / 在那一刻 / 他终于明白 / 她这才意识到 / 原来一切都是
**伪含蓄类:** 不知道为什么 / 说不清为什么 / 不知为何 / 莫名地就

### 4.2 Banned phrase templates

| Pattern | Example |
|---------|---------|
| "...,带着..." | "他说,带着一丝无奈" |
| "像 XX 一样" | "像刀子一样锋利" |
| "他的声音很轻,却像..." | (AI 最爱) |
| "仿佛能 X 一般" | "仿佛能穿透一切一般" |
| "X 的同时,Y" | "他说话的同时,手按在剑上" |
| "X 不语,只是 Y" | "他不语,只是看着远方" |
| "他知道..." (作章末句) | (see Rule 10) |
| "他想起..." (chained 3+ times in one section) | flashback chain |

### 4.3 Replacement strategies

| Original type | Replacement |
|---------------|-------------|
| Abstract emotion word | Concrete action |
| 感到 XX | Externalized expression |
| Adjective pile-up | Direct description (白描) |
| Written-language formality | Spoken-language version |
| Explanatory description | Leave blank (let reader infer) |
| 3+ parallel sentences | Keep strongest one |
| Summary / epiphany sentence | Delete |
| Complex emotion ("神色复杂") | One specific action |
| Time-passage filler ("时间仿佛凝固") | Direct time-skip ("三秒钟没人说话") |

---

## § 5 — Whitelist

If a project has a `.deslop-whitelist` file in the project root, words
listed there (one per line, exact match) are exempt from § 4.1 scanning.

Use this for:
- Proper names that happen to contain banned characters
- Deliberately stylized terminology in the world
- A character's signature speech tic

Example whitelist:
```
心中所想   # 修炼术语,角色用
一丝灵气   # 力量等级单位
```

---

## § 6 — The Self-Check (run mentally after writing)

A writer SHOULD run this check before saving the chapter:

1. Are there any banned words from § 4.1 that aren't deliberate? → replace
2. Does the chapter contain more than one time-reversal payoff (§ 3)? → cut
3. Does the chapter end on summary or epiphany (Rule 10)? → rewrite ending
4. Is every paragraph the same length? → vary
5. Does any 3+ parallel-structure run exist? → cut to one
6. Read the final paragraph alone. Does it sound like a tour guide
   wrapping up, or like someone typing under pressure? → if tour guide,
   rewrite

These checks are NOT exhaustive. They catch the most common slop
patterns. The `deslop-pass` subagent runs deeper checks after.

---

## § 7 — When to Break These Rules

A writer MAY break any rule in this file if breaking serves the chapter.
Specifically:

- A character who deliberately speaks in clichés (pompous official,
  poet) MAY use otherwise-banned phrases in their dialogue.
- A 沉档 passage (see house-style Rule 6, used at most once per chapter)
  MAY use longer sentences and 仿佛-style imagery deliberately.
- A flashback scene MAY use a "long-ago + now" structure once, if the
  scene genuinely requires temporal contrast.

Rule-breaking is a deliberate choice. A writer MUST NOT break a rule
because the AI default came out that way. Break rules to serve the
story; do not break rules out of habit.
