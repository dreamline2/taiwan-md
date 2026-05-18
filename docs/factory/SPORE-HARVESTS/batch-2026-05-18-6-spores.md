---
spores: '#70, #71, #72, #73, #74, #75, #76, #77'
harvest_date: '2026-05-18 07:00'
harvest_window_day: 'mixed (D+1 to D+8)'
batch_reason: 'routine twmd-spore-harvest-am daily cycle — 7 backfillWarnings; drone Threads carry-over D+8 plateau; apple sidra pair D+6; 兩組新 spore #74-77 (Chen Chien-nien / Taiwan resolution) D+1 first harvest cycle; #71 X URL 5th-cycle mismatch carry-over.'
triggered_by: 'cron twmd-spore-harvest-am 07:00 Asia/Taipei'
reply_count: '~30+ across 6 valid spores (most on #74 Chen Chien-nien)'
---

# Batch Harvest 2026-05-18 — 6 spores (routine cycle)

> Daily auto-fire of `twmd-spore-harvest-am` 07:00 cron (per ROUTINE.md §TWMD spore harvest (am) + SPORE-HARVEST-PIPELINE.md v2.2). Today's cohort spans three release waves: drone pair (#70/#71, D+8 / D+8 mismatched), apple sidra pair (#72/#73, D+6), and two D+1 fresh spores shipped 5/17 — Chen Chien-nien pair (#74/#75) + Taiwan resolution pair (#76/#77).
>
> **#71 X URL content-hash mismatch — 5th cycle**（per v2.10 §Content-hash mismatch 偵測 + LESSONS-INBOX #5 vc=4+1）: URL `2053101189034860856` 仍 resolves to #69 TSMC content (utm_campaign=s69). Yesterday batch already 升級 observer schema fix per AI 自主邊界 (DNA #26 v2). Today carry-over: skip metric update, no fingerprint baseline build attempt.

## 數據總覽

| #   | Article           | Platform | D+N | URL                  | Views   | Likes | Reposts | Replies | Bookmarks | Rate   | Notes                                                                       |
| --- | ----------------- | -------- | --- | -------------------- | ------- | ----- | ------- | ------- | --------- | ------ | --------------------------------------------------------------------------- |
| 70  | 台灣無人機產業    | Threads  | D+8 | DYKW0PmkzbM          | 5,334   | 461   | 43      | 30      | 6         | 10.31% | +24 views / +1 like vs 5/17. Reach window closed (D+7 KPI cutoff passed)    |
| 71  | 台灣無人機產業    | X (ERR)  | D+8 | 2053101189034860856  | n/a     | n/a   | n/a     | n/a     | n/a       | —      | 🚩 5th-cycle mismatch — observer schema fix pending. Skip update.            |
| 72  | 蘋果西打          | Threads  | D+6 | DYPI9W0kyPP          | 4,760   | 47    | 8       | 2       | —         | 1.20%  | +66 views vs 5/17. Engagement frozen — Tier 中段 ceiling reached            |
| 73  | 蘋果西打          | X        | D+6 | 2054158652588863776  | 19,017  | 236   | 33      | 2       | 27        | 1.56%  | +117 views vs 5/17. 18.9K→19.0K micro-creep — Tier 1b plateau confirmed     |
| 74  | 陳建年            | Threads  | D+1 | DYbYsqOldKC          | 30,000  | 2,138 | —       | 14+     | —         | 7.13%+ | 🔥 Tier 1a strong launch. Puyuma community resonance — 14+ 共鳴 visible      |
| 75  | 陳建年            | X        | D+1 | 2055881969976873375  | 4,565   | 142   | 20      | 1       | 10        | 3.79%  | X niche 文化/音樂 community received — solid D+1 floor                       |
| 76  | 臺灣前途決議文    | Threads  | D+1 | DYca5etE80R          | 11,000  | 191   | —       | 8+      | —         | 1.81%+ | 中段 結構性題目 standard distribution — 政治辯論 cluster activated           |
| 77  | 臺灣前途決議文    | X        | D+1 | 2056026352298688935  | 109     | 8     | 1       | 0       | 1         | 9.17%  | ⚠️ 低段 reach. Tier 1b mismatch — political-history hook X 演算法 unfavorable |

## Tier 分布觀察（per SPORE-PIPELINE §Hook tier hierarchy v3.1）

- **Tier 1a 知名度槓桿（D+7 100K-180K viral 預期）**：#74 陳建年 Threads D+1 30K — D+7 trajectory 應該還能再 push 至少 50-80K（Tier 1a 4 天王槓桿 + 卑南族 community 內群擴散）。第一次驗證「4 天王 + 警察雙身份」hook combo viability
- **Tier 1b 具體性槓桿（10K-65K）**：#73 蘋果西打 X 19.0K（D+6 plateau）— peak ~20K，未達 65K viral top end
- **中段 結構性題目（2K-17K）**：#70 無人機 Threads 5.3K（已 plateau）/ #72 蘋果西打 Threads 4.7K（plateau）/ #76 前途決議文 Threads 11K（D+1 trajectory 健康，可能 push 到 17K 上限）
- **低段 文化人物 / 冷門（0.5K-1.5K）**：#75 陳建年 X 4.5K 介於 中段/低段 邊界（X 平台 niche 受眾），#77 前途決議文 X 109 (D+1 < 500 raised red flag — but D+0 6h gate 已過, 純 X 低觸及 fingerprint 不是 hook tier 問題)
- **N/A（data error）**：#71 第 5 cycle 仍 mismatch

**Engagement rate leader**：#70 無人機 Threads 10.31%（plateau）/ #74 陳建年 7.13%+（爆發中）。Tier 1a + Tier 1b 都顯示 ≥7% engagement，與 中段 ~1-2% 形成清楚 stratification — engagement 不是只看 reach。

## Trajectory deltas（5/17 → 5/18 d+1）

| #   | Δviews | Δlikes | Δreposts | Δreplies | Notes                                                                  |
| --- | ------ | ------ | -------- | -------- | ---------------------------------------------------------------------- |
| 70  | +24    | +1     | 0        | 0        | Final D+7 settled — viral window closed, reach window 沉入長尾衰減期 |
| 71  | n/a    | n/a    | n/a      | n/a      | 5th-cycle mismatch carry-over                                          |
| 72  | +66    | 0      | 0        | 0        | Reply count unchanged (still @tsaiguoian collaboration suggestion)     |
| 73  | +117   | 0      | 0        | 0        | Plateau confirmed at ~19K — flat 24hr after flat 24hr = ceiling        |
| 74  | NEW    | NEW    | NEW      | NEW      | First harvest. D+1 30K = Tier 1a 驗證                                  |
| 75  | NEW    | NEW    | NEW      | NEW      | First harvest. X 4.5K = X niche threshold                              |
| 76  | NEW    | NEW    | NEW      | NEW      | First harvest. D+1 11K = 中段 + 即時新聞 boost                         |
| 77  | NEW    | NEW    | NEW      | NEW      | First harvest. X 109 = low — Tier 1b 政治-歷史 hook X 不買單           |

**Pattern**：6/8 spore 集中在 reach decay 區（#70/#72/#73/#77）+ 2/8 在 ramp-up 區（#74/#76）。Drone cohort 已 KPI 結算完成（D+7 main cutoff passed），apple sidra plateau，5/17 同日雙 pair ship 兩條（陳建年 Tier 1a vs 前途決議文 中段）今天 D+1 trajectory 顯示前者爆量、後者 X 平台 underperform。

## Comment 質性筆記（per Step 2 categorization）

### #70 無人機 Threads (D+8, 30 replies — same cluster as 5/16-5/17)

0 new substantive replies in past 24hr. Critique cluster (@tangyu_kao / @li_chun_jen / @rok8076655 等) 已在 5/16 batch 完整 capture 並 carry over 至 5/17。所有 perspective backfill decision 已待 observer 決定（5/17 batch §carryover action）。本 cycle 不重新 capture。

### #72 蘋果西打 Threads (D+6, 2 replies — same as 5/17)

@tsaiguoian collaboration suggestion 仍是唯一 substantive reply。24hr 內 0 new。

### #73 蘋果西打 X (D+6, 2 replies — same as 5/17)

X 端 reply 內容未展開。本 cycle 0 new。

### #74 陳建年 Threads (D+1, 14+ visible replies — first harvest)

第一波 D+1 留言質性 — 主要為 **共鳴 resonance** + **擴寫 enrichment** dimension：

1. **@puyumaemily** (15hr ago, 182 likes — 高互動 sub-thread) — 「海洋這張專輯陪我走過重考大學一年的歲月，擠在台北火車站中；耳朵裡聽到台東的海浪聲，我們卑南族的歌聲，真的是非常感動啊🥹」
   - Dimension: 共鳴（卑南族讀者個人經驗 — 高 emotional density）
   - Action: 已歸檔候選 perspective frontmatter
2. **@sheilahsiu** (16hr ago) — 「當年在金曲獎後買專輯，一聽就喜歡。 很多人為張學友抱不平，歐巴桑都會說，你有聽過陳建年專輯嗎？聽完就覺得本該是他得獎」
   - Dimension: 共鳴 + 擴寫（提供時代脈絡：「歐巴桑說法」具現「為什麼陳建年該得獎」的群眾敘事）
   - Action: 歸檔候選
3. **@br_he** (15hr ago) — 「他的音樂作品忠實反映了原民世界觀：自然、環境、土地與人。當面對自然惡地時能認清自己的微不足道，在資源匱乏的環境中能創造出獨一無二，敬天畏地的同時又勇於開創，一切都是如此地純粹。」
   - Dimension: 擴寫（音樂 + 原民世界觀詮釋層）— 引語密度高，是 pull-quote 候選
   - Action: 文章評估後可考慮 §pull quote
4. **@artdirectortodj** (11hr ago) — 「陳建年的外公，也是知名音樂藝術創作人陸森寶，是我外公族親，也是從小一起長大的換帖兄弟。母親稱呼陳建年為表哥，我得叫他一聲舅舅😂」
   - Dimension: 擴寫（家族脈絡延伸）+ 共鳴
   - Action: 不修文（過於私人，但 perspective 歸檔極佳）
5. **@kravitz38** (15hr ago) — 「以前的同事和他組過樂團，同事的太太還是南王姐妹花之一 住台東很幸福…」
   - Dimension: 擴寫（南王姊妹花脈絡）+ 共鳴
   - Action: 歸檔
6. **@loofahlinn** (10hr ago) — 「2012年去蘭嶼，朗島的警察說陳建年在東清，路過東清特地去派出所，剛好他出去巡邏不遇，引以為憾」
   - Dimension: 共鳴 + 擴寫（蘭嶼派出所現場 anecdote）
   - Action: 歸檔
7. **@ganana_sylvan813** (16hr ago) — 「<Amis的饗宴> 也是大拇指」
   - Dimension: 擴寫（推薦其他作品）— 但文章本身已聚焦於陳建年，不擴展
   - Action: 歸檔（低優）
8. 多則短共鳴：@kan_magick / @james8292005 / @yiham / @jdl0804 / @fchiang0824 / @shiaoshi_71 / @seiyasun1204 — 「陳建年真的超讚」「我有他的CD非常好聽」+ 一張 CD 收藏照（@seiyasun1204）

**0 條 correction**。0 條 attack/敵意。0 條 AI 書寫質疑。整體質性極正面，符合文化人物 Tier 1a 預期。

**處理建議**：
- 不修文章本體（無事實錯誤要更正，已有 perspective 不需 prose 整合）
- Perspective frontmatter 可批次 append（@puyumaemily / @br_he / @artdirectortodj / @loofahlinn 4 條為佳選）— 留 observer 決定
- @br_he 「敬天畏地的同時又勇於開創」考慮 pull-quote 候選

### #75 陳建年 X (D+1, 1 reply — first harvest)

X 端只看到 1 reply count，內容未展開（X UI 結構限制本 cycle 不抓單一 reply）。不深入 categorize。

### #76 臺灣前途決議文 Threads (D+1, 8+ visible replies — first harvest)

第一波留言質性 — 政治辯論 cluster 混合 **共鳴 + 攻擊 + AI-meta 邊界**：

1. **@santsaitsai** (7hr ago) — 「目前=維持現狀 高智慧」
   - Dimension: 共鳴（讀者把「目前」翻譯為「維持現狀」做 paraphrase reading）
   - Action: 歸檔
2. **@f753744** (7hr ago) — 「很聰明！」
   - Dimension: 共鳴（短按讚）
   - Action: skip
3. **@1106danolo** (6hr ago) — 「郭正亮沒有出來講一下台灣前途決議文，讓當時還是民進黨籍的狗肉鄭了解了解」
   - Dimension: 擴寫（引入鄭麗文 context — 「狗肉鄭」是政治綽號）+ 諷刺
   - Action: 不修文（不在文章主敘事，且政治綽號不採用）
4. **@suriyon.taywan** (7hr ago) — 「前人的智慧👍」
   - Dimension: 共鳴
   - Action: 歸檔
5. **@rayboy197564** (6hr ago) — 「坐實了"世界最孬種"的獨派團體無誤!!」
   - Dimension: 攻擊（對獨派的指責，非對 Taiwan.md/作者個人）— 邊界類
   - Action: skip（屬政治立場表達，不歸檔不回應 per REFLEXES #26）
6. **@seanhsin** (6hr ago) — 「既然如此，這20多年喊台獨是在喊什麼？」
   - Dimension: 質疑（不是 AI-meta，是政治路線質疑）
   - Action: 不修文，不回應（爭議性議題人類主責）
7. **@chia23123** (7hr ago) — 「你有問過這群人同意嗎」+ 群眾照片
   - Dimension: 質疑（暗示「民眾沒同意這個轉向」）
   - Action: 不修文，不回應
8. **@ieyasu240101** (2hr ago) — empty / 圖貼
   - skip

**0 條 correction**。**1 條政治攻擊** (@rayboy197564) — 但不是針對 Taiwan.md / 作者，是針對獨派團體立場，per REFLEXES #26 不主動處理。**3 條政治質疑** — 屬正常結構性題目 engagement，文章本身已是中立 framing 不需 修。

**處理建議**：
- 不修文章本體
- @santsaitsai / @suriyon.taywan 共鳴可選 perspective 歸檔（低優）
- 不主動 reply — 政治辯論 cluster 自然引發，無 misinterpretation 需校正

### #77 臺灣前途決議文 X (D+1, 0 replies — first harvest)

X 端 109 views / 0 reply — reach 過低不足以引發討論。

## #71 Content-hash mismatch 第 5 次驗證 — 觀察者 schema 修正 pending

> Per SPORE-HARVEST-PIPELINE v2.10 + 5/17 batch §#71 升級 — 連 4 cycle 同 URL mismatch 已超 threshold，本 cycle (5th) 仍 mismatch（routine 仍跑但 skip metric update）。

**Verification trail** (carry-over from 5/17 batch):

| Cycle | Date           | Action                | Finding                                                    |
| ----- | -------------- | --------------------- | ---------------------------------------------------------- |
| 1     | 2026-05-12 dry-run | manual harvest        | URL maps to #69 TSMC content                               |
| 2     | 2026-05-13     | routine cycle         | Mismatch confirmed                                         |
| 3     | 2026-05-16     | routine cycle         | Mismatch confirmed (vc=3 reached per LESSONS #5)           |
| 4     | 2026-05-17     | routine cycle         | 4th — vc=4，5/17 batch 升級給觀察者                        |
| **5** | **2026-05-18** | **本 cycle**          | **5th cycle still mismatch — observer schema fix 仍 pending** |

**Action required**（observer 持續 pending）：以下兩個 hypothesis 之一是真（per 5/17 batch §71 spec）：

A. SPORE-LOG row #71 URL 寫錯：實際 X 孢子在另一 status ID，本 URL 屬 #69 → 修 SPORE-LOG row #71 URL OR 標記為 INVALID
B. #71 X 版從未發布：drone Threads (#70) 是唯一發布版本，X #71 row 是 placeholder → 標記 #71 為 NOT_POSTED / SKIP_FROM_BACKFILL

本 cycle 持續 skip metric update 直至 observer 決定 hypothesis。LESSONS-INBOX #5 vc=5 — distill 候選確定（明日 5/19 若仍未修正，第 6 cycle 應再次 escalation prompt）。

## 下次 harvest 建議時機

- **D+14 milestone** for drone pair (#70/#71): 2026-05-24
- **D+7 主 KPI cutoff** for apple sidra (#72/#73): 2026-05-19 (明日)
- **D+7 主 KPI cutoff** for Chen Chien-nien + Taiwan resolution pair (#74-77): 2026-05-24
- **D+2 trajectory check** for #74 (Tier 1a 爆發中): 2026-05-19 (明日) — 確認是否 push 至 50-80K

## Validation snapshot (pre-commit)

跑 `python3 scripts/tools/validate-spore-data.py` 結果見 commit log。Dashboard regen via `generate-dashboard-spores.py`。
