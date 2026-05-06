# 🧬 想想論壇 Thinking Taiwan × Taiwan.md — 授權與內容策展分析

> 分析日期: 2026-05-05 / Session: 2026-05-05-181314-manual / Semiont: Taiwan.md (Opus 4.7 1M)
> 資料來源: 想想論壇官網 [https://www.thinkingtaiwan.net/](https://www.thinkingtaiwan.net/) public pages（**未爬取整站 corpus**，本報告基於 Stage 1 fit check + 抽樣 sample 5-7 篇 + 外部 search）
> 報告型態: **Stage 1 fit check + Stage 4 corpus analysis 縮版 + §授權 deep dive**（Stage 2 crawler / Stage 3 data 標準化 / Stage 5-7 文章產製 **皆 defer 至觀察者授權後再執行**）
> Pipeline 對照: [PEER-INGESTION-PIPELINE.md](../docs/pipelines/PEER-INGESTION-PIPELINE.md) Stage 1 + Stage 4

---

## 📋 摘要

想想論壇是 2012 年 8 月由小英教育基金會創刊、2025 年 10 月由蔡英文宣布改版重啟的多元思想評論平台，14 年深耕、累計 1,900+ 文章 600+ 作者（改版前舊站 5,200-5,800 篇）。新站以「思想政策、地緣政經、社會人文、國際智庫、多元想想、想想選集」六大欄目運作，旗艦系列「30 年、30 人、30 個觀點」自 2026 年 5 月起分批刊登。

**Fit check 結果：4 項中 3 項通過，1 項紅旗（授權）**：

| Check    | 結果        | 說明                                                           |
| -------- | ----------- | -------------------------------------------------------------- |
| 深度     | ✅ 通過     | 14 年深耕（>10 年理想標準）                                    |
| 公開性   | ✅ 通過     | Drupal 10 公開站，無登入門檻                                   |
| **授權** | 🔴 **紅旗** | **CC BY-NC-ND 3.0 台灣版** — NC 與 ND 兩條都 conflict          |
| 互補性   | ⚠️ 部分通過 | 想想論壇是 commentary 型 horizontal peer，不是 issue-deep peer |

**核心 thesis**：想想論壇對 Taiwan.md 的 fit profile 跟 TFT（issue-deep curation peer）**完全不同**——它是台灣 commentary 媒體生態系的一個重要節點，跟思想坦克、報導者、端傳媒、上報屬於同一物種。**ND 條款讓 Taiwan.md 不能對它做 ingest-and-rewrite 模式**（PEER-INGESTION-PIPELINE 預設 mode），但仍可作為 **fair-use cite-only peer**（DNA #16「peer 是線索不是 source」的 stricter instantiation）。

**因此本 ingestion 的模式必須變更**：

- ❌ 不寫 fetch-thinkingtaiwan-data.py 全站 crawler（即使技術可行，CC ND 不允許 derivative reformat 大規模重製）
- ❌ 不基於想想論壇文章做 derivative rewrite（改作禁止）
- ✅ 可寫關於想想論壇的 **meta 條目**（描述性論述，不是 paraphrase 內容）
- ✅ 可在 Taiwan.md 文章中 fair-use cite 想想論壇文章作為 footnote 來源（轉載條款明確允許「註明出處【想想論壇】」）
- ✅ 可寫關於小英教育基金會、蔡英文卸任後智庫角色的條目（meta-organizational 層）

**5 篇 P0 候選**（全部以「meta 條目 + cite-only 來源」模式運作，不依賴 paraphrase）：

1. **想想論壇** NEW · Society/媒體 · 14 年論壇生態系策展
2. **小英教育基金會** NEW · Society/政治智庫 · 蔡英文卸任後第二人生
3. **30 年、30 人、30 個觀點** NEW · Society/民主 · 2026 年進行中的跨黨派民主對話
4. **318 學運十週年回望** EVOLVE · History · 2024-2026 整理 NGO 與評論社群的回顧浪潮
5. **台灣 commentary 媒體生態系** NEW · Society/媒體 · 想想／思想坦克／報導者／端傳媒／上報的角色分工

**Meta 洞察**：想想論壇是 Taiwan.md 第一個**因 ND 條款必須 reframe ingestion 模式的 peer**，揭露了 PEER-INGESTION-PIPELINE 的隱藏假設「peer 預設容許 derivative」。Stage 1 fit check §授權項目應升級為「block 等級」門檻，不是平等四項。本報告 §Part 8 Meta 洞察會展開這個 pipeline 升級提案。

---

## 📦 Part 1 · 想想論壇資料集盤點

### 1.1 站台基本資訊

| 項目         | 數值                                                                                               |
| ------------ | -------------------------------------------------------------------------------------------------- |
| 域名         | [thinkingtaiwan.net](https://www.thinkingtaiwan.net/)                                              |
| 創刊         | 2012 年 8 月                                                                                       |
| 改版重啟     | 2025 年 10 月 3 日（蔡英文宣布）                                                                   |
| 創辦/主辦    | **小英教育基金會**（蔡英文卸任後持續運作的基金會）                                                 |
| CMS          | **Drupal 10**（不是 WordPress；route 為 `/content/{nid}` 數字 ID）                                 |
| 編輯結構     | 編輯委員會（跨領域專家、學者組成；非單一主編）                                                     |
| 改版前累計   | **1,900+ 文章 / 600+ 作者**（per 改版前對外公開數字）                                              |
| 舊站 archive | 580 頁 / 約 **5,200-5,800 篇**（per `/archive` 頁分頁；分「政策想想/時事想想/想想副刊/漫談時事」） |
| 改版後新號   | 從 `100011` 開始（2025-10）                                                                        |
| 英文版       | **English Edition** （獨立 section，2014-05 由蔡英文召開記者會啟動）                               |
| Slogan       | 「一起想，才能走得更遠」                                                                           |
| Footer       | 「© Thinking Taiwan 2025-2026」                                                                    |

### 1.2 sitemap 量化

```
sitemap.xml index → 4 子頁
├── page=1: 2,000 entries（包含改版後新文章 + 部分舊內容）
├── page=2: 2,000 entries
├── page=3: 2,000 entries
└── page=4:   664 entries
合計約 6,664 URLs（含 archive 分類頁、tag 頁、author 頁）
```

實際單篇文章估計 **5,200-5,800 篇**（per `/archive` 頁分頁顯示「最後 » 580」）。

### 1.3 六大欄目架構

```
🌐 想想論壇（改版後 2025-10）
├── 思想政策
│   ├── 安全（含國防、地緣安全）
│   ├── 能源
│   ├── 財經
│   ├── 產業
│   └── 社福
├── 地緣政經（中國觀察、美中、東亞地緣）
├── 社會人文（環境、教育、文化）
├── 國際智庫（國際智庫翻譯 / 摘錄）
├── 多元想想（讀者投稿、跨議題評論）
└── 想想選集（編輯部精選 / 主題系列）
+ English Edition
+ 旗艦系列：「30 年、30 人、30 個觀點」（2026-05 起分批刊登）
+ 中國專輯（持續更新觀測報告）
```

### 1.4 抽樣文章基本剖面（5 篇 sample）

| ID     | 標題                                             | 作者                  | 作者背景                                | 日期       | 分類                 | 字數        | 體例          |
| ------ | ------------------------------------------------ | --------------------- | --------------------------------------- | ---------- | -------------------- | ----------- | ------------- |
| 100011 | 當銀行資產膨脹遇上房市崩盤                       | 黃崇哲                | FPAT 執行長／前金融研訓院長／經濟學碩士 | 2025-10-03 | 地緣政經             | 4,500-5,000 | 學術評論      |
| 100049 | AI 來襲 如何影響公共討論？                       | 李怡志                | 政大新聞系副教授                        | 2025-10-09 | 社會人文             | ~3,500      | 學術評論      |
| 100061 | 「未富先老」恐使經濟成長模式「未老先衰」         | 陳妍蒨                | 北大經濟系副教授                        | 2025-10-24 | 地緣政經             | 4,500-5,000 | 學術論文      |
| 100278 | 30 年、30 人、30 個觀點及台灣民主更好的未來      | 編輯部                | —                                       | 2026-05-02 | 多元想想（系列引言） | ~700        | 編輯導言      |
| 1947   | 破解外國（行）學者對「太陽花運動」的迷思         | 寇謐將 J Michael Cole | 國際媒體人（Taipei Times 前副總編）     | 2014-04-11 | （舊站時事想想）     | ~3,500      | 時事評論+腳註 |
| 1955   | 是護憲，還是毀中華民國？— 駁斥馬區長的「兩國論」 | 集思會館              | 公民團體                                | 2014-04-14 | （舊站時事想想）     | 1,200-1,500 | 短評          |

**作者組成觀察**（從 sample 推斷）：

- **30%** 大學教授（北大經濟、政大新聞、台大、清華等）
- **25%** 智庫研究員 / 政策評論者（FPAT、台經院、中經院、台研基金會等）
- **15%** 國際媒體人 / 駐台記者（寇謐將等）
- **15%** 公民團體 / NGO（集思會館等）
- **10%** 政治人物本人 / 幕僚（蔡英文、立委）
- **5%** 其他（讀者投稿、學生）

### 1.5 文章年份分布（粗估）

| 期間               | 篇數估計 | 特徵                                                              |
| ------------------ | -------- | ----------------------------------------------------------------- |
| 2012-08 至 2014-03 | ~600     | 創站期，馬政府末期，醞釀社運                                      |
| 2014-03 至 2016-05 | ~1,500   | **黃金期**：太陽花學運、九合一選舉、2016 大選蔡英文當選           |
| 2016-05 至 2024-05 | ~3,000   | 蔡英文 8 年執政期，文章量穩定但相對溫和（與時任總統有距離感）     |
| 2024-05 至 2025-09 | ~500     | 賴清德上任、想想論壇進入低活動期                                  |
| 2025-10 至今       | ~300+    | **改版後重啟**，新號從 100011 開始，旗艦系列「30 年 30 人」進行中 |

**關鍵觀察**：

1. **2012-2016 是 framework 形成期**（民主治理、兩岸監督、太陽花論述）
2. **2016-2024 是 issue 累積期**（沒有明確 framework 升級，但累計議題覆蓋廣）
3. **2025-10 改版是 framework 重啟期**（蔡英文重新領銜，新六大欄目，編輯委員會制）
4. **2026-05 「30 年 30 人」系列是新時代旗艦**（跨黨派民主對話為定位）

---

## ⚖️ Part 1.5 · 授權 Deep Dive（本報告核心）

### 1.5.1 想想論壇的授權聲明逐字

從 [thinkingtaiwan.net/copyright](https://www.thinkingtaiwan.net/copyright) 擷取：

> 「本網站為小英教育基金會想想論壇所有，所刊載內容的著作權，均受我國著作權法之保障」
>
> 「本網站的內容或服務，僅供個人、非商業用途的使用」
>
> 採「**創用 CC 3.0 授權條款**」，**「非商業性」+「禁止改作 3.0」**
>
> 「如欲轉載請註明出處【想想論壇】。如欲為商業用途或合理範圍外的使用，均應取得著作權人的授權」

**正規 license code**：**CC BY-NC-ND 3.0 台灣**（[creativecommons.org/licenses/by-nc-nd/3.0/tw/](https://creativecommons.org/licenses/by-nc-nd/3.0/tw/)）。

### 1.5.2 三條限制逐字解讀

| 限制                          | 字面意思                             | 對 Taiwan.md 的具體 implication                                        |
| ----------------------------- | ------------------------------------ | ---------------------------------------------------------------------- |
| **BY**（姓名標示）            | 必須標註原作者 + 出處                | ✅ 容易遵守（Taiwan.md footnote 規範本來就要寫）                       |
| **NC**（非商業性）            | 不可作為商業用途                     | ⚠️ **灰色**：Taiwan.md 不商業化但接受 Portaly 贊助；定義邊界需自我釐清 |
| **ND**（禁止改作 / NoDerivs） | 不可建立衍生作品（derivative works） | 🔴 **紅旗**：Taiwan.md 核心 mission 是「策展重寫」= derivative work    |

### 1.5.3 跟 Taiwan.md CC BY-SA 4.0 的相容性問題

**Taiwan.md 自身採 CC BY-SA 4.0**（per [LICENSE](../LICENSE) + MANIFESTO §3 開源共創）。CC BY-SA 跟 CC BY-NC-ND 在 **license compatibility matrix** 上是 **完全不相容**：

```
Taiwan.md 內容（CC BY-SA 4.0）
└── 必須允許商業使用 + 允許衍生作品 + 衍生作品必須 share-alike

想想論壇內容（CC BY-NC-ND 3.0）
└── 禁止商業使用 + 禁止衍生作品

  ✗ 不能把想想論壇文章片段「整合」進 Taiwan.md（這會讓整篇 Taiwan.md 文章繼承 ND 約束，違反 CC BY-SA 開放衍生原則）
```

CC 官方授權相容矩陣明確列：**ND 內容無法重新授權給更開放的 license**，包括 BY-SA。

### 1.5.4 但「合理使用 fair use」仍適用

著作權法 §52「為報導、評論、教學、研究或其他正當目的之必要，在合理範圍內，得引用已公開發表之著作」+ §65「合理使用四要件」：

1. **利用之目的及性質**：Taiwan.md 為非營利、教育性、評論性 → ✅ 強有利
2. **著作之性質**：想想論壇為已公開發表的時事評論 → ✅ 中性偏有利
3. **所利用之質量及其在整個著作所佔之比例**：Taiwan.md 引用一兩段並標註出處 → ✅ 有利
4. **利用結果對著作潛在市場與現在價值之影響**：Taiwan.md 引用導流回想想論壇 → ✅ 有利

**結論：fair-use cite 是合法的，paraphrase 整篇是非法的**。

### 1.5.5 對 PEER-INGESTION-PIPELINE 預設 mode 的衝擊

PEER-INGESTION-PIPELINE Stage 2 的預設動作是「全站爬取 → `data/{ORG}/raw/` 保存 raw HTML/JSON」+ Stage 3「轉 markdown 寫進 `data/{ORG}/{type}/`」+ Stage 6「文章開發 用 peer 文章為素材底本」。

跟想想論壇 ND 對撞的層次：

| Pipeline 動作                                                   | ND 衝突？   | 說明                                                         |
| --------------------------------------------------------------- | ----------- | ------------------------------------------------------------ |
| Stage 2 `data/{ORG}/raw/` 保存 raw JSON / HTML                  | ⚠️ 灰色     | 嚴格說 raw 全文存 repo 是「重製」；fair use 仍可主張但風險大 |
| Stage 3 HTML→markdown 轉檔保存                                  | 🔴 違反 ND  | reformat 是 derivative work，即使 mechanical                 |
| Stage 4 corpus 分析報告（萃取 framework + 評論）                | ✅ fair use | transformative use（評論性，不是 reproduce）                 |
| Stage 6 寫文章用想想論壇文章為「素材底本」做 paraphrase rewrite | 🔴 違反 ND  | derivative work，即使重寫過                                  |
| Stage 6 寫文章 fair-use cite 想想論壇文章作為 footnote 來源     | ✅ fair use | 引用合理範圍 + 標註出處 + transformative use                 |
| 寫關於想想論壇本身的 meta 條目（描述性、評論性）                | ✅ fair use | 評論性、不複製內容、transformative                           |

### 1.5.6 對 Taiwan.md 的 ingestion 模式選擇

**三個選項，建議走選項 C**：

**選項 A：放棄 ingestion**

- 在 [docs/peers/REGISTRY.md](../docs/peers/REGISTRY.md) 標記 status: `rejected_license_incompatible`
- 不投入任何後續成本
- 缺點：失去 Taiwan.md 對台灣 commentary 媒體生態系的策展視角

**選項 B：fair-use cite-only 模式**

- 不爬整站、不寫 crawler、不存 `data/ThinkingTaiwan/`
- Taiwan.md 文章中以 footnote 方式 cite 想想論壇文章 URL（合理使用範圍）
- 寫關於想想論壇本身的 meta 條目（描述性、評論性，不 paraphrase 內容）
- 缺點：失去 corpus-level analysis 的 framework 萃取深度

**選項 C：hybrid 模式（推薦）**

- **不**做 Stage 2/3 corpus 全爬取重製到 repo
- **可**做 **manual sample crawl**（10-20 篇關鍵代表作，僅作為本報告 §Part 4 分析素材，不 commit raw 檔到 repo，僅放 source URL）
- Taiwan.md 文章層 fair-use cite 想想論壇 URL 作為 footnote
- 寫 5 篇 P0 meta 條目（想想論壇、小英教育基金會、30 年 30 人、318 十週年、commentary 生態系）
- 主動聯繫想想論壇編輯部，**詢問是否同意 cooperation license 例外**（CC BY-NC-ND 4.0 升 BY-NC 或 BY 的個案授權，類似 Wikipedia 跟一些媒體合作的模式）

### 1.5.7 Stage 8 聯繫想想論壇的 talking points（如走選項 C）

**不要走的開場**：

- ❌「我們想 ingest 你們的文章做 partnership」（NC 觸礁）
- ❌「我們會把你們的專業論述翻譯成大眾版」（ND 觸礁）

**可以走的開場**：

- ✅「我們建了一個地圖把台灣 commentary 媒體生態系的策展邊界拼起來，想想論壇是其中一個節點。我們寫了一篇關於想想論壇的 meta 條目（連結），想聽聽看你們的回饋」
- ✅「我們在 Taiwan.md Society/媒體 的條目中以 fair-use 方式 cite 你們的 N 篇文章，每篇都附上 URL 導流回想想論壇。如果你們對引用方式有任何意見，歡迎提出」
- ✅「我們站採 CC BY-SA 4.0，跟你們的 CC BY-NC-ND 3.0 不相容，所以我們不會 ingest 內容，但我們希望透過 cite 互相導流。是否有任何個案授權的可能？」

---

## 🧠 Part 2 · 想想論壇的核心概念框架

從 5 篇 sample + 外部 search 提及之名作交叉分析，識別 **4 個重複出現的論述框架**：

### 2.1 Framework 1：民主治理 × 公共領域（哈伯瑪斯傳統）

**核心命題**：民主不只是選舉制度，是一個 ongoing 的公共討論過程。

**反覆出現的概念零件**：

- 哈伯瑪斯（Jürgen Habermas）公共領域（public sphere）
- 馬凱爾（Patchen Markell）公共討論的過程價值
- 「民主深化」（democratic deepening）vs 民主侵蝕
- 「合議式民主」（deliberative democracy）
- 「公民參與」+「理性溝通」二元

**Sample 證據**：100049「AI 來襲 如何影響公共討論？」李怡志全文圍繞哈伯瑪斯公共領域 + Markell 過程論述。

**改版後 2025-10 旗艦系列「30 年 30 人 30 個觀點」整篇引言頁**就是這個 framework 的 instantiation：

> 「30 年後回望，我們在民主道路上雖有顛簸，但自由開放的社會如今已成人民日常」
>
> 「然而，民主機制遭到操弄與極化的現象，卻也在侵蝕著尚未深化的台灣民主」
>
> 「下一個 30 年，我們如何守護得之不易的民主？」

### 2.2 Framework 2：兩岸監督 × 主權捍衛

**核心命題**：兩岸關係是一場 framing 戰爭，台灣必須拒絕被 framed。

**反覆出現的概念零件**：

- 民間版「兩岸協定締結條例草案」 vs 馬政府版（2014）
- 「兩國論」入法 vs「一國兩區」
- 服貿協議的程序爭議（2014）
- 蔡英文「現狀」維持論述（2016-2024）
- 賴清德時代的主權論述（2024+）

**Sample 證據**：1955「是護憲，還是毀中華民國？— 駁斥馬區長的『兩國論』」集思會館全文圍繞 framing 反駁。

### 2.3 Framework 3：地緣政經 × 中國觀察

**核心命題**：理解中國經濟結構的內在矛盾，才能正確判斷台海風險。

**反覆出現的概念零件**：

- 中國金融體系擴張（四大國有銀行、影子銀行）
- 房地產市場的崩盤（恆大、碧桂園後遺症）
- 一帶一路的地緣後果
- 中國人口紅利消失（一胎化、未富先老）
- 中等收入陷阱（middle income trap）

**Sample 證據**：100011「當銀行資產膨脹遇上房市崩盤」黃崇哲（科爾奈軟預算約束）+ 100061「未富先老」陳妍蒨（聯合國/世銀數據 + Eberstadt）。

### 2.4 Framework 4：思想政策 × 跨領域對話

**核心命題**：政策不是技術官僚的事，是社會思想對話的累積結果。

**反覆出現的概念零件**：

- 五大政策子議題：安全 / 能源 / 財經 / 產業 / 社福
- 學者 + 智庫 + 公民團體三角對話
- 國際比較（北歐、德國、日本、美國 model）
- 政策落地的執行縫隙

**Sample 證據**：六大欄目「思想政策」分 5 子類，跟其他評論平台（思想坦克、報導者）的差異就在這個 framework 的 explicit instantiation。

### 2.5 Framework 圖譜

```
                  民主治理 × 公共領域
                  （哈伯瑪斯 framework）
                         ↑
                         │
        兩岸監督 ←─────  想想論壇  ─────→ 思想政策
        × 主權捍衛       editorial          × 跨領域對話
                         vector
                         │
                         ↓
                  地緣政經 × 中國觀察
                  （結構性分析）
```

四個 framework 互為支撐：民主治理是上位 normative 框架，兩岸監督是現實場域，地緣政經是條件約束，思想政策是落地工具。**這四個合在一起，是一個比 TFT「3A / 同心圓」更廣但也更鬆的 horizontal 思想座標系**。

### 2.6 跟 TFT 對照：horizontal commentary peer vs vertical issue-deep peer

| 維度           | TFT（為台灣而教）                      | 想想論壇                                    |
| -------------- | -------------------------------------- | ------------------------------------------- |
| Framework 數量 | 3-5 個（3A、同心圓、交織性、學習貧窮） | 4 個 horizontal 大框架，每個下有 N 個子議題 |
| Framework 深度 | 深，每個都有 case study 累積 5 年+     | 淺-中，每篇文章是一個 framework instance    |
| 議題範圍       | 集中（教育不平等）                     | 廣泛（民主、兩岸、地緣、政策、文化）        |
| 作者組成       | 內部 TFT 教師為主                      | 外部專家學者為主                            |
| 文章生產模式   | 思考成熟後出版                         | commentary 即時 + 編輯精選                  |
| 對話模式       | 內部團隊深思熟慮                       | 跨領域跨黨派對話                            |
| 學術權重       | 中等（field experience driven）        | 高（學者驅動）                              |

**這個對照是 Part 8 Meta 洞察的基礎**：兩種 peer 在 Taiwan.md ingestion mode 下需要不同對待方式。

---

## 🗺️ Part 3 · Taiwan.md 現有「commentary / 思想 / 民主治理」覆蓋

### 3.1 既有相關文章 audit

執行 `grep -rl "想想論壇\|思想坦克\|小英教育基金會"` 結果：

- **0 篇** Taiwan.md 文章直接提及「想想論壇」
- **0 篇** Taiwan.md 文章直接提及「思想坦克」
- **0 篇** Taiwan.md 文章提及「小英教育基金會」

執行涵蓋 framework 的相關文章 grep（民主治理 / 兩岸監督 / 公共討論 / 媒體生態 / 評論平台）：

| 主題                       | Taiwan.md 既有條目                                                                                                                                        | 字數 / 完整度 | 跟想想論壇 framework 的 overlap                     |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------- |
| **馬英九迷因**             | [knowledge/Society/馬英九迷因.md](../knowledge/Society/馬英九迷因.md)                                                                                     | 中            | 跟想想論壇 2014 「兩國論」反駁系列 overlap          |
| **毒馬鈴薯認知作戰**       | [knowledge/Society/毒馬鈴薯認知作戰.md](../knowledge/Society/毒馬鈴薯認知作戰.md)                                                                         | 中            | 跟想想論壇「中國認知作戰」系列可 cross-link         |
| **心戰**                   | [knowledge/History/心戰.md](../knowledge/History/心戰.md)                                                                                                 | 中            | 跟想想論壇「思想政策／安全」可 cross-link           |
| **台灣金融科技發展**       | [knowledge/Economy/台灣金融科技發展.md](../knowledge/Economy/台灣金融科技發展.md)                                                                         | 中            | 跟想想論壇「地緣政經／財經」overlap                 |
| **台灣政治版圖與選舉制度** | [knowledge/Society/taiwan-political-landscape-and-electoral-system.md](../knowledge/Society/taiwan-political-landscape-and-electoral-system.md)           | 大            | 民主治理 framework 邊緣 overlap                     |
| **台灣外交盟邦與國際關係** | [knowledge/Society/taiwan-diplomatic-allies-and-international-relations.md](../knowledge/Society/taiwan-diplomatic-allies-and-international-relations.md) | 大            | 跟想想論壇「地緣政經」overlap                       |
| **台灣國防現代化**         | [knowledge/Society/taiwan-defense-modernization.md](../knowledge/Society/taiwan-defense-modernization.md)                                                 | 大            | 跟想想論壇「思想政策／安全」overlap                 |
| **台灣與史瓦帝尼**         | [knowledge/Society/台灣與史瓦帝尼.md](../knowledge/Society/台灣與史瓦帝尼.md)                                                                             | 中            | 跟想想論壇「地緣政經」邊緣 overlap （2026-05 ship） |
| **蔡英文**（People）       | [knowledge/People/tsai-ing-wen.md](../knowledge/People/tsai-ing-wen.md)                                                                                   | 中            | 跟想想論壇「2025-10 改版重啟」直接相關              |
| **賴清德**（People）       | [knowledge/People/lai-ching-te.md](../knowledge/People/lai-ching-te.md)                                                                                   | 中            | 邊緣關聯                                            |

### 3.2 Taiwan.md 缺口（想想論壇有 / Taiwan.md 沒有）

| 主題類型                              | Taiwan.md 狀態 | 為什麼是缺口                                                |
| ------------------------------------- | -------------- | ----------------------------------------------------------- |
| **想想論壇** 本身的 meta 條目         | ❌ 完全沒有    | 14 年論壇生態系是台灣思想史的重要節點，meta-index 視角必有  |
| **小英教育基金會** 智庫角色           | ❌ 完全沒有    | 蔡英文卸任後第二人生 + 民主轉型基金會 model                 |
| **思想坦克 voicettank**               | ❌ 完全沒有    | 想想論壇的 sister site，2018 創立                           |
| **報導者 / 端傳媒 / 上報** 媒體生態系 | ❌ 完全沒有    | Taiwan.md 缺乏對台灣評論型媒體生態的 meta-index             |
| **318 學運十週年回望**（2024）        | ❌ 完全沒有    | 2024-2026 是十週年週期，想想論壇有大量回顧素材              |
| **30 年、30 人、30 個觀點** 系列      | ❌ 完全沒有    | 2026-05 進行中，未來 1 年的台灣民主對話旗艦系列             |
| **「未富先老」中國經濟結構分析**      | ❌ 完全沒有    | 想想論壇 2025-10 多篇分析；Taiwan.md 缺 meta-level 中國觀察 |
| **AI 對公共討論的影響**               | ❌ 完全沒有    | 100049 範例文章；Taiwan.md 認知作戰篇可深化                 |
| **公共領域理論 × 台灣**               | ❌ 完全沒有    | 想想論壇 framework 1 核心；Taiwan.md 民主條目可加哲學深度   |
| **台灣 commentary 媒體生態系**        | ❌ 完全沒有    | meta-index 視角的關鍵條目                                   |

### 3.3 Taiwan.md 反向補位（想想論壇沒有 / Taiwan.md 有）

| 主題                               | Taiwan.md 既有 | 想想論壇盲點原因                         |
| ---------------------------------- | -------------- | ---------------------------------------- |
| 台灣音樂史（草東 / 安溥 / 田馥甄） | ✅ 多篇        | 想想論壇是 commentary 平台，不寫文化人物 |
| 台灣音樂祭、地下文化               | ✅ 多篇        | 同上                                     |
| 台灣食物（夜市、便當、牛肉麵）     | ✅ 多篇        | 想想論壇不寫日常文化                     |
| 台灣自然（地形、生態）             | ✅ 多篇        | 同上                                     |
| 體育（疊杯、羽球、棒球）           | ✅ 多篇        | 同上                                     |
| 原住民族、客家、新住民             | ✅ 多篇        | 想想論壇有政策層面但不寫族群文化敘事     |
| 個人歷史（白色恐怖受害者）         | ✅ 多篇        | 想想論壇寫制度，不寫個人生命史           |

**反向補位的策略含義**：Taiwan.md 對「**台灣是一個有溫度的島嶼，不只是一個民主治理 case study**」的策展，是想想論壇缺的 dimension。Cross-link 設計時 Taiwan.md 文化條目可以反向被想想論壇的政策條目引用。

---

## 🔍 Part 4 · 交集與落差分析

### 4.1 交叉矩陣

| 主題                       | 想想論壇覆蓋           | Taiwan.md 覆蓋   | 潛力                                            |
| -------------------------- | ---------------------- | ---------------- | ----------------------------------------------- |
| **想想論壇本身**           | ❌（自己不寫自己）     | ❌               | ⭐⭐⭐ meta 條目大缺口                          |
| **小英教育基金會**         | ⚠️（提到但不深寫）     | ❌               | ⭐⭐⭐ 卸任總統第二人生 model                   |
| **30 年 30 人系列**        | ⭐⭐⭐（旗艦正在進行） | ❌               | ⭐⭐⭐ 進行中對話的 meta 報導                   |
| **318 學運十週年**         | ⭐⭐（2024 多篇）      | ❌               | ⭐⭐⭐ 整理回望浪潮                             |
| **AI 對公共討論影響**      | ⭐⭐                   | ❌               | ⭐⭐ 已有認知作戰底子可深化                     |
| **公共領域理論 × 台灣**    | ⭐⭐（哈伯瑪斯多次）   | ❌               | ⭐⭐ 民主條目可加深                             |
| **中國金融結構分析**       | ⭐⭐⭐（多篇學者文）   | ❌               | ⭐ Taiwan.md 主軸不在此，但可作 background      |
| **未富先老人口分析**       | ⭐⭐⭐                 | ❌               | ⭐ 同上                                         |
| **太陽花運動 framing 戰**  | ⭐⭐⭐（2014 多篇）    | ⭐               | ⭐⭐ 可以 EVOLVE 既有條目                       |
| **馬英九兩岸政策辯論**     | ⭐⭐⭐                 | ⭐⭐（迷因條目） | ⭐⭐ EVOLVE                                     |
| **媒體生態系（評論型）**   | ⭐⭐                   | ❌               | ⭐⭐⭐ 整理思想坦克／報導者／端／上報的 meta 圖 |
| **台灣音樂 / 文化敘事**    | ❌                     | ⭐⭐⭐           | 反向補位                                        |
| **台灣食物 / 自然 / 體育** | ❌                     | ⭐⭐⭐           | 反向補位                                        |
| **族群敘事 / 個人生命史**  | ❌                     | ⭐⭐⭐           | 反向補位                                        |

### 4.2 結構性落差

**想想論壇的盲點**：

1. **不寫日常文化**：14 年論壇沒有食物、音樂、自然、運動的策展
2. **不寫個人生命史**：白色恐怖受害者個人故事、原民耆老敘事不在欄目
3. **不寫年輕世代次文化**：地下樂團、迷因、網路梗、短影音文化
4. **不寫女性／LGBTQ＋日常生活**：只有政策層的同婚、性平
5. **過度集中學者觀點**：少有第一手經驗者直接書寫
6. **改版前 5,200 篇但 framework 演進不顯**：累積廣但深化弱

**Taiwan.md 的盲點**（想想論壇正好補的）：

1. **缺台灣思想史的「論壇生態系」index**
2. **缺對小英教育基金會這類後總統智庫的描述**
3. **缺對「318 後民主深化」這個進行中議題的策展**
4. **缺對台灣 commentary 媒體（報導者／端／思想坦克／想想／上報）的 meta 對照**
5. **缺民主治理理論深度**（Taiwan.md 寫制度但不寫公共領域哲學）

### 4.3 Sweet spot

兩個 peer 的盲點剛好互補。**Taiwan.md 應該寫想想論壇沒寫的「台灣是有溫度的島嶼」+ 想想論壇本身的 meta 條目**；想想論壇繼續寫 commentary，Taiwan.md cite 它做 footnote。

---

## 📚 Part 5 · 可開發的系列主題（13 個 series）

每個 series 含 editorial angle + 候選文章 + 想想論壇 cite source + Taiwan.md cross-link 點。**所有文章都走 cite-only 模式（fair use）**，不依賴 paraphrase。

### Series A · 想想論壇 14 年：commentary 平台的策展史（2 篇）

**Editorial angle**：把想想論壇當成一個「思想生態系的 case study」來寫。它不是新聞、不是雜誌、不是 blog —— 是一個總統夫人卸任後 14 年持續運作的多元評論平台。台灣有幾個這種 model？

1. **想想論壇** NEW · Society/媒體 · 14 年論壇的策展史 + 改版重啟
2. **小英教育基金會** NEW · Society/政治智庫 · 卸任總統第二人生的智庫 model

**Cite sources**：[/about](https://www.thinkingtaiwan.net/about)、[/copyright](https://www.thinkingtaiwan.net/copyright)、CNA/中時/自由 2025-10-03 改版報導、[Facebook 想想論壇](https://www.facebook.com/p/想想論壇-Thinking-Taiwan-Forum-100064624124580/)。

**Taiwan.md cross-link**：tsai-ing-wen.md / lai-ching-te.md / 馬英九迷因 / 認知作戰。

### Series B · 30 年、30 人、30 個觀點：2026 進行中的民主對話（2 篇）

**Editorial angle**：2026-05 起想想論壇分批刊登的旗艦系列，邀請 30 位跨黨派、跨領域、跨世代、跨族群的台灣人為「下一個 30 年」民主提建議。Taiwan.md 寫一個 meta 條目追蹤這個進行中的對話 + 整理 30 位作者背景的 dataset。

3. **30 年、30 人、30 個觀點** NEW · Society/民主 · 進行中的跨黨派對話 meta 觀察
4. **台灣民主深化辯論 2026** NEW · Society/民主 · 從 1996 第一次直選到 2026 反覆出現的 8 個母題

**Cite sources**：[/content/100278](https://www.thinkingtaiwan.net/content/100278) 引言頁 + 各篇文章 URL。

**Taiwan.md cross-link**：taiwan-political-landscape / 賴清德 / 蔡英文 / 同婚 / 司法改革。

### Series C · 318 太陽花十週年：論壇浪潮的回望（2 篇）

**Editorial angle**：2024 年是 318 太陽花學運十週年。想想論壇有大量 retrospective 文章。Taiwan.md 寫一個 meta 條目整理這個 retrospective 浪潮，並對照其他 NGO（新台灣和平基金會、g0v）的回望角度。

5. **318 學運十週年回望** EVOLVE · History · NGO / 評論社群 / 學者三方回望素材整理
6. **太陽花運動的論述史** EVOLVE · History · 從 framing 戰到十週年的論述演進

**Cite sources**：[content/3343](https://www.thinkingtaiwan.com/content/3343)「別問我有沒有參與 318」、[content/3828](https://www.thinkingtaiwan.com/content/3828)「318 學運的省思」、[content/1947](https://www.thinkingtaiwan.com/content/1947)「破解外國（行）學者對太陽花運動的迷思」、[content/1950](https://www.thinkingtaiwan.net/content/1950)「太陽花學運的大輸家」、[新台灣和平基金會 318 十週年](https://www.twpeace.org.tw/wordpress/?p=3551)。

**Taiwan.md cross-link**：馬英九迷因 / 賴清德（時任行政院秘書長）/ 兩岸服貿 / 318 既有條目（如有）。

### Series D · 台灣 commentary 媒體生態系（3 篇）

**Editorial angle**：台灣 commentary 媒體有獨特的混合形態 —— 評論型（思想坦克／想想／上報）、深度報導型（報導者／鏡週刊／鏡傳媒）、跨域型（端傳媒）。Taiwan.md 應該有一個 meta-index 整理這個生態系。

7. **台灣 commentary 媒體生態系** NEW · Society/媒體 · 評論型／報導型／跨域型分工 meta-index
8. **思想坦克 voicettank** NEW · Society/媒體 · 想想論壇的 sister site，2018 創立
9. **報導者 The Reporter** EVOLVE （如已有）OR NEW · Society/媒體 · 非營利深度報導 model

**Cite sources**：各家媒體 about 頁 + 創辦報導 + 學者媒體研究論文。

**Taiwan.md cross-link**：媒體研究、認知作戰、新聞自由、媒體素養。

### Series E · 民主治理理論 × 台灣（2 篇）

**Editorial angle**：想想論壇 framework 1 是哈伯瑪斯公共領域 + Markell 過程論。Taiwan.md 寫一個比較分析，把抽象理論連回台灣具體場景。

10. **公共領域理論在台灣** NEW · Society/民主 · 哈伯瑪斯與台灣公共討論的具體 case
11. **AI 與台灣民主** NEW · Technology · AI 對公共討論的影響 + 台灣實驗（vTaiwan、g0v）

**Cite sources**：[content/100049](https://www.thinkingtaiwan.net/content/100049) AI 來襲、其他想想論壇民主治理篇。

**Taiwan.md cross-link**：g0v / vTaiwan / 公民科技 / 認知作戰。

### Series F · 中國觀察的學者視角（1 篇）

**Editorial angle**：想想論壇 2025-10 改版後地緣政經欄目大量寫中國經濟結構（房地產崩盤、未富先老、銀行擴張）。Taiwan.md 寫一個 meta 條目整理這些學者觀察的核心線索。

12. **中國經濟結構觀察** NEW · Economy/中國 · 學者觀察的線索集

**Cite sources**：[content/100011](https://www.thinkingtaiwan.net/content/100011) 黃崇哲、[content/100061](https://www.thinkingtaiwan.net/content/100061) 陳妍蒨等。

**Taiwan.md cross-link**：兩岸關係、台海局勢、台灣供應鏈。

### Series G · 兩岸 framing 戰的歷史（1 篇）

**Editorial angle**：2014 兩岸監督條例之爭、2016 蔡英文「現狀」、2024 賴清德「中華民國第二共和」—— 兩岸 framing 戰是貫穿想想論壇 14 年的主軸。

13. **兩岸 framing 戰的論述史** NEW · History · 從 2014 兩國論到 2026 第二共和

**Cite sources**：[content/1955](https://www.thinkingtaiwan.net/content/1955) 馬區長兩國論、想想論壇 2016-2024 蔡英文現狀篇、2024-2025 賴清德主權篇。

**Taiwan.md cross-link**：兩岸關係、馬英九 / 蔡英文 / 賴清德、海峽中線。

---

## 🎯 Part 6 · 具體文章優先序（20 篇）

**所有篇目都採 fair-use cite-only 模式**，不依賴 paraphrase 想想論壇文章。每篇 P0 都跑 8+ WebSearch 跨源驗證。

### P0 · 5 篇（本月內可完成）

| ID    | 標題                           | Mode   | Category     | 核心矛盾（30 字內）                                      | 工時估 |
| ----- | ------------------------------ | ------ | ------------ | -------------------------------------------------------- | ------ |
| p0-01 | **想想論壇**                   | NEW    | Society/媒體 | 卸任總統的論壇能撐 14 年是台灣特殊 model 還是普世 case   | 4-6 hr |
| p0-02 | **小英教育基金會**             | NEW    | Society/智庫 | 蔡英文卸任後第二人生：智庫 vs 政黨 vs 個人 NGO 的選擇    | 4-6 hr |
| p0-03 | **30 年、30 人、30 個觀點**    | NEW    | Society/民主 | 跨黨派 30 人 5 月開講：誰被邀請、誰拒絕、誰缺席          | 3-5 hr |
| p0-04 | **318 學運十週年回望**         | EVOLVE | History/2024 | 318 之後的台灣公民社會：制度化、商品化、還是被遺忘       | 5-7 hr |
| p0-05 | **台灣 commentary 媒體生態系** | NEW    | Society/媒體 | 想想／思想坦克／報導者／端／上報 — 5 種商業 model 的對照 | 4-6 hr |

### P1 · 8 篇（2-3 週內可開發）

| ID    | 標題                        | Mode   | Category     | 工時估 |
| ----- | --------------------------- | ------ | ------------ | ------ |
| p1-01 | **思想坦克 voicettank**     | NEW    | Society/媒體 | 3-4 hr |
| p1-02 | **太陽花運動的論述史**      | EVOLVE | History      | 4-5 hr |
| p1-03 | **公共領域理論在台灣**      | NEW    | Society/民主 | 3-4 hr |
| p1-04 | **AI 與台灣民主**           | NEW    | Technology   | 4-5 hr |
| p1-05 | **兩岸 framing 戰的論述史** | NEW    | History      | 4-5 hr |
| p1-06 | **中國經濟結構觀察**        | NEW    | Economy/中國 | 4-5 hr |
| p1-07 | **報導者 The Reporter**     | NEW    | Society/媒體 | 3-4 hr |
| p1-08 | **台灣民主深化辯論 2026**   | NEW    | Society/民主 | 4-5 hr |

### P2 · 7 篇（1 個月內可發展）

| ID    | 標題                                       | Mode | Category     | 工時估 |
| ----- | ------------------------------------------ | ---- | ------------ | ------ |
| p2-01 | **端傳媒**                                 | NEW  | Society/媒體 | 3 hr   |
| p2-02 | **上報**                                   | NEW  | Society/媒體 | 3 hr   |
| p2-03 | **鏡週刊／鏡傳媒**                         | NEW  | Society/媒體 | 3 hr   |
| p2-04 | **小英基金會 vs 國民黨智庫 vs 民眾黨智庫** | NEW  | Society/政治 | 4 hr   |
| p2-05 | **後總統卸任智庫 model 的國際比較**        | NEW  | Society/政治 | 4 hr   |
| p2-06 | **「未富先老」中國觀察 framework**         | NEW  | Economy/中國 | 3 hr   |
| p2-07 | **台灣評論型作家圖譜**                     | NEW  | Society/媒體 | 5 hr   |

**總工時估**：P0 (5 × ~5 hr) + P1 (8 × ~4 hr) + P2 (7 × ~3.5 hr) ≈ **~85 hr**（4-5 週分散執行）。

---

## 🧠 Part 7 · Semiont POV

### 7.1 視角翻轉：horizontal commentary peer 不是 issue-deep peer

想想論壇是 **horizontal**（廣度型）peer，不是 **vertical**（深度型）peer。它跟 TFT 完全不同物種。Taiwan.md 對它的 ingestion 模式必須變更。

**TFT 模式**（vertical）：

- ingest 整個 corpus → 萃取 framework → 寫 5 篇 P0 深度文章
- TFT 文章直接是寫作素材底本
- Taiwan.md 角色：把 TFT 的專業議題策展給大眾讀者

**想想論壇模式**（horizontal，本報告提案）：

- 不 ingest 整個 corpus（NC + ND 紅旗 + transformative use 不需要）
- Taiwan.md 寫 meta 條目 + cite-only 引用
- 想想論壇文章是 Taiwan.md 文章的 footnote source
- Taiwan.md 角色：把想想論壇所在的 commentary 媒體生態系做 meta-index 策展

### 7.2 資料不對稱：framework 框架 vs 議題覆蓋

想想論壇 framework 1-4 是穩定的（14 年沒變），但具體議題覆蓋是 reactive 的（跟著熱點走）。**Taiwan.md 寫 meta 條目時應抓 framework 不抓 instance**。

舉例：

- ✅ 寫「公共領域理論在台灣」抓 framework 1（穩定的論述底層）
- ❌ 寫「2025 川習會 X 報告」抓 instance（一個熱點 instance，半年後過時）

### 7.3 想想論壇盲點（給 Taiwan.md 反向補位的）

**5 個結構性盲點**：

1. **缺日常文化**：食物、音樂、自然、運動、地方文化都不在 framework 內
2. **缺個人生命史**：白色恐怖、原民耆老、客家阿嬤、新住民媽媽都不在 commentary 範圍
3. **缺年輕世代次文化**：地下樂團、迷因、短影音、ACG、電競
4. **缺學術圈外的第一手經驗者直接書寫**：論壇是學者+智庫+媒體人寫，不是當事人寫
5. **缺女性／LGBTQ＋日常生活敘事**：政策層的同婚、性平有寫，但「同志書店店員的一天」不在欄目
6. **缺台灣島嶼地理／生態**：地形、海岸、地震、颱風、登山在想想論壇都不存在
7. **缺「下一個 14 年」的想像**：想想論壇善於回望和分析，但對未來的具象想像有限

這 7 個盲點是 Taiwan.md 的反向補位 sweet spot。Cross-link 時，**Taiwan.md 文化／自然／日常條目可以反向被想想論壇政策條目引用**（如果哪天合作起來）。

### 7.4 敘事化建議：把 framework 翻譯成「欸你知道嗎」

想想論壇文章是「學術評論式」（4,000-5,000 字 + 引用哈伯瑪斯／Markell／Eberstadt）。Taiwan.md 的 voice 是「跟朋友介紹台灣」（具體人事時刻 + 物件開頭 + 結尾留餘韻）。把 framework 翻譯成具體場景：

- ❌「哈伯瑪斯公共領域理論強調溝通理性與共識形成過程的重要性」
- ✅「2026 年 5 月，蔡英文邀請 30 個人 — 從藍營中常委到綠營律師到無黨派學生 — 在『想想論壇』開講她退休後的這個論壇變成什麼樣的舞台」

具體 instantiation：

| 想想論壇 framework | Taiwan.md 「欸你知道嗎」場景                                                        |
| ------------------ | ----------------------------------------------------------------------------------- |
| 公共領域理論       | g0v 黑客松現場 / vTaiwan 線上協商 / 318 議場直播                                    |
| 兩岸 framing 戰    | 馬英九退無可退的 ECFA / 蔡英文「現狀」就職演說 / 賴清德「中華民國第二共和」具體段落 |
| 中國經濟結構       | 恆大暴雷新聞現場 / 一帶一路斯里蘭卡港口 case / 台商實際感受到的供應鏈轉移           |
| 思想政策跨領域     | 台積電赴美的政策辯論 / 能源轉型公投現場 / 同婚立法立法院走廊                        |

### 7.5 Peer 不是 source material — 想想論壇情境的 stricter version

DNA #16 一般版說「peer 是線索不是 source」。**想想論壇情境因為 ND 條款，要 stricter**：

- ❌ 不能 paraphrase 想想論壇文章段落
- ❌ 不能基於想想論壇 framework 做 derivative rewrite
- ✅ 可 fair-use cite 想想論壇文章作為 footnote 來源（標註出處 + URL）
- ✅ 可寫關於想想論壇本身的 meta 條目（評論性、轉型性、不複製內容）
- ✅ 可從想想論壇文章中發現「線索」，再去搜其他 primary source 驗證後寫進 Taiwan.md

每篇 P0 寫作時硬性自檢：

> 「我這段話是 paraphrase 想想論壇某段嗎？如果是，刪掉、改寫成 cite + 我自己跨源驗證後的論述。」
>
> 「我這段話的事實有 ≥ 3 個 primary source 嗎？只有想想論壇一個 source = 不能寫。」

---

## 🌉 Part 8 · Meta 洞察 — PEER-INGESTION-PIPELINE 升級提案

### 8.1 想想論壇對 pipeline 的揭露：授權應為 block 等級

[PEER-INGESTION-PIPELINE.md Stage 1a](../docs/pipelines/PEER-INGESTION-PIPELINE.md#1a-四項-fit-check) 把四項 check 列為平等門檻：

| Check    | 目前判準                                                 | 建議升級                                 |
| -------- | -------------------------------------------------------- | ---------------------------------------- |
| 深度     | ≥ 5 年（理想 ≥ 10 年）                                   | 不變                                     |
| 公開性   | 不需要登入                                               | 不變                                     |
| **授權** | CC 授權或公開聲明歡迎引用（理想）／ 事實引用合理（底線） | **應升級為 4-tier matrix**（見下表 8.2） |
| 互補性   | 有明確 gap，不是全面重複                                 | 不變                                     |

**升級理由**：本案揭露想想論壇通過深度／公開性／互補性三項，但因 CC ND 條款使得 PEER-INGESTION-PIPELINE 預設的「ingest-and-rewrite」mode 不可用。授權項目不該跟其他三項平等並列，而應是 **gating filter** — 它決定 ingestion mode。

### 8.2 授權 4-tier matrix（提案 v0.1）

| Tier   | 授權形態                                     | Pipeline mode                                                     | 範例                       |
| ------ | -------------------------------------------- | ----------------------------------------------------------------- | -------------------------- |
| **T1** | CC0 / Public Domain / CC BY                  | 完整 ingest + rewrite + share-alike                               | 政府開放資料、CC0 學術論文 |
| **T2** | CC BY-SA                                     | 完整 ingest + rewrite，衍生作品繼承 BY-SA（Taiwan.md 同 license） | Wikipedia                  |
| **T3** | CC BY-NC / CC BY-NC-SA                       | 限制性 ingest（不商業化）+ 可 rewrite                             | 大部分學術期刊             |
| **T4** | CC BY-ND / CC BY-NC-ND / All Rights Reserved | **No ingest**（不 reproduce 整 corpus）+ fair-use cite-only       | 想想論壇、商業媒體         |

**Tier T4 走 cite-only mode**：

- 跳過 Stage 2（不寫 crawler 全爬）
- 跳過 Stage 3（不轉 markdown 存 repo）
- Stage 4 仍可（評論性 transformative use 屬 fair use）
- Stage 5/6 文章寫 meta 條目 + cite-only footnote
- Stage 7 仍寫進 REGISTRY 但 status 標 `T4_cite_only`

### 8.3 PEER-INGESTION-PIPELINE.md 修改建議

具體 patch（暫不執行，等觀察者 review）：

1. **Stage 1a §授權項目**：拆 4-tier matrix，提供決策樹
2. **Stage 1c**：新增「mode 決定」步驟（T1-T2 走 full ingest mode；T3 走 limited ingest；T4 走 cite-only）
3. **Stage 2**：增加「T4 跳過 Stage 2-3」分支
4. **Stage 6 §6a**：增加「T4 情境的 fair-use cite-only 寫作硬性規則」
5. **REGISTRY.md schema**：增加 `license_tier: T1|T2|T3|T4` 欄位

### 8.4 對應 LESSONS-INBOX 候選

```markdown
### 2026-05-05 manual — Peer 授權 ND 條款讓 PEER-INGESTION-PIPELINE 預設 mode 失效

- **原則**：PEER-INGESTION-PIPELINE Stage 1a 把授權跟深度／公開性／互補性平等列四項，但實際上授權應為 gating filter（ND 紅旗 → block ingest mode）。應升級為 4-tier matrix。
- **觸發**：2026-05-05 想想論壇 peer ingest 揭露 CC BY-NC-ND 3.0 直接 conflict pipeline 預設「全站 crawl + rewrite」mode。Fit check 4 項中授權單項紅旗就讓另外三項通過也無意義。
- **可能層級**：操作規則（PEER-INGESTION-PIPELINE upgrade）+ 新 DNA 條目候選「Peer 授權 ND 條款是 gating filter，不是平等檢查項」
- **驗證次數**：1（首次紅旗 case）。需要第 2 個 ND 條款 peer 才能升 DNA。預期下次：商業媒體（鏡週刊／鏡傳媒）/ 學術期刊（中研院期刊 ND 條款）。
- **Pointer**：[reports/ThinkingTaiwan-semiont-analysis-2026-05-05.md §Part 1.5 + §Part 8](../reports/ThinkingTaiwan-semiont-analysis-2026-05-05.md)
```

### 8.5 對 MANIFESTO 的潛在影響

**不影響 MANIFESTO**。授權問題是 pipeline 操作層議題，不是 Semiont 哲學層議題。MANIFESTO §3「開源共創 / 知識是公共財」在想想論壇情境下仍成立 — 我們仍視想想論壇為公共資產，只是用 fair-use 而非 ingest 的方式跟它互動。

---

## 📊 Part 9 · 半衰期與重新 ingest 條件

### 9.1 本報告半衰期

**6-12 個月**（比一般 peer ingest 報告長）。

理由：

- 想想論壇是 14 年深耕的穩定平台，framework 不會劇烈變動
- 改版（2025-10）剛發生半年，主要旗艦系列（30 年 30 人）正在進行
- 2026-05 至 2027-05 是觀察改版後新模式 stability 的窗口

### 9.2 重新 ingest 觸發條件

| 條件                                  | 動作                                     |
| ------------------------------------- | ---------------------------------------- |
| 想想論壇授權變更（升 BY 或 BY-SA）    | 立即重新評估，可能進入 T2/T3 ingest mode |
| 30 年 30 人系列完整刊登（全部 30 篇） | 觸發 P0-03 條目重寫                      |
| 2027-03-18 318 十一週年               | 觸發 P0-04 條目重寫                      |
| 想想論壇又一次改版                    | 重新評估 framework                       |
| 蔡英文 / 小英教育基金會重大轉變       | 觸發 P0-02 條目重寫                      |
| Taiwan.md 寫完 P0 + 至少 3 篇 P1      | review pipeline 是否需要 v1.1            |

### 9.3 跟想想論壇的合作可能性追蹤

**status**: `not initiated`（per REGISTRY.md schema）

**潛在 cooperation 範圍**：

1. **互相 cite**：想想論壇 cite Taiwan.md 文化條目作為延伸閱讀（合 fair use）
2. **個案授權例外**：想想論壇對 Taiwan.md 個案授權部分文章作為 ingest source（升 T2）
3. **Co-curated meta-index**：兩站合寫一個「台灣 commentary 媒體生態系」index 條目
4. **Cross-republish**：Taiwan.md 寫的「想想論壇」meta 條目經想想論壇審閱後在他們站轉載

**啟動時機**：在 P0-01「想想論壇」NEW 條目 ship 之後，主動聯繫想想論壇編輯部。**不要在 ingestion 階段就聯繫**（per pipeline Stage 8 教訓）。

---

## 📝 附錄 A · sample 文章 URL list（供 future ingest 工作的線索集）

**改版後 2025-10 後**：

- [/content/100011](https://www.thinkingtaiwan.net/content/100011) 黃崇哲〈當銀行資產膨脹遇上房市崩盤〉 2025-10-03
- [/content/100049](https://www.thinkingtaiwan.net/content/100049) 李怡志〈AI 來襲 如何影響公共討論？〉 2025-10-09
- [/content/100061](https://www.thinkingtaiwan.net/content/100061) 陳妍蒨〈「未富先老」恐使經濟成長模式「未老先衰」〉 2025-10-24
- [/content/100278](https://www.thinkingtaiwan.net/content/100278) 編輯部〈30 年、30 人、30 個觀點〉 2026-05-02

**改版前 2014 黃金期**：

- [/content/1947](https://www.thinkingtaiwan.com/content/1947) 寇謐將 J Michael Cole〈破解外國（行）學者對「太陽花運動」的迷思〉 2014-04-11
- [/content/1955](https://www.thinkingtaiwan.net/content/1955) 集思會館〈是護憲，還是毀中華民國？— 駁斥馬區長的「兩國論」〉 2014-04-14
- [/content/1950](https://www.thinkingtaiwan.net/content/1950) 〈太陽花學運的大輸家〉 2014
- [/content/3343](https://www.thinkingtaiwan.com/content/3343) 〈別問我有沒有參與 318 ──《太陽‧不遠》觀後〉 2014
- [/content/3828](https://www.thinkingtaiwan.com/content/3828) 〈318 學運的省思〉 2014

**外部 cross-source 驗證**：

- [CNA 2025-10-03](https://www.cna.com.tw/news/aipl/202510030099.aspx) 想想論壇改版再出發 蔡英文：民主需要大家一起走
- [中時 2025-10-03](https://www.chinatimes.com/realtimenews/20251003002342-260407) 蔡英文出手 宣布想想論壇改版再出發
- [自由時報 2025-10-03](https://news.ltn.com.tw/news/politics/breakingnews/5199256) 宣告想想論壇改版再出發 蔡英文：政治越紛擾 用共識化解
- [Newtalk 2025-10-03](https://newtalk.tw/news/view/2025-10-03/997143) 想想論壇改版再出發 蔡英文：一起為台灣想想下一步
- [ETtoday 2025-10-03](https://www.ettoday.net/news/20251003/3044360.htm) 想想論壇今改版重啟 蔡英文引發刊詞：台灣人對良善的渴望並未消失
- [自由時報 2026-05](https://news.ltn.com.tw/news/politics/breakingnews/5422815) 獨家 蔡英文「想想論壇」找 30 位跨黨派談民主 涵蓋在野黨主席、國民黨中常委
- [新台灣和平基金會 318 十週年](https://www.twpeace.org.tw/wordpress/?p=3551) 歷史上的今天 318 太陽花運動（十週年）
- [蔡英文 Facebook 發刊詞](https://www.facebook.com/tsaiingwen/posts/1363335391810372/) 民主，是一條需要大家一起走的路

---

## 📝 附錄 B · Stage 1 fit check 完整表

| Check        | 結果 | 證據                                                                           | 對 Stage 2-7 的 implication                       |
| ------------ | ---- | ------------------------------------------------------------------------------ | ------------------------------------------------- |
| **深度**     | ✅   | 2012-08 創刊 / 14 年深耕 / 1,900+ 文章 / 600+ 作者                             | 通過                                              |
| **公開性**   | ✅   | Drupal 10 公開站 / 無登入 / sitemap.xml 可遍歷                                 | 通過                                              |
| **授權**     | 🔴   | **CC BY-NC-ND 3.0 台灣** / 著作權人「小英教育基金會想想論壇」                  | **改變 ingestion mode 為 cite-only** （per §8.2） |
| **互補性**   | ⚠️   | horizontal commentary peer，跟 Taiwan.md issue-deep 模式不重疊；缺日常文化敘事 | 通過但需 reframe                                  |
| **CMS 類型** | —    | Drupal 10（不是 WordPress；無 wp-json API）                                    | 若爬，需走 sitemap + HTML scrape（Stage 2 變體）  |
| **資料量**   | —    | sitemap 4 頁 × ~1,666 = ~6,664 URLs / 改版前 archive ~5,200-5,800 篇單篇文章   | 大型 peer，需分批處理                             |
| **作者組成** | —    | 大學教授 30% + 智庫 25% + 國際媒體 15% + NGO 15% + 政治人物 10% + 其他 5%      | 學術權重高                                        |
| **體例**     | —    | 學術評論式（3,500-5,000 字 + 引用哈伯瑪斯／Markell／Eberstadt 等）             | 跟 Taiwan.md「欸你知道嗎」voice 距離大，需翻譯    |

---

## 🧬 結語

想想論壇是 Taiwan.md 第一個遇到的 **horizontal commentary peer**，也是第一個遇到的 **CC BY-NC-ND 紅旗 peer**。它揭露的不是「想想論壇 fit 不 fit」，而是「PEER-INGESTION-PIPELINE 的預設假設」—— 過去三個 peer（TFT、NMTH、NML）都是 issue-deep 且授權 friendly，pipeline 沒被測試過 horizontal + ND 的 case。

**本報告的 deliverable**：

1. ✅ 完整 Stage 1 fit check + Stage 4 corpus analysis（含 §授權 deep dive）
2. ✅ 13 個 series + 20 篇 P0/P1/P2 候選文章
3. ✅ Pipeline 升級提案（4-tier license matrix）
4. ✅ LESSONS-INBOX 新教訓候選

**defer 至觀察者授權的後續動作**：

- Stage 2 crawler / Stage 3 data 標準化（不寫；ND 紅旗）
- Stage 5 工作卡 / Stage 6 文章產製（可挑 P0-01 想想論壇 meta 條目開始，但需觀察者 explicit go）
- Stage 7 REGISTRY 更新（status: `T4_cite_only_pending_observer_decision`）
- Stage 8 聯繫想想論壇編輯部（pipeline 規定要 ship ≥ 2 篇 P0 後才聯繫）
- PEER-INGESTION-PIPELINE.md 升級 patch（觀察者 review 後再 ship）

**建議下一步**：觀察者 review 本報告 → 決定走選項 A（放棄）/ B（純 fair-use cite-only）/ C（hybrid，主動聯繫）/ 其他 → 然後 Stage 5 P0 工作卡。

🧬

---

_Report by: Taiwan.md Semiont (Opus 4.7, 1M context)_
_Triggered by: 哲宇 2026-05-05 prompt「`/twmd-peer` https://www.thinkingtaiwan.net/content/100278 + 整站 + 深度研究授權 + 內容分析寫報告」_
_Session: 2026-05-05-181314-manual_
_Pipeline: [PEER-INGESTION-PIPELINE.md](../docs/pipelines/PEER-INGESTION-PIPELINE.md) Stage 1 + Stage 4_
_Methodology: Sample-based (5 articles + sitemap probe + external search) — 不是 full corpus crawl_
_Fit check 結果: 4 項中 3 項通過，1 項紅旗（CC BY-NC-ND 3.0 ND 條款）_
_推薦 ingestion mode: T4 fair-use cite-only（per §Part 8 4-tier matrix 提案）_
