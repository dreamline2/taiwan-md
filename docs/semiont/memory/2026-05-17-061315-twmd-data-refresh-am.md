# 2026-05-17 061315-twmd-data-refresh-am — dashboard sync + 並行 babel race condition

> session 2026-05-17-061315-twmd-data-refresh-am — twmd-data-refresh-am cron routine 5-stage lifecycle
> Session span: 06:13:15 → 06:14:?? +0800 (~10 min, 1 ship commit `cf90406b3`)
> 資料來源：`git log %ai`

## 觸發

cron `0 6 * * *` +0800 自動 fire。前 session 041804-twmd-self-evolve-weekly 04:23 收官後，05:05 + 05:31 兩個 twmd-babel commit（eb5f40777 P2.5 metadata bump + d6e87d075 P0 cascade 30 fresh）入庫但**未 push**。本 session 啟動時 HEAD 領先 origin/main 2 commits。

## refresh-data.sh Step 1 hard abort：並行 babel race condition

Step 1 git sync `git pull --rebase` 失敗 — auto-stash + pull + pop 流程中，stash 之後 pull 之前另一個 babel routine 寫了新檔，rebase 報「unstaged changes」hard abort。

Working tree 開場 368 files modified（前一輪 babel scan 留下的 `sourceContentHash` / `sourceBodyHash` metadata bump，translation 內容無變）。stash → pull → pop 之間並行寫入再添 5 files 到 373。

**判斷**：HEAD `d6e87d075` 已是最新（origin 落後 2 commits 而非超前），git pull 在 logical 上是 no-op，可安全 skip Step 1 改手動跑 Steps 2-12。`git log HEAD..origin/main` 確認空 → 進入手動模式。

## Steps 2-12 手動執行

依序跑 6 個 generator + 4 個 gate：
- Step 2 fetch-sense-data（CF/GA4/SC 三源全 200）
- Step 3 sync-translations-json（3576 entries）
- Step 4 generate-dashboard-spores（73 spores / top 300K views / 4 warnings 2 OVERDUE + 2 waiting）
- Step 5 i18n-coverage-audit（dashboard-i18n.json）
- Step 6 npm run prebuild（309/310 imageprep，1 failure 屬 known）
- Step 7 refresh-llms-txt（zh702 / en723 / ja713 / ko708 / es704 / fr724 / contrib 61）
- Step 8 update-stats（⭐991 🍴147 👥57 📄4290）
- Step 9 extract-build-perf（latest 746s / 7d avg 755s — ms/page 746000 仍 >200ms threshold，已知 build 效能議題）
- Step 10 freshness gate：✅ 10/10 dashboard JSON 今天 mtime
- Step 11 validate-spore-data：✅ 0 errors + 2 warnings（Portaly 首兩筆贊助感謝 + 寶島聯播網訪談 SPORE-LOG 有但 knowledge/*.md 無，已知 historical）
- Step 12 sync-spore-links：✅ 85 entries consistent，0 changes needed

Stage 3 commit `cf90406b3` 405 files +17153 / -15891。Push `c8b8a8a9d..cf90406b3` 三 commit 一起上：babel batch1 + babel cascade + data-refresh。

## Beat 5 反芻

並行 routine race condition 在 stash 視窗內首次 surface（之前 stash window 都假設 atomic）。Step 1 wrapper 的 dirty handle 是 dirty-at-start，沒處理 dirty-during-pull。Workaround「skip Step 1 if HEAD == origin」是 ad-hoc，沒升 SOP — 屬 LESSONS-INBOX 候選：cron 排程密集化（00:00 rewrite-daily → 01:00 rewrite × 5 / news-lens → 01:14 news-lens memory → 03:15 distill → 04:14 babel-bump-pre / 04:17 self-evolve → 05:00 babel cascade → 06:00 data-refresh-am）下，相鄰 routine 在彼此 stash 視窗交集的機率上升，需要 refresh-data.sh 加 `--skip-sync-if-current` flag 或在 stash 後 detect 新 dirty 改 retry。

Babel 兩個 commit 未 push 是另一層 surface — 上游 routine 可能 commit 後 push 失敗 silent，下游 routine 一併帶上去剛好遮蓋。理想是上游 push 失敗時 alert，但本次「帶上去」是 valid 的 graceful recovery。

## Handoff 三態

- [ ] pending: refresh-data.sh Step 1 並行 race condition workaround 升 LESSONS-INBOX entry（解除條件：寫進 inbox 等下次 distill）
- [ ] pending: build perf `746000 ms/page` 仍超 200ms threshold — 已知議題持續觀察，無 immediate action

## 教訓候選（去 LESSONS-INBOX）

並行 routine 在 stash 視窗交集 race condition + 上游 routine push 失敗 silent 被下游 graceful 吸收。
