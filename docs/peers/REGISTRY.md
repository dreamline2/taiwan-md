# Peer Registry — Taiwan.md curation-layer peers

> Taiwan.md 作為 Meta-Index 的第一層：所有已 ingest 的 curation-layer peer 及其狀態。
>
> 相關：[PEER-INGESTION-PIPELINE.md](../pipelines/PEER-INGESTION-PIPELINE.md) · Obsidian 策略文件 `Taiwan.md — Meta-Index 策略`

---

## 架構

每個 peer 一個條目，含：

- **id / name / issue area**
- **status**: `active` / `paused` / `archived` / `rejected`
- **first ingested / last re-ingested / next re-ingest 建議**
- **raw data 位置 + crawler 路徑**
- **analysis report 連結**
- **articles shipped**: P0 × 5 / P1 × 8 / P2 × 7 進度
- **partnership status**: `not initiated` / `contacted` / `active` / `declined`
- **notes**: 重要的 session 或里程碑

---

## Active Peers

### TFT · Teach For Taiwan · 為台灣而教

- **ID**: `tft`
- **Name**: 為台灣而教 Teach For Taiwan
- **Issue area**: 教育不平等 / 偏鄉教育 / 師資
- **Website**: https://www.teach4taiwan.org/
- **Status**: 🟢 active
- **First ingested**: 2026-04-11（Codex 爬取 + Taiwan.md Semiont 分析）
- **Last re-ingested**: 2026-04-11
- **Next re-ingest 建議**: 2026-09-11（3-6 個月後，視 peer 內容更新頻率）
- **Raw data**: [`data/TFT/`](../../data/TFT/) （450+ articles, 37MB）
- **Crawler**: [`scripts/tools/fetch-tft-data.py`](../../scripts/tools/fetch-tft-data.py)
- **Analysis report**: [`reports/TFT-semiont-analysis-2026-04-11.md`](../../reports/TFT-semiont-analysis-2026-04-11.md) （523 行 / 9 Part / 12 系列 / 20 篇 P0-P2 優先清單）
- **Articles shipped (P0)**: **5/5** ✅
  1. [`Society/台灣原住民族教育與語言復振的交界.md`](../../knowledge/Society/台灣原住民族教育與語言復振的交界.md) — evolution v2 `45b62300`
  2. [`Society/偏遠地區學校教育發展條例全解.md`](../../knowledge/Society/偏遠地區學校教育發展條例全解.md) — evolution v2 `8e0d85f2`
  3. [`Society/一個教師的誕生：台灣師資培育制度.md`](../../knowledge/Society/一個教師的誕生：台灣師資培育制度.md) — evolution v2 `e5be81a5`
  4. [`Society/學習貧窮.md`](../../knowledge/Society/學習貧窮.md) — fresh `e22337b2`
  5. [`People/劉安婷.md`](../../knowledge/People/劉安婷.md) — fresh `4f008ac1`
- **Articles pending (P1)**: 0/8
  - 台灣新住民子女的教育之路
  - 台灣融合教育與身心障礙學生
  - 台灣教育裡的性別議題
  - 你想找的教育數據都在這（工具型策展）
  - 台灣代課老師：佔比 14% 的隱形教育工作者
  - 屏東恆春半島的教育翻轉
  - 方新舟與誠致教育基金會
  - 非認知能力是什麼？考試考不出的那些
- **Articles pending (P2)**: 0/7
  - 台灣教育資料開放史
  - 台灣教育生態系地圖
  - 410 教改的遺產
  - 台灣實驗教育運動
  - 李吉仁人物頁
  - 台灣私立雙語學校熱潮
  - 台灣教師檢定制度
- **Partnership status**: `not initiated` — ingestion 全部使用公開資料。觀察者有跟 TFT（劉安婷）實體接觸的歷史，但尚未以 peer partnership 的角色聯繫。
- **Key contacts**:
  - 劉安婷（TFT 創辦人，2024 卸任董事長轉任董事）
  - 林妍希（2024 接任董事長）
- **Notes**:
  - 第一個完整 ingest 的 curation-layer peer
  - 誕生 `PEER-INGESTION-PIPELINE.md` v1.0（2026-04-12）
  - 誕生 Taiwan.md 第三身份階段宣告「Meta-Index」（2026-04-11）
  - ζ+ session 跨 24+ 小時 / 13+ commits / 跌倒兩次（P0 #1-3 淺薄 v1 被觀察者抓出 → evolution 重寫）
  - Session 記憶：[`memory/2026-04-12.md`](../semiont/memory/2026-04-12.md) / [`diary/2026-04-12.md`](../semiont/diary/2026-04-12.md)
  - Muse sparring review：[[Obsidian / Taiwan.md — Meta-Index 策略 · Muse 反迴聲 × Semiont 反芻 2026-04-11]]

### NML · 數位荒原 · No Man's Land

- **ID**: `nml`
- **Name**: 數位荒原 No Man's Land
- **Issue area**: 當代藝術 + 科技 + 表演 + 東南亞區域共享歷史（南方視角）
- **Website**: https://www.heath.tw/
- **Status**: 🟢 active
- **First ingested**: 2026-05-04（Taiwan.md Semiont sitemap-driven HTML scrape）
- **Last re-ingested**: 2026-05-04
- **Next re-ingest 建議**: 2026-11-04（6 個月，或 NML 公告 Issue 57+ 時提前）
- **Raw data**: [`data/NML/`](../../data/NML/)（555 items / 37 MB / 56 issues + 384 articles + 31 podcasts + 74 announcements + 3 navigations + 7 pages）
- **Crawler**: [`scripts/tools/fetch-nml-data.py`](../../scripts/tools/fetch-nml-data.py)
- **Analysis report**: [`reports/NML-semiont-analysis-2026-05-04.md`](../../reports/NML-semiont-analysis-2026-05-04.md)（670 行 / 9 Part / 13 系列 / 20 P0-P2 文章）
- **Articles shipped (P0)**: **0/5** 🟡（全 pending in [ARTICLE-INBOX](../semiont/ARTICLE-INBOX.md)）
  1. 鄭文琦：台灣最深耕的「南方策展人」（People × Art, fresh）
  2. 數位荒原 12 年：一個網路藝評平台如何活了下來（Art × Technology, fresh）
  3. 群島思維：把台灣放回馬來世界這一塊地圖（Culture × History, fresh）
  4. 王福瑞：從 NOISE 雜誌（1993）到聲音實驗（2024）（People × Music, fresh）
  5. 新生態藝術環境（1990-1995）：九〇年代台南的另類藝術空間（Art × History, fresh）
- **Articles pending (P1)**: 0/8（區秀詒 / 高森信男 evolve / 在地實驗 IT Park / Nusantara 政治含義 / 海盜電波隔離圈 / How to NOISE / 群島資料庫方法論 / 經.神.經 噪音前史）
- **Articles pending (P2)**: 0/7（南洋廣播電台 / Mark Teh / 共享歷史四時刻 / 南島原鄉假說 / 新媒體藝術南方 evolve / 翻譯作為策展 / 原住民藝術網絡反向補位）
- **Partnership status**: `not initiated` — 全用公開資料（明確 cite-original 開放授權）
- **Key contacts**:
  - 鄭文琦 Tenn, Bun-ki（主編，自 2011 持續至今）
  - 黃文浩（DAF 數位藝術基金會 founder + NML 刊頭 / financial supporter）
  - 編輯顧問委員會 7 人：黃文浩、區秀詒、葉紹斌、高森信男、羅仕東、吳庭寬、黃瀞瑩
- **Key features**:
  - **論述型藝評平台**（vs TFT 二手轉述 / vs NMTH 一手史料）：12 年累積中文當代藝術評論
  - **南方視角 framework**：群島 Nusantara × 邊陲 × 解殖 × 海盜電波隔離圈四基底向量
  - **Meta-aggregator**：56% 文章帶 Original Source 轉載（《藝術家》《今藝術》《Voices of Photography》《群島資料庫》⋯⋯）
  - **群島資料庫子計劃**：2017-2019 第一期 + 2021- Twinning Archipelago 第二期 / 10 冊獨立 imprint
  - **單一編輯 driven**：鄭文琦編輯 88% 文章 → 引用時主動補多元 voice 避免 peer-bias
- **Notes**：
  - 第三個 curation-layer peer（前兩個 = TFT 教育 + NMTH 海外史料）
  - 三 peer 在「論述深度 × 立場敘事性 × 當代性」三軸最遠分布（避免同位 peer ingest）
  - NML 是 meta-aggregator → ingest NML 等於解鎖 NML 的所有 secondary sources（《藝術家》《典藏今藝術》《Voices of Photography》⋯⋯ 是下一批 peer 候選）
  - 2023 article 萎縮到 5 篇（vs 2016 高峰 49）→ NML 進入 publication 沈澱期，Taiwan.md 入場時間恰好
  - **Crawler 雙 commit**：`90cfe924` (Stage 2-3 ingest data) + `ab037d3df` (Stage 4 corpus analysis)
  - 已知 corpus 缺口：王福瑞 standalone「How to NOISE」「Before NOISE」未抓進 corpus（issue 不收錄），Stage 6 寫 P0 #4 時補抓

### NMTH-overseas · 國立臺灣歷史博物館 · 海外史料看臺灣

- **ID**: `nmth-overseas`
- **Name**: 國立臺灣歷史博物館「海外史料看臺灣」
- **Issue area**: 歷史（17-19 世紀西方觀察者視角 / 一手史料翻譯）
- **Website**: https://taiwanoverseas.nmth.gov.tw/archives
- **Status**: 🟢 active
- **First ingested**: 2026-04-12（Semiont crawler via hybrid SSR+API）
- **Last re-ingested**: 2026-04-12
- **Next re-ingest recommendation**: 2026-10-12（6 months，臺史博新增計畫時提前）
- **Raw data**: [`data/NMTH-overseas/`](../../data/NMTH-overseas/) （12 plans × 51 collections, 20.2 MB）
- **Crawler**: [`scripts/tools/fetch-nmth-overseas-data.py`](../../scripts/tools/fetch-nmth-overseas-data.py)
- **Analysis report**: [`reports/NMTH-overseas-semiont-analysis-2026-04-12.md`](../../reports/NMTH-overseas-semiont-analysis-2026-04-12.md) （9 Parts / 12 series / 17 P0-P2 articles）
- **Articles shipped (P0)**: **0/5** 🟡
  1. 史溫侯：當外交官變成博物學家（People × History, fresh）
  2. 法軍遠征福爾摩沙：清法戰爭（History, fresh）
  3. 李仙得臺灣紀行（People × History, fresh）
  4. 乙未之役：臺灣民主國的 148 天（History, fresh）
  5. 福爾摩沙：西方人如何「發現」台灣（History, fresh）
- **Articles pending (P1)**: 0/5
- **Articles pending (P2)**: 0/7
- **Partnership status**: `not initiated` — 公開資料爬取，未聯繫臺史博
- **Key features**:
  - **一手史料翻譯**（非二手論述）：86% 已有專業中譯
  - **物件性**：手稿、地圖、照片、帳簿（策展式敘事的物件抓手）
  - **時代集中**：80% 在 1800s（恰好填 Taiwan.md History 軸最大空白）
  - **觀察者類型**：博物學家 / 外交官 / 軍人 / 傳教士 / 旅行家
- **Notes**:
  - 第二個 curation-layer peer（第一個 = TFT）
  - 與 TFT 完全互補：TFT = 當代教育，NMTH = 前現代歷史
  - API 限制：/api/collection/search 回 500，需 seed plan UUIDs 從 SSR 抓
  - 已有 `data/ilhaformosa/` = 臺史博另一子站（臺灣史新手村），不同資料集

---

## Paused Peers

（空）

---

## T4 cite-only Peers（ND 條款限制 — fair-use cite only，無 ingest）

> 這個 section 收 **CC BY-NC-ND** 或 **All Rights Reserved** 類型的 peer。Pipeline mode 從 ingest-and-rewrite 改為 fair-use cite-only。不寫 crawler、不存 raw data；僅作為 footnote 來源 + meta 條目主題。
>
> 設計理由：本 section 誕生於 2026-05-05 想想論壇 ingestion case — 揭露 PEER-INGESTION-PIPELINE Stage 1a §授權項目應為 gating filter 而非平等檢查項。完整論述見 [reports/ThinkingTaiwan-semiont-analysis-2026-05-05.md §Part 8 Meta 洞察](../../reports/ThinkingTaiwan-semiont-analysis-2026-05-05.md)。

### ThinkingTaiwan · 想想論壇

- **ID**: `thinking-taiwan`
- **Name**: 想想論壇 Thinking Taiwan
- **Issue area**: 民主治理 / 兩岸觀察 / 地緣政經 / 思想政策 / 社會人文（horizontal commentary peer，非 issue-deep）
- **Website**: https://www.thinkingtaiwan.net/
- **Status**: 🟢 **active (T4 cite-only)** — 觀察者 2026-05-05 選定 mode B/C，第一篇 P0-01 想想論壇 meta 條目已 ship
- **License**: **CC BY-NC-ND 3.0 台灣** — 著作權人「小英教育基金會想想論壇」 — NC + ND 兩條都跟 PEER-INGESTION-PIPELINE 預設 ingest mode 衝突
- **First analyzed**: 2026-05-05（Stage 1 fit check + Stage 4 corpus analysis 縮版，**未** Stage 2 crawler）
- **Raw data**: ❌ **無**（per ND 條款，不爬整站、不存 corpus 進 repo）
- **Crawler**: ❌ **無**（不寫）
- **Analysis report**: [`reports/ThinkingTaiwan-semiont-analysis-2026-05-05.md`](../../reports/ThinkingTaiwan-semiont-analysis-2026-05-05.md)（817 行 / 9 Part / 13 系列 / 20 P0-P2 候選 / §Part 1.5 授權 deep dive / §Part 8 Pipeline 升級提案）
- **Articles shipped (P0)**: **1/5** 🟢
  1. **想想論壇 NEW · Society/媒體** ✅ — [knowledge/Society/想想論壇.md](../../knowledge/Society/想想論壇.md)（2026-05-05 ship by main-session manual / fair-use cite-only mode / ~5,500 字 / 30 footnotes / HARD=0 / score=3 PASS）
  2. 小英教育基金會 NEW · Society/智庫（pending）
  3. 30 年、30 人、30 個觀點 NEW · Society/民主（pending — 等系列 30 篇全部刊出後 ship 較合理）
  4. 318 學運十週年回望 EVOLVE · History（pending）
  5. 台灣 commentary 媒體生態系 NEW · Society/媒體（pending）
- **Articles pending (P1)**: 0/8（思想坦克 / 太陽花論述史 / 公共領域理論 / AI 與民主 / 兩岸 framing 戰 / 中國經濟結構觀察 / 報導者 / 民主深化辯論 2026）
- **Articles pending (P2)**: 0/7（端傳媒 / 上報 / 鏡週刊 / 智庫對照 / 後總統卸任智庫國際比較 / 未富先老 framework / 評論型作家圖譜）
- **Partnership status**: `not initiated` — pipeline Stage 8 規定 ship ≥ 2 篇 P0 後才聯繫；本案因 ND 條款另增「主動詢問個案授權例外」可能性
- **Key contacts**:
  - 蔡英文（小英教育基金會創辦人；2025-10-03 改版發刊詞）
  - 編輯委員會（跨領域專家學者組成，未公開名單）
- **Key features**:
  - **Horizontal commentary peer**（vs TFT/NMTH/NML 都是 vertical issue-deep peer）
  - **6 大欄目**：思想政策（含安全/能源/財經/產業/社福）/ 地緣政經 / 社會人文 / 國際智庫 / 多元想想 / 想想選集 + English Edition
  - **CMS**: Drupal 10（不是 WordPress；無 wp-json API）
  - **規模**: 改版前 ~5,200-5,800 篇 / 1,900+ 文章 / 600+ 作者 / sitemap 4 頁 ~6,664 URLs
  - **作者組成**: 大學教授 30% + 智庫 25% + 國際媒體 15% + NGO 15% + 政治人物 10% + 其他 5%
  - **2025-10 改版重啟**: 蔡英文宣布重啟 + 新編輯委員會制 + 旗艦系列「30 年、30 人、30 個觀點」
  - **4 個 framework**: 民主治理（哈伯瑪斯）/ 兩岸監督 / 地緣政經 / 思想政策跨領域對話
- **Notes**:
  - **第一個 T4（CC BY-NC-ND）peer**，揭露 PEER-INGESTION-PIPELINE Stage 1a 授權項目應為 gating filter 而非平等檢查項
  - 觸發 4-tier license matrix 提案（v0.1，待觀察者 review）—— [reports/ThinkingTaiwan-semiont-analysis-2026-05-05.md §Part 8.2](../../reports/ThinkingTaiwan-semiont-analysis-2026-05-05.md)
  - 觸發 LESSONS-INBOX 候選（DNA 候選 #52「Peer 授權 ND 條款是 gating filter」，verification_count = 1，需 ≥ 3 升 canonical）
  - **三個選項 pending observer decision**：(A) 放棄 / (B) 純 fair-use cite-only / (C) hybrid（cite-only + 主動聯繫想想論壇詢問個案授權）
  - Session 記憶: [`memory/2026-05-05-181314-manual.md`](../semiont/memory/2026-05-05-181314-manual.md)（待寫）

---

## Archived Peers

（空 — peer 從 active 移到 archived 的條件見 PEER-INGESTION-PIPELINE.md §Peer Deprecation Criteria）

---

## Rejected Peers

（空 — 失敗的 fit check 會在這裡列，含拒絕原因）

---

## Pending Peers（候選名單，尚未 ingest）

詳見 Obsidian 策略文件 `Taiwan.md — Meta-Index 策略：台灣議題策展生態系的元索引` 的 **Candidate Peers** 段落。~35 個高潛力候選，分 10 個議題領域：

- **教育 / 青年**（TFT ✅ / 均一 🟡 / 誠致 🟡 / DFC ⚪ / 台少盟 ⚪）
- **人權 / 法治**（台權會 🟡 / 人約盟 🟡 / 民間司改會 🟡 / 廢死聯盟 ⚪ / 特赦組織 ⚪）
- **環境 / 生態**（綠盟 🟡 / 地球公民 🟡 / 荒野保護協會 🟡 / 環權會 ⚪ / 環資協會 ⚪）
- **民主 / 公民參與**（公督盟 🟡 / g0v 🟡 / 公庫 🟡 / 沃草 ⚪ / 民主實驗室 ⚪）
- **性別 / 多元**（婦女新知 🟡 / 同志諮詢熱線 🟡 / 勵馨 🟡 / 性平教協 ⚪）
- **勞工**（台灣勞陣 🟡 / 全教總 🟡 / 桃產總 ⚪ / 高教工會 ⚪）
- **移民 / 新住民 / 原住民**（TIWA 🟡 / 南洋姊妹會 🟡 / 原住民政策協會 🟡）
- **文化 / 在地**（文策院 🟡 / 台灣文化協會 🟡 / 各地文史工作室 ⚪）
- **科技 / 資訊**（OCF 🟡 / Hackathon Taiwan 🟡）
- **健康 / 長照 / 身障**（殘盟 🟡 / 弘道 🟡 / 失智症協會 ⚪）

**R5 硬性規則**（來自 Meta-Index 策略 + Muse sparring）：**每 ingest 一個 peer，必須至少寫出該 peer analysis 裡的 2 篇 P0 文章才能 ingest 下一個**。

---

## 下一個 peer 建議

根據 TFT 第一次 ingest 的經驗：

1. **優先選同議題的第二個 peer**（例：TFT 之後選均一或誠致做教育 cluster 內的交叉校正）
   - 理由：可以驗證 R1 peer-bias inheritance 緩解是否有效
2. **或選不同議題的 peer 測試 pipeline 通用性**（例：選台權會或綠盟）
   - 理由：驗證 PEER-INGESTION-PIPELINE 的步驟是否只適用於 TFT 還是可以通用

**觀察者決定**。

---

## 版本歷史

- **2026-04-12** — Registry 誕生 · 首批條目：TFT
- **預計 2026-06** — Phase 1 結束時回來檢討 Registry 結構

---

🧬 _這份 Registry 是 Taiwan.md Meta-Index 架構的 Layer 1。Layer 2 = `data/{org}/`，Layer 3 = `reports/{org}-semiont-analysis-*.md`，Layer 4 = `knowledge/**/*.md`。_
