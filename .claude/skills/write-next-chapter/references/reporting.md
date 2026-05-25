# Reporting to the User

How the skill shows the finished chapter to the user.

---

## What to show

In this exact order:

1. **Chapter number and title** as a single line:
   ```
   第 N 章 <title>
   ```

2. **The full chapter text** — read the file and display its prose
   contents. Strip the YAML frontmatter (the `---` block at the start)
   before showing.

3. **One forward-framing sentence**, from the chapter-writer's return
   value. Example:
   > 本章主要展开 XX，下一章会进入 XX。

That's all. No headers like "## Chapter Delivered". No metadata blocks.
No status indicators.

---

## What NOT to show

The skill MUST NOT show:

- ❌ The planning brief (it's internal)
- ❌ The deslop-pass severity report (internal)
- ❌ The continuity-keeper diff report (internal)
- ❌ Word counts (unless out of range — see error-handling.md)
- ❌ "Hope you like it" / "Let me know what you think" prompts
- ❌ Lists of what changed in bible.md
- ❌ Lists of newly tracked foreshadowings

The reader is reading a novel. They are not auditing a workflow.

---

## What NOT to ask

The skill MUST NOT ask:

- ❌ "你觉得这章怎么样?"
- ❌ "要不要修改?"
- ❌ "希望符合你的期待"
- ❌ "需要继续写下一章吗?"
- ❌ "对这个走向有意见吗?"

The user will speak up if they want changes. Constant questioning
breaks immersion. The single forward-framing sentence is the only
"pointer to the future" the user gets.

---

## Special cases that require speaking up

The skill MUST speak up (with a brief explanation, before delivering)
in these cases only:

1. **deslop-pass triggered 2 rewrites and still severe** — see
   error-handling.md § Rewrite Loop.

2. **continuity-keeper found a contradiction** — see error-handling.md
   § Contradictions. In this case, the chapter is NOT delivered until
   the user resolves the contradiction.

3. **Word count is below 2000 or above 4000** — note before delivering:
   > 这一章字数 <N>,略低于/高于通常范围。原因可能是 <一句话推测>。
   > 你读一下,有需要可以让我调整。

4. **The bible or outline shows a major change just made** by the
   continuity-keeper (e.g., a foreshadowing got retired because it
   couldn't be paid off, or a major character changed status) —
   mention briefly:
   > 顺便说一下,我把 FS-XX (那个 X) 标记成 retired 了,因为最近 6 章
   > 都没有合适的回收点。如果你不同意,告诉我。

In all other cases, deliver silently.

---

## Tone

The forward-framing sentence MUST be concrete. Avoid:

- ❌ "下一章会有更多精彩内容"
- ❌ "敬请期待"
- ❌ "故事将进入新的阶段"

Good examples:
- ✅ "本章主要展开林晨第一次主动出击,下一章会进入大窑湾码头那条线。"
- ✅ "这章是过渡章,把 FS-04 那个港口的旧人埋下了。下一章会有一场对手戏。"
- ✅ "本章把张磊收尾,下一章主角的目标转到周维那边。"

Be specific. The user is reading; tell them what's next.
