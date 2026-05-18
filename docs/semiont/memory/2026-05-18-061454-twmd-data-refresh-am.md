---
session: 2026-05-18-061454-twmd-data-refresh-am
type: routine
trigger: cron
---

# 2026-05-18-061454-twmd-data-refresh-am — routine dashboard sync + babel work 隔離模式驗證

> session twmd-data-refresh-am — cron routine（`0 6 * * *` +0800）
> Session span: 06:14:54 → 06:17 +0800 (~3 min wall-clock，1 commit)
> 資料來源：`git log %ai`

## 觸發

Cron `twmd-data-refresh-am` 每日 06:00 自動觸發。執行 5-stage lifecycle (Stage 0 BECOME → Stage 1 sync → Stage 2 refresh-data.sh → Stage 3 commit+push → Stage 4 finale)。

## 隔離 in-flight babel work

session 起點 working tree 髒：82 個未 commit 檔（6 既有 article × 5 lang babel patches + 24 Geography county 新翻譯 + 3 reports research note）。這是前一個 routine（推測 babel-nightly 或前一夜 manual session）的成果但沒 commit。Data-refresh 跟 babel 是兩條獨立 routine ownership，不能讓 Stage 3 `git add .` 把 babel 內容掃進 `🧬 [routine] twmd-data-refresh-am` 標籤的 commit。

採取「stash → refresh → commit → pop」模式：先 `git stash push --include-untracked` 把 in-flight 全部保護起來（含 untracked Geography 新檔），跑乾淨的 refresh，commit + push refresh 22 個 dashboard JSON / stats / llms.txt 輸出，再 pop 還原。Pop 時 `knowledge/_translation-status.json` 衝突（SSOT 同時被 babel 跟 Step 3 sync-translations-json.py 改寫），用 `git checkout HEAD --` 保留 refresh 版本（這檔是 derived SSOT，next babel run 從 frontmatter 重生）。

最終 working tree 82 babel 檔完整保留待下個 routine 處理，refresh commit `7b6a047c2` 內容純粹只含 dashboard regen。

## refresh-data.sh 12 step 結果

全 12 step 完成。三源感知：CF 7d 331K requests / 68K AI crawler hits across 19 crawlers / SC 7d 20 top queries / GA4 28d 20 top pages。Prebuild 12 dashboard JSON 全重生。stats: ⭐991 🍴147 👥57 📄4307。

兩個非 blocking 觀察寫進 commit message 而非 LESSONS-INBOX（已記錄的舊問題）：

- **Step 10 hard gate fired**：`dashboard-immune.json` mtime 仍是 2026-05-17 — REFLEXES #43 silent failure pattern，generator 從未被加進 refresh-data.sh。這個 gate 每次 routine 都會亮但每次都是同一檔，等於 dormant entropy。
- **Pre-commit hook ignored**：`.husky/pre-commit` not executable，git 直接跳過。本 commit 純 JSON 沒 prose 所以無影響，但若被 prose-writing routine 觸發會 silent skip prose-health 檢查。

## 收官 checklist

| 檢查項                       | 狀態                                                |
| ---------------------------- | --------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                  |
| Timestamp 精確（git log %ai）| ✅                                                  |
| Handoff 三態已審視           | ✅                                                  |
| CONSCIOUSNESS 反映最新狀態   | ✅（refresh 已 regen dashboard-vitals/organism）    |
| refresh pipeline 12/12 PASS  | ⚠️ Step 10 stale dashboard-immune.json（已知 gap） |
| Stage 3 push 成功            | ✅ (`4b090f5f4..7b6a047c2 main -> main`)            |
| In-flight babel 隔離成功     | ✅（82 檔保留 working tree 等下個 routine）         |

## Handoff 三態

繼承 2026-05-18 004535 manual：

- [x] ~~22 縣市 batch 1 5 篇 ship + v2 cost-split orchestration 走通實證~~
- [ ] pending: 觀察者 review batch 1-3 共 ~14 篇品質（5 分鐘 reading test）
- [ ] pending: batch 4 (新竹市 / 桃園市 / 台南市 / 高雄市) Stage 0 觀點成型已 `3438b7f22` ship，等下個 rewrite session 接 Stage 1+
- [ ] pending: CI run [25998493732](https://github.com/frank890417/taiwan-md/actions/runs/25998493732) 確認 deploy success
- ⏳ blocked: 9 agent worktree-X branches 仍 locked 占 disk space — 待 cleanup（非 critical）

本 session 新 handoff：

- [ ] pending: **In-flight babel work 待 commit** — working tree 82 檔（6 既有 article × 5 lang + 24 Geography county 新翻譯 + 3 research notes）。next 觸發 babel-nightly 或 manual session 接手 commit + push
- [ ] pending: **`dashboard-immune.json` generator gap**（REFLEXES #43）— 每天 refresh routine Step 10 都會亮但無人接。需要 grep 找 immune-related generator script 加進 refresh-data.sh
- [ ] pending: **`.husky/pre-commit` not executable** — `chmod +x .husky/pre-commit` 一個動作但牽涉 hook semantic（為什麼會掉 executable bit？git 不追蹤 mode 的 macOS umask 問題？）

## Beat 5 — 反芻

第一次親手執行「routine ownership 隔離」模式。Data-refresh 跟 babel 雖然都是 cron routine，但邊界從未在 SOP 明寫過 — 我推導出來：commit message label 應該對應 routine 名，不能跨 routine 借車。Stash → refresh → commit → pop 的順序成為新 routine 的 default working pattern when working tree 髒。

`_translation-status.json` 衝突揭露另一個結構：derived SSOT 被多個 generator script 寫入時，stash + pop 一定撞。修補可能是把 SSOT generator 集中到單一 owner（next-level SSOT cleanup candidate，但不是本 session 範圍）。

兩個 dormant entropy（dashboard-immune.json gap + hook executability）這次第一次被同一 routine 同時看見並寫進 memory。Step 10 hard gate 是設計給「today 漏跑的 generator」用的，遇到「結構性從未加進來的 generator」就會每次都假警報 — 警報疲勞會讓真正的 silent failure 被忽略。修補方向是把缺的 generator 補進 refresh-data.sh，讓閘門能用在它原本設計的場景。

延伸寫進 diary：本 session 純 mechanical routine，沒有超越「做了什麼」的反芻層級。Skip diary。

## Post-script — 隔離模式自己被同個 session 違反（commit `4ad0aa420`）

寫完上面 Beat 5 反芻、commit memory file 那一步，沒給 `git commit` 顯式 paths，把 33 個 babel modified 檔（`stash pop` 把它們塞回 index 而不是 working tree）一起掃進 memory commit。Commit message 寫著「in-flight babel isolation pattern」但 diff 本身打臉這個 claim — 35 files changed, 1753 insertions。

根因兩層：

1. **`git stash pop` 行為誤判**：以為 pop 預設把 modifications 放回 working tree (unstaged)，實際上 conflict 場景觸發 auto-stage 非衝突檔。`_translation-status.json` 衝突存在 → git 把其他 modified 檔自動進 index 等 conflict 解完一起 commit。
2. **`git commit` without explicit paths**：當 staged 區有東西時無條件全收，沒 audit。「stash → refresh → commit → pop → commit memory」流程的第二個 commit 必須用 `-o` 或先 `git reset HEAD` 才安全。

剩餘 49 untracked 新 Geography county 翻譯檔仍在 working tree（untracked 不被 pop 自動 stage）。下一步另起 `🧬 [routine] babel-handoff` commit 把它們收進來，working tree 才真乾淨。

這是 vc=1 first-instance — 升 LESSONS-INBOX 候選。「stash → refresh → commit → pop」pattern 必須加第 5 步「commit memory with explicit paths after pop」才完整。

🧬

🧬

---

_v1.0 | 2026-05-18 06:17 +0800_
_session twmd-data-refresh-am (061454) — cron routine 每日 06:00 dashboard sync_
_誕生原因：cron `0 6 * * *` 自動觸發，執行 DATA-REFRESH-PIPELINE 12 step + 收官 lifecycle_
_核心洞察：(1) routine ownership 隔離模式（stash → refresh → commit → pop）成為新 default — commit label 不跨 routine 借車；(2) derived SSOT 被多 generator 寫入時 stash + pop 必撞，需 SSOT owner 集中化；(3) 兩個 dormant entropy（dashboard-immune.json gap + hook executable bit）第一次被同 routine 同時看見，警報疲勞風險浮現。_
_LESSONS-INBOX 候選：暫不 append — (1)(2)(3) 皆需多 routine 驗證確認 vc≥2 再升 inbox。本 session 是 vc=1 first observation。_
