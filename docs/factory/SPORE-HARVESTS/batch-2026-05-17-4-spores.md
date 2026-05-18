---
spores: '#70, #71, #72, #73'
harvest_date: '2026-05-17 07:00'
harvest_window_day: 'mixed (D+5 to D+7)'
batch_reason: 'routine twmd-spore-harvest-am daily cycle — 4 backfillWarnings (2 OVERDUE D+7 drone + 2 waiting D+5 apple sidra); D+1 delta vs 5/16 batch on same 4-spore cohort'
triggered_by: 'cron twmd-spore-harvest-am 07:00 Asia/Taipei'
reply_count: '~12 visible across 3 valid spores (skip #71 url mismatch; +1 new reply on #72 since 5/16)'
---

# Batch Harvest 2026-05-17 — 4 spores（routine cycle, D+1 delta vs 5/16）

> Daily auto-fire of `twmd-spore-harvest-am` 07:00 cron (per ROUTINE.md §TWMD spore harvest (am) + SPORE-HARVEST-PIPELINE.md v2.2). Same 4-spore cohort as 5/16 batch — D+1 trajectory update. Drone pair now at D+7 (主要 KPI cutoff), apple sidra pair at D+5.
>
> **Content-hash mismatch — 3rd verification on #71**（per v2.10 §Content-hash mismatch 偵測 + LESSONS-INBOX #5）：URL `2053101189034860856` resolves to #69 TSMC content (utm_campaign=s69), confirming SPORE-LOG row for #71 has wrong URL OR #71 X version was never posted. Vc now reaches threshold 3 → 升級給觀察者 schema 修正（per DNA #26 v2 AI 自主邊界）.

## 數據總覽

| #   | Article         | Platform | D+N | URL                     | Views  | Likes | Reposts | Replies | Bookmarks | Rate   | Notes                                                              |
| --- | --------------- | -------- | --- | ----------------------- | ------ | ----- | ------- | ------- | --------- | ------ | ------------------------------------------------------------------ |
| 70  | 台灣無人機產業  | Threads  | D+7 | DYKW0PmkzbM             | 5,310  | 460   | 43      | 30      | 6         | 10.34% | +11 views vs 5/16. Flatline reach decay (d+6→d+7), engagement frozen — 主要 KPI cutoff snapshot |
| 71  | 台灣無人機產業  | X (ERR)  | D+7 | 2053101189034860856     | n/a    | n/a   | n/a     | n/a     | n/a       | —      | 🚩 DATA ERROR carryover (**3rd verification**) — URL resolves to #69 TSMC (utm_campaign=s69). Skip metric update per v2.10. |
| 72  | 蘋果西打        | Threads  | D+5 | DYPI9W0kyPP             | 4,694  | 47    | 8       | 2       | —         | 1.21%  | +7 views, +1 like, +1 reply vs 5/16. New reply @tsaiguoian (13hr ago) — collaboration suggestion |
| 73  | 蘋果西打        | X        | D+5 | 2054158652588863776     | 18,900 | 236   | 33      | 2       | 28        | 1.58%  | Flatline (~18.9K from 5/16 18,972). Tier 1b 突破 10K trajectory holds; D+7 預期 ~20-25K          |

## Tier 分布觀察（per SPORE-PIPELINE §Hook tier hierarchy v3.1）

- **Tier 1b 具體性槓桿（10K-65K）**：#73 蘋果西打 X 18.9K（D+5 flatline，可能 plateaued — 等 D+7 確認）
- **中段 結構性題目（2K-17K）**：#70 無人機 Threads 5.3K / #72 蘋果西打 Threads 4.7K
- **低段 文化人物 / 冷門（0.5K-1.5K）**：無
- **N/A（data error）**：#71 SPORE-LOG mapping 第三次驗證仍 mismatch

**Engagement rate leader**：#70 無人機 Threads 10.34%（與 5/16 10.36% 基本相同，爭議性激活 plateau）。Tier 1b 黏度型 + 中段結構性題目混合 D+7 確認。

## Trajectory deltas（5/16 → 5/17 d+1）

| #   | Δviews     | Δlikes   | Δreplies         | Notes                                                          |
| --- | ---------- | -------- | ---------------- | -------------------------------------------------------------- |
| 70  | +11        | 0        | 0                | Reach decay 已啟動，d+6 vs d+7 微增量說明演算法窗口逼近收尾    |
| 71  | n/a        | n/a      | n/a              | 仍 mismatch                                                    |
| 72  | +7         | +1       | +1               | tsaiguoian collaboration suggestion — 低聲量但有 brand 對話    |
| 73  | -72 (flat) | 0        | 0                | 18.9K plateau — Tier 1b 突破後可能 saturate 在此 viral cohort |

**Pattern**：4 spore 同時進入 d+5 / d+7 reach decay 區，無新爆發 — 演算法窗口正常衰減，符合 cadence 預期。

## Comment 質性筆記（per Step 2 categorization）

### #70 無人機 Threads（30 replies — same cluster as 5/16，no new substantive critique）

所有 substantive critique 已在 5/16 batch 完整 capture（[batch-2026-05-16-8-spores.md §#70](batch-2026-05-16-8-spores.md)）。今日 0 new replies — critique cluster pushback 已飽和。

**Carryover action**（仍待 observer / maintainer 評估）：

1. @tangyu_kao / @li_chun_jen / @jgo911131 critique cluster 觸及「雷虎現況 ≠ 全盛雷虎人馬」+「BlueUAS 不用太迷信」+「未拿到標案」三 angle — 是否更新文章 prose 加註 reader perspective？
2. @huian.c / @rok8076655 political-tone critiques 屬「立場表達」非事實校正，不需修文。

**Status**: 文章 perspectives frontmatter 已 5/16 標記，不再 backfill。

### #72 蘋果西打 Threads（2 replies — +1 since 5/16）

1. **@tsaiguoian (5/16, 13hr ago)** — 「希望能和 @kandao.tw 合作」
   - Dimension: 建議（外部合作建議 — kandao 看 X handle 推測為品牌帳號）
   - Action: 不修文。AI draft optional reply：「謝謝建議！這條我們轉給原作者 Taiwan.md maintainer 評估」(human post)

### #73 蘋果西打 X（2 replies — same as 5/16，未開新文）

5/16 已 record 2 replies（內容未展開 - 需要 click 進去看）。本次 24hr 內無新 reply。

## #71 Content-hash mismatch 第三次驗證 — 升級

> Per SPORE-HARVEST-PIPELINE v2.10 §Content-hash mismatch 偵測：「連續 3 cycle 同 URL mismatch → 升級給觀察者 SPORE-LOG schema 修正」

**Verification trail**：

| Cycle | Date            | Action                            | Finding                                                   |
| ----- | --------------- | --------------------------------- | --------------------------------------------------------- |
| 1     | 2026-05-12 dry-run | manual harvest                     | URL maps to #69 TSMC content                              |
| 2     | 2026-05-13 first prod | routine cycle                    | Mismatch confirmed                                        |
| 3     | 2026-05-16     | routine cycle                     | Mismatch confirmed (vc=3 threshold reached per LESSONS #5) |
| **4** | **2026-05-17** | **本 cycle**                      | **第 4 cycle 仍 mismatch — SPORE-LOG schema 必修正**       |

**Action required**（observer）：以下兩個 hypothesis 之一是真：

A. SPORE-LOG row #71 URL 寫錯：實際 X 孢子在另一 status ID，本 URL 屬 #69 → 修 SPORE-LOG row #71 URL OR 標記為 INVALID
B. #71 X 版從未發布：drone Threads (#70) 是唯一發布版本，X #71 row 是 placeholder → 標記 #71 為 NOT_POSTED / SKIP_FROM_BACKFILL

**建議解法**：observer 確認 hypothesis 後手動修正 SPORE-LOG row #71 URL column 或加 `status: not_posted` flag，避免下次 routine 再撞同一 mismatch。

LESSONS-INBOX #5 verification_count 從 vc=3 升 vc=4 — distill 候選確定。

## 下次 harvest 建議時機

- **D+14 milestone** for drone pair (#70/#71): 2026-05-24
- **D+7 主 KPI cutoff** for apple sidra (#72/#73): 2026-05-19
- 預期 5/19 是 4 spore cohort 全進入「主 KPI 結算」第一日，可拉 D+7 final reach 比較表

## Validation snapshot（pre-commit）

跑 validate-spore-data.py 結果見 commit log。Dashboard regen via generate-dashboard-spores.py。
