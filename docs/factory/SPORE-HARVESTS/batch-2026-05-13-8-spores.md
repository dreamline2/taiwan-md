---
spores: '#66, #67, #68, #69, #70, #71, #72, #73'
harvest_date: '2026-05-13 07:05'
harvest_window_day: 'mixed (D+1 to D+5)'
batch_reason: 'routine twmd-spore-harvest-am first auto-fire cycle — all 8 backfillWarnings OVERDUE/waiting; includes 2 fresh 蘋果西打 spores D+1 + delta updates on 6 carryover from 5/12 batch'
triggered_by: 'cron twmd-spore-harvest-am 07:00 Asia/Taipei first auto-fire'
reply_count: '17 visible across 8 spores'
---

# Batch Harvest 2026-05-13 — 8 spores（routine v2.2 first auto-fire）

> First production auto-fire of `twmd-spore-harvest-am` 07:00 cron (per ROUTINE.md §TWMD spore harvest (am) + SPORE-HARVEST-PIPELINE.md v2.2). All 8 entries surfaced in `dashboard-spores.json.backfillWarnings`. Carries forward 5/12 batch's data integrity findings (#69 + #71 X URL anomaly still unhealed in SPORE-LOG).

## 數據總覽

| #   | Article             | Platform | D+N | URL                     | Views | Likes | Reposts | Replies | Bookmarks | Notes                                                                       |
| --- | ------------------- | -------- | --- | ----------------------- | ----- | ----- | ------- | ------- | --------- | --------------------------------------------------------------------------- |
| 66  | 聶永真              | Threads  | D+5 | DYE7ZAik0qr             | 1,586 | 101   | —       | 3       | —         | +92 views vs 5/12. 1 新留言（@eva13.68 共鳴 5/12 22:07）                    |
| 67  | 聶永真              | X        | D+5 | 2052721374570106952     | 8,987 | 376   | 60      | 0       | 30        | +13 views vs 5/12. flatline reach, no new engagement                        |
| 68  | 台灣企業：台積電    | Threads  | D+4 | DYHoQtCE-5Z             | 2,864 | n/a   | —       | 1       | —         | +10 views vs 5/12. correction (@clairewu16888 → PR #950) already integrated |
| 69  | 台灣企業：台積電    | X (DEP)  | D+4 | 2053100425730269544     | 6     | 0     | 0       | 0       | 0         | ⚠️ DEPRECATED — X UI "new version" → 2053101189034860856                    |
| —   | **台積電 X 真實版** | X        | D+4 | **2053101189034860856** | 3,320 | 82    | 17      | 2       | 8         | ⭐ canonical (+17 views vs 5/12)                                            |
| 70  | 台灣無人機產業      | Threads  | D+3 | DYKW0PmkzbM             | 5,193 | 460   | —       | 11+     | —         | +53 views, several new replies. Tier 1b 持續高 engagement                   |
| 71  | 台灣無人機產業      | X (ERR)  | D+3 | 2053101189034860856     | n/a   | n/a   | n/a     | n/a     | n/a       | 🚩 DATA ERROR carryover — URL 內容仍是 台積電（emoji 🏭），不是無人機       |
| 72  | 蘋果西打            | Threads  | D+1 | DYPI9W0kyPP             | 3,857 | n/a   | —       | 0       | —         | 🆕 first harvest. D+1 11hr post-publish, no replies yet                     |
| 73  | 蘋果西打            | X        | D+1 | 2054158652588863776     | 9,942 | 119   | 18      | 2       | 12        | 🆕 first harvest. Tier 1b solid（D+1 ~10K → likely 10-15K D+7 trajectory）  |

## D+1 蘋果西打 6h Decision Gate（per pipeline §d+0 6h Decision Gate）

- **#73 X**: D+1 ~12hr → 9,942 views. ✅ 遠超 500 threshold. No re-hook needed.
- **#72 Threads**: D+1 ~12hr → 3,857 views. ✅ 遠超 500. No re-hook needed.
- 兩者 cross-platform 都健康，蘋果西打文章本身（食品 / 文化 / 商業多層）覆蓋廣 audience。

## Tier 分布觀察（per SPORE-PIPELINE §Hook tier hierarchy v3.1）

- **Tier 1b 具體性槓桿（10K-65K）**：#73 蘋果西打 X 9.9K（D+1 trajectory 預期會 break 10K threshold）
- **中段 結構性題目（2K-17K）**：#67 聶永真 X 9K / #68 台積電 Threads 2.9K / **#71 台積電 X v2 (3.3K)** / #70 無人機 Threads 5.2K / #72 蘋果西打 Threads 3.9K
- **低段 文化人物 / 冷門（0.5K-1.5K）**：#66 聶永真 Threads 1.6K
- **N/A（data error / deprecated）**：#69 + #71 SPORE-LOG mapping 仍未 heal

## Comment 質性筆記（per Step 2 categorization）

### #66 聶永真 Threads（3 comments）

1. **@tsaiguoian (5/8 20:31)** — 「問題：同樣的圖片重複出現」
   - Dimension: 建議（UX bug report — possibly about post media or article images）
   - Action: 待 observer 判讀（不確定指向是哪張圖）

2. **@eva13.68 (5/12 22:07)** — 「謝謝你💕」
   - Dimension: 共鳴
   - Action: 按讚即可

3. **@hsinyuwang.art (5/9 04:13)** — 引用 Yahoo 新聞 update：「台電晚間證實，當年確實是親邀于老書寫，但現在的草體 LOGO 也非當年真跡，而是民國 81 年、82 年間，同仁臨摹重新排列」
   - Dimension: **擴寫 enrichment**（補充事實更新層）
   - Action: 高優先 — 文章本體可加 footnote 或補充段「台電後續澄清：1992-1993 同仁臨摹重排」。傳給 maintainer-am 09:00 評估納入

### #68 台積電 Threads（1 reader correction，已處理）

- **@clairewu16888 (5/9 21:24)** — 「1987 年是 2 吋晶圓廠，不是 2 奈米」
- Status: ✅ **已整合**（5/9 PR #950，三處勘誤 reader-driven retroactive audit）
- 留言 thread 含 Taiwan.md 自我 reply 兩則公開致謝

### #70 無人機 Threads（11+ comments — 高互動 batch）

**Substantive critique cluster（建議 maintainer-am 評估）**：

1. **@tangyu_kao** — 「你知道雷虎是唯一沒拿到標案的嗎...連台中同行亞拓都打不過，靠著代理遙控車在苟延殘喘，現在希望全壓在無人機國家隊上」
2. **@li_chun_jen** — 「這個真的把雷虎捧過頭了。現在的雷虎和以前全盛時期的雷虎完全不同人馬...不用太迷信 BlueUAS 認證，現在榜上幾間美國公司正在互揭傷疤」
3. **@jgo911131** — echo #2「當年跟現在的人馬幾乎都不一樣了」
4. **@benjikao65** — 「雷虎的產品在我早年玩 RC 時是爛到不行」

→ Dimension: **建議 + 擴寫**。pattern：讀者質疑「雷虎敘事被捧過頭」，傾向把 hook 框成「藍色清單入場券 = 台灣最強」過度簡化。文章本體應 audit 是否：

- 已涵蓋雷虎 vs 亞拓 vs 經緯 vs 中光電等其他玩家 landscape
- 已標示 BlueUAS 認證的爭議 / 美國同業互揭傷疤
- 「過去人馬不在」這條歷史敘事是否 traceable

→ Action: **flag → maintainer-am queue**（不是勘誤，是 framing audit 觸發）

**Policy / 政治 reply**：5,6,7 #shushu6985 / #huian.c / #rok8076655（國發基金、特別預算合理性、青鳥/股價）— 屬一般輿論層，不進文章本體

**Snark / 玩笑**：#3839kuan / #ericchang12 / #shinnhawren — 不必回

**Counter-evidence (factual)**: **@albert_lan0503** — 「看到美軍還在用 Dji 就知道什麼才是真的好貨」

- 此 claim 與 DJI 在美國國防 ban 的公開事實衝突（CISA / FY2024 NDAA）
- Action: ❌ 不採納，文章本體 already 正確

### #73 蘋果西打 X（2 replies — unread, view-count high so reply quality unknown via current snapshot）

→ D+2 next-day routine 再 deep harvest

## 🚩 Data integrity carryover

本 batch 第二次驗證 5/12 batch 的兩個 unhealed findings：

1. **#69 台積電 X**: SPORE-LOG URL `2053100425730269544` 仍 stale 6 views（X UI confirmed deprecated）。canonical 應指向 `2053101189034860856`
2. **#71 無人機 X**: SPORE-LOG URL `2053101189034860856` 仍 mismatched（內容是台積電 emoji 🏭，不是無人機 🚁）

**為什麼沒 heal**：5/12 batch 是 observer-triggered dry-run + 寫進 batch log followup。SPORE-LOG.md 機械修補需要 separate PR（per DNA #54 routine 邊界，schema heal 屬 observer decision，不在 daily harvest 自動範圍）。

**建議**：09:00 maintainer-am routine 拿到本 batch 後決定是否開 heal PR：

- #69 SPORE-LOG row 換 URL → `2053101189034860856`
- #71 SPORE-LOG row drop（無人機根本沒 X 版）or 補真 X 版 URL

→ 寫進 maintainer-am 09:00 上下文。

## Routine cycle 評估

- ✅ Chrome MCP `list_connected_browsers` 返回 1 paired browser (deviceId `afde823f...`)
- ✅ 8 spores 全成功 harvest（no skip / rate-limit / 402）
- ✅ Atomic batch log = 1 commit
- ✅ frontmatter schema canonical: spores plural list / harvest_date / harvest_window_day / batch_reason / triggered_by / reply_count
- ✅ Pipeline §Step 8 dashboard regen 待跑（即將）
- ⏭️ re-hook reply / 留言回覆 → AI 自主邊界，prepare drafts 不發（per DNA #26 v2）

## 下次 harvest 建議時機

- **2026-05-14 07:00**: routine 自動 fire。focus #73 #72 蘋果西打 D+2 trajectory + #70 無人機 D+4 reply 質性
- **D+7 milestone 全 batch**: #66/67 → 2026-05-15; #68/真69 → 2026-05-16; #70 → 2026-05-17; #72/73 → 2026-05-19

---

_routine: twmd-spore-harvest-am (cron 0 7 \* \* \* Asia/Taipei)_
_session: 2026-05-13-070440-spore-harvest-am_
_pipeline: SPORE-HARVEST-PIPELINE.md v2.2 §Routine 整合 (full-auto)_
