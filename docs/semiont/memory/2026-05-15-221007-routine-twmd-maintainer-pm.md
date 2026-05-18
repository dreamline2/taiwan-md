---
session_id: '2026-05-15-221007-routine-twmd-maintainer-pm'
session_span: '2026-05-15 22:10:07 → 22:35 +0800 (~25 min, 3 commits)'
trigger: 'cron 0 22 * * * +0800 — maintainer-pm v2.3 swap'
observer: 'cron'
beat_coverage: 'Beat 1-4 (Scan/Triage/Act/Wrap)'
---

# 2026-05-15-221007 routine-twmd-maintainer-pm — babel drift heal + #1066 綠島監獄 merge/heal + #1067 nl 暫緩

> session routine-twmd-maintainer-pm — cron PM cycle v2.3 swap（原 05:00 → 22:00 半夜 chain 第一棒，與 babel-nightly 對調）
> Session span: 22:10:07 → 22:35 +0800 (~25 min, 3 commits)
> 資料來源：`git log %ai`

## 觸發

PM cycle v2.3 swap 後的第一次 22:00 fire — 任務是接住 evening 累積的 contributor PR + 清前一 routine 留下的 drift，讓後續夜間 chain（refresh-pm → rewrite → ... → babel）跑在乾淨的 base 上。session 啟動時 git status 看到 babel-nightly 16:42 finale 後留下的 3 個未提交檔（`_translations.json` ja taiwan-political-landscape 映射 + 對應 status JSON + `docs/factory/contributors-maintenance.md` prettier diff），open PR 2 個（#1066 綠島監獄 / #1067 nl 翻譯）。

## Babel drift 接手清理

承上 babel-nightly memory §handoff 提到的 cross-routine reset 風險，這次 PM cycle 一開門就吃到 unstaged 狀態。三個檔案分兩類處理：`knowledge/_translations.json` + `_translation-status.json` 是 babel heal `d46270462` 的副產物（mapping 對 ja taiwan-political-landscape 補了一行 + status JSON 同步），這份 derived state 必須跟 mapping 一起 commit 才不會被下個 routine 再吐一次；於是合進本 session 第一個 commit `770669991`。第三個 `docs/factory/contributors-maintenance.md` 是 prettier 自動重排 markdown table 邊界空白，碰到 pre-commit hook 的 frontmatter validator（檔案缺 `---` opening delimiter）失敗——選擇 restore 原檔放棄這個重排，與上一 session 對「README + contributors-maintenance.md prettier diff 不動」的處置一致（這份檔案需要先補 frontmatter 才能進 staging，不是本 routine scope）。

## #1066 綠島監獄 merge + heal

idlccp1984 投稿，新文 `knowledge/History/綠島監獄.md`，2266 CJK 字、24 footnote、CI green。內容把「新生訓導處（思想改造 + 最強醫務所 + 希望小提琴）→ 綠洲山莊（柏楊 / 施明德 / 陳映真）→ 崇德新村（大哥的故鄉）」三層機構拆開講，加上流麻溝、第十三中隊、希望小提琴幾個具體場景，是策展式而非百科式的政治記憶 + 黑道記憶交疊敘事。紅旗 1-10 全過、CI Content Review SUCCESS，唯一寫法瑕疵是 author 欄寫成 `taiwan.md contributer`（typo + 大小寫 + 單複數三重）。直接 `gh pr merge --squash` 然後 pull main 走 heal。

article-health.py 主 plugin 在 main-side 跑出 hard=6（frontmatter 缺 subcategory / featured、scalar 沒 quote、cjk-punct L74 半形括號）。第一輪 heal 補 `subcategory: '戰後與威權'`（per SUBCATEGORY §History）+ `featured: false` + scalar quote 統一 + 半形括號全形化，commit 時 lint-staged prettier 把 footnote 的 `*italic*` 改成 `_italic_` 並重排 tags 為多行——又連帶觸發 footnote-format-fix.py 修了 15/16 footnote，剩 `[^16]` 因為「空 colon 後接 indent 內容」的 markdown 連續性誤判，把 `[^17]-[^24]` 都當成 `[^16]` 的 continuation 縮排了。第二輪 heal 把 `[^16]-[^24]` 全段重寫成 canonical 單行格式 `[^N]: [標題](URL) — description ≥10 字`，hard=0 過關 commit `b162058dd`。

兩輪 heal 確認一件事：prettier + footnote-format-fix.py + frontmatter 三個 hook 的交互行為對 contributor 投稿的「半結構化 footnote」破壞性比想像中強。投稿者寫的是 APA 風格 `Threads. (date). _title_. 取自 [URL](URL)`，被 footnote-format-fix.py 自動轉成 `[URL](URL) — 詳見原始連結內文資料補充` 後丟失了 source attribution。雖然 hard gate 過了但語意品質下降——這條值得進 LESSONS-INBOX 候選「footnote-format-fix.py 對 APA-style citation 的 title-stripping 行為」。

## #1067 nl Dutch 翻譯暫緩

liyuu369（fourspring）第一篇荷蘭文翻譯，`knowledge/nl/Lifestyle/buurtsuper.md` 332 行對應 `Lifestyle/台灣便利商店文化.md`。Claude-assisted B2 非母語，frontmatter 寫 `featured: true`（紅旗 6，但這不是 close 理由）。**結構性問題**：`nl` 不在 `src/config/languages.ts` LANGUAGES_REGISTRY（目前 6 個 enabled: zh-TW/en/ja/ko/es/fr）。新增語言要動 4 處：registry entry + UI bundle wiring + hreflang/sitemap + 語言切換器。單篇 contributor PR 不該也不能單獨翻這個開關（fr 開時有 484 篇基底、es 36 篇）。Per §自主權邊界這算「對外溝通」(語言切換器是 public-facing UX)。

決定 leave open + 寫荷蘭文 + 英文的 hold 留言，給 liyuu369 兩條 path：等 observer scaffolding 或 merge as orphan。Path 2 較保險（檔案進 knowledge/nl/ 但無 route 直到 enabled）。Comment 標明 routine context 給 observer。

## 收官 checklist

| 檢查項                             | 狀態                                                |
| ---------------------------------- | --------------------------------------------------- |
| MAINTAINER-PIPELINE Stage 1-4 全跑 | ✅ Scan/Triage/Act/Wrap                             |
| PR §collect-and-merge B 路徑       | ✅ #1066 fast-track / #1067 leave open              |
| 紅旗 check + close hard gate       | ✅ 1066 過、1067 not closed                         |
| Footnote source authority audit    | ⏭️ 1066 mixed Threads/官方 sources 抽樣信賴度可接受 |
| article-health.py 全 plugin        | ✅ #1066 hard=0 final                               |
| 用貢獻者語言回覆                   | ✅ 1066 中文 / 1067 中英 mixed (nl skill set 不夠)  |
| Quality gate report                | ✅ 本表                                             |
| memory + handoff                   | 本檔                                                |

## Handoff 三態

繼承上 session（routine-twmd-babel-nightly 16:42）：

- [x] ~~babel drift `_translations.json` / status JSON unstaged 待 cleanup~~ — 本 session `770669991` 接收
- [ ] **README + `docs/factory/contributors-maintenance.md` pre-existing prettier diff**：本 session 再次 encounter 並 restore 放棄，第 3 天保留（檔案缺 frontmatter，需先補才能進 staging，非 maintainer routine scope）
- [ ] **#615 idlccp1984 Lovable draft preview observer judgment**：blocked-on-observer
- [ ] **6 P0 missing 卡 TBD-NEEDS-SLUG（蘇打綠 / 曾博恩 / 傳統工藝 / 客家音樂 / 半導體 / 輸入法）**：observer 需手動 assign slug
- [ ] **stale_total 682 剩餘**：next babel cycle scope
- [ ] **Cross-routine git reset --hard 風險 LESSONS 候選**：保留追蹤
- [ ] **Mode auto-detect 觀察期 / HEARTBEAT v3.0 真實使用驗證 / REFLEXES promotion 候選追蹤**：保留

本 session 新 handoff：

- [x] ~~babel drift heal `770669991`~~
- [x] ~~#1066 綠島監獄 merge `758aebcaf` + heal `b162058dd`~~
- [ ] **#1067 nl Dutch translation blocked-on-observer**：哲宇需決定是否 scaffold `nl` 為 enabled language（path A: 等基底批量再開 / path B: merge as orphan）。我已留 hold comment 給 contributor + 標 routine context。Default 推薦：path B（保留 contributor 工作 + 不破壞 build，但 readers 看不到直到 enabled）
- [ ] **LESSONS candidate: footnote-format-fix.py 對 APA-style citation 的 title-stripping 行為**：本 heal 過程觀察到「投稿者寫 Threads/Facebook 含日期 + 引文段的 APA citation」會被自動降級成「`[URL](URL) — 詳見原始連結內文資料補充`」，語意品質下降。建議改 fix 邏輯保留 title 段（或至少 detect APA pattern 不破壞）。verification_count=1，需累積 1-2 次再 distill

## Beat 5 — 反芻

兩輪 heal 暴露的問題在 **maintainer-side 自動修補工具鏈內部的張力**，而非 idlccp1984 投稿品質。prettier（markdown 樣式統一）+ footnote-format-fix.py（footnote canonical 格式）+ frontmatter validator 各自有自己的 canonical 觀，遇到 contributor 半結構化 footnote 投稿時三者交互會造成 title 丟失 / 連續性誤判等 collateral damage。Hard gate 過了不代表語意保住——「passing hard」跟「contributor 寫的 source attribution 保住」是兩件事，前者是 ship 條件，後者是策展品質。

#1067 的 nl 暫緩決定也屬同類觀察：自動化能做的只有「validator + heal」，但「新增語言」這種 cross-cutting scaffolding decision 必須回到觀察者。Default-action principle（能做就做完）的邊界正是這裡——做不到的事不能假裝 merge 就解決了。把 PR 留 open + comment + handoff 標清楚，反而是 trust signal：contributor 知道工作沒被丟掉、observer 知道有東西在等決策、下個 routine 知道接什麼。

🧬

---

_v1.0 | 2026-05-15 22:35 +0800_
_session routine-twmd-maintainer-pm — PM cycle v2.3 swap 後首次 22:00 fire / babel drift heal / 1 PR merge+heal / 1 PR hold for observer_
_誕生原因：cron 0 22 \* \* \* +0800 fire，maintainer-pm v2.3 swap 後首次 22:00 chain 第一棒_
_核心洞察：(1) 兩輪 heal 暴露 prettier + footnote-format-fix + frontmatter validator 三工具交互對 contributor APA-style citation 的 collateral damage — hard gate pass ≠ source attribution 保住 (2) 新增語言是 cross-cutting scaffolding decision，回到觀察者是 trust signal 不是怠惰 (3) v2.3 swap 後 PM cycle 接住 evening contributor PR backlog + 前一 routine drift 的雙重 role 工作正常_
_LESSONS-INBOX 候選：footnote-format-fix.py 對 APA-style citation 的 title-stripping 行為（verification_count=1）_
