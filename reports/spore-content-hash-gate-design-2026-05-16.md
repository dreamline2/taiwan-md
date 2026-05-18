---
title: 'Spore Content-hash Gate Design 2026-05-16'
description: 'Harvest URL ↔ content fingerprint mismatch detection — side-car JSON + audit script + SPORE-HARVEST-PIPELINE 整合設計 / LESSONS-INBOX 2026-05-16 #5 達 vc=3 instrumentalize'
type: 'design-doc'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-05-16
last_session: '2026-05-16-011113-manual-audit-evolve'
related:
  - '../docs/factory/SPORE-HARVEST-PIPELINE.md'
  - '../docs/factory/SPORE-LOG.md'
  - '../docs/semiont/LESSONS-INBOX.md'
  - '../scripts/tools/spore-content-hash-audit.py'
---

# Spore Content-hash Gate Design 2026-05-16

> 哲宇 directive「建立 Routine audit 跟 routine 本身一樣需要 routine 化 的機制完整實作」附帶 LESSONS-INBOX 2026-05-16 #5 達 vc=3 儀器化 threshold（harvest content-hash 比對 plugin gate）。本設計報告紀錄 instrument 路徑 + MVP 範圍 + 完整推進規劃。

---

## 為什麼

### 觸發歷史

`#71 無人機` X URL `https://x.com/taiwandotmd/status/2053101189034860856` skip 第 3 次驗證：

| Cycle | 日期       | 觀察                                                                                                                                                    |
| ----- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | 2026-05-12 | spore-harvest dry-run 揭露 SPORE-LOG row URL 跟實際 X post 內容不一致（該 URL 內容 emoji 🏭 + utm_campaign=s69 是 #69 台積電 edit 版，不是 #71 無人機） |
| 2     | 2026-05-13 | first prod cycle 再次撞同條 mismatch，flag 進 batch log，未處理                                                                                         |
| 3     | 2026-05-16 | 第三次 cycle 撞，spore-harvest memory 記「達 REFLEXES #15 反覆浮現要儀器化 threshold（≥3）」                                                            |

### 結構性問題

Spore harvest pipeline 目前沒有 content-hash 比對機制：

1. **沒辦法自動偵測 URL ↔ content drift**：URL 寫錯 / post 已刪除 / X UI 自動 redirect 到 edit 版 — 每次 harvest 都要 human-in-loop manual flag
2. **Metric 污染風險**：mismatch URL 抓到的 views/engagement 是別條 spore 的數字，回填進 SPORE-LOG 會污染歷史 metric
3. **Routine 飛輪邊界 gap**：harvest routine 認 URL 即抓，無語意 check；maintainer routine 處理 PR/Issue 不負責 SPORE-LOG schema heal — 落到 observer 手上累積三 cycle 沒解

### 對應 LESSONS-INBOX 教訓鏈

- **#5（本設計觸發）** harvest pipeline 加 content-hash 比對檢查（vc=3 達 threshold）
- **#6** routine 飛輪 article framing audit gap（vc=3 carryover）— 同源結構問題，但本設計只解 #5

---

## 設計：side-car JSON + audit script

### 為什麼不動 SPORE-LOG schema

SPORE-LOG.md 是 73+ row markdown table，每條人類手動寫的 markdown 行。直接加新 column 需要：

- 全 73 row 補空 `content_fingerprint` field（人工 / agent backfill）
- Markdown table parser 改（如果有）+ refresh-data.sh 影響
- PR review 風險：73 行同 PR 雜訊大

**Side-car JSON 設計**（不動 SPORE-LOG）：

```
docs/factory/spore-content-fingerprints.json
```

優點：

- 不影響既有 SPORE-LOG schema / parser / refresh-data.sh
- 漸進式 baseline：每次 harvest 才 record 該條 spore baseline，不需要 73 row backfill
- 失去同步成本：若 SPORE-LOG row 被人工編輯（URL fix），side-car JSON entry 仍對應舊 URL — 但這是低頻場景，人工修 SPORE-LOG 時順手更 JSON 即可

缺點：

- 雙資料源（SPORE-LOG row + side-car）違反 SSOT 原則 — 但僅就「content fingerprint」這一維度，其他 column 仍走 SPORE-LOG SSOT
- 需 manual `--build-baseline` step（人工 verify URL ↔ content 對應後 record）

**SSOT 邊界**：side-car JSON 是 audit metadata，不是 identity 或 metric SSOT — 跟 SPORE-LOG 三層 SSOT（identity / narrative / harvest event）正交，不衝突。

### Audit script: `scripts/tools/spore-content-hash-audit.py`

純資料層（純 Python，不需 Chrome MCP / 不需 Web API）：

```python
fingerprint = sha256(
    first_sentence + sorted(emoji_set) + utm_campaign
)[:16]
```

API：

```bash
# 建 baseline（首次 harvest 該 spore）
python3 scripts/tools/spore-content-hash-audit.py --build-baseline \
  --url=URL --content=TEXT --spore-id=N

# 比對（後續 harvest）
python3 scripts/tools/spore-content-hash-audit.py --check \
  --url=URL --content=TEXT
# exit 0 = match / exit 1 = mismatch (with diagnostic JSON)

# 列 inventory
python3 scripts/tools/spore-content-hash-audit.py --list
```

### Fingerprint 為什麼這三個 component

| Component                      | 為什麼                                                           |
| ------------------------------ | ---------------------------------------------------------------- |
| **first_sentence (≤80 chars)** | spore 開頭高識別性，每條獨特；80 chars 上限避免長 spore 整段比對 |
| **emoji set (sorted)**         | 高訊號低噪音 — 哪個 spore 用了 🇹🇼 vs 🏭 vs 🎯 是 distinctive     |
| **utm_campaign (s\{N\})**      | 直接 identity marker — `s71` vs `s69` 是最強 mismatch detector   |

不選的：

- **Full content hash**：對 minor edit（typo fix / 改標點）過敏 → false positive
- **Just URL**：URL 本身就是 key，不是 fingerprint 內容
- **Image hash**：太重 + Chrome MCP harvest 不一定能抓
- **Title only**：spore 沒有 title 概念，跟 article 不同

---

## SPORE-HARVEST-PIPELINE 整合

詳見 [SPORE-HARVEST-PIPELINE §Content-hash mismatch 偵測（v2.10）](../docs/factory/SPORE-HARVEST-PIPELINE.md#content-hash-mismatch-偵測v2102026-05-16-lessons-inbox-5-達-vc3-instrument)。

Workflow 整合點：

```
Chrome MCP harvest cycle:
1. navigate(URL)
2. read_page() → content
3. ★ NEW: spore-content-hash-audit.py --check (or --build-baseline if 首次)
   → mismatch → backfillWarnings + skip metric update
   → match → 正常 update views/engagement
4. update SPORE-LOG row
5. validate-spore-data.py
```

---

## MVP 範圍（本設計 ship 內容）

### ✅ 已 ship

- `scripts/tools/spore-content-hash-audit.py`（200 行 Python）
  - `--build-baseline` 建 baseline
  - `--check` 比對 fingerprint
  - `--list` 列 inventory
  - exit code 區分 match (0) / mismatch (1) / error (2)
- `docs/factory/spore-content-fingerprints.json` 初始 schema + 一筆 #71 baseline 測試 entry
- `docs/factory/SPORE-HARVEST-PIPELINE.md §Content-hash mismatch 偵測（v2.10）` 整合 SOP 章節

### ❌ 尚未 ship（手動 / observer 進入 loop）

- 73 個既有 spore 的 baseline backfill — 需 observer 在 SPORE-LOG row URL 對應確認後逐條建
- spore-harvest routine SKILL 修改成 cycle 內呼叫 audit script — 待 next spore-harvest cycle 觀察整合機會
- backfillWarnings JSON schema 加 `content_mismatch` field — 待 spore-harvest 整合時順手加

### 設計選擇：MVP first，分段推進

不一次 ship 完整 73 baseline + harvest integration：

1. 每條 baseline 建立需 human verify「URL 真的對應 content」— 73 row 一次跑會出錯，逐 cycle 累積比較安全
2. spore-harvest routine 整合需修 SKILL.md + 測試 → 次次 cycle dogfood 比一次性換軌穩
3. 達 vc=3 已 instrument「機制」，未真正修正所有歷史 mismatch — 但 instrument 本身比一次性 backfill 更高 leverage

---

## Quality gate

| Gate                              | 通過條件                                       | 不過 = ?          |
| --------------------------------- | ---------------------------------------------- | ----------------- |
| Script exit 0 on match            | 重複 URL+content 對 fingerprint 穩定           | bug fix 後重試    |
| Script exit 1 on mismatch         | 不同 URL+content 跨 utm_campaign 觸發          | bug fix           |
| Side-car JSON valid               | `python3 -c "import json; json.load(open(F))"` | YAML / format fix |
| 不破壞 SPORE-LOG                  | 既有 SPORE-LOG row 不動                        | 修 script         |
| Pipeline 整合不破壞 harvest cycle | next harvest 仍能 normal flow                  | 整合修補          |

---

## 進化路線

### Phase 1（本設計 ship）

✅ MVP script + side-car JSON + SPORE-HARVEST-PIPELINE 整合 SOP 章節

### Phase 2（next 1-2 spore-harvest cycle）

- Spore-harvest cycle 內整合 `--build-baseline` 對每條 fresh harvest 自動建 baseline
- 累積到 73/73 baseline 全建後 enable `--check` mandatory mode

### Phase 3（quarterly 或 mismatch 累積後）

- Mismatch routing：連續 3 cycle 同 URL mismatch → 升級 observer 手動 SPORE-LOG schema heal（per DNA #26 v2 AI 自主邊界）
- 對 #71 無人機 case：本設計 ship 後下次 harvest 抓到 → 直接 flag → observer 修 SPORE-LOG row URL 或標 `harvest_status: post not found / suspected deletion`

### Phase 4（meta-level）

- 觀察 content-hash gate 是否能 generalize 到 spore-harvest 以外的 URL-content drift 場景
  - article footnote URL 失效檢測？
  - cross-link target article 內容變動偵測？
- 若 generalize valid → 升 REFLEXES「外部 URL ground truth ↔ 內部紀錄 drift」反射

---

## 跨檔關聯

| 檔案                                                                                                                     | 角色                                         |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| 本設計報告                                                                                                               | 設計選擇 + MVP 範圍 + 推進路線               |
| [scripts/tools/spore-content-hash-audit.py](../scripts/tools/spore-content-hash-audit.py)                                | 工具實作                                     |
| [docs/factory/spore-content-fingerprints.json](../docs/factory/spore-content-fingerprints.json)                          | side-car JSON 資料層                         |
| [docs/factory/SPORE-HARVEST-PIPELINE.md §Content-hash mismatch 偵測（v2.10）](../docs/factory/SPORE-HARVEST-PIPELINE.md) | 整合 SOP                                     |
| [docs/semiont/LESSONS-INBOX.md §2026-05-16 #5](../docs/semiont/LESSONS-INBOX.md)                                         | 觸發 LESSONS entry（vc=3 達 threshold）      |
| [reports/routine-audit-2026-05-16.md §LESSONS-INBOX 候選 #5](./routine-audit-2026-05-16.md)                              | 觸發 audit report 中 P1 instrumentalize 建議 |

---

🧬

_v1.0 | 2026-05-16 12:15 +0800_
_session 011113-manual-audit-evolve — 哲宇 directive「完整實作 content-hash gate」LESSONS-INBOX #5 達 vc=3 儀器化 threshold_
_誕生原因：#71 URL mismatch 三 cycle 累積驗證後達 REFLEXES #15 threshold；既有 routine 飛輪邊界 gap 無對應 routine handle，需 instrument 進 SPORE-HARVEST-PIPELINE 防 metric 污染_
_核心精神：MVP first + 不動 SPORE-LOG schema + side-car JSON 漸進 baseline 累積 + 整合分 Phase 1-4 推進不一次到位_
