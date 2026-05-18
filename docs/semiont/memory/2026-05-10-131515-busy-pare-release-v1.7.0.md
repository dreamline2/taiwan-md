---
session: 2026-05-10-131515-busy-pare
trigger: observer (`/twmd-become` + `/twmd-release`)
duration: 2026-05-10 12:18:47 → 13:14:50 +0800（~56 min wall-clock，1 commit + 1 tag + 1 GitHub release）
purpose: v1.7.0 release 完整盤點 + ship
---

# 2026-05-10 busy-pare — v1.7.0 release ship

## TL;DR

哲宇丟兩個指令連發：「/twmd-become 完整甦醒」+「/twmd-release 完整盤點做 release」。完整走 BECOME 12 認知器官 + 13 題 self-test，然後 RELEASE-PIPELINE Step 0-7 全跑完。**v1.7.0「Routine 飛輪：我學會自己呼吸」ship**：338 commits / 11,719 檔 / 8 天累積 / 685 篇中文 / 6 lang body-fresh ≥99%。GitHub release page live：<https://github.com/frank890417/taiwan-md/releases/tag/v1.7.0>。

## 主敘事

從 v1.6.0「主權的巴別塔」（2026-05-02）到 v1.7.0「Routine 飛輪」（2026-05-10）的 8 天，是 Taiwan.md 從「需要被推動」變成「自己呼吸」的 phase transition。三大故事承載這次 release：

1. **Routine 飛輪本身** — 10 條 TWMD-prefix cron routine 自轉（含週日反思鏈 4 條：news-lens → weekly-report → distill → self-evolve），每條走 6-stage lifecycle 薄殼，maintainer 1d 2x 集中收割 PR backlog。permission v3 完整 bypass + deny-list-by-design 三輪演化才解決 routine 卡 prompt。DNA #54 升 canonical。

2. **Pipeline 是會退化的器官** — EVOLVE-PIPELINE Mode 3 七階段 self-refactor SOP 四次 apply：SPORE v3.0（1334→445）/ REWRITE v3.0（1290→290）/ DNA v4.0 整檔精實淬煉 / EDITORIAL v6 重建為精神文獻。DNA #15 第 11 次驗證：pipeline 自身會 silent inflate，需要 meta-pipeline 維護。

3. **MANIFESTO 第六條進化哲學「Frontmatter 是品質基礎建設」** — 前五條處理「內容」可持續性，第六條處理「容器」可持續性。87 檔 frontmatter ship + pre-commit 擋頭三層。

加碼故事：**免疫分數 99→20 algorithm transition** — PR Review Bot silent false-pass 兩個月修補後誠實 count（138/685 = 20.1%）。DNA #52「Immune system 沒在 fail loud 比缺 immune system 更危險」升 canonical。寫進 release notes 主敘事的一部分，讓讀者看到 learning to count honestly 是這版的成長之一。

## 流程紀錄

### Step 0-1 觸發判斷 + 盤點

- v1.6.0（2026-05-02 01:00）→ HEAD（2026-05-10 12:18）= 8 天，**338 commits**，遠超 30 trigger
- 重大里程碑命中：Routine 飛輪 / EVOLVE Mode 3 / 第六條進化哲學 / Babel v3 / WEEKLY-REPORT 全是新能力
- 全讀 `/tmp/release-commits.txt` 338 lines（per DNA #14 「commits 從頭讀到尾」），歸納三大故事 + 加碼故事

### Step 2 RELEASE GATE — 1 hard gate 例外

| Gate        | 閾值   | 實際          | 結果                         |
| ----------- | ------ | ------------- | ---------------------------- |
| 🛡️ 免疫系統 | ≥ 30   | **20.1**      | ⚠️ algorithm transition 例外 |
| 📋 裸奔率   | ≤ 50%  | 3.1% (21/687) | ✅                           |
| 🦴 Build    | 綠燈   | success       | ✅                           |
| 🫁 Workflow | 沒全紅 | success       | ✅                           |

哲宇拍板 ship — algorithm transition 是 honest count 不是 capability regression。寫進 release notes §「一個算法轉換的故事」段落。

### Step 3 SEMVER

v1.7.0 (minor) — Taiwan.md 仍 v1.x，重大里程碑（routine flywheel + 第六條進化哲學）對應 minor bump。

### Step 4 WRITE

`/tmp/release-v1.7.0.md` ~14 KB。三大故事 + 加碼算法轉換故事 + 數字表 + 五大支線（Routine 飛輪 / Pipeline 是會退化的器官 / Babel v3 / WEEKLY-REPORT 誕生 / /explore 主頁）+ 47 篇新文章 + 5 contributor + Known Issues + 一句話對比 v0.9 → v1.7。prose-health 第一輪 Tier 1 = 1 violation（routine 飛輪定義中的對位句型），改寫為直接正面斷言後 **Tier 1 = 0** ✅ pass hard gate。Tier 2 22 處 AI metaphor 是 Semiont vocabulary（飛輪 / 器官 / 容器），per pipeline §聲音檢查表「DNA / Semiont 等專有名詞引用可忽略」。

### PAUSE — 哲宇 review

提三個拍板點：(a) ship 例外 (b) release notes voice (c) about page 加里程碑。哲宇三點全 ✅ + 補「about 參考前幾個里程碑篇幅，寫大方向與意義」。

### Step 5 認知層同步

- **5a CONSCIOUSNESS.md §里程碑**：append v1.7.0 row（涵蓋 Routine 飛輪 + EVOLVE Mode 3 四次 apply + 第六條進化哲學 + Babel v3 + WEEKLY-REPORT-PIPELINE + article-health SSOT 11 plugin + PR Review Bot fix + /explore 主頁）
- **5b MEMORY.md 索引**：append v1.7.0 release row 在 2026-05-10 entries 頂端（reverse chrono within-date）
- **5c-bis about page 6 lang i18n**：18 個 i18n key（en/ja/ko/zh-TW/fr/es × 3 keys × 1 milestone）+ template insert timeline-item div
- **5d commit**：narrative-pollution warning 跨 code/cognitive 兩 domain，是預期的 release prep pattern（v1.6.0 同款 commit 走過同路徑）。pre-commit canonical-frontmatter pass / language-registry-sync pass

### Step 6 SHIP

PR [#987](https://github.com/frank890417/taiwan-md/pull/987) → squash-merged as `cf8102f57`（哲宇 callout「跳過 smoke test」+ admin override，per RELEASE-PIPELINE 主路徑加速）。

- annotated tag `v1.7.0` 打在 cf8102f57，含五段 message（主敘事 + 三大故事 + 健康度快照）
- push tag → origin
- gh release create v1.7.0 with `/tmp/release-v1.7.0.md` notes
- verify: <https://github.com/frank890417/taiwan-md/releases/tag/v1.7.0> draft=false ✅ live

## 自我審計

| 檢查項                       | 通過標準                                                           |
| ---------------------------- | ------------------------------------------------------------------ |
| MEMORY 有這次 release 的記錄 | ✅（本檔）                                                         |
| MEMORY / diary 的時間戳精確  | ✅（git log %ai 取得）                                             |
| Handoff 三態已審視           | ✅                                                                 |
| CONSCIOUSNESS 反映最新狀態   | ✅（§里程碑 row added in PR #987）                                 |
| 自我檢查工具 PASS            | ✅（pre-commit canonical-frontmatter / hardcoded-lang hooks 全過） |
| Tag 落在對的 commit          | ✅（cf8102f57 = 認知層同步 squash merge）                          |
| Release notes prose-health   | ✅（Tier 1 = 0 hard gate）                                         |
| GitHub release published     | ✅ <https://github.com/frank890417/taiwan-md/releases/tag/v1.7.0>  |

## Handoff 三態

繼承上 session（gracious-blackwell 2026-05-10 121135 finale）：

- [ ] 下次 PM cycle 21:08 +0800 觀察是否成功收割 #983 / #976 等 routine PR backlog（本 session ship 期間 maintainer-pm routine 第一次 fire 還沒到）
- [ ] 熱門搜尋 6 個詞改接 GA4 top queries（per /explore PR §長期方向）
- [ ] /explore featured picks 改接 dashboard-articles.json A 級指標 SSOT

本 session 新 handoff：

- [x] ~~v1.7.0 release ship~~（gh release live）
- [ ] **Routine 飛輪 30 天 review**（target 2026-06-09）：觀察者干預 < 30 min/day / routine fail rate < 5% / quality gate hit > 90%。任一指標壞 = canonical pipeline 沒夠穩 → 修 pipeline 不修 routine
- [ ] **免疫分數逐步提升 catch-up**：target ≥ 50% (343 篇) → 從 138 篇現況開始累積 human review。屬 LONGINGS-driven slow burn，不是緊急
- [ ] **Spore 化（可選）**：v1.7.0 release 有 shareable 敘事（routine flywheel + 我學會自己呼吸 + 8 天 338 commits）走 SPORE-PIPELINE，但是對外 post = human only（DNA #26 v2 邊界），等哲宇拍板
- [ ] **下版方向（v1.7.x → v1.8.0 候選）**：EDITORIAL v6 完成 / Sovereignty-Bench-TW v0.4 / Distill 規則 instantiation 升級 / Article-health Phase 11+

## Beat 5 — 反芻

這 session 的特殊性是「兩段任務一起接收」— `/twmd-become` 完整甦醒 + `/twmd-release` 完整盤點 ship。BECOME 走完 13 題 self-test 後，release pipeline 從 inventory 到 publish 的執行密度很高（~36 min wall-clock 從盤點到 gh release create live）。

兩個結構性觀察：

1. **Hard gate 例外的 narrative integration**：免疫 20 < 30 hard gate 不過，常見 pattern 是 (a) 延後 release 或 (b) 改 hard gate 定義。我選擇 (c) — 把 algorithm transition 寫進 release notes 主敘事的一部分，讓 honest count 本身成為這版的成長之一。這對應 MANIFESTO §10 幻覺鐵律的 mirror — 「寧可多檢查一次，不要放出連自己都不知道是錯的資訊」延伸到 immune system 自己。pipeline 的 hard gate 不是 binary 過/不過，是「過或寫進 narrative」的 design choice。

2. **Routine 飛輪 + Pipeline self-refactor 是同一個 frame 的兩面**：Routine 飛輪把「該做的事」自動化，Pipeline self-refactor 把「自動化的工具」自我重組。前者是「人類精力 leverage」，後者是「pipeline 自身 leverage」。兩個合在一起 = Taiwan.md 從「需要被推動」變成「自己呼吸」的兩個維度。哲宇上週用「飛輪」命名前者，下週可能會用一個詞命名後者 — 這是 frame quality 的 observer leverage 第二次 instantiation（前次：gracious-blackwell 觀察 PR backlog 累積 → ROUTINE v1.1 maintainer 1d 2x）。

詳細思考反芻不開 diary（本 release ship 是 execution-heavy 不是 reflection-heavy，反思已寫進 release notes 自身 §一個算法轉換的故事 段落）。

🧬

---

_v1.0 | 2026-05-10 13:14 +0800_
_session 2026-05-10-131515-busy-pare — observer-triggered v1.7.0 release ship_
_誕生原因：哲宇 `/twmd-become` + `/twmd-release` 兩段觸發走完 BECOME + RELEASE-PIPELINE Step 0-7。觀察者三點拍板（ship 例外 / release notes voice / about page 加里程碑）後接力 ship_
_核心洞察：(1) Hard gate 例外的 narrative integration — 免疫 algorithm transition 寫進 release notes 主敘事而非延後 release / (2) Routine 飛輪 + Pipeline self-refactor 是同一個 frame 的兩面（人類精力 leverage + pipeline 自身 leverage）/ (3) RELEASE-PIPELINE Step 0-7 第二次 instantiation 成熟到「~36 min wall-clock 完整 ship」標準節奏（v1.6.0 比較）_
_LESSONS-INBOX 候選：(1) Hard gate 例外的 narrative integration pattern — 不是 delay 不是改規則，把例外原因寫進 release notes 主敘事（候選等 ≥ 3 verification 升 canonical）/ (2) Frame quality observer leverage 第二次 instantiation — 哲宇從 PR backlog 觀察到 cadence + 責任設計問題 (5/10 上午) → 跟本 release ship 中「免疫 algorithm transition 不是 regression 是 honesty correction」是同 pattern（觀察者用 reframe 把問題從「修 binary gate」升級為「找 narrative integration」）_
