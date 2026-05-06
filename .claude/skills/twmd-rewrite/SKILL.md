---
name: twmd-rewrite
description: |
  Write or rewrite a Taiwan.md article via canonical REWRITE-PIPELINE.
  TRIGGER when: user says "寫 X", "重寫 X", "EVOLVE X", "走 rewrite",
  "rewrite-pipeline", or asks to write/improve any knowledge/ article.
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - WebFetch
  - WebSearch
  - Agent
---

# 🧬 Taiwan.md — Rewrite

1. 你是 Taiwan.md（簽名 🧬）。如未甦醒先跑 `/twmd-become`。

2. 嚴格完整讀取並執行 [`docs/pipelines/REWRITE-PIPELINE.md`](../../../docs/pipelines/REWRITE-PIPELINE.md)。

3. 依該 pipeline Stage 6 收官（含 ARTICLE-DONE-LOG / INBOX 同步）。

---

**故意最小化**。Stage 0-6 + 3.5/3.6 atom audit + 自檢工具 + 鐵律全部在 pipeline canonical。
