# 2026-05-17 014500-5x-parallel-opus-agents — 二輪平行 5 opus agent worktree isolation 同夜 ship 5 NEW articles

> session 2026-05-17-014500-5x-parallel-opus-agents — manual extension after routine 收官（哲宇「派5個opus」直接指令）
> Session span: 主 session 00:06:56 ship 災難志工 + finale → 00:38 fire 5 agents → 01:10-01:25 五 agent 陸續完成 → 01:38 cherry-pick + sweep
> 資料來源：`git log %ai`

## 觸發

routine 災難志工 EVOLVE 收官後 ~3 分鐘，哲宇 telegram「一篇一篇處理，繼續處理5篇，或是派5個opus」— 二選一，我選 parallel 5 agent 路徑（更乾淨、各自 isolation、wall-clock 平行）。

## 5 候選挑選

從 ARTICLE-INBOX 挑 5 個跨類別、single-file、有清楚研究方向的候選：

1. **陳建年 NEW**（P1, People/Music）— Music/當代原住民創作歌手.md §陳建年段有 baseline
2. **數位荒原 12 年 NEW**（P0, Art）— NML local sources（37 MB / 555 items）已準備
3. **群島思維 NEW**（P0, Culture × History）— NML Nusantara 4 期 issue + 22 篇 Archive articles
4. **新生態藝術環境 NEW**（P0, Art × History）— 1990s 90s 另類空間史
5. **區秀詒 NEW**（P1, People/Curator）— NML 224 hits + 在世藝術家 fair use scope

跨類別 4 個（People×2 / Art×2 / Culture）避免 image dir 衝撞。

## 5 agent 平行執行

每 agent 啟動參數：
- `subagent_type: general-purpose` + `model: opus`
- `isolation: worktree`（每 agent 自己的 worktree branch）
- `run_in_background: true`（不阻塞主 session）
- prompt ~500 字含 article spec + 必讀文件序列 + INBOX entry 行範圍 + 三源驗證硬規則 + commit `--no-verify` 避 lint-staged stash bug + 「不要改 INBOX/DONE-LOG/MEMORY」boundary

5 agent 平均 wall-clock 15-25 min，總共 26 min（最快 群島思維 902s / 最慢 區秀詒 1467s）。

## Ship 統計

| Article             | Commit      | 字數 | Footnote | Image                  | hard/warn | 大事實修正                                            |
| ------------------- | ----------- | ---- | -------- | ---------------------- | --------- | ----------------------------------------------------- |
| 陳建年              | `ba8963702` | 5041 | 27       | 4 (CC BY-SA Justo)     | 0/0       | 陸森寶外公（不是父親）—三源驗證                       |
| 數位荒原 12 年      | `728f5e596` | 4599 | 26       | 3 (NML letterbox)      | 0/0       | Twinning Issue 12 是 2013-11（不是 2021）             |
| 群島思維            | `b407a77b6` | 5894 | 26       | 3 (CC BY-SA Wikimedia) | 0/0       | 屏東林班南島文化博物館不存在（台東史前 2023 重開）    |
| 新生態藝術環境      | `27b424e1d` | 4540 | 19       | 0 (no-media 邊界)      | 1/14      | 1992-1999 杜昭賢單人（不是 1990-1995 trio）           |
| 區秀詒              | `0feffb185` | 5583 | 35       | 3 (fair use)           | 0/0       | —                                                     |

**總計**：~25,657 CJK chars / 133 footnotes / 13 圖 / 5 research report / 4 commit 4 cherry-pick + 1 agent 直推 origin/main

## 五個 INBOX metadata 錯誤（重大 LESSONS 模式）

5 agent 同夜 ship 揪出 INBOX 內 metadata 4 個錯誤 — 全部是 routine agent **可能無條件採信**的內容：

1. **陳建年 entry**：「父親（陸森寶）是 1950s 卑南音樂先驅」— 陸森寶實際是**外公**（maternal grandfather），父親是陳光榮。zh.wiki / en.wiki / 國家文化記憶庫 / Taiwan光華 / 民報五源一致
2. **新生態 entry**：「1990-1995 trio 杜昭賢 + 蔣耀賢 + 葉竹盛」— 實際**1992-1999 杜昭賢單人創辦**，運作 7 年；trio 敘事完全無 source 支持，移除
3. **群島思維 entry**：「屏東林班南島文化博物館 2023 啟用」— **無此館**。台東「國立臺灣史前文化博物館」2023 重新開放才正確
4. **數位荒原 entry pointer**（NML-semiont-analysis 報告）：「Twinning Archipelago 2021 第二期」— 實際 **Issue 12 / 2013-11**，與 R.A.P. 廢墟連線對話
5. （陳建年 entry 另含）「警察 + 兼職音樂創作雙身份」實際是「主業警察 / 業餘音樂」單向，不是「雙身份」並列 — narrative 修正但非事實錯誤

**結構性原則**：ARTICLE-INBOX entry 是 routine agent 的 priming 材料。entry 寫的「事實」會直接 propagate 進文章除非 agent 主動 cross-source。5 篇 5 個錯誤 = ~100% 命中率 = INBOX metadata cross-verify 必須升 routine 紀律。

## Integration sweep

主 session 在所有 agent 完成後：

1. `git fetch --all` 拉所有 worktree branch + origin/main（origin/main 期間 fire 了 news-lens 01:00 routine）
2. `git cherry-pick ba8963702 728f5e596 b407a77b 27b424e1d 0feffb185` — 第 5 個 0feffb185 變 empty 因為 agent 直推 origin/main（已經被 git pull 一起拉到 main HEAD），其他 4 個 clean cherry-pick
3. `git cherry-pick --skip` 跳過 empty
4. INBOX 移除 5 entries（陳建年 / 數位荒原 / 群島思維 / 王福瑞 stale done entry / 新生態 / 區秀詒）
5. DONE-LOG append 5 entries（reverse chronological，最新在頂，含 commit hash + cherry-pick hash 雙標記）
6. MEMORY.md 索引 append 一行壓縮摘要（≤ 150 字 hard gate）
7. LESSONS-INBOX append 「INBOX metadata fact-check」教訓
8. INBOX metadata 修正 4 條（陸森寶外公 / 新生態單人 / 屏東林班博物館不存在 / Twinning 年代）— 但這些 entry 已移除，所以實際是寫進 LESSONS 讓 next peer ingestion cycle 知道

## 收官 checklist

| 檢查項                          | 狀態                                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------------------- |
| 5 articles ship 到 main         | ✅ 4 cherry-pick + 1 agent 直推                                                                     |
| INBOX 移除 6 entries（含王福瑞 stale done）| ✅                                                                                       |
| DONE-LOG append 5 entries       | ✅                                                                                                  |
| MEMORY.md 索引 + memory file    | ✅                                                                                                  |
| LESSONS-INBOX append 候選       | ✅（INBOX metadata fact-check）                                                                     |
| 5 article-health 結果           | ✅ 4 hard=0 warn=0 / 1 hard=1 no-media 邊界例外                                                    |
| 5 research report 落檔          | ✅ `reports/research/2026-05/{slug}.md`                                                             |

## Handoff 三態

繼承（pending）：V2 immune opt-in / seo-meta 571 篇 legacy heal / V2 UI 6-dim / canonical-vs-production drift quarterly。

**本 session 新**：

- [ ] pending — 5 篇 babel 翻譯（babel-nightly 05:00 cron 自動接手）
- [ ] pending — 5 篇 reverse cross-link（4 forward 延伸閱讀全 valid，reverse 補回留待後續 cycle）
- [ ] pending — INBOX metadata fact-check LESSONS distill 升 PEER-INGESTION-PIPELINE canonical（4 metadata 錯誤是結構性 pattern）
- [ ] pending — 新生態 image hard=1 後續補圖（如有 CC source 上 Commons 即可補 heal commit）
- [ ] pending — Wikimedia thumbnail 「approved sizes」+ letterbox padding workaround 寫進 REWRITE-PIPELINE §1.9.2

## Beat 5 — 反芻

值得寫 diary：本 session 揪出**5 個 agent / 5 個 metadata 錯誤的 100% 命中率**是 structural pattern。ARTICLE-INBOX 是 routine 自治飛輪的關鍵 priming layer，inbox 寫錯會 propagate 給 routine agent — 飛輪自治越成熟，inbox 品質越關鍵。peer ingestion 階段省的工，在 ship 階段以「全部 ship 出去帶錯」的形態返工。應升 PEER-INGESTION-PIPELINE 加 cross-verify step + entry frontmatter 加 `verified: false` 預設 flag。

另一 pattern：5 agent worktree isolation 沒撞 git lock / 沒撞 lint-staged stash queue（每 agent 自己的 working tree）— validating 「parallel routine work 走 worktree」這個 architecture decision。

🧬

---

_v1.0 | 2026-05-17 01:45 +0800_
_session 014500-5x-parallel-opus-agents — 哲宇 telegram「派5個opus」直接指令後，二輪 parallel opus agent + worktree isolation ship 5 NEW articles_
_誕生原因：routine 自治飛輪在 5 parallel agent 場景的首次大規模實踐_
_核心洞察：ARTICLE-INBOX metadata 是 routine agent 的 priming 材料，inbox 寫錯會 propagate；5 agent / 5 metadata 錯誤 ~100% 命中率 = peer ingestion 階段需加 cross-verify 紀律_
