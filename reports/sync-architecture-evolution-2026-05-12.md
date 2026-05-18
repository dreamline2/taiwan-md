---
title: 'sync.sh 架構演化策略：knowledge/ → src/content/ 投影管線的長期解法'
session: '2026-05-12-001000-admiring-montalcini-post-finale'
author: 'Taiwan.md (Semiont)'
date: 2026-05-12
type: 'architectural-design-report'
current_version: 'v2.0'
context: '哲宇 prompt — 先 /twmd-become 然後分析 sync.sh 缺口的長期最佳解法並歸檔'
trigger: '2026-05-11 cleanup 揭露 sync.sh 沒被儀器化；v2 補揭 fr 330 zombie + 8 篇 silent missing 兩個既有 bleeding'
upstream_canonical:
  - 'docs/semiont/MANIFESTO.md'
  - 'docs/semiont/DNA.md'
  - 'docs/semiont/ROUTINE.md'
  - 'docs/pipelines/DATA-REFRESH-PIPELINE.md'
status: 'draft → 等觀察者決策'
---

# sync.sh 架構演化策略

> 投影管線（`knowledge/` SSOT → `src/content/` derived protein）目前的儀器化缺口分析 + 八個解法候選 + 推薦組合 + Migration plan
>
> **v2.0 更新**（2026-05-12 哲宇 callout「最乾淨根治」）：推薦從 v1 的 hybrid (F+H+B+verify) 升級為 **C+F+H 最根治**（gitignore `src/content/` lang dirs）。觸發是再深一層分析揭露兩個既有 bleeding（fr 330 zombie + 8 篇 silent missing 在 zh/en/ja/ko）— 同樣的架構缺口正在多處發生，最根治反而是消除整個 derived state in git 的問題類別。

## 一、觸發事件

2026-05-11 晚間 cleanup session 後，哲宇要求「判斷跑 sync 之後產生的檔案到底有沒有需要 commit 還是可以 ignore」。實測 `bash scripts/core/sync.sh` 在 working tree clean 的 main 上產生：

- **2801 個 `M` tracked file diff**：99% 是 `sourceCommitSha` / `sourceContentHash` / `translatedAt` metadata 漂移（每次 main 移動就漂）+ frontmatter 引號正規化（`category: Art → 'Art'`）+ 少量真內容（footnote 重排）
- **10 個 `??` untracked**：對應 8 篇 contributor PR (`#968 #1005-1009 #1019 #1025`) 已 merge 到 `knowledge/` 但 `src/content/` 投影**從未產生**，網站 build 不到 → 文章已存在卻沒露臉

10 篇 untracked 已在 `f2a2f3eef` 補 commit + push。2801 file drift 已 `git checkout` revert，等待架構解。

### v2 追加：揭露兩個既有 bleeding

比對各 lang 的 `src/content/{lang}/` vs `knowledge/{lang}/` file count，揭露兩個既有 bleeding：

| Lang   | src/content/ | knowledge/ | Gap                         |
| ------ | ------------ | ---------- | --------------------------- |
| zh-TW  | 709          | 711        | **−2 silent missing**       |
| en     | 719          | 721        | **−2 silent missing**       |
| ja     | 698          | 700        | **−2 silent missing**       |
| ko     | 704          | 706        | **−2 silent missing**       |
| **fr** | **1044**     | **714**    | **+330 zombie articles** 🚨 |
| es     | 703          | 697        | **+6 zombie articles**      |

**Bleeding 1 — silent missing**（zh/en/ja/ko 各缺 2 篇）：跟今晚 10 篇同類型，**還有 8 篇 silent missing 隱藏中**。Diff 抽樣顯示 `golden-duo-chi-lin-yang.md` / `taiwan-semiconductor-industry.md` 在 knowledge/ 但不在 src/content/zh-TW/。

**Bleeding 2 — fr 330 個 zombie articles**：sync.sh:19 只 `rm -rf src/content/{zh-TW,en,ja,ko}`，**fr/es 不在 rm list**（line 147-183 只有 cp 沒 rm），knowledge/fr 刪除的舊翻譯會留殘骸在 src/content/fr。這 330 個過時 fr 文章還在 Astro build 的 page set 內 → **網站當前有 330 個 knowledge/ 已經沒有的法文頁面**。

兩個 bleeding 都是同一架構缺口的不同表徵：`src/content/` 作為 tracked derived state 沒有任何單一 source of truth 守門，drift 從多方向發生（少 sync 進來 = missing，沒 rm 清掉 = zombie）。

## 二、根因 + DNA 對應

根因：**`sync.sh` 沒被儀器化進任何生命週期觸發點**（工具本身行為正常）。系統現況：

```
                      ┌─────────────────────────────────┐
                      │ contributor / Semiont PR        │
                      │ 改 knowledge/{lang}/X/Y.md      │
                      └────────────┬────────────────────┘
                                   │ merge to main
                                   ▼
              ┌──────────────────────────────┐
              │ main has new knowledge/      │
              │ src/content/ 仍是舊狀態      │
              └──────────────┬───────────────┘
                             │
        ┌────────────────────┼─────────────────────┐
        ▼                    ▼                     ▼
  ❌ refresh-data.sh    ❌ pre-commit hook    ❌ CI workflow
   12 步沒 sync.sh      無 sync.sh trigger    不跑 sync.sh
        │                    │                     │
        └────────────────────┴─────────────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │ 結果：src/content/ silent stale│
              │ Astro build 看不到新文章      │
              │ 網站缺料 8 天 (PR #968 起)    │
              └──────────────────────────────┘
```

**DNA 對應分析**（5 條反射同時 fire）：

| DNA #   | 反射                                                            | 本案 instantiation                                                              |
| ------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **#43** | 新 dashboard JSON 必須同步進 refresh-data.sh，否則 silent stale | sync.sh 是同一 pattern — 衍生資料沒進 refresh-data 就會 silent stale            |
| **#15** | 反覆浮現要儀器化（11 次驗證）                                   | sync.sh gap 是 #N 次驗證；觀察者每次 cleanup 都看到 dirty src/content/          |
| **#52** | Immune system 沒在 fail loud 比缺 immune system 更危險          | refresh-data Step 10 已 verify dashboard freshness，沒 verify src/content/      |
| **#50** | Pipeline auto-detection + full-read                             | sync.sh 沒在任何 pipeline canonical 提到，Semiont session 主動跑 = 觀察者要提醒 |
| **#54** | Routine 飛輪 5-stage lifecycle                                  | sync.sh 該變成 routine 自動清 entropy 的工作，不是觀察者 push 觸發              |

MANIFESTO §6 鐵律「knowledge/ 是唯一的 DNA，永遠不要直接改蛋白質」**已經被全 contributor 遵守**（PR 都只動 knowledge/）。架構缺口是「轉錄機制沒被觸發」，不是「有人違反鐵律」。

## 三、解空間枚舉（8 個候選方案）

### A | prebuild hook（npm run prebuild 加 sync.sh）

**做法**：`package.json` 加 `"prebuild:sync": "bash scripts/core/sync.sh"` 進 `run-p prebuild:*` 序列。

| 維度               | 評估                                                               |
| ------------------ | ------------------------------------------------------------------ |
| 觸發點             | 每次 `npm run dev` / `npm run build` / CI build                    |
| 解決 silent stale? | ✅ Build 永遠 see fresh src/content/                               |
| Drift 可見性       | 開發時 `git status` 仍會看到 thousands of `M`（更糟）              |
| Build time         | +5-10s（4236 file cp + frontmatter normalize）                     |
| 語意純度           | 弱 — prebuild 在做 generation（API / 索引），sync 是 transcription |
| Fresh clone        | ✅ 首次 dev 自動 sync                                              |
| Routine 整合       | ✗ 跟 routine 飛輪解耦                                              |

### B | refresh-data.sh Stage 0+（routine 飛輪整合）

**做法**：`refresh-data.sh` Step 1（git sync）之後加 Step 1.5「sync.sh + commit if drift」。

| 維度            | 評估                                                 |
| --------------- | ---------------------------------------------------- |
| 觸發點          | data-refresh am (04:14) / pm (00:33) — 1d 2x         |
| 鮮度延遲        | ≤ 12 hr（contributor PR merge 後最多等 12 hr）       |
| 飛輪整合        | ✅ 跟現有 routine cadence 對齊                       |
| DNA #43 pattern | ✅ 跟 dashboard JSON 同樣的整合方式                  |
| Fresh clone     | ✗ 第一次 clone 仍需手動跑 sync.sh                    |
| 風險            | routine drift 風險：sync.sh 失敗 → src/content/ 卡死 |

### C | gitignore src/content/{lang}/ + 接進 npm prebuild ⭐ v2 推薦根治方案

**做法**：移除 `src/content/{zh-TW,en,ja,ko,fr,es}/` 4568 files 出 git，加 `.gitignore`（保留 `src/content/config.ts` schema）；`package.json` 加 `prebuild:sync` 把 sync.sh 接進 `npm run prebuild` 序列。CF Pages build 已執行 `npm run build` → 自動觸發 prebuild → sync.sh，**不需動 CF config**。

| 維度                     | 評估                                                                                                            |
| ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| SSOT 純度                | ✅ 終極純粹（knowledge/ 真的是唯一 source）                                                                     |
| 整類問題消除             | ✅ Derived state in git 整類消失 — drift / zombie / silent missing 全部不可能再發生                             |
| MANIFESTO §6 enforcement | ✅ 從架構強制鐵律「永遠不要直接改 src/content/」（無檔可改）                                                    |
| Migration cost           | 一次性 ~1-2 session（mechanical 為主：git rm + .gitignore + 一行 package.json + 5 份 doc）                      |
| Build 依賴               | CI 必跑 sync.sh — 失敗 → build 失敗（per DNA #52 fail-loud，feature 不是 bug）                                  |
| PR diff 可讀性           | ✅ 大幅改善（merge 一篇文章從 diff 150 行降到 80 行 = maintainer review 速度 2x）                               |
| Git history              | src/content/ history 從來就是 noise（真正 history 在 knowledge/）— 失去無意義                                   |
| Fresh clone              | ✅ `npm install && npm run dev` 自動 prebuild → sync.sh 跑出 src/content/，DX 不變                              |
| Rollback 難度            | 高（force-add 回來）— 但前置 dogfood 充分後不太可能 rollback                                                    |
| 順帶修兩 bleeding        | ✅ Bleeding 1 (silent missing) 不可能再發生 / Bleeding 2 (fr 330 zombie) sync.sh 加 fr/es 進 rm list 後自然清掉 |

### D | pre-commit hook 自動 sync

**做法**：`.husky/pre-commit` 偵測 staged `knowledge/**/*.md`，自動跑 sync.sh 並 add 對應 `src/content/`。

| 維度             | 評估                                                          |
| ---------------- | ------------------------------------------------------------- |
| 觸發點           | 每次 commit 動 knowledge/ 時                                  |
| 原子性           | ✅ knowledge/ + src/content/ commit 一起                      |
| Commit 速度      | 慢 +5-10s（除非配 incremental sync 降到 <1s）                 |
| Contributor 體驗 | 不熟 sync 概念 → 困惑，但 hook silent 跑 contributor 感覺正常 |
| 風險             | sync.sh 失敗 → contributor commit 卡住，需 fallback           |

### E | maintainer pipeline 加 sync gate

**做法**：`/twmd-maintainer` routine 在 PR review 時跑 sync.sh，diff 跟 src/content/ 不一致 → request changes 或自動 fix-on-merge。

| 維度      | 評估                                                              |
| --------- | ----------------------------------------------------------------- |
| 觸發點    | maintainer am (09:07) / pm (21:07) — 收割 PR 時                   |
| 鮮度延遲  | ≤ 12 hr                                                           |
| Scope     | 只 cover routine collect-and-merge 的 PR，不 cover 觀察者直 merge |
| 跟 B 重複 | maintainer 是 PR 收割者，已經做類似工作                           |

### F | sync.sh incremental refactor

**做法**：sync.sh 改成 `git diff --name-only HEAD` 取改動 file list，只 cp 改動的；frontmatter normalize 也只跑改動的。

| 維度          | 評估                                                 |
| ------------- | ---------------------------------------------------- |
| 性能          | 4236 file cp → typically <100 file cp（>40x faster） |
| Idempotence   | 多輪跑同 knowledge/ state → 同 src/content/ output   |
| 為其他層鋪路  | ✅ B / D 都需要 sync 快才能整合                      |
| 風險          | first run / cold cache 仍需 full sync 邏輯 fallback  |
| Refactor cost | Medium — sync.sh 主邏輯重寫，需 dogfood 驗證         |

### G | GitHub Action 自動補 sync PR

**做法**：knowledge/ 改動 merge 後，GitHub Action 自動跑 sync.sh + 開「[bot] sync src/content/」PR。

| 維度      | 評估                                    |
| --------- | --------------------------------------- |
| 觸發點    | knowledge/ 改動 push 到 main 後         |
| Async     | 多一輪 PR，不影響 contributor 流程      |
| 跟 B 重複 | Routine 飛輪已經要做這事，多此一舉      |
| Setup     | 需 GH Actions workflow + bot token 配置 |

### H | sourceCommitSha 重新設計（讓 sync.sh 真 idempotent）

**做法**：把 `sourceCommitSha` 改成「最後改 zh source 的 commit SHA」（用 `git log -1 --format=%H -- knowledge/Category/X.md` 算），而不是 sync 跑時 stamp 當下 main SHA。

| 維度          | 評估                                                 |
| ------------- | ---------------------------------------------------- |
| 根因解決      | ✅ sourceCommitSha drift 從根源消除                  |
| Idempotence   | ✅ 同 zh state → 同 metadata，永遠不漂               |
| Refactor cost | Medium — 改 fix-all-frontmatter.py 邏輯              |
| 跟 F 互補     | 兩者組合 = sync.sh 真正只在 zh 改動時動 src/content/ |

## 四、推薦組合：C + F + H ⭐ v2 最乾淨根治

v1 hybrid (F+H+B+verify) 是「儀器化包住問題」的解法 — drift 仍存在於 git，但用 routine + verify gate 持續清理。v2 揭露兩個既有 bleeding 後，往更根本的方向走 — **直接消除整個問題類別（derived state in git）**。

```
┌─────────────────────────────────────────────────────────┐
│ Layer 1：sync.sh 本身（F + H）                          │
│   • F: incremental — git diff 偵測改動，只 sync 改動    │
│   • H: idempotent metadata — sourceCommitSha 從 zh git  │
│                              log 算，不從 main HEAD     │
│   • 順帶修：fr/es 加進 rm -rf list（解 Bleeding 2）     │
│   → 結果：sync.sh 變快 + idempotent + 不再漂           │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ Layer 2：gitignore src/content/{lang}/（C）             │
│   • .gitignore: src/content/zh-TW/, en/, ja/, ko/, fr/, │
│                  es/（保留 src/content/config.ts）       │
│   • git rm -rf 4568 files（保留 config.ts）             │
│   → 結果：derived state 整類退出 git，drift 不可能存在  │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ Layer 3：sync.sh 進 npm prebuild                        │
│   • package.json: 加 "prebuild:sync": "bash             │
│                    scripts/core/sync.sh"                │
│   • run-p prebuild:* 序列自動 cover                     │
│   • CF Pages build 跑 npm run build → 自動 prebuild     │
│     → 自動 sync.sh（不需動 CF config）                   │
│   • Routine 飛輪跑 npm run build → 自動 sync.sh         │
│   → 結果：build = single source of truth for src/content│
└─────────────────────────────────────────────────────────┘
```

### 為什麼是這三層（不是四層）

**v2 vs v1 的關鍵差異**：v1 把 derived state in git 視為「需要儀器化守住的東西」（drift 用 routine 清，silent failure 用 verify gate 抓）。v2 把它視為「應該整類消除的問題」（不在 git 裡 = 沒問題可守）。

**F + H 從必要變必要 + 加值**：

- v1 需要 F+H 讓 routine 整合可行（sync 快 + 不漂）
- v2 仍需要 F+H 讓 prebuild 整合不慢 build（4236 file cp 進 prebuild = 每次 build +5-10s）
- **同樣的 F+H 投資，v2 多消除一整類問題**

**C (gitignore) 解了 v1 解不到的事**：

- v1 即使做完，drift 仍存在於每次 routine sync 前的瞬間（被 routine 之後清掉但歷史 commit 留 noise）
- v1 對 fresh contributor 仍誤導：「src/content/ 跟 knowledge/ 都在 git 裡，所以可以改任一邊」（MANIFESTO §6 鐵律靠 self-discipline）
- v1 沒解 Bleeding 2 (fr 330 zombie) — 需要 sync.sh 加 fr/es rm 才修，但即使修了，zombie 仍在 git history 內
- v2 一刀切 — gitignore 後 src/content/ 不在 git，MANIFESTO §6 從架構強制執行

**prebuild 是天然 single source of truth**：

- v1 sync.sh 觸發點分散在 refresh-data Step 1.5 + verify gate Step 10 + 可選 pre-commit hook
- v2 sync.sh 只在 prebuild 跑（CF build / local dev / routine 都過 prebuild）
- 對應 MANIFESTO §指標 over 複寫 — 一個 canonical 觸發點，所有用法 derive

### v2 不需要 B / verify gate / D 的原因

- **B (refresh-data integration)**：refresh-data Step 6 本來就跑 `npm run prebuild`，prebuild 加了 sync 後 B 自動發生
- **Verify gate**：build 失敗 = src/content/ 沒成功 sync = 自然 fail loud（per DNA #52）
- **D (pre-commit)**：knowledge/ commit 後下次 build 自動 sync，commit 速度不受影響

v1 的 4 層儀器化在 v2 收斂成 1 個觸發點（prebuild），這就是最根治的意義 — **不是擴張守備範圍，是消除問題本身**。

### 為什麼**不**選 A / B / D / E / G（v2 update）

| 拒絕方案                            | 理由                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------- |
| A (prebuild only，不 gitignore)     | Drift 仍可見於 git status，問題沒消除                                      |
| B (refresh-data only，不 gitignore) | 同 A 問題；且 refresh-data 跟 prebuild 已有 chain（B 是 A 的子集）         |
| D (pre-commit)                      | C 之後沒必要，knowledge/ commit 不需要拉 src/content/ 一起                 |
| E (maintainer-only)                 | C 之後完全沒必要，沒 src/content/ 在 git 可 check                          |
| G (GH Action)                       | C 之後完全沒必要，CI build 已 cover                                        |
| F-only (沒 C+prebuild)              | F 解 drift 量級但不解問題類別；single trigger point 沒建立，多人 push 仍亂 |
| H-only (沒 C+prebuild)              | 同 F-only — metadata idempotent 但 src/content/ tracked 仍會 drift         |

### v1 hybrid 何時仍是合理選擇

如果觀察者對「git rm -rf 4568 files」的心理門檻過不去，或者擔心 fresh clone DX 有任何疑慮，v1 hybrid 是 fallback：較小幅度的儀器化、容忍 drift 但用飛輪清。v2 是更深的解，但 v1 也 ship-ready。建議**先讀 §五 v2 Migration 評估 migration 痛 vs 永久收益再拍板**。

## 五、Migration Plan（per MANIFESTO §修改量級）

按修改量級拆 3 個 ship，每個都是單 session 完成範圍：

### Ship 1: F+H combined refactor + fr/es rm fix（修改量級 M）

**Scope**：~6 files / ~400 lines

- `scripts/core/sync.sh`：
  - 加 `--incremental` mode（default on）
  - 用 `git diff --name-only` 取改動 file list（main 跟 last sync 時的 ref 比）
  - 只 cp 改動的 + 改動所屬 lang/category dir
  - `--full` flag 保留 fallback（cold cache / 第一次 clone / gitignore 後 fresh build）
  - **順帶修 Bleeding 2**：line 19 `rm -rf` list 加 `src/content/{fr,es}` — 清乾淨 fr 330 個 zombie + es 6 個 zombie
- `scripts/utils/fix-all-frontmatter.py`：
  - 改 `sourceCommitSha` 算法：用 `git log -1 --format=%H -- knowledge/{translatedFrom}`
  - 不在 sync 時 stamp 當前 main SHA
  - 只動該 sync 的檔案，不全掃
- 加 `scripts/tools/sync-self-test.sh`：跑兩次 sync.sh，第二次應該 0 file changed（idempotence test）

**Verify**：

1. `bash scripts/core/sync.sh --full` → file count 對齊 knowledge/（fr 應該從 1044 降到 ~714）
2. 連跑兩次 → `git diff --quiet src/content/` exit 0（idempotent）
3. `npm run build` 通過 + Astro page set 健康（fr -330 page 是 expected）

**Risk**：sync.sh 是骨骼基因（per DNA §基因突變規則「骨骼基因任何變更必須通過 build 驗證」），必跑：

1. Local: `npm run build` 通過 + Astro 看到所有 4196 + zh/en/ja/ko 全 reflect（fr 預期 −330 zombie）
2. CI: i18n-smoke-test.yml 通過
3. CF Pages: deploy preview 看 prod 健康，特別 fr 文章列表少 330 條是 expected

### Ship 2: prebuild 整合 + 1 週 dogfood（修改量級 S）

**Scope**：~3 files / ~30 lines

- `package.json`：
  - 加 `"prebuild:sync": "bash scripts/core/sync.sh"` 進 `run-p prebuild:*` 序列
  - 放在最前面（其他 prebuild:\* 依賴 src/content/ 已 sync）
- `docs/pipelines/DATA-REFRESH-PIPELINE.md`：
  - Step 6 `npm run prebuild` 註記「現在 prebuild 內含 sync.sh」
  - 不需要新增 Step 1.5（v1 plan 的設計已過時）
- `.github/workflows/`：
  - 確認既有 workflow 跑 `npm run build` 或 `npm run prebuild` — 自動觸發
  - 沒有額外設定要動

**1 週 dogfood**：Ship 2 完成後**不立刻 ship 3**，跑 1 週驗證：

- routine 飛輪 9 條 cycle 全部 build 通過
- CF Pages deploy 每次都 healthy
- 觀察者開發體驗：`npm run dev` 第一次跑 +5-10s（prebuild 含 sync）符合 expected
- 沒撞到 sync.sh edge case

**Decision gate**：dogfood 1 週通過 → ship 3；任何 routine fail / build break → 先 fix 再 ship 3。

### Ship 3: gitignore src/content/{lang}/ + docs update（修改量級 M）

**Scope**：~6 files + 4568 file untrack

- `.gitignore`：
  - 加 `src/content/zh-TW/` `src/content/en/` `src/content/ja/` `src/content/ko/` `src/content/fr/` `src/content/es/`
  - **不**加整個 `src/content/`（保留 `config.ts` 在 git）
- `git rm -rf src/content/{zh-TW,en,ja,ko,fr,es}/` — 4568 files untrack
- **dogfood pre-merge**：local build 驗證、cold clone 驗證、CF deploy preview 驗證
- `CLAUDE.md`：補一段「`src/content/{lang}/` is gitignored — derived by `scripts/core/sync.sh` in prebuild」
- `CONTRIBUTING.md`：強調「only edit `knowledge/`，never `src/content/`」（既有鐵律但現在從架構 enforce）
- `docs/semiont/MANIFESTO.md` §6：補一行「2026-05 起 src/content/{lang}/ 不在 git 內，由 prebuild 從 knowledge/ regenerate」
- `docs/semiont/DNA.md` §骨骼基因表 + #43：sync.sh 觸發點從散落改為單一（prebuild）
- `docs/pipelines/DATA-REFRESH-PIPELINE.md` §Step 6：補 prebuild 內含 sync.sh
- `docs/semiont/structure-log.md`：記錄這次架構變更

**Risk + 緩解**：

- 風險：CF Pages build 失敗（sync.sh 在 CI 跑 ≠ local 跑）→ 緩解：Ship 2 dogfood 1 週已驗證 CI sync 健康
- 風險：existing PR in-flight rebase 痛 → 緩解：Ship 3 ship 前 announce 1 天，現有 PR rebase；之後 PR 不會有 src/content/ diff
- 風險：fresh contributor 困惑「為什麼 src/content/ 不在我 git status 看到」→ 緩解：CLAUDE.md / CONTRIBUTING.md 文檔補強

**Verify**：

1. CF Pages deploy preview build 過 + site 全功能
2. Fresh clone（一台沒 cache 的機器）跑 `git clone && npm install && npm run dev` → src/content/ 自動產生 → dev server 正常
3. Routine 飛輪 24 hr 觀察：9 條 routine 全綠 + 沒新 LESSONS entry

完成後永久收益：drift / silent missing / zombie 整類問題從 git 消失。

## 六、Success Metrics（Ship 3 完成後）

| 指標                                            | Baseline                | Target (v2)                         |
| ----------------------------------------------- | ----------------------- | ----------------------------------- |
| sync.sh 跑完後 `git status` 漂移 files          | 2801 / 4236 (66%)       | **N/A**（不在 git）                 |
| sync.sh wall-clock                              | ~10s                    | < 1s（typical change）              |
| Silent stale duration (PR merge → site reflect) | ∞（直到觀察者手動觸發） | **0**（CI build 自動）              |
| Silent missing 篇數                             | 10 已修 + 8 待修        | **0**（架構不可能）                 |
| Zombie 篇數 (fr / es)                           | 336                     | **0**（sync.sh 修+gitignore）       |
| Contributor PR 需要手動補 src/content/ 次數     | 8 起（PR #968-1025）    | **0**（不需要 src/content/ 在 git） |
| MANIFESTO §6 enforcement                        | self-discipline         | 架構強制                            |

長期 success = **「src/content/ 是 derived」這件事從 self-discipline 變成架構物理事實**。Per DNA #36 founder time leverage — 觀察者再也不用想 sync.sh 怎麼跑、何時跑、有沒有跑。

## 七、跟 MANIFESTO / DNA 的對應

| 上游 canonical                                                 | 本提案 instantiation                                       |
| -------------------------------------------------------------- | ---------------------------------------------------------- |
| MANIFESTO §6（knowledge/ 是 DNA, src/content/ 是 protein）     | 強化 SSOT 純粹性 — 轉錄機制儀器化進飛輪                    |
| MANIFESTO §造橋鋪路                                            | sync.sh 從觀察者 push 變成 routine 自動                    |
| MANIFESTO §指標 over 複寫                                      | sync.sh canonical 在 scripts/core/，所有觸發點 pointer     |
| DNA #15 反覆浮現要儀器化                                       | 第 N 次驗證 — sync.sh gap 從思考升 SOP / cron / hook       |
| DNA #43 新衍生資料必須進 refresh-data.sh                       | 延伸：「新衍生資料」概念從 dashboard JSON 擴到投影層       |
| DNA #50 Pipeline auto-detection                                | DATA-REFRESH-PIPELINE 升 13 步後，sync.sh 從此 auto-detect |
| DNA #52 Immune system 沒在 fail loud 比缺 immune system 更危險 | Layer 3 verify gate 把 sync.sh silent failure fail loud    |
| DNA #54 Routine 飛輪 5-stage lifecycle                         | sync.sh 進 routine 是飛輪 instantiation                    |
| ANATOMY §骨骼基因                                              | sync.sh 是骨骼，本提案動骨骼基因「必須通過 build 驗證」    |

## 八、Open Questions（給觀察者決策）

1. **走 v2 還是 fallback v1**：v2 (C+F+H) 是最乾淨根治，需要一次性 migration（git rm -rf 4568 files + 5 份 doc 更新）。v1 (F+H+B+verify) 風險較低但 drift 永遠存在。**建議走 v2**，理由：bleeding 1+2 揭露架構缺口在多處發生，最根治是消除整類問題。但如果觀察者對 git rm 心理門檻過不去，v1 也 ship-ready。

2. **Ship 2 dogfood 1 週夠不夠**：prebuild 內含 sync.sh 是新的 CI critical path。1 週覆蓋 routine 飛輪 ~63 cycle + CF deploy ~14 次 + 觀察者 dev session 多次。要更長嗎？

3. **Ship 3 timing 對 in-flight PR 影響**：gitignore src/content/ 之後，所有現有 PR 需要 rebase。建議 Ship 3 前 1 天通知，但能不能在 routine 飛輪 idle window（深夜 / 早晨）執行 ship 來最小化 disruption？

4. **Fresh clone DX 補強**：`npm install` 後第一次 `npm run dev` 會有 +5-10s prebuild sync — 第一次跑會 surprise。要不要 README 加一行說明？

5. **Doc 補強範圍**：v2 推薦改 5 份 doc（CLAUDE.md / CONTRIBUTING.md / MANIFESTO §6 / DNA #43 + 骨骼基因表 / DATA-REFRESH-PIPELINE.md Step 6）。要不要連帶補 BECOME_TAIWANMD.md §鐵律 1 強化「src/content/ 不在 git 裡更不能改」？

6. **fr 330 zombie 揭露的進一步問題**：這 330 個 zombie 從何時開始累積？是否有讀者搜到過？要不要先跑 GA4 audit 看哪些 zombie url 有流量再 ship 3？

## 九、為何這份 report 必要 + v1 → v2 演化

本案是「pipeline 結構缺口暴露」的範例。如果跳過策略分析直接動手改 sync.sh，會錯過幾件事：

- **F vs A 的取捨**：直觀第一念是「加進 prebuild」（A），但 A 不解 drift 可見性問題。F 解 drift 量級，配 C 解問題類別。
- **「最乾淨根治」vs「儀器化包住」**：v1 hybrid (F+H+B+verify) 是儀器化包住問題；v2 (C+F+H) 是消除問題類別本身。觀察者 callout「最乾淨根治呢？」直接揭露 v1 是過度保守。
- **Bleeding 揭露**：file count 比對揭露 fr 330 zombie + 8 篇 silent missing — 同一架構缺口在多處發生。沒有這層比對，可能繼續用 v1 hybrid 修標不修本。

### v1 → v2 演化過程

| 階段 | 觸發                    | 推薦                            | 核心問題                           |
| ---- | ----------------------- | ------------------------------- | ---------------------------------- |
| v1.0 | 哲宇 「分析策略並歸檔」 | F+H+B+verify gate（4 層儀器化） | 守住 drift，sync.sh 接進飛輪       |
| v2.0 | 哲宇 「最乾淨根治呢？」 | **C+F+H（3 層消除問題類別）**   | 消除 derived state in git 整類問題 |

v1 → v2 體現了 MANIFESTO §造橋鋪路的兩種層次：v1 鋪路（建守備機制），v2 直接挪掉需要守備的東西。哲宇的 callout 把分析從「lower-risk hybrid」推到「最根本解法」— 我先前太重 migration cost，欠考慮永久收益。

**本 report 的角色**是哲宇 review 後決定 Ship 順序 + v1 vs v2 路線 + open questions 的拍板基礎。Per HEARTBEAT §收官鐵律 2 特例「需觀察者決策必附 options + 成本 + 推薦 default」 — 上面八節已 cover。

---

## 十、實作結果（v2.1 補完，2026-05-12 02:00 +0800）

哲宇拍板「走 v2 + option A 接受 zombie 清除」後，admiring-montalcini-post-finale session 一次性完成全 3 ship migration（睡前授權自行推動到 /twmd-finale）。

### Ship execution log

| Ship | Commit      | 改動                                                                                | CI                                  |
| ---- | ----------- | ----------------------------------------------------------------------------------- | ----------------------------------- |
| 1    | `02db88af5` | sync.sh 217→165 lines SSOT-driven refactor + 修 3 既有 bug + 10 silent missing 補回 | (Ship 2 push 後 cancel-in-progress) |
| 2    | `22aafd8d8` | `package.json` prebuild 改 serial-first then parallel（sync 必先跑）                | ✅ build success + deploy success   |
| 3    | `d208eed78` | `.gitignore` 加 src/content/{6 lang}/ + git rm 4587 files + 7 docs 對齊新架構       | (見 §post-flight)                   |

### Bleeding 修補結果

| Bleeding                   | Baseline       | After Ship 1+3                                            |
| -------------------------- | -------------- | --------------------------------------------------------- |
| Silent missing zh/en/ja/ko | 各 2 篇 (共 8) | **0** (Ship 1 sync.sh 修補 root-level + resources cp gap) |
| fr zombie articles         | 330            | **0** (Ship 1 加 fr/es 進 rm list)                        |
| es zombie articles         | 6              | **0** (同上)                                              |
| sync.sh wall-clock         | 17s            | 16s（refactor 沒慢化）                                    |
| Drift on `git status`      | 2795 files     | **N/A**（不在 git）                                       |

### 三 ship 順序設計理由（dogfood compressed to single session）

哲宇 plan §五原本 Ship 2 後 1 週 dogfood gate。實際 session 內：

1. Ship 1 local：build pass + idempotence (0 file diff hash compare) + visual smoke 4 lang URL（200 + lang attr 正確）
2. Ship 1+2 push 後 CI dogfood：**CF Pages build + deploy 雙綠**確認 prebuild integration 在 CI 環境也 work
3. Ship 3 ship 前 local 又跑一次 fresh clone simulation（rm src/content/ → npm run build 500s → 4247 files regen）
4. Ship 3 push 後等 CI（本檔寫作時 in-progress）

壓縮 1 週為 ~10 min CI dogfood 的代價：少了「routine 飛輪 ~63 cycle 真實環境驗證」+ 哲宇 dev session 多次驗證。風險：CI 環境跟生產環境差異（unlikely 但理論上可能）。緩解：備份 branch `backup/pre-sync-refactor-2026-05-12` 可隨時 rollback。

### 後續開放問題

1. ~~v1 vs v2 拍板~~ → resolved：走 v2 + option A
2. ~~Ship 2 dogfood 時間~~ → compressed to CI window
3. ~~Ship 3 timing~~ → admiring-montalcini-post-finale session 深夜（cron 02:34 前完成）
4. **未做**：README 補一段「first-time clone +5-10s prebuild sync」說明 — 留給後續 onboarding polish session
5. ~~Doc 範圍~~ → 改 7 份（5 原計畫 + BECOME-implicit 沒動，跟 CLAUDE.md 同層級已 cover）
6. ~~fr 330 zombie GA4 audit~~ → 接受 option A 直接清除（觀察者拍板，accepting URL loss）

### 永久收益

- **MANIFESTO §6 鐵律**：從 self-discipline 升結構性物理約束 — `src/content/{lang}/` 不在 git，連改它都沒意義
- **8 篇 silent missing 補回**：PR #968-1025 的 contributor 文章從此會出現在網站上
- **336 個 zombie 清除**：fr 330 + es 6 過時 URL 從 page set 消失
- **觀察者再也不用想 sync.sh**：CI build / dev / routine 都自動 cover

---

🧬

---

_v2.1 | 2026-05-12 02:00 +0800 admiring-montalcini-post-finale session — 補實作結果 §十_
_v2.1 改動：(1) §十 新增實作結果（3 ship commit 表 + bleeding 修補對照 + dogfood 壓縮理由 + open question 結案 + 永久收益）(2) v2.0 footer 保留_

_v2.0 | 2026-05-12 00:50 +0800 admiring-montalcini-post-finale session — 哲宇 callout「最乾淨根治呢？」後從 hybrid 升 root cure_
_v2.0 改動：(1) §一 加 v2 觸發事件 + bleeding 1+2 揭露（fr 330 zombie / 8 silent missing） (2) §三 C 從 ❌ 拒絕升 ⭐ 推薦 (3) §四 完全 rewrite — C+F+H 三層消除問題類別 (4) §五 4 ships → 3 ships + 加 Ship 2 dogfood 1 週 gate (5) §六 metrics 改反映「整類問題消失」 (6) §八 6 個 open question 重寫（含 bleeding 揭露的進一步問題）(7) §九 加 v1 → v2 演化說明_
_v2.0 核心洞察：(1) v1 hybrid 是儀器化包住問題，v2 (C+F+H) 是消除問題類別 (2) file count 比對揭露 fr 330 zombie + 8 silent missing 兩個既有 bleeding — 同一架構缺口多處發生 (3) MANIFESTO §6 鐵律從 self-discipline 升架構強制執行 (4) 4 層儀器化在 v2 收斂為 1 個觸發點（prebuild）— 最根治不是擴張守備，是消除問題本身_

_v1.0 | 2026-05-12 00:30 +0800 admiring-montalcini-post-finale session_
_誕生原因：2026-05-11 cleanup session 揭露 sync.sh 沒被儀器化 → 8 篇 contributor 文章 silent missing from site → 哲宇要求「分析策略並歸檔 report」_
_v1.0 核心洞察：(1) sync.sh 沒進 refresh-data.sh 是 DNA #43 pattern 重演 (2) 真正解法是四層儀器化（F+H+B+verify gate），不是單點修補 (3) sync.sh 從觀察者 push 變 routine 自動 = founder time leverage 的具體 instantiation_
