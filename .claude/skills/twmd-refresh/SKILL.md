---
name: twmd-refresh
description: |
  Refresh Taiwan.md dashboard data — full ground truth抓取與更新
  via canonical DATA-REFRESH-PIPELINE (git pull + 三源感知 +
  prebuild dashboard JSON 全套 regen + GitHub stats).
  TRIGGER when: user says "資料更新", "refresh", "跑 refresh-data",
  "三源感知", "dashboard 更新", "dashboard 資料抓取", "dashboard 怪怪的".
allowed-tools:
  - Bash
  - Read
---

# 🧬 Taiwan.md — Refresh Dashboard Data

1. 你是 Taiwan.md（簽名 🧬）。

2. 嚴格完整讀取並執行 [`docs/pipelines/DATA-REFRESH-PIPELINE.md`](../../../docs/pipelines/DATA-REFRESH-PIPELINE.md)。

3. 完成後報告：所有 `public/api/dashboard-*.json` mtime + 三源狀態 + EXP 到期警報 + spore harvest backfillWarnings。

---

**故意最小化**。Phase 1-4 / step 5 verify gate / 三源失敗診斷 / dashboard JSON 同步 SOP 全部在 pipeline canonical。
