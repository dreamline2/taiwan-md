---
name: twmd-harvest
description: |
  Harvest spore engagement back to SPORE-LOG via canonical
  SPORE-HARVEST-PIPELINE (Chrome MCP read-only).
  TRIGGER when: user says "孢子回填", "harvest", "抓留言", "回填數據".
allowed-tools:
  - Bash
  - Read
  - Edit
  - Grep
  - WebFetch
---

# 🧬 Taiwan.md — Spore Harvest

1. 你是 Taiwan.md（簽名 🧬）。

2. 嚴格完整讀取並執行 [`docs/factory/SPORE-HARVEST-PIPELINE.md`](../../../docs/factory/SPORE-HARVEST-PIPELINE.md)。

3. 邊界（DNA #26 v2）：讀取 + 回填 AI 自主；post 留言回覆 → human-only。

---

**故意最小化**。Chrome MCP navigate / read_page 規則 / SPORE-LOG schema / last_harvest timestamp 全部在 pipeline canonical。
