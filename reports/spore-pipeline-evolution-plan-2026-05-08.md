# SPORE-PIPELINE 進化計畫 — 從 1334 行 prose dump 到精實閘門生態系

> Session: `2026-05-08-200328-intelligent-khayyam`
> 觸發：哲宇問「Spore pipeline 超級長，有沒有可能重組／最佳化讓 pipeline 精實準確？先完整評估與思考」
> 階段：**評估 + 思考**（未動工，等哲宇 3 題校準後才提具體 PR scope）

---

## 1. 問題 statement

SPORE-PIPELINE.md 從 v1.0（2026-03 初）走到 v2.9（2026-05-03），累積 1334 行。寫一則 200 字 spore 要讀 1334 行 SOP（**比例 7:1**）。

對比 REWRITE-PIPELINE：寫 5000 字深度文章用 1500 行 SOP（比例 0.3:1），spore 是當前生態系中**文檔密度過載最嚴重**的 pipeline。

直觀症狀：

- 哲宇本人主觀感受「超級長」
- AI agent 跑 pipeline 時要不停回頭找「我這次該跑哪些 step」
- 同一條規則同時在 SPORE-PIPELINE Step 3c 跟 SPORE-TEMPLATES.md 出現（重複）
- v1.5+ 累積的 Rule #11-#18 大部分**沒儀器化**，仍是 prose 提醒

---

## 2. 規模盤點

```
docs/factory/
├── SPORE-PIPELINE.md         1334 行    ← v2.9（本檔聚焦）
├── SPORE-TEMPLATES.md         438 行    ← 模板 + 寫作禁令
├── SPORE-LOG.md               284 行    ← 發文紀錄（data，不算 SOP）
├── SPORE-HARVEST-PIPELINE.md  575 行    ← v1.2 收割產線
├── SPORE-BLUEPRINTS/          14 個     ← per-spore artifact
└── SPORE-HARVESTS/             4 個     ← batch harvest log
```

純 SOP 文件層 ~2347 行（PIPELINE + TEMPLATES + HARVEST）。

對比參考（同類 pipeline）：

- REWRITE-PIPELINE.md ~1500 行 / 5000 字產品 = 0.3:1
- MAINTAINER-PIPELINE.md ~1200 行 / 多 PR 處理流程 = 多用途
- SPORE-PIPELINE.md 1334 行 / 200 字產品 = **7:1（離群值）**

---

## 3. 結構診斷 — 6 大問題

### 問題 1：編號膨脹（structural fat）

當前編號層級（**最深三層**）：

```
Step 0  回填
Step 1  選文
Step 2  品質關卡（三層：自動掃描 / EDITORIAL 語境 / 人工判斷）
Step 2.5 事實藍圖
Step 2.6 針對性事實驗證
Step 2.7 紀實 vs 煽情閘
Step 3  萃取 + 寫作
  3a   讀原文萃取
  3b   選模板
  3b.5 Hook Blueprint           ← v2.7 新增
  3c   寫孢子（18 條子規則）    ← 第三深層
  3c.5 事實查核閘
  3c.7 §11 書寫節制閘            ← 跳過 3c.6（編號斷層）
  3d   URL 編碼
  3e   配圖
  3.5  多版本提案
  3.6  混合策略
Step 4  品檢 + 發佈
Step 4.5 發佈後追蹤
  4.5a Platform allocation
  4.5b Hook tier
  4.5c d+0 harvest cadence
  4.5d Re-hook opportunity
  4.5e Harvest 資料流
    4.5e.i   數字格式鐵律       ← 第三深層
    4.5e.ii  validation
    4.5e.iii Dashboard rendering 視覺驗證
    4.5e.iv  文章頁 SporeFootprint 渲染驗證
    4.5e.v   Chrome MCP exact harvest workflow
Step 5  英文版 + 多語 freshness（5a/5b/5c/5d）
Step 6  48h 回填                ← 跟 Step 0 部分重複
```

**根因**：每次踩坑就 append 新編號子層，從未從上方剖析「這個 step 該不該存在 / 該屬於哪個 stage」。三層深編號（3c.5 / 4.5e.iv）是強烈的編號膨脹訊號。

### 問題 2：跟 SPORE-HARVEST-PIPELINE 邊界混亂

文件自己說：「**SPORE 管上線、HARVEST 管收割**」。

但 SPORE-PIPELINE 的 Step 4.5 整段約 300 行做的是收割 SOP：

- 4.5a Platform allocation（Threads vs X 平台差數據）
- 4.5b Hook tier（d+0 6h 擴散預期）
- 4.5c d+0 harvest cadence（D+0/D+1/D+7 timeline）
- 4.5d Re-hook opportunity（views < 500 救援）
- 4.5e Harvest 資料流（雙寫 + 數字格式 + validation + 視覺驗證）

→ 違反 MANIFESTO §**指標 over 複寫**。同一個收割 SOP 兩個 canonical 同時存在，讀者讀完 SPORE-PIPELINE 還要再讀 SPORE-HARVEST-PIPELINE 才知道全貌，且兩處可能漂移。

### 問題 3：Step 3c「18 條寫作規則」= 寫作手冊塞進 process pipeline

Step 3c 第 1-18 條規則本質上是 **arrival writing rules**（如何寫好），不是 **process steps**（如何跑流程）：

```
Rule #1-5  結構（第一句 / 結尾 / 連結 / 鉤子三要素）
Rule #6-7  自檢（鉤子三要素命中 / 念三遍）
Rule #8-12 文體（重複專名 / 引語場景 / 排比過硬 / 時間語境 / 數字密度）
Rule #13   事實鐵三角（算術 / 單位 / 引語逐字）
Rule #14   朋友 tone prime
Rule #15   避免編年體 lead 病
Rule #16   Scene-List-Scene 結構
Rule #17   全形標點
Rule #18   結構性題目用問題入口
```

問題是 **SPORE-TEMPLATES.md 才是 writing rules 的家**。當前兩處已有重複：

- 「念三遍」同時在 SPORE-PIPELINE Rule #7 + SPORE-TEMPLATES「寫完念三遍」
- 「深層 pattern 三板斧」同時在 SPORE-PIPELINE 跟 SPORE-TEMPLATES
- 禁用清單「不是 X 是 Y」「破折號連用」也雙重存在

### 問題 4：Hard Gate / Soft Check / Tool Gate 混雜無 inventory

當前散落 prose 中，沒任何一張表盤點：

| 類別                | 不過 = ?       | 範例                                                       |
| ------------------- | -------------- | ---------------------------------------------------------- |
| **真 Hard gate**    | 不過不發       | Step 2 / 2.6 / 2.7 / 3c.5 / 3c.7                           |
| **Soft self-check** | 信任 AI 自律   | Rule #6/14/15/18 寫完自檢                                  |
| **Tool gate**       | CLI 跑         | article-health.py / make-spore.sh / validate-spore-data.py |
| **Visual verify**   | 觀察者眼睛驗證 | 4.5e.iii dashboard / 4.5e.iv SporeFootprint                |

AI 跑 pipeline 時要從 prose 自己抽出「這次該跑哪些 gate」。沒有 inventory 表 = retrieval cost 永遠在 working memory 上。

### 問題 5：條件式 step 散落 prose（無路由總表）

至少 7 個 sub-section 是條件式（不是線性必跑）：

| Sub-step | 觸發條件                               |
| -------- | -------------------------------------- |
| 2.7      | blueprint 含敏感度 flag（死亡/創傷等） |
| 3b.5     | 結構性題目（政治/外交/制度/經濟）      |
| 3.5      | 互斥 focal point ≥ 2                   |
| 3.6      | 觀察者選 angle 混合                    |
| 4.5c     | 6h views < 500（觸發 decision gate）   |
| 4.5d     | 同上 → 觸發 re-hook                    |
| 5a       | 國際題材（觸發 freshness check）       |

但**沒有路由總表**。AI 跑 pipeline 不停回頭問「這條我這次需要嗎」、「我看完 3b.5 該跳 3c 還是 3.5」。

### 問題 6：「Pipeline 才是閘門」喊了但很多 v 升級沒儀器化

DNA #15「memory 是自律，pipeline 才是閘門」反覆驗證 12+ 次。但實際看 v1.5 → v2.9 的升級 pattern：

```
v 升級 = append 一條規則 + 講教訓 + 換條紅字提醒
```

**沒升級成 article-health.py plugin gate** 的規則：

| Rule | 內容             | 當前狀態       | 該如何 instrument                                |
| ---- | ---------------- | -------------- | ------------------------------------------------ |
| #11  | 時間語境一致     | prose 提醒     | grep `\d+\s*歲那年.*每天` pattern                |
| #14  | 朋友 tone prime  | prose 提醒     | 第一行偵測 lead pattern                          |
| #15  | 編年體 lead 病   | prose 提醒     | regex `^\d{4}\s*年\s*\d+\s*月\s*\d+\s*日`        |
| #16  | Scene-List-Scene | prose 提醒     | 結構偵測（hard，需 LLM-as-judge）                |
| #17  | 全形標點         | bash grep 自檢 | 進 article-health plugin 跟 prose-health 同 gate |

唯一真正成 gate 的是 §11 prose-health（2026-04-23 β 造，整合進 article-health.py）。其他規則退化回 memory layer，pipeline 變成「教訓 archive」而非「gate enforcer」。

對比 §11 是怎麼成功儀器化的：

1. MANIFESTO §11 哲學論述
2. DNA #29 跨層紀律
3. EDITORIAL v5.3 實作清單
4. **article-health.py prose-health plugin（CLI gate）**
5. pre-commit hook（自動跑）
6. SPORE-PIPELINE 3c.7（call site）

→ 哲學 → 規則 → 工具 → hook → 文件，五層都到位才是真閘門。Rule #11/14/15/16/17 大多卡在第一二層。

---

## 4. 重組方向 — 4 條路 + trade-off

### Direction A：拆檔（DNA-first 切割）

把 SPORE-PIPELINE.md 拆成多個 canonical，每個專注一個 axis：

```
docs/factory/spore/
├── SPORE-PIPELINE.md       ~400 行 ← stage 流程，純 process + pointer
│   Step 0-5 線性，每個 step 一句話 + pointer 到 WRITING / VERIFY
├── SPORE-WRITING.md        ~300 行 ← 寫作規則（合併 TEMPLATES + Step 3c）
│   模板 / 18 條 rule / 起手式 / 禁令 / 念三遍 / 三板斧
├── SPORE-VERIFY.md         ~250 行 ← Hard gate inventory（獨立檔）
│   品質三層 / 事實鐵三角 / fact-check gate / 紀實閘 / §11
├── SPORE-HARVEST-PIPELINE  existing ← 把 Step 4.5 整段挖過來
│   d+0/+1/+7 cadence / re-hook / Chrome MCP / 雙寫 / SporeFootprint verify
└── SPORE-BLUEPRINTS/       existing ← per-spore artifact 不動
```

**好處**：

- 寫一則 spore 不用每次 read 1334 行（PIPELINE 400 行 + WRITING 300 行 = 700）
- Hard gate inventory 獨立 audit
- HARVEST 邊界清晰
- 違反 §指標 over 複寫的重複（Step 4.5 vs HARVEST）解了

**壞處**：

- 跨 file pointer 多了 → BECOME 載入時多 grep
- 4 file 的 commit history 變散
- Cross-ref 破壞（但 SPORE-PIPELINE 不在 BECOME 12 必讀器官中，影響範圍可控）

### Direction B：5 stage 線性重編號（替代 A 的局部 fix）

```
舊（10+ step 含三層子層）→ 新（5 大 stage 線性）

STAGE 0: PRE-FLIGHT  ← 0 + 1（回填 + 選文）
STAGE 1: VERIFY      ← 2 + 2.5 + 2.6 + 2.7（品質+事實+倫理 三閘合一）
STAGE 2: WRITE       ← 3 + 3.5 + 3.6（萃取+模板+Hook+18 條+多版本）
STAGE 3: SHIP        ← 4（品檢+發佈+UTM+sporeLinks 寫回）
STAGE 4: HARVEST     ← 整段移到 HARVEST-PIPELINE
STAGE 5: TRANSLATE   ← 5（多語 freshness）
```

**好處**：5 stage 在認知 7±2 範圍內，每個 stage 有清晰 verb（PRE-FLIGHT/VERIFY/WRITE/SHIP/HARVEST/TRANSLATE）

**壞處**：v 編號改了會 break docs/semiont/MEMORY/DNA/diary 的歷史 cross-ref pointer（過去 SPORE 教訓寫「Step 3c 第 13 條」會 dead link）

→ 不推薦獨立做。如果 Direction A 拆分了，B 的好處自動實現（每個 sub-file 內部 5±2 stage）。

### Direction C：Hard Gate Inventory 表（最低成本，treat 症狀）

不動結構，pipeline 開頭加一張 audit 表：

```markdown
## 🚦 Hard Gate Inventory（一張表 audit 全 pipeline）

| Gate           | 觸發 step | 觸發條件        | 工具                        | 不過 = ?     |
| -------------- | --------- | --------------- | --------------------------- | ------------ |
| 品質三層       | Step 2    | 所有 spore      | validate / article-health   | 回爐 rewrite |
| 事實藍圖       | Step 2.5  | 所有 spore      | manual blueprint            | 不能寫 prose |
| 針對性驗證     | Step 2.6  | bullet 標需驗證 | WebSearch ×3 來源           | 移除 bullet  |
| 紀實/煽情閘    | Step 2.7  | 敏感度 flag     | 四問自檢                    | 重寫或棄用   |
| Hook Blueprint | Step 3b.5 | 結構性題目      | 四格自填                    | 不能進寫作   |
| 18 條寫作規則  | Step 3c   | 所有 spore      | mental check                | 修正         |
| 事實查核表     | Step 3c.5 | 所有 spore      | 7 類 claim audit            | 不放 prose   |
| §11 書寫節制   | Step 3c.7 | 所有 spore      | article-health prose-health | 改寫         |
| URL encode     | Step 3d   | 所有 spore      | python urllib               | 重 encode    |
| 品檢清單       | Step 4    | 所有 spore      | 12 項 manual                | 修補         |
| 發布後 6h gate | Step 4.5c | views < 500     | Chrome MCP                  | 觸發 re-hook |
| 多語 freshness | Step 5a   | 國際題材        | knowledge/en/ check         | 先更 SSOT    |
```

**好處**：

- 半天可做、low-risk
- AI 跑 pipeline 一眼看完整圖
- 不動歷史 cross-ref，反向相容

**壞處**：

- 治療症狀不解 root cause（編號膨脹依然在）
- 1334 行還是 1334 行 + table（甚至更長）

→ **適合作為先手 polish**，但長期解不了 friction。

### Direction D：規則升級成 article-health.py plugin（DNA #15 真正解）

把 v1.5+ 的 prose 規則從「提醒 + 信任 AI 自律」升級為 plugin gate：

```python
# scripts/tools/plugins/spore_writing.py
class SporeWritingPlugin:
    def check_chronicle_lead(text):  # Rule #15 編年體 lead 病
        if re.match(r'^\s*\d{4}\s*年\s*\d+\s*月\s*\d+\s*日', text):
            return HARD("編年體 lead 病：第一句不該是日期開頭")

    def check_full_width_punct(text):  # Rule #17 全形標點
        # 中文段落含半形 , . : ( ) ? ! 但排除 URL / 純英文句
        ...
        if violations: return HARD(...)

    def check_quote_inversion(text):  # Rule #9 引語倒裝
        if re.search(r'「[^」]{5,30}」.*[他她].*說', text):
            return WARN("引語倒裝沒場景，改 '他在 [場景] 說：「...」'")

    def check_repeated_name(text):  # Rule #8 同名連用 ≥3
        # 連續三句同一專名 → 紅燈
        ...

    def check_friend_tone_prefix(text):  # Rule #14 朋友 tone prime
        first_line = text.split('\n')[0]
        if matches_news_lead_pattern(first_line) and not has_friend_prefix(first_line):
            return WARN("第一行像新聞 lead，建議加 '你知道嗎？' prefix")
```

Pipeline call site 改成：

```bash
# Step 3c.5（取代 Step 3c 18 條 mental check）
python3 scripts/tools/article-health.py docs/factory/SPORE-BLUEPRINTS/<slug>-<n>.md \
  --check=spore-writing
```

任一 HARD = 不放行 prose。

**好處**：

- DNA #15 真正解（不是嘴上說「pipeline 才是閘門」）
- §11 plugin 已有成功 precedent（2026-04-23 β）
- Pipeline prose 可大幅瘦身（18 條 → pointer 到 plugin docs）
- 未來新 rule 直接加 plugin，不再 prose 提醒

**壞處**：

- Plugin 開發成本（每條規則 ~30-60 min coding + 測試）
- 部分規則難純 regex 偵測（如 Rule #16 Scene-List-Scene 結構需 LLM-as-judge）
- 開發過程可能發現規則本身定義模糊（例：怎麼定義「編年體 lead」邊界？是 4 數字 + 年月日格式，還是只要日期開頭？）

→ **長期 leverage 最高**，但不是 quick win。

---

## 5. 推薦執行波次：C → A → D

按優先序（先低風險高收益、後結構性升級）：

| 波次  | 方向 | 工作量      | 帶來什麼                  | 風險                             |
| ----- | ---- | ----------- | ------------------------- | -------------------------------- |
| **1** | C    | 半天        | Gate inventory 表立刻能用 | 極低（純 append）                |
| **2** | A    | 2-3 session | 1334 → 400 行 + 邊界清    | 中（cross-ref 破壞，但可控）     |
| **3** | D    | 5+ session  | 5 條 rule 真正成 gate     | 高（plugin 開發 + 規則邊界調整） |

**不推薦 B 獨立做**（A 拆分後 B 自動受益，每個 sub-file 內部 5±2 stage）。

### 波次 1（Direction C）執行細節

範圍：

- SPORE-PIPELINE.md 開頭加「🚦 Hard Gate Inventory」表（~30 行）
- 加「📍 條件式 step 路由表」(~20 行)
- 加「⚠️ 你最常忘的 Top 5 step」（從 SPORE-LOG / LESSONS-INBOX 抽 → 前置 prose 段）

驗收：

- AI session 啟動 spore work 時 read inventory 表 → 知道完整 gate 圖
- 條件式 step 路由表降低「我這次該跳過嗎」決策成本

### 波次 2（Direction A）執行細節

範圍：

1. 建 `docs/factory/spore/` 子資料夾
2. 拆出 `SPORE-WRITING.md`（合併 TEMPLATES + Step 3c 18 條 + 三板斧）
3. 拆出 `SPORE-VERIFY.md`（Hard gate inventory canonical 化）
4. 把 Step 4.5 整段移到 `SPORE-HARVEST-PIPELINE.md`
5. 原 SPORE-PIPELINE.md 瘦身成 ~400 行 stage 流程 + pointer
6. 更新 DNA / BECOME / HEARTBEAT 中所有 SPORE-PIPELINE pointer

驗收：

- 寫 spore 主路徑：read PIPELINE (400) + read WRITING (300) = 700 行（原 1334 行的 52%）
- HARVEST 跑收割不需 read SPORE-PIPELINE
- Hard gate audit 直接 read VERIFY 一份

### 波次 3（Direction D）執行細節

範圍（按優先度）：

1. **Rule #17 全形標點** — 純 regex，最容易，先做
2. **Rule #15 編年體 lead** — regex `^\d{4}\s*年.*\d+\s*月`
3. **Rule #9 引語倒裝** — regex 偵測「『...』他/她說」
4. **Rule #8 同名連用 ≥3** — token 比對，需斷句
5. **Rule #14 朋友 tone prime** — 新聞 lead pattern 偵測 + prefix 白名單
6. **Rule #16 Scene-List-Scene** — 結構偵測，需 LLM-as-judge（可能轉 sub-agent gate 而非 plugin）

每條獨立加進 article-health.py plugins/spore_writing.py，新增 `--check=spore-writing` flag。

驗收：

- `article-health.py spore-draft.md --check=spore-writing` HARD=0 → 18 條規則中至少 5 條自動 enforce
- Pipeline Step 3c 從 18 條 prose 規則瘦身為 pointer + 提醒「跑 spore-writing plugin」
- 新 spore 撞 Rule 時 fail 在 plugin gate（不依賴 AI 自律記得 Rule #17）

---

## 6. 給哲宇的 3 題校準（用數據點 derisk 重構方向）

不抽象決定方向，先用 **真實 friction** 校準診斷：

### Q1：你寫 spore 時最常跳過 / 忘記的 step 是哪個？

可能答案 → 對應方向：

- 「Step 0 回填」→ Direction C（inventory 表前置 reminder 能解）
- 「Step 3c 18 條我每次只記得 5-6 條」→ Direction A WRITING 拆檔 + Direction D plugin
- 「Step 4.5 不知道是 SPORE 還是 HARVEST」→ Direction A 拆檔最直接
- 「Step 5a 多語 freshness 我幾乎沒做」→ 該 step 是不是該降級到 conditional / soft gate？

### Q2：SPORE-LOG / LESSONS-INBOX 過去三個月 ~20 則 spore，最常 ship 後撤回 / 校正的是哪個 step 漏？

這是 **root cause data**，比抽象重組更值得 instrument。

歷史 trace 候選：

- 高鐵 s35（2026-04-19）→ 觸發 3c.5 fact-check gate 誕生（時序錯誤）
- 草東 #33（2026-04-18）→ 觸發 2.6 讀者級驗證 + 倫理閘 v2 校準（貝斯手名字錯）
- 李洋 #28（2026-04-15）→ 觸發 3c 鐵三角自檢（算術錯 + 杜撰引語）
- 邦交國 #51/#52（2026-04-29）→ 觸發 3b.5 Hook Blueprint（briefing 病）

→ 最常漏的 step **本身**就是哪個方向 leverage 最高的訊號。

### Q3：Step 4.5（~300 行收割 SOP）對你來說感覺是「SPORE 的尾巴」還是「HARVEST 的開場」？

你的直覺決定 boundary 該怎麼劃：

- 「SPORE 尾巴」→ 留在 PIPELINE，但 4.5e.i-v 子層拆解
- 「HARVEST 開場」→ 整段移走（Direction A 推薦）
- 「兩個都是」→ 該寫 cross-pipeline marker 標明 handoff point

---

## 7. 寫這份 report 本身的 leverage 分析

按 MANIFESTO §造橋鋪路四問：

1. **「這能不能變成系統？」** — 重構 pipeline 後，未來新增 rule 走 plugin 而非 prose append → 是
2. **「下次心跳能不能自動帶這個能力？」** — Direction D plugin 是 instrumented gate，不依賴 AI 自律 → 是
3. **「走過的泥巴路鋪成高速公路？」** — 1334 行 read 成本是泥巴路，拆檔 + plugin 是高速公路 → 是
4. **「新細胞天生健康 > 回頭修舊細胞？」** — 重構後新 spore 跑新流程，舊 spore artifact（BLUEPRINTS / HARVESTS）不動 → 是

四題全 yes，重構符合 §造橋鋪路精神。

但有 trade-off：

- **保留歷史證據鏈**（per MANIFESTO §時間是結構修補協議）：v1.0 → v2.9 累積的教訓不該抹除。重構應該走「降級到 historical 段落」而非「刪除」
- **DNA #15 第 N 次驗證**：「memory 是自律，pipeline 才是閘門」 — 重構不該讓 pipeline 退化為 archive，要強化 gate 能力
- **指標 over 複寫**：拆檔同時要建立清楚 pointer 網絡，避免「拆完 4 個 file 互相又開始漂移」

---

## 8. Out-of-scope（本 plan 不解）

- **SPORE-TEMPLATES.md 跟 SPORE-PIPELINE 寫作規則重複**：這是 Direction A 副產品，但需獨立 audit 兩邊定義是否一致
- **SPORE-LOG.md schema 升級**：當前 markdown table 跟 dashboard JSON 雙寫機制（per Step 4.5e）的 silent drift 風險（已有 v2.8 validate-spore-data.py 部分解）
- **SPORE-BLUEPRINTS/ 跟 SPORE-HARVESTS/ 命名統一**：blueprint 用 `<n>-<slug>.md`，harvest 用 `batch-<date>-<n>-spores.md`，沒一致格式
- **跟 REWRITE-PIPELINE 的指標 over 複寫**：例 Stage 3.5 hallucination audit 跟 SPORE Step 3c.5 fact-check gate 高度重疊，可能整合成跨 pipeline plugin

---

## 9. 後續決策

哲宇回答 Q1-Q3 後，可以收斂到 **單一 PR scope**：

候選 PR scope：

- **PR-A（半天）**：純 Direction C inventory 表
- **PR-B（一個 session）**：Direction C + 觀察者 Q1-Q3 答案揭示的 top 1 friction fix
- **PR-C（2-3 session）**：Direction A 完整拆檔 + Direction C inventory canonical 化
- **PR-D（roadmap）**：Direction D 規則 plugin 升級分 5 條 rule 各自獨立 PR

預設推薦：**PR-B**（先低風險，但不只 inventory 表，根據 Q1-Q3 答案處理最大 friction）。

---

## 附錄 A：可能反駁的視角

寫 report 該誠實列出可能的反方論述：

1. **「1334 行不是 bug，是 spore 真的需要這麼細的 SOP」**
   反駁：但 spore 是 200 字產品，比例 7:1 在所有 pipeline 中是離群值。即使 spore 真的複雜，當前結構也可以拆得更清晰（Direction A）

2. **「重構會破壞累積的證據鏈」**
   反駁：per MANIFESTO §時間是結構修補協議 — 歷史不刪除，搬到 historical/ 段落保留。重構不等於抹除

3. **「Plugin 開發成本太高，不如保留 prose 提醒就好」**
   反駁：DNA #15 反覆驗證 12+ 次「pipeline 才是閘門」 — 不儀器化的後果是教訓不停重複。短期成本 vs 長期 leverage 對比清楚

4. **「Direction A 拆 4 個檔案會讓 BECOME 載入更累」**
   反駁：SPORE-PIPELINE 不在 BECOME 12 必讀器官中，只在「寫 spore」場景被 read。拆檔反而讓主路徑更輕（700 行 vs 1334 行）

5. **「SPORE-PIPELINE 是 spore-pipeline 的問題，不是整個系統的問題，不該過度設計」**
   反駁：同樣的 prose-vs-instrument 張力在 REWRITE-PIPELINE 也有跡象（Stage 3.5 hallucination 也是 prose 提醒）。SPORE 是先驗的 worst case，解了之後 pattern 可移植

---

## 附錄 B：跟其他 canonical 的對齊檢查

本計畫如何符合既有認知層原則：

| 原則                            | 本計畫如何遵守                                                  |
| ------------------------------- | --------------------------------------------------------------- |
| MANIFESTO §造橋鋪路             | Direction D plugin = 系統升級 > 手動苦工                        |
| MANIFESTO §指標 over 複寫       | Direction A 拆檔解決 SPORE / HARVEST 重複                       |
| MANIFESTO §時間是結構           | 歷史 v1.0-v2.9 教訓搬 historical/ 不刪除                        |
| DNA #15 反覆浮現要儀器化        | Direction D 是這條的具體實踐（5 條 rule 從 prose 升 plugin）    |
| DNA #50 pipeline auto-detection | 本 plan 不破壞 task → pipeline 對應表，反而簡化（拆檔後更清楚） |

---

_v1.0 | 2026-05-08 session intelligent-khayyam — 觸發：哲宇 `/twmd-become` 後問「Spore pipeline 超級長，有沒有可能重組／最佳化讓 pipeline 精實準確？先完整評估與思考」_

_作者：Taiwan.md（Semiont 自我評估認知層 SOP 的元思考）_

_狀態：**未實作 plan**。等哲宇 Q1-Q3 答案後收斂單一 PR scope_

🧬
