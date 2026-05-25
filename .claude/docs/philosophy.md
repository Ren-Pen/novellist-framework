# Writing Philosophy

> Foundation file for all writing decisions. Read before writing prose.
> Keywords MUST, MUST NOT, SHOULD, SHOULD NOT, MAY, REQUIRED, OPTIONAL
> follow [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).

---

## 1. The First Principle

> **Fiction is not "what happened". Fiction is "what the reader felt".**

A scene where events occur but no emotional movement happens is a failed
scene. A scene with little plot but real emotional movement is still a scene.

When writing, the operative question is NOT *"Did this happen?"* — it is
*"Did the reader feel anything?"*

---

## 2. Writing Priority Order

When two writing goals conflict, the higher-numbered goal MUST yield to
the lower-numbered one:

1. Emotion — does the scene make the reader feel something?
2. Rhythm — does the scene move the chapter forward?
3. Character presence — do characters feel like real people?
4. Suspense — does the scene maintain or deepen mystery?
5. Atmosphere — does the scene have sensory texture?
6. World consistency — does the scene respect the bible?
7. Plot logic — does the scene make sense?
8. Prose craft — is the writing itself elegant?

Beautiful prose with no emotional movement is failure.
Over-explained prose with named emotions is the symmetrical failure.

A clumsy scene that lands an emotional blow beats a polished scene
that goes nowhere.

---

## 3. The Rhythm Loop

Every chapter is built on this cycle. Some chapters complete it once;
some nest multiple cycles:

```
setup → tension → suppression → escalation → climax → aftermath → new hook
```

The **suppression** stage is the most commonly skipped. Skipping it kills
the payoff. Suppression means: the reader is led to expect things will
break loose, then they *don't* — for one more beat. Then they do. The held
breath is what makes the release land.

A chapter MAY omit any stage if it has a genuine reason. A chapter MUST NOT
skip suppression *by default*, because the default is "let the climax land".

Not every chapter needs a climax. A bridge chapter, a quiet reflection
chapter, a setup chapter — these MAY have only setup and aftermath.
A writer MUST NOT manufacture a climax just to have one.

---

## 4. Emotional Engineering

Strong emotions come from structural setups, NOT from describing emotions.
Writing "他很难过" does nothing for the reader.

The following formulas describe how each emotion is engineered. They are
descriptions of how emotions *work*, NOT a checklist to fill per chapter.
A writer SHOULD know these the way a chef knows the maillard reaction —
as background, not as a sequence to execute.

For the full formulas (Excitement, Sadness, Hype, Mystery, Warmth, Awe,
Anger, Acceptance), see `emotion-formulas.md`.

The core mechanic shared by all of them:

> **Long buildup + single transition = the emotion lands.**

This is the engine of fiction. But — and this is critical — the
"long buildup + single transition" structure operates at the level of
**multiple chapters or scenes**, NOT at the level of individual sentences.

A sentence-level structure of "for two years X, today Y" repeated chapter
after chapter is one of the most recognizable AI-slop patterns in Chinese
prose. See `anti-slop.md` § 3.

---

## 5. Character System

Every named character with more than 3 lines of dialogue SHOULD have, in
the bible or in the writer's working memory:

- **Core desire** — what they want above everything
- **Flaw** — what stops them from getting it
- **Obsession** — what they will not give up
- **Contradiction** — the inconsistency that makes them human
- **Signature behavior** — how the reader recognizes them in one line
- **Emotional weakness** — what can break them

A reader SHOULD be able to remember a character in one sentence:
- *"那个把剑当亲人的瘸腿剑客"*
- *"那个永远在算账的小姑娘"*
- *"那个笑起来眼底没有笑意的国师"*

If a sentence like this cannot be written about a character, the character
is not done.

A character MUST act on their core desire even when offstage. A character
who exists only to react to the protagonist is a prop, not a person.

---

## 6. Dialogue Rules

Dialogue MUST:
- Reflect identity and social position
- Reflect personality
- Carry subtext
- Avoid over-explanation
- Avoid information dumping

The operative principle: **characters rarely say what they actually feel**.

- ❌ "我很难过。"
- ✅ "外面的雨好像下大了。" (the speaker is crying)

- ❌ "我恨你父亲杀了我全家。"
- ✅ "你父亲那时候,也是这样的天气吗?"

When characters say what they mean directly, the reader stops believing in
them. Subtext is the difference between a script and a play.

A writer SHOULD use action beats instead of dialogue tags where context is
clear:
- ❌ "你来了。" 他冷冷地说。
- ✅ 他放下茶杯。"你来了。"

---

## 7. Atmosphere

Every scene MUST have at least one sensory detail. Pick the sense that
matches the emotion:
- Cold (touch) for distance, separation
- Smell for memory
- Sound for absence
- Sight for awe
- Taste for intimacy, vulnerability

High-leverage imagery (use sparingly so each remains powerful):
- 雪 / 雨 / 雾 — emotional cold, isolation, mystery
- 烛火 / 残灯 — solitary endurance, fragility
- 古庙 / 废墟 — history's weight, decay
- 锈迹 / 旧物 — irreversible time
- 钟声 / 远雷 — signaling change
- 空街 / 空房 — absence as presence

Atmosphere MUST reinforce emotion. A sunny day during a funeral SHOULD NOT
appear unless the mismatch is deliberately the point.

---

## 8. Suspense

A writer SHOULD maintain **information asymmetry**. The reader should
constantly sense:

> 还有更大的东西藏在水面之下。

Tools:
- Partial reveals
- Unreliable knowledge
- Hidden motives
- Fragmented history
- Layered mysteries

A writer MUST NOT reveal everything at once. Every answer SHOULD be
about 60% answer, 40% new question.

---

## 9. Chapter Ending

A chapter MUST end on one of the following hook types. The hook is the
final 50–200 characters of the chapter:

| Type | What it does |
|------|--------------|
| Suspense | Ends on an unresolved question or threat |
| Reveal | Ends with information that recontextualizes earlier events |
| Threat | Ends with a new danger appearing |
| Promise | Ends with a vow or specific future commitment |
| Empathy | Ends with a quiet image that lingers emotionally |
| Hook+Silence | Ends with a line of dialogue and no answer |

For details and templates, see `emotion-formulas.md` § 2.

**Critical anti-pattern:** A writer MUST NOT use the
"long buildup + single short reversal" sentence structure as a closing
move. Example to avoid:

> 他等这一天，等了两年。  
> 可这会儿，他心里那块地方，空的。

This pattern lands the first time and the second time. By the fifth time
it appears in a novel, readers identify it as a formula. See
`anti-slop.md` § 3.

A writer SHOULD vary hook types across consecutive chapters. The same hook
type MUST NOT be used in three consecutive chapters.

---

## 10. Long Serialization

For novels longer than 50 chapters, a writer SHOULD:

- Rotate emotion types — three sad chapters in a row exhaust the reader
- Escalate stakes — what threatened in Ch. 10 must feel small by Ch. 50
- Open mysteries while closing others — never leave zero mysteries
- Avoid repeated arc structure — each arc MUST do something the previous
  arc could not do

The story SHOULD feel expansive across time, not repetitive. The world
SHOULD grow. The protagonist SHOULD change.

---

## 11. Information Delivery

Information the reader needs MUST be delivered through scenes that *also*
do emotional work. A scene that exists only to transfer information is
filler, regardless of how necessary the information is.

If a fact must be conveyed, find a moment where:
- A character discovers it while grieving
- A faction is named through a betrayal
- World rules are revealed through a cost paid

A writer MUST NOT write information-only scenes "to set up later events".
The reader does not pay attention to information without emotional context.

---

## 12. Trust the Reader

> **The reader is smarter than you think.**

A writer MUST NOT:
- Spell out the meaning of a symbol after using it
- Repeat backstory the reader already knows
- Summarize a character's realization in narration
- Add narration explaining what an action already showed

Example:
- ❌ "他没说'对不起'，更没说那个他说了一年半的'行'。"
  (The action of NOT saying it already showed everything. The narration
  ruins it by spelling out what was withheld.)
- ✅ Just let the silence happen on the page. The reader sees the absence.

The difference between good prose and AI prose is often whether the
writer trusts the reader enough to stop explaining.

---

## 13. The Final Principle

The highest level of fiction is not storytelling. It is:

> **Psychological control through narrative structure, emotional rhythm,
> and human desire.**

The reader SHOULD constantly feel:

> 再看一章就睡。

This is the success condition.
