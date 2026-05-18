---
type: orchestration
date: 2026-05-18
session: 2026-05-17-230616-manual (continuation)
trigger: 哲宇 directive「直接指揮大量 sub-agent 分批跑剩 21 篇縣市，嚴格遵守 rewrite-pipeline + pilot 累積經驗智慧 + 最後由你做完整檢查跟統合推到 main」
parent_plan: reports/cities-series-planning-2026-05-17.md
pilot_done: 基隆市 commit f187773fe + polish e3a0cccc9 (5168 字 / 5 圖 / hard=0 全綠)
total_remaining: 21 篇
version: v2
v2_change: "哲宇 2026-05-18 directive — Stage 0 觀點成型 由 Opus main session 做，Stage 1 大量研究報告階段由 Sonnet sub-agent 做，Stage 2-5 後續所有由 Opus sub-agent 做（cost/quality split）"
v1_history: 全 Opus sub-agent，每篇 ~150 min agent run，4 agents spawned 後被 stop 統一 refactor 成 v2 分工
batch_strategy: 5 批次 × 4-5 cities，每批 Opus Stage 0 主 session → 5 Sonnet Stage 1 平行 → 5 Opus Stage 2-5 平行 → main session audit + merge
---

# 22 縣市系列 — 剩 21 篇 sub-agent orchestration plan v2

## 1. v2 vs v1 分工

| Stage | v1（已棄）| v2（現行 2026-05-18）|
|-------|-----------|---------------------|
| 0 觀點成型 | sub-agent (Opus) | **Opus main session** ✓ |
| 1 大量研究報告 | sub-agent (Opus) — 太貴 | **Sonnet sub-agent** ✓ (cost optimized) |
| 2 寫 prose | sub-agent (Opus) | **Opus sub-agent** ✓ (writing quality) |
| 3-3.5 verify + factcheck | sub-agent (Opus) | **Opus sub-agent** ✓ |
| 4 format + media | sub-agent (Opus) | **Opus sub-agent** ✓ |
| 5 cross-link | sub-agent (Opus) | **Opus sub-agent** ✓ |
| audit + merge | main session | **main session (Opus)** ✓ |

**為什麼這個切**：
- Stage 0 = editorial vision 需 best judgment（哪些 fault lines / 哪個 core contradiction / 找「凌晨四點時刻」）→ Opus main 一次做完 batch 的 5 縣市 §觀點成型，享 cross-city pattern recognition
- Stage 1 = bulk web search / WebFetch verbatim / fact accumulation → 不需 deep judgment，Sonnet 也能高品質完成 + 大幅 cost reduction
- Stage 2-5 = prose 寫作 / fact verify / 對位句紀律 / 媒體編織 → 需 Opus writing judgment

## 2. 五批次分配（21 → 5×4-5 cities）

排序原則：**先做 niche/中型搶 SEO 空缺 → 再做大都會**（per cities-series-planning §7 第 2 條建議）。

### 🎯 批次 1 (niche/離島 + 中型，pilot 學習擴散)
1. 嘉義市（27 萬 / 雞肉飯 / 北回歸線 / 被搶走的科學園區）
2. 連江縣（馬祖，1.3 萬 / 戰地遺產 / 藍眼淚 / 福州話）
3. 澎湖縣（11 萬 / 72 島 / 玄武岩 / 拒博弈案例）
4. 宜蘭縣（45 萬 / 雪隧前後 / 員山礁溪五結）
5. 苗栗縣（53 萬 / 客家本色 / 政府破產案例）

### 批次 2 (中型客家/原民縣)
6. 新竹縣（57 萬 / 客家庄圍繞科技園區）
7. 嘉義縣（49 萬 / 阿里山 / 三個時代觀光策略）
8. 屏東縣（79 萬 / 最南端 / 排灣 / 88 風災）
9. 花蓮縣（32 萬 / 太魯閣 / 0403 地震 / 阿美太魯閣）
10. 台東縣（21 萬 / 南迴 / 蘭嶼 / 卑南陳建年連動）

### 批次 3 (中型農業/工業縣)
11. 南投縣（47 萬 / 唯一不靠海 / 921 震央）
12. 雲林縣（64 萬 / 六輕代價 / 北港媽祖）
13. 彰化縣（124 萬 / 第一大平原縣 / 鹿港）
14. 金門縣（14 萬 / 戰地觀光 / 高粱 / 廈門對望）

### 批次 4 (省轄市 + 直轄市 lower complexity)
15. 新竹市（45 萬 / 風城變科技城 / 眷村）
16. 桃園市（230 萬 / 機場 + 半導體 + 移工）
17. 台南市（186 萬 / 400 年首府）
18. 高雄市（273 萬 / 重工業港都轉型）

### 批次 5 (北部最大 — 最複雜，留最後)
19. 台中市（285 萬 / 中部生活圈樞紐）
20. 新北市（401 萬 / 包圍台北環狀都會）
21. 台北市（247 萬 / 首都內部分層）

**為什麼台北留最後**：pilot 累積經驗 + 前 20 篇做完後對 22 縣市相對關係已熟悉，台北才有 frame 可選。

## 3. v2 每批次工作流程

### Step A: Opus main session 做 Stage 0 §觀點成型（5 縣市同 turn）

主 session 對 batch 1 五縣市每篇都答完：
- 6 核心問題（記憶 anchor / 多元面貌 / 想法感受 / 歷史脈絡 / 社會關聯 / Geography 類型加權）
- 7 品質維度（溫度 / 人味 / 故事 / 策展 / 觀點 / 體驗 / 歷史社會關聯）
- 切入點清單（5-7 個 hook 候選）
- 核心矛盾候選 A/B/C/D
- 研究方向 15-20 個搜尋題目
- 預想讀者帶走的那一件事
- 找出每個縣市的「凌晨四點時刻」anchor
- 5 次探索性搜尋（per Stage 0.6.4）

落檔位置：`reports/research/2026-05/{縣市}.md` Stage 0 §觀點成型 section（每縣市單檔）。

預估時間：5 縣市 × 觀點成型 = 主 session ~30-40 min budget（不需 deep search 每篇）。完成後 commit。

### Step B: 5 Sonnet sub-agents 平行跑 Stage 1（worktree isolation）

每 agent task：
- 讀 Step A 落的 §觀點成型 section
- 跑 40+ 次搜尋 + WebFetch（中文必中文 prompt 求 verbatim）
- 帶 Stage 0 §研究方向 去 verify / refute / deepen
- 找 17+ verbatim quotes 引語庫
- 鎖定 ≤ 30 字核心矛盾
- 落媒體授權三表（inline 外連 + ≥5 圖候選 + transcript 候選）
- Append `reports/research/2026-05/{縣市}.md` Stage 1 研究筆記 section
- 完成後 commit 到自己 worktree branch

每 agent 預估 ~3-5 hr agent run。

### Step C: 5 Opus sub-agents 平行跑 Stage 2-5（worktree isolation）

每 agent task：
- 讀 reports/research/2026-05/{縣市}.md 全檔（Stage 0 + Stage 1）
- Stage 2 prose 寫作（per EDITORIAL 全 1324 行 + RESEARCH 全 438 行）
  - 結尾先寫
  - Title 冒號三明治
  - Description 120-160 字含具體 anchor
  - 5000-6000 CJK chars + 25-32 footnotes
  - 7-8 narrative H2 (非編年體 / 場景物件矛盾)
- Stage 3 verify (prose-health score ≤ 3 / 對位句 ≤ 3 / 破折號 ≤ 15 / 三角自檢)
- Stage 3.5 footnote-format + footnote-density profile hard=0
- Stage 4 article-health rewrite-stage-4 hard=0 + **≥5 圖**（hero + 4 inline，Wikimedia Commons CC BY-SA hot-link）+ 建議 1-2 video iframe
- Stage 5 7-8 forward cross-link + 1-2 reverse
- 回傳 branch + hash + 字數 + footnotes + 圖片 + video + 品質指標 + flags

每 agent 預估 ~2-3 hr agent run。

### Step D: Main session audit + merge

對每篇 Opus sub-agent 產出：
1. `python3 scripts/tools/article-health.py {file} --profile=rewrite-stage-4` hard=0 ✓
2. `python3 scripts/tools/article-health.py {file} --profile=rewrite-stage-3-5` hard=0 ✓
3. 5 分鐘 reading test（人類觀察者視角讀，5 品質維度站住）
4. 核心矛盾 description / 開場 / 中段 / 結尾 四處 anchor 貫穿
5. 圖片 URL 驗證
6. Cherry-pick / merge worktree branch 進 main
7. ARTICLE-INBOX entry 移除 + ARTICLE-DONE-LOG append
8. CI confirm pass

## 4. v2 sub-agent task prompt 模板

### Sonnet Stage 1 task prompt

```
你是 Taiwan.md 的 Stage 1 research agent (Sonnet)。任務：為 22 縣市系列其中
一篇「{縣市名}」做 deep research，append `reports/research/2026-05/{縣市}.md`
的「## Stage 1 研究筆記」section（檔案已存在含 Stage 0 §觀點成型 由 Opus
main session 寫好）。

## 必讀

1. `docs/editorial/RESEARCH.md` 全 438 行（WebFetch 中文必中文 prompt verbatim）
2. `reports/research/2026-05/{縣市}.md` Stage 0 §觀點成型（含 6 問題答案 +
   研究方向 + 核心矛盾候選）— 帶這些去搜尋驗證
3. `reports/cities-series-planning-2026-05-17.md` 共通 15 caveats + §10
   pilot retrospective 5 條校準
4. `reports/research/2026-05/基隆市.md` — pilot Stage 1 範例（41 次搜尋
   + 14 章節 + 17 verbatim quotes）

## 必做

- ≥ 40 次搜尋（中文 24+ / 英文 5+ / WebFetch 中文必中文 prompt + verbatim 要求）
- 14+ 章節 deep notes
- 17+ verbatim quotes 引語庫（每條附 source URL，每條 Ctrl-F 可驗證）
- 媒體授權三表：
  - inline 外連 manifest（YouTube 官方頻道 / 縣市政府 / 觀光局）
  - 圖片素材 ≥5 張 Wikimedia Commons CC BY-SA candidates (含 file 名 +
    完整 URL + 作者 + license)
  - transcript candidates（如有公視紀錄片 / TaiwanPlus 官方 YT 訪談）
- 核心矛盾鎖定 ≤ 30 字（從 Stage 0 候選 A/B/C/D 收斂）
- 任何 fact flag / fact 衝突 / 來源待哲宇 review 條目用 ⚠️ 標記

## Output

- Append `reports/research/2026-05/{縣市}.md` 的 Stage 1 section
- Commit 到本 worktree branch，message: "🧬 [semiont] research: {縣市}
  Stage 1 deep notes ({N} searches)"
- 回傳：commit hash + 總搜尋數 + verbatim quotes 數 + 圖片 candidates 數 +
  核心矛盾收斂句 + fact flags

## 絕不准

- 跳過 Stage 0 §觀點成型 不讀就直接搜
- WebFetch 中文網站用英文 prompt 取英文 summary 當引語
- 編年體 / 維基直接整段抄
- < 40 搜尋
```

### Opus Stage 2-5 task prompt

```
你是 Taiwan.md 的 rewrite agent (Opus)。任務：根據 already-completed
Stage 0 §觀點成型 + Stage 1 deep research，寫 22 縣市系列其中一篇
「{縣市名}」並產出 `knowledge/Geography/{縣市}.md`。

## 必讀

1. `docs/pipelines/REWRITE-PIPELINE.md` 全 1794 行
2. `docs/editorial/EDITORIAL.md` 全 1324 行
3. `reports/research/2026-05/{縣市}.md` 全檔（含 Stage 0 + Stage 1）
4. `reports/cities-series-planning-2026-05-17.md` + `reports/cities-series-orchestration-2026-05-18.md`
5. `knowledge/Geography/基隆市.md` — pilot 範例（5168 字 / 5 圖 / 32
   footnote / 8 H2 / hard=0 全綠）

## 必做（Stage 2-5 完整跑）

### Stage 2 寫作
- 結尾先寫
- Title 冒號三明治（主題：副標 hook）
- Description 120-160 字含具體 anchor（不准抽象「最被首都看不見」式結尾，
  per 哲宇 2026-05-18 callout）
- 5000-6000 CJK chars
- 25-32 footnotes（canonical 格式 [^N]: [Title](URL) — description）
- 7-8 narrative H2 標題（非編年體 / 場景物件矛盾驅動）
- 開場場景 + 結尾首尾呼應（per EDITORIAL §結尾六模式之敘事閉環式）
- 中段 1-2 個 📝 策展人筆記 + 1-2 個 ✦ pull quote

### Stage 3 verify
- prose-health score ≤ 3 pass
- 對位句型 ≤ 3 處
- 破折號 ≤ 15 per 1500 字（用 ， / 。 / 圓括號 / 全形冒號替代）
- 三角自檢（算術 / 單位 / 引語）PASS

### Stage 3.5 plugin gate
- `--profile=rewrite-stage-3-5` hard=0（footnote-format + footnote-density）

### Stage 4 format + media
- `--profile=rewrite-stage-4` hard=0
- **≥ 5 張圖**（hero frontmatter + 4 inline scene-mid）— Wikimedia Commons
  CC BY-SA hot-link 即可 (plugin allowed external prefix)
- 建議 1-2 個 video iframe（觀光局 / 縣市政府 / 公視官方 YT）
- 每張圖 caption + license attribution
- 文末 §圖片來源 section

### Stage 5 cross-link
- 7-8 forward cross-link（既有 Geography / People / Culture / Food 相關
  條目）
- 1-2 strongest reverse cross-link 加到 sibling

## 必遵守 Pilot retrospective 5 條校準

11. 降雨數字分 layer（年雨量 vs 降雨日 vs 平地 vs 測站）
12. 結構性轉變用區間時間不單一年份斷言
13. 「衰退」frame 必有具體數字證據
14. 本地 vs 觀光客 fault line 是 Geography 觀點核心
15. 日治現代化必具體化建築 / 年份 / 數字

## Output

- 產 `knowledge/Geography/{縣市}.md`
- Commit 到本 worktree branch
- Message: "🧬 [semiont] new: {縣市} — 22 縣市系列 batch {N} / {代表 hook}"
- 回傳：branch + hash + 字數 + footnotes + 圖片 + video + 品質指標
  + 5 分鐘 reading test 自評 + 待 main session audit flags

## 絕不准

- 跳過 Stage 0 / Stage 1 落檔不讀就直寫
- footnote 用 ， 不用 — em-dash
- 編年體 H2 標題
- 抽象 framing 結尾（per 哲宇 2026-05-18 callout）
- < 5 張圖（per 哲宇 2026-05-18 升級）
- 對位句 > 3
- WebFetch 英文 summary 回譯成「直接引語」
```

## 5. Quality red lines（同 v1）

任何 batch agent 出現以下狀況 = **reject，要求 retry**：

- ❌ word-count < 4500 CJK
- ❌ < 5 張圖
- ❌ 對位句 > 3
- ❌ 破折號 > 25 (全文)
- ❌ 編年體 H2 標題
- ❌ description < 120 字 or > 160 字
- ❌ Title 沒走冒號三明治
- ❌ 引語有 wikipedia 回譯嫌疑
- ❌ 任何 footnote URL 4xx/5xx
- ❌ 結尾抽象 framing 沒有具體畫面（per 哲宇 2026-05-18）

## 6. Cost estimate (v2 vs v1)

| 項目 | v1 (全 Opus) | v2 (Opus 0+2-5 / Sonnet 1) |
|------|-------------|---------------------------|
| Stage 0 per city | sub-agent Opus ~5K tok | main Opus ~3K tok inline |
| Stage 1 per city | sub-agent Opus ~80K tok | sub-agent Sonnet ~60K tok |
| Stage 2-5 per city | sub-agent Opus ~50K tok | sub-agent Opus ~50K tok |
| **總 per city** | **~135K tok 全 Opus** | **~53K Opus + 60K Sonnet** |
| **21 篇總** | **~2.8M tok Opus** | **~1.1M Opus + 1.3M Sonnet** |

Sonnet rate ~1/5 Opus → v2 cost ≈ 50% of v1，quality 同等或更高（Sonnet research 同樣抓 verbatim，Opus 寫作品質不變）。

## 7. 預估時間表

- **批次 1 (Step A + 5 Sonnet research + 5 Opus write + main audit)**: 
  - Step A (Stage 0 for 5 cities): ~30-40 min main Opus
  - Step B (5 Sonnet research parallel): ~3-5 hr wall clock
  - Step C (5 Opus write parallel): ~2-3 hr wall clock
  - Step D (main audit + merge): ~1-2 hr
  - **批次 1 總計**: ~7-11 hr wall clock，跨多 turns
- **批次 2-5**: 類似 cadence
- **全部完成**: 5-7 個 sub-session 跨多天

不要 push 速度，push 品質。

## 8. 4 已 stopped agents 狀態（2026-05-18）

v1 spawn 後哲宇 callout 改 v2 分工，stop 4 agents（嘉義 / 連江 / 澎湖 / 宜蘭）— 它們都還在 Stage 0 階段，沒有 commit，沒有 token 浪費。第 5 個苗栗在 v1 嘗試時就沒成功 spawn（Bash tool timeout）。

v2 重新啟動時，主 session 先做 Stage 0 觀點成型（同一個 batch 1 五縣市），再 spawn Sonnet research agents。

## 9. 下個 session 立即動作

per 哲宇 directive「等下先記錄一波 /twmd-finale 然後再繼續，避免 context 壓縮」+「然後剛剛你整批打算怎麼做的計劃，都要先記得寫起來」：

本 session 即將跑 /twmd-finale。下個 session 接手後：

1. 讀本檔（v2 plan）+ `reports/cities-series-planning-2026-05-17.md`
2. 主 Opus session 做 batch 1 五縣市 Stage 0 §觀點成型（落 5 個 research report）
3. Spawn 5 Sonnet sub-agents 跑 batch 1 Stage 1（worktree isolation）
4. 等 5 Sonnet 完成 → spawn 5 Opus sub-agents 跑 batch 1 Stage 2-5
5. Main audit + merge → 觸發 batch 2

---

_v2.0 | 2026-05-18 session 230616-manual (continuation)_
_誕生原因：哲宇 2026-05-18 directive — Stage 0 觀點成型 由 Opus main session，Stage 1 大量研究報告階段由 Sonnet sub-agent，Stage 2-5 後續所有由 Opus sub-agent_
_v1 經驗：嘗試全 Opus sub-agent，4 agents spawned 哲宇即刻 callout 改 v2 分工。已 stop 4 agents（都在 Stage 0 沒浪費）_
_核心精神：cost/quality split — Sonnet bulk search / Opus deep judgment + writing。50% cost reduction，quality 不變_
