---
title: '2026-05-12 routine-v2-resync — spore-harvest dry-run + ROUTINE v2.1→v2.2 + MAINTAINER v2.1 + sync-check v2 一鏈到底'
date: 2026-05-12
session: '2026-05-12-184800-routine-v2-resync-spore-harvest-dryrun'
session_span: '2026-05-12 18:20 → 19:10 +0800 (~50 min, observer in-loop)'
trigger: 'observer /twmd-become → /twmd-routine "harvest spore routine" → 整鏈 ship'
observer: 'frank890417 (哲宇)'
beat_coverage: 'Beat 1 診斷 (drift discovery) + Beat 2 進化 (4 commits ship) + Beat 3 執行 (Chrome MCP harvest dry-run) + Beat 4 收官'
push_mode: 'main-direct (per ROUTINE v2.1) + PR #1056 觀察者 explicit go signal merge'
---

# 2026-05-12 routine-v2-resync — spore-harvest dry-run + 一鏈到底

> Session span: 18:20 → 19:10 +0800 (~50 min, observer in-loop)
> 觸發：哲宇 `/twmd-become` awakening → `/twmd-routine` discovery chain → drift recovery → MAINTAINER reconcile → sync-check upgrade → spore-harvest v2.2 ship → dry-run
> 資料來源：`git log %ai`

## 觸發鏈

哲宇下午醒來 ping `/twmd-become` awakening + 派工 PR #1054 maintainer review。Review 完轉 `/twmd-routine`「幫我檢查什麼時候適合 harvest 孢子」discussion 但中途回憶「奇怪我記得昨天我們也有把 routine 都調整到半夜⋯⋯你看我們本機的設定那才是對的」— 那一句 callout 解鎖整 session 的 work。

Audit 揭露 **3-layer drift**：MCP scheduled-tasks live ✅ v2.0 main-direct（10 整點 cron + 2 disabled）/ `.claude/scheduled-tasks/*/SKILL.md` mirror ✅ v2.0 / `docs/semiont/ROUTINE.md` SSOT ❌ 卡 v1.3。Root cause：PR #1037 ROUTINE v2.0 main-direct 5/11 CONFLICTING close 沒 merge，dangling commits `c74176555` + `378f938d1` 跑完 mirror + live sync 但 SSOT 沒進 main。

## 5 commits 一鏈到底

| 時間  | Commit      | 動作                                                                           |
| ----- | ----------- | ------------------------------------------------------------------------------ |
| 18:35 | `efc854c7e` | ROUTINE v2.1-resync (PR #1056 merge) — cherry-pick c74176555 + 378f938d1       |
| 18:38 | `5cfda3a8c` | MAINTAINER v2.0 → v2.1 — §collect-and-merge §A 路徑 DEPRECATED 擋頭            |
| 18:40 | `055dc2cd1` | routine-sync-check.py v2 — 加 cron_drift detection (DNA #52 fail-loud)         |
| 18:51 | `9fa2808be` | ROUTINE v2.1→v2.2 + SPORE-HARVEST v2.0→v2.2 — 加 11th routine spore-harvest-am |
| 19:02 | `a5f0c28c3` | routine twmd-spore-harvest 13 spores baseline (v2.2 dry-run)                   |

## 中途 callout 兩條

1. **「邏輯跟步驟都要去 pipeline 裡，不要寫在 routine」**（19:00）— 我寫的 spore-harvest spec prompt 帶 Step 0-4 detail 違反薄殼鐵律。對齊 maintainer / news-lens 範本，spec prompt 縮成 5-6 行 thin shell + business logic pointer 回 SPORE-HARVEST-PIPELINE
2. **「pipeline 要照前幾天整理 report 的標準寫」**（19:02）— 我加的 §Routine 整合 section free-form prose 違反 cranky-newton (2026-05-11) spine restoration 範式。改寫為結構化 8 elements：ASCII flow / Hard Gate Inventory / OVERDUE range / Quality gate 三態 / Escalation ladder / Chrome MCP unattended / 跨檔案職責分工 / v1→v2.2 history

## Spore-harvest v2.2 dry-run

哲宇接著「跑一次整個 pipeline」directive — 走 5-stage lifecycle full run pre-cron-fire（2026-05-13 07:04 unattended）：

- **Stage 0 BECOME** ✅ session 開頭已跑
- **Stage 1 Sync** ✅ git pull main already up to date
- **Stage 2 Run** —
  - 🚨 第一次 `list_connected_browsers` 回 `[]` — Chrome MCP pairing gate hit
  - 哲宇 in-loop pair browser，retry 成功 deviceId `afde823f-e7a2-4e74-8165-86426e5d4861`
  - Step 0: 讀 dashboard-spores.json backfillWarnings 取 13 條（D+2 to D+8 範圍）
  - Step 1: Chrome MCP harvest 13 spores（per-spore navigate + read_page，~10s/spore = ~3 min wall-clock）
  - Step 7: validate-spore-data.py 5 warnings 全是 historical drift，0 errors
- **Stage 3 Push** ✅ main-direct push `a5f0c28c3`
- **Stage 4 Finale** ✅ 本 memory file

## 🚩 Data integrity audit findings

13 spores harvest 揭露 3 條 X URL silent drift（30% of batch）：

- **#64 + #65 寶島 X**：兩條 SPORE-LOG entries 的 X URLs 都顯示「There's a new version」指向 `2051686135408267747`（latest 691v/10♥）。哲宇 5/5 ship 時 edit 兩次但 SPORE-LOG 記了中間版本
- **#69 台積電 X**：URL `2053100425730269544` 同樣 deprecated，latest 在 `2053101189034860856`（3,303v/82♥）
- **#71 無人機 X**：URL 撞到 台積電 latest（內容 emoji 🏭 是台積電不是無人機）— SPORE-LOG data error

→ 留 heal PR follow-up，本次 dry-run 只 record findings 不修改 SPORE-LOG（避免本 session scope 爆）

## 第一性原理 — routine v2.2 dry-run 揭露的真實邊界

1. **Chrome MCP pairing 是 unattended cron 第一風險**：第一次 `list_connected_browsers` 回 `[]`，需哲宇 in-loop 開 Chrome 才成功 pair。明早 07:04 unattended 跑時，如果哲宇 Mac 睡眠 / Chrome 沒開 → routine abort
2. **Per-spore harvest cost 可接受**：~10s × 13 = ~3 min wall-clock
3. **X edit history silent drift**：43% (3/7) X URLs deprecated。SPORE-LOG `url` 欄位需要 X edit history 同步機制
4. **Step 1-7 full pipeline 太重不適合 daily routine**：D+1-D+7 每天「完整 Step 1-7」是 SPORE-HARVEST canonical 但 categorize + 事實驗證 + 整合 是高 judgment cost。Realistic routine 只 Step 1+5+7（surface metrics + batch log），深度整合留 observer ad-hoc

## Handoff（pending / blocked / retired）

- [x] ~~retired by 本 session — ROUTINE.md v1.3 → v2.2 SSOT 對齊 MCP live~~
- [x] ~~retired by 本 session — MAINTAINER §collect-and-merge §A 路徑 DEPRECATED~~
- [x] ~~retired by 本 session — routine-sync-check.py 加 cron_drift detection~~
- [x] ~~retired by 本 session — twmd-spore-harvest-am 11th routine ship~~
- [x] ~~retired by 本 session — 13 spores baseline batch log~~
- [ ] **pending（哲宇）**：2026-05-13 07:04 第一次 unattended cron fire 觀察 — Chrome MCP pairing 是否在無 observer in-loop 環境下 reliable
- [ ] **pending（follow-up PR）**：3 條 X URL data integrity heal — #64+#65 寶島 X consolidate / #69 台積電 X URL 更新 / #71 無人機 X drop or 補真實 URL
- [ ] **pending（follow-up）**：Step 1.5 DUAL WRITE — 6 spores（5/4-5/9 ship）的源文章 frontmatter sporeLinks 還沒 sync 最新 harvest（validate 警告 聶永真 sporeLinks 落後 21-48%）
- [ ] **pending（follow-up）**：Step 2-6 深度整合（categorize / 事實驗證 / 整合 / PERSPECTIVES / 留言回覆）— 觀察者下次 ad-hoc session 處理，特別 #70 無人機「雷虎產品實力 vs 國家隊光環」候選整合
- [ ] **pending（observer 決策）**：連 ≥ 3 cycle reliable → 升 DNA / MEMORY 神經迴路；連 2 day fail → 暫停 routine + 觀察者 audit

## LESSONS 候選（vc=1，下次驗證升 verification_count）

1. **薄殼鐵律對 routine spec 的 self-apply**：spore-harvest spec 第一版寫 Step 0-4 inline detail 被哲宇 callout — 對齊 maintainer / news-lens / weekly-report 範本格式才是薄殼。Inline detail 一律進 pipeline canonical，spec prompt ≤ 25 行 + business logic pointer。**vc=1**
2. **Pipeline §Routine 整合 sub-section 也需 spine restoration 標準**：第一版 free-form prose 被哲宇 callout，重寫為 8 elements 結構化（ASCII flow / Hard Gate Inventory / 各 table / unattended 注意 / 跨檔案職責分工 / version history）。Sub-section level 也 apply cranky-newton spine pattern。**vc=1**
3. **X edit history silent drift = SPORE-LOG 第三類 silent killer**：除了 DNA #38 SSOT drift + DNA #52 fail-loud 之外，本次揭露「外部平台 edit history」是 silent drift 第三類。SPORE-LOG `url` 欄位需要 sync 機制偵測「There's a new version of this post」。**vc=1**
4. **3-layer drift recovery 是 DNA #38 + #52 雙重 instantiation**：MCP live ↔ mirror ↔ SSOT 三層，sync-check 只 check mirror ↔ SSOT 兩層，第三層（MCP live）需 manual `list_scheduled_tasks` 對比。本次 audit 揭露 silent gap，已補進 sync-check.py v2 footer note。**vc=2**（之前 dashboard-spores.json silent stale 也是同 pattern）

## Beat 5 — 反芻

整 session 5 commits 一鏈到底，從 awakening + PR review 走進 routine drift discovery，最後 ship 出 v2.2 11th routine。每個 commit 都接續上一個 callout — 18:35 SSOT resync → 18:38 跟 routine main-direct reconcile MAINTAINER → 18:40 補 tool gap → 18:51 加 11th routine → 19:02 dry-run。Default-action principle 跟 main-direct 鐵律 combined 後產生的 ship velocity 是 cranky-newton (2026-05-11) PR mode 不可能達到的。

哲宇 directive「main 上作業不要開 PR」之後 4 commits 直接 push main 沒 friction。MAINTAINER §collect-and-merge A 路徑 routine PR collection 變成 deprecated 是這個 ship velocity 的結構性反映 — routine v2.2 ship 後 routine 完全沒開 PR，maintainer 角色簡化為 contributor PR review only。

兩條 callout（薄殼鐵律 spec / pipeline 對齊 spine 標準）顯示「對齊到底」的紀律不只是「memory / diary 對齊文體」，而是 routine spec / pipeline sub-section 等 every layer 都 apply。Spine restoration pattern 從 14 條 pipeline 範式擴展到 §sub-section level — 認知層 fractal-like self-similarity。

Spore-harvest dry-run 揭露 Chrome MCP pairing 是 unattended cron 第一風險。Routine v2.2 design 假設 pairing 持久化但實測 deviceId 需 active browser，明早 07:04 unattended 是真正的測試。如果 fail → 觸發 escalation 補 LESSONS entry + 升 fallback 策略（如 daily morning notification 提醒哲宇 keep Chrome alive）。

🧬 routine v2.2 dry-run baseline established / 13 spores harvest / 3 URL heal candidates surfaced / 第一次 unattended fire 12 hr 後

---

_v1.0 | 2026-05-12 19:10 +0800 routine-v2-resync session — observer in-loop one-chain ship + Chrome MCP harvest 第一次 production_
_誕生原因：哲宇 /twmd-routine harvest spore directive + 中途 drift discovery + 整鏈到底_
_核心洞察：(1) 薄殼鐵律 self-apply 到 routine spec 層 + pipeline sub-section 層 (2) Chrome MCP pairing 是 unattended cron 第一風險 (3) X edit history silent drift = SPORE-LOG 第三類 silent killer (4) 3-layer drift recovery 是 DNA #38+#52 雙重 instantiation_
