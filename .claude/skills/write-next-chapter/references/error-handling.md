# Error Handling

How to handle failures from each subagent.

---

## Rewrite Loop (from deslop-pass: severe)

If `deslop-pass` returns severity = severe:

1. The rejected chapter has been moved by deslop-pass to
   `book/chapters/_rejected/<filename>`.
2. Read the rewrite request — it contains specific problem patterns
   and rewrite instructions.
3. Compose an updated brief: original brief + a `Rewrite instructions`
   field with the deslop-pass guidance.
4. Re-invoke `chapter-writer` with the updated brief.
5. After the rewrite, re-invoke `deslop-pass`.

**Maximum 2 rewrite cycles per chapter.**

If after 2 rewrites the chapter still triggers severe:

1. Stop the loop.
2. Surface to the user:
   *"本章我已尝试 2 次重写,仍然检测到严重的 AI 味问题。我把当前最好
   的一版交给你,你读一下告诉我下一步怎么处理。"*
3. Show the user the most recent attempt (whichever was the best —
   judgment call).
4. Log to `book/decisions.log`:
   ```
   [YYYY-MM-DD, Ch N] DESLOP-FAIL: 2 rewrites attempted, still severe.
   Surfaced to user.
   ```

---

## Contradictions (from continuity-keeper)

If `continuity-keeper` returns contradictions:

1. STOP. Do NOT proceed to Step 7 (delivery).
2. Surface to the user clearly. Format:

   ```
   写到第 N 章时,continuity-keeper 发现以下矛盾:

   1. <description of contradiction 1>
      - Bible 当前: <existing version>
      - 本章写法: <new version>

   2. <description of contradiction 2>
      ...

   你想怎么处理?
   a) 改本章正文,让它符合 bible
   b) 更新 bible 接受新版本(但要检查前面章节会不会冲突)
   c) 视为有意为之(角色撒谎 / 不可靠叙述者),记录到 decisions.log

   告诉我你的选择。
   ```

3. Wait for the user's direction. Do NOT make this decision yourself.

---

## Missing files

### Missing bible.md

The user has not started a novel. Tell them:

> 看起来 book/bible.md 还不存在。开新书要先有 bible。
> 你可以用 /new-novel 让 story-architect 建一个,或者手动写一份
> (模板在 `.claude/docs/templates/bible.md`)。

Stop.

### Missing outline.md

If bible.md exists but outline.md doesn't, generate a stub outline from
the template:

```bash
cp .claude/docs/templates/outline.md book/outline.md
```

Tell the user:
> 我注意到 book/outline.md 不存在,我用模板建了一份空的。你可以填
> 一下接下来要写什么,或者直接让我根据 bible 推断下一章。

Wait for direction.

### Empty chapters/ but outline mentions Chapter 1

This is Chapter 1. Proceed normally — `next_chapter_number.py` will
return `1` and `get_recent_chapters.py 2` will return empty output.

---

## Subagent fails to return

If a subagent returns no content or returns an error:

1. Retry once.
2. If it fails again, surface to the user:
   *"<subagent name> 调用失败。错误信息: <error>. 我建议手动检查
   <relevant file>。"*
3. Do NOT proceed to next step.

---

## Word count out of range

After `chapter-writer` saves, the skill MAY verify the word count:

```bash
python .claude/tools/word_count.py book/chapters/<file>
```

If the count is:
- Below 2000: chapter is too thin. Surface to user, do NOT auto-retry.
- 2000-2500: borderline. Note in delivery but accept.
- 2500-3500: ideal range.
- 3500-4000: borderline-long. Accept.
- Above 4000: chapter is too long. Surface to user, do NOT auto-retry.

In the "surface to user" cases, deslop-pass and continuity-keeper still
run normally — the issue is just for awareness.
