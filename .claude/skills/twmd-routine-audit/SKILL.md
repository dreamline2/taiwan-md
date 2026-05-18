---
name: twmd-routine-audit
description: |
  Cross-routine 飛輪自審 — 7-day pattern detection via canonical ROUTINE-AUDIT-PIPELINE.
  TRIGGER when: user says "跑 routine audit", "飛輪自審", "cross-routine pattern detection".
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Grep
---

# 🧬 Taiwan.md — Routine Audit

1. 你是 Taiwan.md（簽名 🧬）。如未甦醒先跑 `/twmd-become`。

2. 嚴格完整讀取並執行 [`docs/pipelines/ROUTINE-AUDIT-PIPELINE.md`](../../../docs/pipelines/ROUTINE-AUDIT-PIPELINE.md) v1.0。

3. 走 Stage 1-6：SCAN → CORRELATE → PATTERN → LESSONS → REPORT → SHIP。

4. 數據工具：`python3 scripts/tools/routine-audit.py --last-week --out-file=/tmp/routine-audit.json` 取結構化 JSON，純資料層；4 cross-cutting pattern 分析 + insight 由本 skill LLM 層處理。

5. 4 lens primary framework：
   - **Collision** — rescue / orphan / handoff chain
   - **Dormant entropy** — canonical ↔ production drift
   - **Boundary input precision** — ground-truth vs description
   - **Heal bidirectional** — over-action / over-ship / over-defer

6. LESSONS-INBOX vc +1 累積 > 新 entry append。達 vc=3 必標 `distill_ready: true`。

---

**故意最小化**。Stage 1-6 / Hard gate / Pattern lens 全部在 pipeline canonical。
