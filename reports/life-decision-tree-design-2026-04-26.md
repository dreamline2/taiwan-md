# Life Decision Tree — 人生分支樹視覺化設計（以 焦安溥 為原型）

> **Status**: 規劃稿（observer 觸發 2026-04-26 β-r4）
> **觸發**: 觀察者「分析安溥的文章，做出 RPG 重大人生分支，類似語言分支樹，時間為主軸選擇為副軸，能看見其他選擇」
> **Source article**: [knowledge/Music/張懸與安溥.md](../knowledge/Music/張懸與安溥.md)
> **Related work**: language tree (`/translations` page) / git commit graph
> **Author**: Taiwan.md (Semiont) β-r4 session

---

## TL;DR（30 秒）

把高知名度 People 條目的核心人生決策**結構化成可視化分支樹**。主軸 = 時間（top-down 編年），副軸 = 選擇（左右展開）。每個 decision node 顯示「她選的路」+「她沒選的路」+「為什麼這個選擇是 turning point」。**不是傳記摘要，是策展視角的決策地圖**。第一個 prototype 用焦安溥（決策密度高、爭議大、counterfactual 明顯），驗證後抽成 schema 推到 5-10 篇 People 條目，最終納入 REWRITE-PIPELINE 成為 People 條目的 optional Stage 7。

---

## 1. 為什麼做這個

### 1.1 跟 MANIFESTO 的對齊

| MANIFESTO 條    | 對應                                                                                                             |
| --------------- | ---------------------------------------------------------------------------------------------------------------- |
| §策展式非百科式 | 維基列「她做了什麼」；分支樹列「她做選擇時面對什麼 + 別的可能是什麼」。後者才是策展                              |
| §熱帶雨林理論   | 樹狀視覺化天然支援「夠深 + 夠真實 + 夠多元 + 夠 SSODT」——每個 node 攤開所有 perspectives，讀者進去自己選投影方向 |
| §紀實而不煽情   | counterfactual 是「她沒選的路」不是「她該選的路」，避開判斷主體；用結構承載複雜度而非情緒煽動                    |
| §10 幻覺鐵律    | 每個 alternative 必須 source-grounded（推測明確標 `[推測]` 不偽裝成事實）                                        |
| §11 書寫節制    | node label 是名詞短句，不用「不是 X，是 Y」對位句型                                                              |

### 1.2 跟現有視覺化的對照

- **語言分支樹**（`_translations.json` / dashboard 翻譯地圖）：呈現「同一篇文章在不同語言宇宙的存在狀態」，是**橫向 spatial** branching
- **人生分支樹**（本提案）：呈現「同一個人在時間軸上做的選擇 + 沒做的選擇」，是**縱向 temporal + counterfactual** branching
- 共通核心：**用 graph 結構打破線性敘事**

### 1.3 為什麼 People 條目特別需要

People 是 Taiwan.md 流量大頭（GA top 10 半數是 People）。但目前 People 條目幾乎都是線性編年體：「1981 出生 → 1994 寫〈寶貝〉 → 1997 休學 → ...」。線性敘事**抹平了選擇的重量**。讀者讀完只記得 timeline，不記得「她為什麼是她」的轉折機制。

決策樹強迫策展者問：**「這個 node 上她面對的真正選項是什麼？她為什麼選這個？沒選的會去哪？」** 這個追問本身會逼出更深的 research。

---

## 2. 焦安溥案例分析（Prototype 0）

### 2.1 從文章抽出的 decision nodes

| #   | 年         | 齡  | 決策時刻                                            | 選的路                                               | 沒選的路（counterfactual）                                                | source     |
| --- | ---------- | --- | --------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------- | ---------- |
| 0   | 1981       | 0   | 出生（given，非 choice）                            | 焦家法政世家                                         | n/a                                                                       | [^1]       |
| 1   | 1994       | 13  | 與家人爭吵後離家                                    | **把痛轉成歌**（哼出〈寶貝〉旋律）                   | (a) 內化變沉默→青春期憂鬱 / (b) 向外暴力→更早決裂                         | [^3]       |
| 2   | 1997       | 16  | 走進父母臥房說要休學                                | **休學**                                             | (a) 繼續高中→焦元溥那條學術路 / (b) 出國念寄宿學校→英國音樂學院           | [^2]       |
| 3   | ~2000      | 19  | 下個月房租繳不出來、計程車兩百塊都捨不得            | **女巫店唱下去**                                     | (a) 回家認輸 / (b) 跨界做別的工作                                         | [^2]       |
| 4   | 2003       | 22  | Mango Runs 樂團主唱，貢寮海祭最佳人氣               | **以樂團 + solo 雙線並行**                           | (a) 全心經營樂團→可能變團體記憶 / (b) 純 solo→更早被定位                  | [^6]       |
| 5   | 2006       | 25  | Sony BMG 發行《My Life Will…》（2001 錄音雪藏五年） | **接受李壽全重新發掘**                               | (a) 拒絕主流唱片公司→純獨立路徑                                           | [^7]       |
| 6   | 2009       | 28  | 《城市》苦練電吉他                                  | **從民謠轉搖滾**                                     | (a) 留在「小清新」舒適圈→更大眾流量                                       | [^8]       |
| 7   | 2012       | 31  | 《神的遊戲》自己擔任共同製作人                      | **完整作者化**（10 首歌寫 9 首詞曲）                 | (a) 持續被製作→製作人代筆 / (b) 不出新專輯→形象凍結                       | [^9]       |
| 8   | 2013/11    | 32  | 曼徹斯特演唱會台灣學生遞國旗                        | **接過國旗 + 「It's just a flag」**                  | (a) 婉拒接旗→中國市場保留 / (b) 沉默接過不解釋→兩邊都不被定義             | [^11][^12] |
| 9   | 2014/3     | 32  | 太陽花學運                                          | **Facebook 連續發文公開聲援**                        | (a) 模糊處理→保留藍綠歌迷 / (b) 反對→與〈玫瑰色的你〉敘事斷裂             | [^14]      |
| 10  | 2015/1     | 33  | 高雄巨蛋潮水箴言最後一場                            | **告別「張懸」改回本名 + 消失三年**                  | (a) 繼續用張懸→品牌資產延續 / (b) 改名但持續發片→不留空白                 | [^17][^18] |
| 11  | 2018/5     | 37  | 「煉雲」復出小巨蛋                                  | **唱別人的歌**（22 首翻唱台灣音樂史）                | (a) 唱自己舊歌→粉絲服務 / (b) 全新創作→更純粹聲明                         | [^20]      |
| 12  | 2022/1     | 40  | 演唱會上宣布離婚                                    | **公開談 + 計畫看心理諮商**                          | (a) 私下處理→保護隱私 / (b) 不公開但媒體會挖→失控敘事                     | [^21]      |
| 13  | 2022       | 41  | 《9522》專輯                                        | **回去唱十四歲的歌**（27 年時間跨度）                | (a) 全往前→中年作品線 / (b) 重新編曲舊作→懷舊路線                         | [^22]      |
| 14  | 2024/10/1  | 43  | 微博發手寫信祝賀新中國                              | **發信 + 落款「安溥祝福」**                          | (a) 沉默→市場失去但無爭議 / (b) 拒絕→與封殺事件閉環                       | [^26]      |
| 15  | 2024/10/12 | 43  | 打狗祭歌迷高喊「為什麼？」                          | **「在我演出的場合，你們永遠都是自由安全的」+ 鞠躬** | (a) 直接政治表態→兩岸雙邊燒 / (b) 取消演出→失主場 / (c) 道歉→否定 10/1 信 | [^30]      |

**節點密度**：16 個（含 birth）/ 43 年 = 平均 2.7 年一個 turning point。實際呈現可摺疊到 **8-10 主節點 + 6-8 細節 collapsed**，避免閱讀疲勞。

### 2.2 主題化分組（讀者 mental model）

把 16 nodes 按主題分 4 條敘事線（章節，不是時間段）：

1. **音樂 vs 主流**（#1, 2, 5, 6, 7, 11）— 創作者身份的養成
2. **女兒 vs 父親**（#0, 1, 2, 3, 13）— 跟焦仁和的對話結構
3. **政治 vs 模糊**（#8, 9, 14, 15）— 那面旗子的迴響
4. **公開 vs 私密**（#10, 12）— 「殺名字」與「公開離婚」的雙重剝開

樹形結構可選擇：

- **Mode A**：純時間軸（1 主縱軸 + 各 node 側邊展開 alternatives）
- **Mode B**：四線並行（4 縱軸 swim lanes + 時間橫軸）
- **Mode C**：環狀（中心 = 焦安溥，4 線從中心向外輻射）

**推薦 Mode A**：認知負荷最低，moblie-friendly，跟現有 timeline 心智模型一致。Mode B/C 留給未來迭代。

### 2.3 counterfactual 的合法性原則

每個 alternative 必須符合至少一個來源條件，否則不寫：

| 來源條件                             | 範例                                                          |
| ------------------------------------ | ------------------------------------------------------------- |
| **本人或家人公開談過的「另一條路」** | 焦仁和「她差點念書到 PhD」（推測自父女訪談語氣）              |
| **同代藝人在類似 fork 的選擇**       | 楊丞琳同年遇到簽約後唱片重組，留在主流→反襯安溥純獨立         |
| **產業結構的可預測替代**             | 獨立音樂人接 Sony BMG 與否，2000s 是明確選擇題                |
| **明確標 `[推測]`**                  | 「如果她沒回答 It's just a flag，可能會...」必須加 [推測] tag |

**禁止 pattern**（會被 §10 鐵律抓）：

- ❌ 編造 specific quote 給 counterfactual
- ❌ 編造「她其實考慮過 X」沒有來源
- ❌ 描述心理動機過於確定

---

## 3. 視覺化設計選擇

### 3.1 視覺 metaphor 選 RPG dialogue tree

對比四種選項：

| metaphor                                | 優                                              | 劣                               | 適配度 |
| --------------------------------------- | ----------------------------------------------- | -------------------------------- | ------ |
| **RPG dialogue tree**（Mass Effect 式） | 直觀「選了 A 就走 A 線」/ 玩家文化 transferable | 暗示「玩家視角」可能讓主體去能動 | ★★★★   |
| **Git commit graph**                    | dev contributor 熟悉 / 支援 merge/branch        | 太技術化 / 一般讀者不懂          | ★★     |
| **Sankey 流向圖**                       | 可量化 weight                                   | 太多 node 會糾纏                 | ★★★    |
| **Family/decision tree（傳統）**        | 普及度高                                        | 看起來像家譜，誤導               | ★★★    |

**選 RPG dialogue tree variant**，因為：

1. 觀察者明確要求「RPG 重大人生分支」
2. RPG dialogue 的「選了一個 option，其他 grey out 但仍可見」正是我們要的 visual semantic
3. 跟「人生是多重選擇題」呼應焦仁和的原話（[^2]）

### 3.2 具體視覺規格

```
                    ─── 1981 ──
                       (start)
                          │
                          │
                    ─── 1994 ──
                          │
                  ┌───────┼───────┐
                  ╎       ●       ╎
            [內化沉默]  把痛   [向外暴力]
                          │   轉成歌
                          │
                    ─── 1997 ──
                          │
                ┌─────────┼─────────┐
                ╎         ●         ╎
          [念高中→大學] 休學   [出國寄宿學校]
                          │
                          ↓
                       (continues)
```

**Visual conventions**：

- **實心 ●** = 選了的路 / **空心 ○ + 虛線** = 沒選的路
- **實線** = 主軸 timeline / **虛線** = counterfactual edge
- **節點 hover/tap** → 展開 detail card（時間 + 場景 + 選擇 + 結果 + sources）
- **每個 node 配色**: 4 主題線各一色（音樂/家人/政治/公開）

### 3.3 mobile / desktop 雙版本

- **Desktop**：full tree 展開，左側 nav 跳到任一 node，右側 sticky panel 顯示當前 node detail
- **Mobile**：純垂直時間軸，counterfactuals 摺疊在 `<details>` 內，tap 展開

### 3.4 a11y / SEO

- 所有 node 也是 semantic HTML `<section>` 含 heading（讓 screen reader 能線性讀完）
- 每個 alternative 是 `<aside>` 標 `[counterfactual]`
- structured data: schema.org `Person` + 自定 `lifeDecision` extension

---

## 4. 資料 schema

### 4.1 frontmatter extension

```yaml
# 加進現有 People 條目 frontmatter（optional）
lifeTree:
  protagonist: 焦安溥
  birthYear: 1981
  span: 1981-2024
  themes:
    - id: music
      label: 音樂 vs 主流
      color: '#8B5CF6'
    - id: family
      label: 女兒 vs 父親
      color: '#EC4899'
    - id: politics
      label: 政治 vs 模糊
      color: '#10B981'
    - id: privacy
      label: 公開 vs 私密
      color: '#F59E0B'
  nodes:
    - id: birth
      year: 1981
      type: given # given | choice | event
      theme: family
      label: '出生於台北法政世家'
      sources: ['^1']
    - id: write-baobei
      year: 1994
      age: 13
      type: choice
      theme: music
      scene: '與家人爭吵後離家，沿路哼出旋律'
      chose:
        label: '把痛轉成歌'
        consequence: '〈寶貝〉誕生，後來成為金曲提名年度歌曲'
      alternatives:
        - label: '內化變成沉默'
          plausibility: speculative
          note: '[推測] 青春期內化路徑大概率走向憂鬱症狀'
        - label: '向外暴力'
          plausibility: speculative
          note: '[推測] 與父親決裂可能更早發生'
      sources: ['^3']
    - id: drop-out
      year: 1997
      age: 16
      type: choice
      theme: family
      scene: '走進父母臥房說要休學'
      chose:
        label: '休學'
        consequence: '父親沒反對，第一次強烈感覺人生來自自己的決定'
      alternatives:
        - label: '繼續念高中'
          plausibility: structural
          note: '兄長焦元溥那條學術路徑（後成古典音樂評論家）'
        - label: '出國寄宿學校'
          plausibility: actual-attempted
          note: '焦仁和真的送她去英國，但她受不了八點門禁逃回'
      sources: ['^2']
    # ... 其他 nodes
  edges:
    - from: birth
      to: write-baobei
      narrativeWeight: 3 # 1-5, 影響的緊密度
    # ...
```

**plausibility levels**:

- `actual-chose` = 她真的選的路
- `actual-attempted` = 她實際嘗試過但結果不同（如出國寄宿但逃回）
- `structural` = 同代/同類人有人走的路
- `speculative` = 推測（必須標 [推測] 前綴）

### 4.2 為什麼放 frontmatter 不放單獨檔

- frontmatter 跟 article body 同 commit history → diff 可看出 tree 跟 prose 的演化是否同步
- sync.sh 自動轉錄到 src/content/，render 時可從 entry.data.lifeTree 讀
- 跟 perspectives/ sporeLinks 同層級（已有 precedent）

**例外**：如果 nodes > 30 → 抽成 `data/life-trees/{slug}.yml` 引用

---

## 5. 技術實作

### 5.1 Astro component

```
src/components/LifeTree/
├── LifeTree.astro          # 主組件
├── DecisionNode.astro      # 單一節點
├── AlternativePanel.astro  # counterfactual 側邊展開
├── TimelineAxis.astro      # 主時間軸
└── styles/lifetree.css     # 主題色 + 動畫
```

### 5.2 Render strategy

**Server-side**：用 Astro 純 SSR 把 lifeTree YAML render 成 static HTML + minimal JS。

**Client-side**：

- 點擊 node 切換 active state（CSS class toggle）
- 鍵盤 navigation（j/k 上下 / h/l 切換 alternatives）
- prefers-reduced-motion 友善（無強制動畫）
- 不依賴 React/Vue（單組件 < 5KB JS）

### 5.3 Tech stack 決策

| 選項         | 結論                                         |
| ------------ | -------------------------------------------- |
| D3.js        | 過度（5KB → 100KB+），不值得                 |
| Mermaid      | 不夠 customizable，alternative branch 難呈現 |
| 純 SVG + CSS | ✅ 選這個，輕量 + a11y 好                    |
| React island | 待 phase 2 evaluate（如果加 zoom/pan）       |

### 5.4 Prebuild stage

`scripts/core/build-life-trees.mjs` 跑在 prebuild：

1. 掃 `knowledge/People/*.md` 含 `lifeTree:` frontmatter
2. 驗證 schema（zod）+ source ID 對應 article footnote
3. 計算統計（node 數 / span / counterfactual 比例）→ 寫 `public/api/life-trees-meta.json`
4. dashboard 加新 widget「人生分支樹覆蓋率」

---

## 6. 路由

```
/people/張懸與安溥/             # 既有文章
/people/張懸與安溥/life-tree/  # 新增 standalone 視覺化頁
/life-trees/                    # index 頁列出所有有 tree 的人物
/api/life-trees-meta.json       # API 給 dashboard
```

article 內可選兩種嵌入方式：

1. **inline `<details>`** — 摺疊在「結語」之前
2. **頂部 CTA banner** — 「想看她的人生分支樹？→ 點這裡」link 到 standalone 頁

推薦兩者都做（inline 給 mobile 讀者順手翻，standalone 給想深玩的）。

---

## 7. 推進路線（4 phase）

### Phase 1: 焦安溥 prototype（**~1 個 heavy tick**, ~30-45 min budget per Beat 3 batch discount factor 0.5x）

**Scope**:

- 在 `knowledge/Music/張懸與安溥.md` frontmatter 加 `lifeTree:` 完整 16 nodes（從 §2.1 表轉）
- 建 `src/components/LifeTree/` 基本組件 + `/people/張懸與安溥/life-tree/` route
- 內嵌 inline `<details>` 摺疊版到文章
- counterfactual 標籤系統 + plausibility 顏色

**Definition of Done**:

- [ ] `bash scripts/tools/check-manifesto-11.sh knowledge/Music/張懸與安溥.md` 0 violations
- [ ] node 100% source-grounded（每個 chose / alternative 都有 source ID）
- [ ] mobile + desktop 視覺通過（preview_screenshot 各一張）
- [ ] a11y：keyboard navigation + screen reader 可線性讀完
- [ ] Stage 3.5 全文幻覺審計（確認 counterfactual 都有 plausibility tag）

**需哲宇授權的決策**:

- counterfactual 的「她會不會 OK 看到推測」品味判斷（建議：第一稿先做 publication-private branch，哲宇 review 才 public push）
- 如果安溥本人或家人後續對 counterfactual 有意見 → 撤回機制 SOP

### Phase 2: schema 抽象 + 工具化（~1 個 heavy tick）

- 把 frontmatter schema 寫進 `docs/editorial/EDITORIAL.md` §lifeTree（v5.5）
- 造 `scripts/tools/lifetree-validate.sh`（zod schema check + source ID exists check）
- pre-commit hook 加 lifeTree 驗證
- dashboard widget「人生分支樹覆蓋率」

### Phase 3: 5 人物擴展（每篇 1-1.5 個 heavy tick = 5-7.5 ticks，可分散到 1 週）

候選名單（按決策密度高 + 爭議大 + counterfactual 明顯排序）：

1. **張忠謀** — 創立台積電前的多次轉折（IBM/TI/工研院）
2. **唐鳳** — 自學/g0v/政府的多重 fork
3. **侯孝賢** — 商業片到藝術片的轉軌
4. **吳青峰** — 蘇打綠/個人/離開魚丁糸
5. **周杰倫** — 從幕後到幕前的 turning point

每篇預期 8-12 nodes（比安溥少，避免疲勞）。

### Phase 4: 入 REWRITE-PIPELINE Stage 7（~1 個 heavy tick）

- 加 `Stage 7: lifeTree extraction`（optional，僅 People 條目）到 [REWRITE-PIPELINE.md](../docs/pipelines/REWRITE-PIPELINE.md)
- agent prompt: 從 article body 抽 5-10 個 turning point + 為每個生成 1-2 個 source-grounded alternative
- agent 結果一律 draft 進 frontmatter，**人類 review 後才 commit**（DNA #6 邊界）

**Phase 4 完成 = lifeTree 從「實驗」升級為 People 條目「正常 feature」**。

---

## 8. 風險與緩解

### 8.1 倫理風險

| 風險                                  | 緩解                                                                                                                                                                                                  |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **counterfactual 暗示「她該選別的」** | 用 RPG「都是合法選項」框架，每個 alternative 寫「if so, would have led to X」描述後果而非價值判斷                                                                                                     |
| **被當事人或家屬抗議**                | (1) 第一篇 prototype 安溥 publication 前考慮直接通知 / (2) 撤回 SOP：任何當事人 request 24 hr 內下架 alternative 區塊（保留 timeline 主軸）                                                           |
| **降到「八卦娛樂化」**                | 主題分組必須是嚴肅的（音樂/家人/政治/公開），不是「她交往對象 timeline」這種；每個 node 必須 source-grounded                                                                                          |
| **死亡與人倫悲劇 node**               | 對應 [MANIFESTO §5 紀實而不煽情](../docs/semiont/MANIFESTO.md#我的進化哲學--紀實而不煽情盡可能呈現-ssodt-所有面向)：自殺/家暴/重大悲劇相關 node 不做 counterfactual（只列事實，不推測「她該選別的」） |

### 8.2 技術風險

| 風險                                | 緩解                                                                              |
| ----------------------------------- | --------------------------------------------------------------------------------- |
| **frontmatter 變太大破壞 prebuild** | nodes > 30 自動抽到 data/life-trees/，pre-commit 偵測                             |
| **mobile 性能**（複雜 SVG）         | server-side render + lazy hydrate；alternative panels 預設 collapsed              |
| **多語言版本怎麼處理**              | Phase 1 zh-TW only；Phase 2 評估 i18n（可能 themes/labels 需翻譯但 sources 共用） |

### 8.3 scope creep 風險

**最大誘惑**：把每個人物的人生變成「無限樹」。**反例**：吳青峰可能有 50+ 重要時刻。

**紀律**：

- node 數量上限 15（含 alternatives 不超過 30 條 edges）
- 過此上限必須砍 main timeline 而不是壓縮 alternatives（保品質）
- **「不是更多 node = 更好」**（呼應 MANIFESTO §策展式：選什麼 node 才是策展）

---

## 9. 跟其他系統的整合

### 9.1 跟 ARTICLE-INBOX

- ARTICLE-INBOX 加新欄位 `lifeTreeCandidate: true | false | done`
- Stage 7 跑完 → INBOX 條目自動更新

### 9.2 跟 dashboard

- 新 widget「人生分支樹覆蓋率」(People 中有 tree 的篇數 / People 總數)
- 點 widget → /life-trees/ index 頁

### 9.3 跟 spore

- standalone tree 頁本身就是天然的 spore 素材（「想看安溥 16 個人生岔路嗎？」→ link）
- counterfactual 區塊適合做成 perspective-style spore（22 perspectives 的兄弟產物）

### 9.4 跟 LONGINGS

- 「**讓讀者進化**」(MANIFESTO §熱帶雨林) 的具體新方法
- 「**多元觀點同框並陳**」的視覺化新形態

---

## 10. 觀察者待答決策

按優先級排：

1. **Phase 1 prototype 是否現在開做？** — 若 yes，本 session 就可以進 frontmatter（~30-45 min budget per batch discount）
2. **counterfactual publish 機制** — 直接 main branch push，還是先 publication-private branch + 哲宇 final review？
3. **mobile/desktop 雙版本順序** — 先做哪個？（建議 mobile-first 因為流量大頭）
4. **要不要直接通知安溥本人 / 焦仁和** — 第一篇做完之後（建議：不主動通知，但設撤回 SOP）
5. **standalone tree 頁的 URL pattern** — `/people/{slug}/life-tree/` 還是 `/life-trees/{slug}/`?
6. **node 內 perspectives 引用** — 現有文章的 22 perspectives 要不要 link 到對應 node？（建議 yes，是 SSODT 與決策樹的天然合流）

---

## 11. 為什麼這份報告值得做

跟 Taiwan.md 既有產物的 differentiation：

| 既有                              | 局限                   | lifeTree 補了什麼            |
| --------------------------------- | ---------------------- | ---------------------------- |
| **線性編年文章**                  | 抹平選擇的重量         | 把 turning point 結構化      |
| **22 perspectives**（如安溥條目） | 讀者觀點，不是主體決策 | 主體本人的「我為什麼選這個」 |
| **語言分支樹**                    | 翻譯狀態的 spatial map | 人生決策的 temporal map      |
| **arc 描述**（title 副標）        | 一句話，無法展開       | 視覺化展開所有 turning       |
| **時間軸 sidebar**                | 只有 chosen path       | + counterfactual 軸線        |

**最深層的價值**：lifeTree 強迫策展者不只 research「她做了什麼」，而是 research「她**面對的選擇集合**是什麼」——這個 research 質量會反向提升 article body 的 prose 品質。

---

## 12. 下一步

**如果 Phase 1 立刻開做**：

1. 開新 branch `feat/life-tree-anpu`（避免污染 main 直到 review）
2. 在 `knowledge/Music/張懸與安溥.md` frontmatter 加 `lifeTree:` 完整 16 nodes
3. 建 `src/components/LifeTree/` 基本組件
4. preview_start + preview_screenshot mobile/desktop 視覺
5. PR review 後 merge main

**如果暫不開做**：

- 此 report 留 reports/ 等 Phase 1 trigger
- Issue 開「Life Decision Tree feature spec」link 此 report
- LESSONS-INBOX append「lifeTree 概念」待 verification 累積

🧬

---

_作者：Taiwan.md (Semiont) β-r4 session_
_v1.0 | 2026-04-26_
_誕生背景：觀察者「分析安溥的文章，做出 RPG 重大人生分支」一句指令引發。從 §11 polish 5 篇 + LESSONS-INBOX distill v2.0 + HEARTBEAT Beat 3 自我估算偏誤校準的同 session 內擴出來的 Phase 5。本身是 §造橋鋪路 × §策展式非百科式 × §熱帶雨林理論的具體交集產物。_
