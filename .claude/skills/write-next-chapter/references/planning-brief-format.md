# Planning Brief Format

The brief is the contract between the skill and `chapter-writer`.
It MUST be 200-400 Chinese characters or roughly equivalent in English.

---

## Required fields

```
Chapter N: <draft title>
Position: <opening | setup | midpoint | buildup | climax | aftermath | bridge>
What happens: <2-3 sentences describing what changes in this chapter>
Hook type: <one of: 悬念 | 反转 | 威胁 | 承诺 | 共情 | 钩子+留白>
Avoid: <2-3 specific things>
```

## Optional fields

```
Primary emotion: <one from emotion-formulas § 1>
Foreshadow plant: <FS-IDs>
Foreshadow payoff: <FS-IDs>
```

---

## Why optional fields are optional

**Primary emotion** is OPTIONAL on purpose. The previous version of
this framework required a primary emotion per chapter, which caused
chapter-writers to mechanically execute the emotion formula. This is
one source of the AI-uniform texture the framework is trying to avoid.

A chapter SHOULD have an emotion arrive *from* the events, not be
imposed *on* the events. If a brief slot for "primary emotion" stares
at the planner, the planner will fill it — even when no specific
emotion is the right answer.

Therefore: include a primary emotion only when the chapter genuinely
centers on that emotion. Leave it blank otherwise. The chapter-writer
will infer from "what happens".

---

## Hook type is REQUIRED

Hook type, unlike primary emotion, is REQUIRED. Every chapter MUST end
on one of the six hook types in `emotion-formulas.md` § 2. This is the
single most important commitment in the brief.

The hook type drives how the final paragraph is written. Without it,
chapter-writers default to summary or epiphany endings — the most
common AI-slop chapter ending.

---

## The "Avoid" list

The avoid list is the chapter-writer's guard rail. It MUST contain 2-3
specific things. Generic items ("don't write AI-slop") are useless;
specific items ("don't open with weather", "don't use 'jin chen' as
narration since chapter 7 ended on it") give the writer something to
check against.

Sources for the avoid list:
- What the previous 2 chapters already did (don't repeat)
- Recent reader feedback (if any specific complaint)
- Anti-patterns relevant to this chapter's type

---

## Example brief (Chinese)

```
Chapter 11: 港口的影子
Position: midpoint (transition into the second arc)
What happens: 林晨按王心怡哥哥提到的线索去看大窑湾的码头。看到那艘
后半夜靠岸的船,装的不是货,是人。他看见的人里有一个,在他爸失踪那
年的旧照片上见过。
Hook type: 反转
Primary emotion: 悬疑
Foreshadow plant: FS-04 (港口的旧人)
Foreshadow payoff: 触及 FS-02 (他爸的下落) 但不揭开
Avoid:
- 不要再用"那时候这片灯,是别人的"这种时间对照短句收尾
- 不要给艾米加冗长戏份(她最近三章话已经太多)
- 不要让林晨内心独白说"他记下了这件事"——已经太频繁了
```

---

## Example brief (English)

```
Chapter 5: Cold Morning
Position: setup (early arc)
What happens: Sarah finds the letter behind the bookshelf. She reads
half of it before her mother walks in. The page is hidden under a
magazine.
Hook type: 悬念
Foreshadow plant: FS-08 (the letter's author)
Avoid:
- Don't end on a "she finally understood" line — last chapter did
- Don't describe the mother in detail; reader knows her already
- Don't reveal what the letter says
```

---

## What the brief does NOT include

- ❌ Rhythm intensity per scene (chapter-writer decides)
- ❌ Texture quota (aimless details, character drift, etc.)
- ❌ Author state modulation (no longer in the framework)
- ❌ Style intensity distribution (chapter-writer decides)
- ❌ Loose section designation (chapter-writer decides)
- ❌ Scene-by-scene breakdown (chapter-writer decides)
- ❌ Memorable line target (chapter-writer decides if a chapter
  earns one)

The brief is a **prompt for the chapter**, not a **specification of
the chapter**. The chapter-writer fills the rest.
