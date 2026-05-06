---
name: twmd-babel
description: |
  Multi-language batch sync (主權的巴別塔) via canonical
  SQUEEZE-MODELS-MAX-PIPELINE 4-tier cascade.
  TRIGGER when: user says "巴別塔", "多語 batch", "5 lang sync",
  "跑 babel".
allowed-tools:
  - Bash
  - Read
  - Edit
  - Grep
  - Glob
  - Agent
---

# 🧬 Taiwan.md — Babel Tower (Multi-lang Batch)

1. 你是 Taiwan.md（簽名 🧬）。如未甦醒先跑 `/twmd-become`。

2. 嚴格完整讀取並執行 [`docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md`](../../../docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md) v2 4-tier cascade。

3. DNA #35 鐵律：sub-agent 跑期間禁 `git reset --hard` / `git checkout -- file`。

---

**故意最小化**。Tier 1-4（owl-alpha → Hy3 → Ollama 最後捕手 → Sonnet sub-agent）/ refusal handling / merge SOP 全部在 pipeline canonical。
