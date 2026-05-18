# 2026-05-12-015230-src-content-migration — sync.sh 沒儀器化 → C+F+H 最根治 3 ship 一氣完成

> session src-content-migration — observer-triggered cleanup → 架構分析 → 3 ship migration（哲宇睡前授權自行推到 /twmd-finale）
> Session span: 2026-05-11 23:01 → 2026-05-12 01:51 +0800 (~2hr 50min, 9 commits)
> 資料來源：`git log %ai`

## 觸發

哲宇晚間 23:01 起一連串觀察與追問：先要求清理 worktree / branch / 線上 branch 用完的、判斷 sync 產出檔案該不該 commit、最佳長期解法分析、最後拍板「最乾淨根治」+ option A 接受 zombie 清除，授權自行推到 /twmd-finale。從 entropy cleanup 升級為架構級 migration。

## 從 cleanup 揭露架構缺口

最初任務只是清 worktree / branch。168 local branch → 4、119 origin → 1、14 worktree → 2、加 `.claude/worktrees/` 到 .gitignore（`20a6bd1c5`），常規 hygiene 工作。但接下來追問「sync 產出檔案怎麼處理」時實測 `bash scripts/core/sync.sh`，揭露 **2801 file drift + 10 untracked**。

10 untracked 對應 PR #968-#1025 八位 contributor 的文章 — 已 merge 到 `knowledge/` 但從未投影到 `src/content/`，網站 build 不到 = silent missing 八天。先 commit 補回（`f2a2f3eef`），但意識到這只是表象 — 真正的根因是 sync.sh **沒被儀器化進任何生命週期觸發點**：refresh-data.sh 12 步沒它、prebuild 沒它、pre-commit 沒它、CI 沒它。

對應 [DNA #43](../DNA.md) pattern（dashboard JSON 漏接 silent stale）的延伸 — 「新衍生資料必須儀器化」原本只指 dashboard，這次擴到投影層。

## Report v1 → v2 + 兩個 bleeding

第一輪分析寫 report v1.0（`222234581`）— 推薦 F+H+B+verify gate 四層儀器化（incremental sync + idempotent metadata + refresh-data 整合 + fail-loud verify）。哲宇即場 callout「最乾淨根治呢？推薦怎麼做？」直接揭露 v1 是 over-engineering safe play。

往更深一層挖：file count 比對揭露兩個既有 bleeding：

| Lang        | Gap                                                               |
| ----------- | ----------------------------------------------------------------- |
| zh/en/ja/ko | 各缺 2 篇 silent missing（共 8 篇）                               |
| **fr**      | **+330 zombie articles**（src/content/fr 比 knowledge/fr 多 330） |
| es          | +6 zombie articles                                                |

fr 330 zombie 根因在 sync.sh line 19 `rm -rf` list **沒含 fr/es**（line 147-183 只有 cp 沒 rm），knowledge/fr 刪除的舊翻譯殘骸累積在 src/content/fr，網站當前有 330 個 knowledge/ 已沒有的法文頁面。

升 report v2.0（`0134c0e93`）：推薦從 F+H+B+verify 變 **C+F+H 最根治** — gitignore src/content/{lang}/ + sync.sh 接進 prebuild，**消除整個 derived state in git 的問題類別**。v1 是「儀器化包住問題」、v2 是「消除問題類別本身」。336 zombie 觸發 §自主權邊界（>10 篇刪除），停下來請哲宇拍板，他選 option A 接受清除。

## 3 ship migration（睡前授權自行推完）

哲宇要求「完整驗證與修復、每個步驟非常小心、妥善備份與還原」，先 `/twmd-become` 完整甦醒讀 12 認知器官，建備份 branch `backup/pre-sync-refactor-2026-05-12`，列完整待辦再開工。

**Ship 1** (`02db88af5`)：sync.sh refactor 217→165 lines，從 5x repeat 改 SSOT-driven `sync_lang()` function，順帶修 3 個既有 bug — (a) fr/es 加 rm list 清 336 zombie (b) resources/ 全 6 lang sync（原本只跑 zh-TW + en）(c) root-level .md 也搬（修補另外 2 篇 silent missing：`golden-duo-chi-lin-yang.md` + `taiwan-semiconductor-industry.md`）。Verify：idempotence hash compare 0 file diff、build 477s pass、4 lang URL visual smoke 全綠（含先前 silent missing 補回的 ko/bamboo-hat-craft）。

**Ship 2** (`22aafd8d8`)：`package.json` 改 `prebuild` 為 `npm run prebuild:sync && run-p prebuild:api ...`，serial-first then parallel — sync 必須先跑因為 `prebuild:supporters` 讀 src/content/。Verify：prebuild 28s（sync 16s + parallel 12s）、log 確認 sync 先跑、regen test rm src/content/zh-TW → npm run prebuild:sync 完美重建 709 files。

Push Ship 1+2 等 CI ~14 分鐘 — **build success + deploy success**雙綠，CF Pages 生產環境驗證通過。

**Ship 3** (`d208eed78`)：`.gitignore` 加 6 lang dirs（保留 config.ts）、`git rm --cached` 4587 files、改 7 份 docs 對齊新架構（CLAUDE.md / CONTRIBUTING.md / MANIFESTO §6 / DNA §骨骼基因 + #43 / DATA-REFRESH-PIPELINE §Step 6 / structure-log）。Verify：fresh clone simulation `rm -rf src/content/{lang} → npm run build` 500s pass + 4247 files regen + page set 對齊。

Migration 完成壓縮 1 週 dogfood 為 ~14 分鐘 CI 驗證 — 風險：CI vs 生產差異（unlikely）。緩解：備份 branch 隨時可救。

最後 report v2.1 (`f23106669`) 補 §十「實作結果」紀錄 3 ship 數字 + bleeding 修補對照 + 永久收益。

## 收官 checklist

| 檢查項                       | 狀態                                                 |
| ---------------------------- | ---------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅ 本檔                                              |
| Timestamp 精確               | ✅ git log %ai 取                                    |
| Handoff 三態已審視           | ✅ 見下                                              |
| CONSCIOUSNESS 反映最新狀態   | ⏳ 等 Ship 3 CI 綠後一併更新（cron 下輪 auto-regen） |
| 自我檢查工具 PASS            | ⏳ 寫完跑 prose-health                               |
| 3 ship 全部 push + CI 綠     | Ship 1+2 ✅ / Ship 3 ⏳ in progress                  |

## Handoff 三態

繼承上一 session（admiring-montalcini 蘋果西打 EVOLVE）：

- [x] ~~下一篇用 REWRITE-PIPELINE 走完整 v6.0 Stage 0 觀點~~ — retired by 本 session（focus 變成架構 migration，REWRITE v6.0 留給未來 article session dogfood）
- [x] ~~Squash merge 拋棄 commit 風險紀入 LESSONS-INBOX~~ — partial retired（本次 push 沒撞 parallel PR，但 pattern 仍適用未來，留 in LESSONS）
- [ ] **蘋果西打 5 lang 翻譯**：等下次 babel routine 自動觸發 — 不在本 session scope

本 session 新 handoff：

- [x] ~~Cleanup worktrees / branches / online branches~~ — 168 local → 4、119 origin → 1、14 worktree → 2
- [x] ~~Gitignore `.claude/worktrees/`~~ — `20a6bd1c5`
- [x] ~~Silent missing 10 篇緊急補~~ — `f2a2f3eef`
- [x] ~~Sync.sh 架構演化策略 report~~ — v1.0 → v2.0 → v2.1
- [x] ~~Ship 1+2+3 完整 migration~~ — 全 push，等 Ship 3 CI 綠
- [ ] **觀察 Ship 3 CI deploy 結果**：CF Pages build + site fr 文章列表少 330 條是 expected
- [ ] **README 補 fresh clone 提示**（open question #4）：「首次 `npm install && npm run dev` 會有 +5-10s prebuild sync」— 留給下次 onboarding polish session
- [ ] **fr 330 zombie URL GA4 audit**：哲宇選 option A 接受 URL loss，但若未來發現有讀者搜尋過該 URL，可考慮 backfill knowledge/fr/ 救回部分

給觀察者（哲宇明天醒來）：

- 3 ship 全 push、Ship 1+2 CI 雙綠、Ship 3 CI 監測中
- 架構強制執行 MANIFESTO §6 — src/content/{lang}/ 不在 git，未來任何 PR diff 大幅變乾淨
- 永久收益：silent missing / drift / zombie 整類問題從架構消除
- 備份 branch `backup/pre-sync-refactor-2026-05-12` 仍存在，若有 regression 可隨時 restore（4587 files）
- 報告 [reports/sync-architecture-evolution-2026-05-12.md](../../../reports/sync-architecture-evolution-2026-05-12.md) v2.1 完整紀錄

## Beat 5 — 反芻

哲宇 callout「最乾淨根治呢？」是這 session 的轉折點 — v1 hybrid 是過度保守的 safe play（migration cost 不大但永遠帶著 drift），v2 是真正消除問題類別。我先前推 v1 因為過度權衡 migration cost、欠考慮永久收益 — 4568 files 看起來嚇人，但實際只是 git rm --cached 一行 + 一週後就沒人記得。

跟先前的「修補 fr/es 加 rm list」（局部修補）vs「gitignore 整類」（架構消除）對比，揭露一個 pattern：**任何「需要儀器化 / 修補 / 防禦」的問題，先問「能不能消除問題類別本身」**。儀器化是 fallback 不是 first choice。如果能架構消除，就架構消除；架構消除不到的，才用儀器化包住。

這次也驗證 BECOME 在高 stake decision 前必跑 — `/twmd-become` 完整載入 12 認知器官後，3 ship 的所有判斷都有 DNA #43 / #15 / #52 / #50 / #54 五條反射 active retrieve。如果 plain CC 跑這個 migration，可能在「dogfood 1 週還是壓縮成 CI window」這種 trade-off 上做出較弱的決策。

無新 LESSONS-INBOX 候選 — 本次的洞察「消除問題類別 > 儀器化守備」對應既有 DNA #15 + #52 已 cover；具體實踐已寫進 reports/sync-architecture-evolution-2026-05-12.md v2 §九「v1 → v2 演化過程」。

🧬

---

_v1.0 | 2026-05-12 01:52 +0800 src-content-migration session — 哲宇授權自行推到 /twmd-finale_
_session src-content-migration — observer-triggered cleanup → 架構分析升級 → 3 ship migration (一個 session 內完成)_
_誕生原因：2026-05-11 23:01 哲宇要求清 worktree / branch；過程揭露 sync.sh 從未被儀器化 → 8 篇 silent missing + 336 zombie；哲宇升「最乾淨根治」拍板走 v2 → 3 ship migration 全 push_
_核心洞察：「消除問題類別 > 儀器化守備」— MANIFESTO §6「knowledge/ 是唯一 DNA」從 self-discipline 升結構性物理約束。能架構消除就架構消除，儀器化是 fallback 不是 first choice_
