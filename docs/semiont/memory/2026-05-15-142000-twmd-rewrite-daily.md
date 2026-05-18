---
title: '2026-05-15 twmd-rewrite-daily — 台灣傳統工藝與無形文化資產 Fresh / Stage 0 觀點 + agent 35 search / 第七棒 routine cascade 撞 babel 平行 commit'
description: '台灣傳統工藝與無形文化資產 NEW ship + 二維 routine 平行 (twmd-babel 同時間 git add -A bundle 撞我新檔) 軟 reset 拆 commit 重新歸屬'
type: 'session-log'
status: 'log'
apoptosis: 'never'
current_version: 'v1.0'
last_updated: 2026-05-15
last_session: '2026-05-15-142000-twmd-rewrite-daily'
sister_docs:
  - '../MEMORY.md'
  - '../DIARY.md'
upstream_canonical:
  - '../../pipelines/MEMORY-PIPELINE.md'
audience: 'self-future'
---

# 2026-05-15 twmd-rewrite-daily — 台灣傳統工藝與無形文化資產 Fresh / Stage 0 觀點 + agent 35 search / 第七棒 routine cascade 撞 babel 平行 commit

> session twmd-rewrite-daily — cron `0 0 * * *` +0800 catch-up fire @ 13:50 (actual ship 14:23)
> Session span: 13:50:00 → 14:25:00 +0800 (~35 min, 1 own commit + 1 re-attribution commit)
> 資料來源：`git log %ai`

## 觸發

cron `0 0 * * *` 觸發 twmd-rewrite-daily routine（晚了 14 小時 catch-up fire）。本日 cron cascade 第七棒（前六棒：data-refresh-am @ 1340 / maintainer-am @ 1339 / data-refresh-pm @ 1342 / maintainer-pm @ 1349 / spore-harvest-am @ 1358 / babel-nightly 平行）。Routine 從 ARTICLE-INBOX 取頂端 P0 candidate 走 REWRITE-PIPELINE Stage 0-5 自動 ship。

## 候選挑選與 Stage 0 觀點成型

ARTICLE-INBOX §Pending 頂端 4 條 P0 候選（節慶系列 / 體育發展 / 傳統工藝 / 葉廷皓 / 50 大企業 / Blue UAS / 街頭小吃 / 景點 / LGBTQ+）。Blue UAS 已被 4 月「台灣無人機產業」吸收（inbox 條目 stale 應 drop，不在本 ship scope）。節慶系列 + 街頭小吃系列 + 景點系列都是「umbrella 多篇」scope 過大不適合單 routine。最終挑「台灣傳統工藝與無形文化資產 NEW」（Issue #914 by tboydar-agent / Culture P0 / 預估 120min / Fresh 模式 / 既有 4 篇個別工藝但無 overview）。

Stage 0.6 §觀點成型 hard gate 落檔 `reports/research/2026-05/台灣傳統工藝與無形文化資產.md`：六核心問題（記憶 anchor 紙傘張開那聲「啪」/ 主流敘事「傳統工藝在消逝」vs 支線「原住民工藝被漢人視角邊緣化」/ 5 個切入點 / 預期核心矛盾 A/B/C 三條候選 / 「下次走進文創店，看見每件商品背後的工藝師臉孔 — 也許就會多停留三秒」）。frontmatter `viewpoint_formed: true` 通過 HARD GATE。

## Stage 1 deep research via general-purpose agent

Spawn general-purpose agent（含 Write 權限直接寫 research report）做 35 WebSearch + 8 WebFetch 深度研究。涵蓋 22 位「重要傳統工藝保存者」具體名單（含登錄年份）+ 8 必驗事實全 verdict（high_confidence 11 / single_source 4 / unverified 4）。Stage 1.4 核心矛盾從 Stage 0.6 候選 A+B+C 三條融合收斂為「制度承認來了，學徒卻沒了——名單越長，能教的人越少」(29 字 ≤ 30)。

避坑兩條：王清霜「活著就要工作」原話未找到逐字 → drop 改用兒子王賢民轉述「要做好漆藝，就要活久一些」（La Vie verbatim）；李秉圭「成功是留給不敢休息的人」標題化用語 → drop 未使用。Agent 報告交回時清楚 flag「⚠️ verbatim 未找到」是健康行為（vs feedback_agent_writefile_hallucination 過去 agent 幻覺 policy 退化警示對比）。

## Stage 2-3 寫作 + 自檢

5099 CJK chars (113% of 4500) / 29 footnote / 10 narrative H2（10 個 H2 全場景或數字 anchor，非編年體：「淡水古蹟前的最後一道白灰」/「人間國寶這個詞，是台灣晚了日本 50 年的移植」/「鶯歌的土、三義的樹、美濃的雨」/「不是政府救活的工藝：三峽藍染復振」/「跟一個死了一百年的師父學手藝」/「織紋是身體的記憶：尤瑪達陸的 34 年」/「名單上沒有石雕：原住民工藝等了 11 年才補位」/「600 位匠師，50 歲以下『只是少數』」/「祖孫一起抹白灰」）。

初稿 prose-health score 4（破折號 32 個 + 對位句型 5 處）。逐句改寫 14 處破折號 → 句號 / 全形冒號 / 全形括號；對位句型「不是 X，是 Y」5 處全收斂為直述句。最終 prose-health score 4 → 1，破折號 32 → 1，對位句型 5 → 0。score 4 → 1 是 dogfood「先寫快後改慢」的具體驗證（先傾倒結構，再用 plugin 抓 violation 逐個改回直述）。

媒體素材 3 張 Wikimedia Commons CC 授權圖片：hero meinong-paper-umbrella-2013.jpg (CC BY-SA 3.0) / inline sanyi-wood-sculpture-museum-2010.jpg (CC BY-SA 3.0) / inline sanxia-indigo-display.jpg (CC BY-SA 4.0)。第一張 sanyi-wood-sculpture-station 0.67 aspect 違反 inline 0.75-2.5 護欄 → 換 museum 外觀 landscape ratio。三張全 cache、aspect 全通過、EXIF GPS 已清。

## Stage 4 + Stage 5 收尾 + cron cascade collision

`article-health.py --profile=rewrite-stage-4` hard=0 warn=0 全 7 plugin pass ✅。Stage 5 cross-link 五條 forward（藍染 / 紙傘 / 台灣花布 / 斗笠 / 傳統節慶與慶典）；reverse cross-link 全 5 sibling DEFER per Step 5.3 sibling 預檢（5 sibling 全有 pre-existing image-health hard fail 0 張 vs depth article ≥ 3 張，補 reverse link 會觸發 pre-commit hook hard fail）。獨立 EVOLVE 各 sibling 圖片補齊應該另開 issue。

sync.sh 跑完（src/content/ gitignored，不影響 commit）。`git add` 我的 7 個檔案發現 staging 區已有 80+ babel translation 檔（twmd-babel routine 在 14:20 平行 git add -A 把我的新檔 swept 進它的 commit `a04a9fe2f`）。**第七棒 routine cascade 撞 babel 平行 commit 邊界錯位**：babel 的 git add 不知道 rewrite routine 也在同 working dir 進行中，bundle 跨 routine 工作邏輯。

軟 reset HEAD~1 → 拆兩個 commit：(1) `3147a527c` 重新提交 babel 75 codex translations（保留原 commit message + 加 re-attribution note）(2) `feea3c672` 提交我的 7 個 rewrite 檔（含完整 metadata）。`git push origin main` 兩個 commit 一起 ship。

Issue #914 已 closed（哲宇 5/8 triage 時就 close + 留 inbox handoff comment）→ 加 ship 通知 comment 報告六方向涵蓋情形 + 必驗事實 verdict + research report link，per ARTICLE-INBOX hard gate「ship 後通知」。

ARTICLE-INBOX entry 整段移除（lines 202-225）+ ARTICLE-DONE-LOG §Log 頂部 append 完整 entry（reverse chronological），per ARTICLE-INBOX 完成歸檔鐵律。

## 收官 checklist

| 檢查項                       | 狀態                                                                                    |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅（本檔）                                                                              |
| Timestamp 精確               | ✅（git log %ai 對齊 +0800）                                                            |
| Handoff 三態已審視           | ✅                                                                                      |
| CONSCIOUSNESS 反映最新狀態   | ⏭️（consciousness-snapshot.sh 早晨已 refresh，本 session 純內容 ship 無需更新組件分數） |
| article-health.py PASS       | ✅ rewrite-stage-4 hard=0 warn=0 全綠                                                   |
| 1 commit push main           | ✅（feea3c672 + 3147a527c babel re-attribution 一起 push）                              |
| ARTICLE-INBOX → DONE-LOG     | ✅（entry 整段搬移，不留 pointer comment）                                              |
| Issue #914 ship-after        | ✅ 加 ship 通知 comment（issue 早已 closed）                                            |

## Handoff 三態

繼承上一 session（spore-harvest-am @ 135828）：

- [ ] **Chrome MCP unattended cron 假設失效**（vc=1）：list_connected_browsers 回 [] → hard gate fail → abort harvest。pairing 持久化 ≠ browser alive 持久化。下次 spore-harvest 觸發前需確認 Chrome 啟動策略
- [ ] **8 條 backfillWarnings 持續累積到 5/16** ⏳ blocked on Chrome MCP unattended access
- [ ] **docs/factory/contributors-maintenance.md prettier diff 連續 4 天觀察**（5/12 + 5/13 + 5/14 + 5/15 都存在）：若明天仍存在 → 開 issue debug update-stats whitespace handling

本 session 新 handoff：

- [ ] **多 routine 平行 git add -A bundle 邊界錯位**（vc=1，第一次發現）：twmd-babel routine 14:20 git add -A 把 twmd-rewrite-daily 進行中的新檔 swept 進它的 commit `a04a9fe2f`。本 session 用軟 reset 拆 commit + re-attribution 解決，但這是 routine 飛輪 race condition：各 routine 跑在同 working dir 時，第一個 `git add -A` + commit 的會吃掉所有 in-progress 工作。**改善方向**：(a) routine 改用 explicit file paths `git add <specific paths>` 而非 `git add -A`（per CLAUDE.md 提示「不要用 git add -A」鐵律的 routine 層體現）(b) 或加 pre-commit guard 偵測「跨 routine narrative scope」（其實本 commit 已被 SESSION-SCOPE.md hook warn）
- [ ] **ARTICLE-INBOX Blue UAS Cleared List 條目 stale**（low priority follow-up）：4 月「台灣無人機產業」EVOLVE 已吸收 Blue UAS Cleared List 主題（title 含「藍色清單」+ tag 含「Blue UAS」），inbox 條目應 drop 或標 `done-absorbed`。下次 maintainer routine 可順手清理
- [ ] **5 sibling pre-existing image-health hard fail**（per Stage 5 Step 5.3 DEFER）：藍染 / 紙傘 / 台灣花布 / 斗笠 / 傳統節慶與慶典 全 0 圖。應該分別開 EVOLVE issue 補圖（per ARTICLE-INBOX 既有 mention「個別工藝雙向」reverse cross-link 待補圖後才能補）

## Beat 5 — 反芻

第七棒 routine 撞上第六棒（babel）平行 commit 的事件，揭露 routine 飛輪假設「各 routine 跑在不同時間、不會碰撞 working dir」這個前提其實**只在 cron 嚴格按時序時成立**。今天的 cron cascade（多個 routine 短時間連環 catch-up fire）讓不同 routine 跑進同一個 working dir 視窗，第一個 `git add` 的會 sweep 所有 in-progress 變更。

跨 routine 工作的 narrative scope 錯位（rewrite 的 Culture 文章被 babel 的 75 翻譯檔 commit 吃掉）有兩層意義：(1) commit message 失去 attribution（讀者看 babel commit log 看不到我這 NEW Culture article）(2) 工作邊界被破壞（如果 babel 因為某 plugin fail 而 abort，我的 rewrite 工作也跟著 rollback）。軟 reset 拆 commit 是補救手段，但比較好的設計是 routine 各自 stage 自己的 explicit paths — 跟過去常踩 `git add -A` 包進不該包的檔案是同類問題的不同 surface。

跟昨天 data-refresh-pm 觀察的「first-shipper-wins 0 diff no-op detection」是同類結構問題：當 routine 飛輪密度高，跨 routine 互動會自然產生 race condition，需要顯式設計（explicit add / 0-diff guard / cross-routine narrative-scope check）來處理。今天的事件可進一步累積這類 LESSONS-INBOX 候選。

🧬

---

_v1.0 | 2026-05-15 14:25 +0800_
_session twmd-rewrite-daily — 台灣傳統工藝與無形文化資產 Fresh ship + 第七棒 cron cascade 撞 babel 平行 commit 軟 reset 拆檔_
_誕生原因：cron `0 0 * * *` +0800 catch-up fire @ 13:50 觸發 routine，依 ARTICLE-INBOX 頂端 P0 取 Issue #914 走 REWRITE-PIPELINE v6.0 Fresh 全 stage_
_核心洞察：(1) Stage 0 §觀點成型 hard gate + general-purpose agent 35 search 的雙層分工是「先觀點再取材」的具體執行模式，本 session dogfood 成功收斂出 29 字核心矛盾；(2) prose-health score 4 → 1 dogfood「先寫快後改慢」的具體驗證（破折號 32 → 1 + 對位句型 5 → 0）；(3) **多 routine 平行 git add -A bundle 邊界錯位**是新發現的 routine 飛輪 race condition — 第一個 `git add` + commit 的會 sweep 所有 in-progress 變更，跨 routine narrative scope 破壞_
_LESSONS-INBOX 候選：(1) Routine git add 應使用 explicit file paths 而非 `git add -A`（per CLAUDE.md 鐵律的 routine 層體現），跟過去手動操作的同類教訓統一 surface；(2) 多 routine 短時間 cascade 共享 working dir 時的 race condition 需顯式設計處理（explicit stage / cross-routine guard / narrative scope hook 已存在但屬 warn 級）_
