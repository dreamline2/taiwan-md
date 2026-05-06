# zhtw-mcp 整合評估報告 — 完整詞條吸收 + Taiwan.md 交叉比對

> **任務觸發**：哲宇 2026-05-05 13:50+ 透過未實作的 `/twmd-research` 觸發評估與整合提案。
>
> **核心 finding**：zhtw-mcp 有 Taiwan.md 缺的 **ai_filler / translationese / MoE punctuation/variant 引擎**；Taiwan.md 有 zhtw-mcp 缺的 **2336 詞條完整 etymology metadata + 七型分歧分類**。雙方互補，整合 high-leverage。
>
> **推薦執行路徑**：先 Option A（cherry-pick 1411+908 雙向缺口補洞）+ Option D（採 MoE punctuation/variant 為新 plugin），暫緩 MCP server full bind（Option B 待後續）。

---

## 一、zhtw-mcp 專案概述

| 維度        | 數值                                                                    |
| ----------- | ----------------------------------------------------------------------- |
| Repo        | [sysprog21/zhtw-mcp](https://github.com/sysprog21/zhtw-mcp)             |
| Created     | 2026-03-10                                                              |
| Last update | 2026-05-05 14:25 (active)                                               |
| Stars       | 306                                                                     |
| License     | MIT                                                                     |
| 語言        | Rust + browser extension (JS/WASM) + MCP server                         |
| 拓樸        | CLI binary + MCP server (stdio JSON-RPC) + Chrome extension + Cargo lib |

### Mission

> A linguistic linter for Traditional Chinese (zh-TW) that enforces Taiwan Ministry of Education (MoE) standards on vocabulary, punctuation, and character shapes.

三個官方標準：

1. **重訂標點符號手冊（MoE punctuation）** — `,` → `，`、`""` → `「」`
2. **國字標準字體（MoE variant）** — 裏→裡、着→著、麪→麵
3. **OpenCC TWPhrases/TWVariants** + 自製跨海峽詞彙 — 軟件→軟體、內存→記憶體

### Ruleset 拓樸（assets/ruleset.json，1804 spelling + 15 case）

| Category             |    Count | 用途                                  |
| -------------------- | -------: | ------------------------------------- |
| `cross_strait`       | **1621** | 主力跨海峽詞彙差異                    |
| `ai_filler`          |   **66** | AI filler phrase 偵測 ⭐ Taiwan.md 缺 |
| `variant`            |   **48** | MoE 國字標準字體（裏/裡 等）          |
| `translationese`     |   **45** | 翻譯腔偵測 ⭐ Taiwan.md 缺            |
| `confusable`         |       18 | 易混淆詞（字體/字型）                 |
| `political_coloring` |        5 | 政治用語（祖國/內地）                 |
| `typo`               |        1 | 錯字（乞業→企業）                     |
| `case_rules`         |       15 | JavaScript/GitHub/macOS 大小寫        |

### Profiles + Flags（多態檢查模式）

| Profile  | 用途                                            |
| -------- | ----------------------------------------------- |
| `base`   | 跨海峽詞彙 + 標點 + casing + 政治用語           |
| `strict` | 全 MoE：variant char + grammar + 全 punctuation |

| Flag        | 用途                                                           |
| ----------- | -------------------------------------------------------------- |
| `relaxed`   | UI 字串：disable colon/dunhao/grammar                          |
| `detect_ai` | AI 寫作評審：filler / 安全詞 / passive voice / density pattern |

### MCP Server 介面（docs/mcp.md）

- 1 tool: `zhtw` (lint / fix / gate unified)
- 2 resources / 3 prompts
- Sampling-based disambiguation（server 反向問 LLM 處理 ambiguous case）
- Output modes: full / compact / tabular / summary
- Political stance: roc_centric / neutral / international
- Per-call `ignore_terms` suppression
- Document-level scan metadata: `coverage` / `oral_density` / `quality_flags`（spaced_acronyms / stutter_detected / asr_artifacts）

---

## 二、Taiwan.md 既有 terminology infrastructure

### 資產規模

| 維度                     |                                                                                                                  數值 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------: |
| **YAML 詞條檔**          |                                                                          **2336 entries** (`data/terminology/*.yaml`) |
| Per-entry metadata       |                                             id / category / fork_type / etymology / usage / sources / added / updated |
| 分歧類型                 |        **7 種**（A 日語遺產 / B 1949 分流 / C 網路時代 / D 台客語底層 / E 分歧中 / F 語感 / semantic / orthographic） |
| **Active detection.tsv** |                                                                                **36 entries**（A=29 紅燈 + B=7 黃燈） |
| Active rate              |                                                                                               36 / 2336 = **1.5%** ⚠️ |
| False-positive 校正      |                                                              `china-term-false-positives.tsv`（博客來 → 不誤判 博客） |
| Plugin                   | [`scripts/tools/lib/article_health/checks/terminology.py`](../scripts/tools/lib/article_health/checks/terminology.py) |
| Source 引用              |                                                                   國家教育研究院雙語詞彙 + 《大陸用語檢索手冊》(1997) |
| Hook                     |                                                                            pre-commit + article-health.py SSOT plugin |

### 詞條結構範例（軟體.yaml）

```yaml
id: software
category: tech
fork_type: B # 1949 分流
display: { taiwan: 軟體, china: 軟件 }
english: software
etymology:
  origin: 英語 software 的中文翻譯
  taiwan_path: 「體」系列：軟體、硬體、韌體
  china_path: 「件」系列：軟件、硬件
  fork_point: ~1980s
  fork_cause: 兩岸分別建立電腦術語體系
detection: { severity: A } # ⭐ opt-in
sources: [國家教育研究院雙語詞彙, 《大陸用語檢索手冊》(1997)]
```

### 設計哲學差異

Taiwan.md 是**博物館式詞條保存系統**（每條都有 etymology + fork_cause + sources）。
zhtw-mcp 是**工程化高 recall linter**（每條極簡：from / to / type / context）。

---

## 三、量化交叉比對

### 詞條集合運算

| 集合                      |              數量 | 註                              |
| ------------------------- | ----------------: | ------------------------------- |
| Taiwan.md `china:` 唯一詞 |              2307 | 從 2336 YAML 抽取               |
| zhtw-mcp `from` 唯一詞    |              1804 | 全部 spelling_rules             |
| **兩邊都有**              | **896** (overlap) | 共識 — 已驗證 cross-strait pair |
| **zhtw-mcp only**         |           **908** | Taiwan.md 缺口                  |
| **Taiwan.md only**        |          **1411** | zhtw-mcp 缺口                   |
| **聯集（universe）**      |          **3215** | 雙方合併後完整跨海峽宇宙        |

### Recall gap 警報

| 指標                     | Taiwan.md |       zhtw-mcp |
| ------------------------ | --------: | -------------: |
| 總詞條庫                 |      2336 |           1804 |
| **Active 偵測**          |    **36** |       **1804** |
| **Active recall ratio**  |  **1.5%** |       **100%** |
| Active recall **倍數差** |         — | **50× higher** |

⚠️ **Taiwan.md 結構性 silent risk**：2305 個 YAML 詞條有完整 metadata 但**沒打開 detection 區塊**，等於「庫存 2336，貨架上只有 36」。`Issue #616` 設計成 opt-in 是為了避免 false positive（同詞語感差異），但 1.5% active rate 對 PRC 用語滲透 baseline 太弱。

### Sample mismatch

**zhtw-mcp 有 / Taiwan.md 缺**（高優先補洞）：

```
32 位架構, 64 位架構, CPU核心, Google工具條, PN結, ...
```

→ 多為 IT 技術 specific（zhtw-mcp 從 OpenCC + sysprog21 的 C/Rust/CS 領域知識補的）。Taiwan.md tech 詞條雖多但缺這些 compound term。

**Taiwan.md 有 / zhtw-mcp 缺**（雙向 enrichment 候選）：

```
便當, 計程車, 三溫暖, 一筆勾銷, 三分鐘熱度, 三觀, ...
```

→ 多為**文化詞 + 日常用語**（zhtw-mcp 偏 IT，Taiwan.md 涵蓋廣泛文化光譜）。

---

## 四、互補維度分析

| 維度                                 | Taiwan.md                                | zhtw-mcp                             |
| ------------------------------------ | ---------------------------------------- | ------------------------------------ |
| **詞庫規模（總）**                   | 2336 ⭐ 大                               | 1804                                 |
| **Active recall**                    | 36 ❌ 弱                                 | 1804 ⭐ 強                           |
| **Etymology / sources**              | ✅ 豐富                                  | ❌ 無                                |
| **Fork type 分類**                   | 7 種 ⭐ 細                               | 8 種（單一 cross_strait dominant）   |
| **MoE punctuation engine**           | ❌                                       | ✅ context-sensitive                 |
| **MoE variant chars (裏→裡)**        | ⚠️ partial in YAML                       | ✅ comprehensive 48 rules            |
| **AI filler 偵測**                   | partial（MANIFESTO §11 對位句 / 破折號） | ✅ **66 rules `ai_filler`**          |
| **Translationese 偵測**              | ❌                                       | ✅ **45 rules `translationese`**     |
| **政治用語 (祖國/內地)**             | ⚠️ 散在 YAML                             | ✅ 5 rules canonical                 |
| **Casing rules (JavaScript/GitHub)** | ❌                                       | ✅ 15 rules + word boundary          |
| **MCP server**                       | ❌                                       | ✅ JSON-RPC stdio + Sampling         |
| **Browser extension**                | ❌                                       | ✅ Chrome WASM                       |
| **Pre-commit hook**                  | ✅ article-health                        | ⚠️ via CLI subprocess                |
| **False-positive 校正機制**          | ✅ TSV pattern                           | ✅ 假朋友 disabled rules             |
| **Profiles**                         | 單一（A/B 二級）                         | 4 種 (base/strict/relaxed/detect_ai) |

---

## 五、五個整合 option

### Option A：詞條雙向 cherry-pick（短期高 leverage）

**動作**：

1. 908 個 zhtw-mcp-only 詞 → 補進 Taiwan.md `data/terminology/*.yaml` 為新 entry，加 `detection: { severity: A }` 直接 active
2. 用 zhtw-mcp ruleset.json 的 cross_strait classification 作為 reference，把現有 2305 個沒 detection block 的 Taiwan.md YAML，**自動補 detection block**（從 zhtw-mcp 找對應 from/to pair → 推 severity A/B）
3. 對 1411 個 Taiwan.md-only 詞 → upstream PR 回饋 zhtw-mcp（Taiwan.md 的文化詞庫對 zhtw-mcp 是 enrichment）

**工作量級**：M (4-10 檔案 / 100-500 行 / session 內 5-10 分鐘可造出 sync 工具，再幾小時跑 cherry-pick)
**風險**：低 — 純資料 merge，無架構變動
**獲益**：active recall 從 36 → 1500+（**40× 增幅**）
**副作用**：可能短期 false positive 暴漲，需要 false-positives.tsv 跟著擴張

### Option B：MCP server bind 為次層 lint（中期高 leverage）

**動作**：

1. `cargo install` zhtw-mcp 為 binary
2. 加進 Taiwan.md `.claude/settings.json` MCP servers 清單
3. article-health terminology plugin 改寫，可 chain call zhtw-mcp tool 做 second-pass strict mode 檢查
4. pre-commit hook 增 zhtw-mcp linter 步驟（在 article-health 之後）
5. 寫一個 `/twmd-zhtw-lint` skill 包裝 MCP tool 供觀察者呼叫

**工作量級**：L (10-30 檔案 / session 內 20-40 分鐘)
**風險**：中 — Rust binary 跨平台、cargo 依賴、配置漂移風險
**獲益**：full 1804 rules + MoE punctuation/variant 即時生效；觀察者寫文章時 inline lint
**副作用**：增加 toolchain 依賴；需要文檔化新 hook 行為

### Option C：Vendoring zhtw-mcp ruleset.json 為 upstream sync source（中風險中收益）

**動作**：

1. 寫 `scripts/tools/sync-zhtw-mcp-ruleset.sh` 定期 `gh api repos/sysprog21/zhtw-mcp/contents/assets/ruleset.json` fetch 最新版
2. terminology.py extend，可同時讀 Taiwan.md detection.tsv 跟 zhtw-mcp ruleset
3. 衝突解決：Taiwan.md detection.tsv 優先（local override），zhtw-mcp 為 fallback baseline

**工作量級**：M
**風險**：中 — zhtw-mcp 哲學跟 Taiwan.md 不完全一致（zhtw-mcp roc_centric flag vs Taiwan.md SSODT），可能引入過嚴 flagging
**獲益**：upstream 維護工作大部分 outsource 給 zhtw-mcp 社群（306 stars 動量）
**副作用**：drift 風險 — sysprog21 可能改 schema

### Option D：採 MoE punctuation/variant 為新 plugin（短期針對性補洞）

**動作**：

1. 寫 `scripts/tools/lib/article_health/checks/moe-standards.py` plugin
2. 內部 subprocess 呼叫 zhtw-mcp binary（profile=strict）只跑 punctuation + variant 兩 category
3. 排除 cross_strait（Taiwan.md 自己有）+ ai_filler/translationese（後續另案）
4. integrate 進 article-health.py SSOT，加 `--check=moe-standards` flag

**工作量級**：S-M
**風險**：低 — 只補 Taiwan.md 沒有的 MoE 字形 + 標點層
**獲益**：knowledge/ 內可能有 100+ 篇舊文有半形標點 / 異體字未發現；新文章自動防護
**副作用**：subprocess 跨 toolchain；需文檔化 install 流程

### Option E：吸收 ai_filler + translationese 進 prose-health plugin（長期戰略）

**動作**：

1. 把 zhtw-mcp 的 66 ai_filler + 45 translationese rules **手動 review + cherry-pick** 進 Taiwan.md 既有 `prose-health` plugin（MANIFESTO §11 同源）
2. 為每條補 Taiwan.md context（哪些 ai_filler 跟 §11 對位句重疊、哪些是新規則）
3. 把 prose-health 從 16 維擴 16+30 維

**工作量級**：M-L
**風險**：低-中 — review 成本但無架構變動
**獲益**：MANIFESTO §11 從 9 變體 + 破折號密度 → 包含 AI filler + translationese 全光譜偵測
**副作用**：prose-health 報告變長，需要 severity tier 調整

---

## 六、推薦執行路徑

### 立即執行（本週內，high confidence）

**1. Option A 優先 — 雙向詞條 cherry-pick**

理由：

- 解決 Taiwan.md 1.5% active rate 結構性弱點
- 純資料 merge 無架構風險
- 直接對應 §造橋鋪路 — 走過的路鋪成高速公路

具體步驟：

- (a) 寫 `scripts/tools/sync-zhtw-mcp-detection.py` 工具：
  - Read zhtw-mcp ruleset.json → for each cross_strait rule with `from/to` pair
  - Find matching Taiwan.md YAML entry (by `china: <from>`)
  - 自動 patch 該 YAML 加 `detection: { severity: A }`（with safety: only patch if `taiwan: <to>` 也 match）
  - For zhtw-mcp `from` not in Taiwan.md YAML → 列 candidate list 給觀察者人工 review 後新建 YAML
- (b) Cherry-pick 1411 Taiwan.md-only 詞回饋 zhtw-mcp upstream PR（長期 community contribution）

**2. Option D 並行 — MoE punctuation/variant plugin**

理由：

- 跟 Option A 正交（一個是詞，一個是標點/字形）
- 補 Taiwan.md 完全沒有的維度
- subprocess 呼叫 binary 的工程量小

### 中期（兩週內 / 觀察者觸發）

**3. Option E — 吸收 ai_filler + translationese 進 prose-health**

理由：

- 跟 MANIFESTO §11 §對位句型 + 破折號連用 同源
- 補 §11 三條紀律（對位句 / 破折號 / AI filler / translationese）為四條
- DNA #29 prose-health plugin 自然延伸

### 後期（月度 / 哲宇拍板）

**4. Option B — MCP server full bind**（需評估 Cargo 依賴接受度）
**5. Option C — Vendoring 自動 sync**（需哲學一致性 alignment 對話）

---

## 七、風險與開放問題

### 哲學 alignment 待對話

| 議題                        | zhtw-mcp 立場                             | Taiwan.md 立場                           | 整合衝突？                            |
| --------------------------- | ----------------------------------------- | ---------------------------------------- | ------------------------------------- |
| 政治用語                    | `political_stance: roc_centric` flag 預設 | MANIFESTO §土壤層：台灣島史觀 + 主權獨立 | 對齊（雙方都認同 Taiwan-perspective） |
| 「文件」處理                | 假朋友 — disabled 避免誤判                | 視 fork_type 分類處理                    | 對齊                                  |
| 性別中立（父節點→親代節點） | 主動 flag                                 | 未專門關注                               | zhtw-mcp 引領，Taiwan.md 可借鏡       |
| 「臺/台」                   | strict profile only                       | YAML semantic 級分類                     | 對齊（雙方都認 strict 模式必修）      |
| MoE 字形（裏→裡）           | variant rules canonical                   | 散在 YAML orthographic 類別              | zhtw-mcp 更系統化                     |

### 工程風險

1. **False positive 暴漲**：1.5% → 50%+ active rate 後，舊文章可能爆出大量 violations。需先 dry-run 看影響範圍 + 漸進式 enable
2. **Schema drift**：Option C 若採 vendoring，zhtw-mcp 後續 schema 改可能 break Taiwan.md plugin
3. **Cross-toolchain 依賴**：Option B/D 需要 `cargo install zhtw-mcp` 或 release binary distro，新 contributor onboarding 多一步
4. **語感誤判**：Taiwan.md 的 fork_type=F「同詞不同語感」（領導 / 水平）類，zhtw-mcp 可能不分類就 flag → 需要 false-positives.tsv 補強

### 待哲宇拍板的決策

1. Option A 自動 patch detection block 的 severity policy：默認 A（紅燈）還是 B（黃燈）？
2. Option D MoE strict 模式對既有舊文是否一次性 audit + ship 修補（M-L 規模）還是新文 only？
3. 1411 Taiwan.md-only 詞要不要主動 upstream PR 給 zhtw-mcp（哲學貢獻 + 物種繁殖 MANIFESTO §3）？
4. `/twmd-zhtw-lint` skill 是否新增（trigger zhtw-mcp 直接呼叫）？

---

## 八、Action Items 工作量級

| #   | Action                                                           | Option | 量級 | 拍板需要                      |
| --- | ---------------------------------------------------------------- | ------ | ---- | ----------------------------- |
| 1   | 寫 sync-zhtw-mcp-detection.py 工具                               | A      | M    | 可自主                        |
| 2   | 對現有 2305 YAML 自動 patch detection block (with zhtw-mcp 比對) | A      | M    | severity policy               |
| 3   | Cherry-pick 908 zhtw-mcp-only 詞建新 YAML                        | A      | L    | YAML batch policy             |
| 4   | Upstream PR 1411 Taiwan.md-only 詞回 zhtw-mcp                    | A      | L    | 哲宇拍板 + community 對外溝通 |
| 5   | MoE punctuation/variant plugin (subprocess wrapper)              | D      | M    | toolchain 依賴                |
| 6   | ai_filler + translationese 進 prose-health                       | E      | M-L  | review schedule               |
| 7   | MCP server bind 為 .claude/settings.json                         | B      | L    | toolchain + observer testing  |
| 8   | `/twmd-zhtw-lint` skill 薄殼                                     | B/D    | S    | option 確認後                 |
| 9   | sync-zhtw-mcp-ruleset.sh 自動 fetch                              | C      | M    | 哲學 alignment                |

**推薦先做：1+2+5（短期最高 leverage，低風險，工作量級加總約 L = 30-50 min）**

---

## 九、引用 / 連結

- **zhtw-mcp**: [github.com/sysprog21/zhtw-mcp](https://github.com/sysprog21/zhtw-mcp) (MIT, 306★)
- **MoE Punctuation Standard**: [language.moe.gov.tw/001/upload/files/site_content/m0001/hau/c2.htm](https://language.moe.gov.tw/001/upload/files/site_content/m0001/hau/c2.htm)
- **MoE 國字標準字體**: [language.moe.gov.tw/001/Upload/files/SITE_CONTENT/M0001/STD/F4.HTML](https://language.moe.gov.tw/001/Upload/files/SITE_CONTENT/M0001/STD/F4.HTML)
- **OpenCC TWPhrases**: [github.com/BYVoid/OpenCC](https://github.com/BYVoid/OpenCC)
- **FAccT 2025 zh-CN bias study**: [arxiv.org/abs/2505.22645](https://arxiv.org/abs/2505.22645)

### Taiwan.md 內 references

- [`docs/editorial/TERMINOLOGY.md`](../docs/editorial/TERMINOLOGY.md)
- [`docs/editorial/EDITORIAL.md`](../docs/editorial/EDITORIAL.md) §兩岸用語
- [`scripts/tools/lib/article_health/checks/terminology.py`](../scripts/tools/lib/article_health/checks/terminology.py)
- [`data/terminology/`](../data/terminology/) 2336 YAML 詞條
- [`data/terminology/.china-terms.detection.tsv`](../data/terminology/.china-terms.detection.tsv) 36 active
- [Issue #616](https://github.com/frank890417/taiwan-md/issues/616) opt-in detection 設計
- [MANIFESTO §11 書寫節制](../docs/semiont/MANIFESTO.md) 對位句 / 破折號（跟 zhtw-mcp ai_filler / translationese 同源）

---

🧬

_v1.0 | 2026-05-05 13:55+0800_
_作者：Taiwan.md（哲宇 trigger via `/twmd-research` unimplemented skill）_
_誕生原因：哲宇要求評估 sysprog21/zhtw-mcp 並提整合方案。發現 zhtw-mcp 有 ai_filler/translationese/MoE punctuation 三大 Taiwan.md 缺的 instrumented 寫作紀律維度；Taiwan.md 有 zhtw-mcp 缺的 2336 詞條 etymology/fork_type 完整 metadata。雙方互補幅度極大，Option A+D 為短期 high-confidence 推薦執行路徑。_
_LESSONS-INBOX 候選：「`/twmd-research` skill 不存在 → 觀察者 fuzzy intent 暴露 skill family gap」— 應補 `/twmd-research` 薄殼 (Stage 1 research 套裝 + WebFetch + 專案評估 SOP)。_
