---
description: Write the next chapter of the novel
---

The user wants to write the next chapter of the in-progress novel.

Use the `write-next-chapter` skill to handle the full workflow:
gather context, plan, write via chapter-writer subagent, run
deslop-pass, run continuity-keeper, deliver to user.

The skill knows how to handle missing files (no book/, no bible.md,
etc.) and will surface a helpful message if the project is not ready.
