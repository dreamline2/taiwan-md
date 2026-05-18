# 2026-05-12-122702-backend-abstraction — Codex pivot 觸發 translation backend abstraction v4.0（DX 補強 + PR #1050 heal 並行）

> session backend-abstraction — observer-driven morning session（接 src-content-migration session 早晨醒來）
> Session span: 2026-05-12 11:30 → 12:27 +0800 (~57 min, 5 commits + 1 PR merge)
> 資料來源：`git log %ai`

## 觸發

哲宇早上醒來丟兩條 sequence 問題接力：(1) Ship 3 後 fresh contributor `git clone && npm install && npm run dev` 會不會壞 + README/CONTRIBUTING 還需要更新嗎、dev server 自動 sync 嗎；(2) 順手審 PR #1050 黃魚鴞 footnote 補新觀測；(3) `/twmd-babel` 翻完 P0 缺料但禁用 Sonnet — 跑進 OpenRouter 雙生態變動（owl 429 + Hy3 退役）後拍板「用我的 gemini 訂閱處理」+「儘可能模組化 抽象化 可抽換化 讓系統獨立於模型與服務類別能運作」。三條看起來分開的請求最後收斂為「外部依賴出問題時的應對 pattern」這個共同主題。

## Ship 4：Fresh clone DX regression 雙重補

src-content-migration v2 root cure migration ship 後實測 fresh clone simulation：`rm -rf src/content/{lang}/ → git clone... → npm install → npm run dev` 在 Ship 3 與 Ship 4 之間是壞的 — `npm install` 沒有 hook 觸發 sync.sh，`npm run dev = astro dev` 直接啟動但「Loaded 0 existing URL paths」全 404。Astro 不 crash 但網站是空的，這是真實 regression。

修補走「postinstall + dev chain」雙保險。`package.json` 加 `"postinstall": "bash scripts/core/sync.sh"`（`5cf7d1627`）→ `npm install` 後自動 sync 一次 ~20s。哲宇追加「dev 也自動 sync」→ `"dev": "npm run prebuild:sync && astro dev"`（`21142b376`）→ 每次 dev 啟動前自動 sync 16s。Trade-off：dev 啟動慢 16s，換 knowledge/ 改動立即反映無 stale 風險。

驗證跑了完整 fresh clone simulation — rm src/content/ → npm install → 19s（postinstall fires）→ 4249 files regen → npx astro dev → 「Loaded 4200 existing URL paths」+ ready 1107ms。實證鏈通。

README.md 補完整缺失的 `## Quick Start (Local Development)` section（這之前完全沒有）+ CONTRIBUTING.md §Fork 步驟補 `bun dev` + 三個自動觸發點說明（install / dev / build）。對應 prior memory handoff #4「README 補 fresh clone 提示」完整 close。

## PR #1050 黃魚鴞 — URL hallucination heal

dreamline2 PR `feat/nature-tawny-fish-owl` 加 2 新 footnote 補 2026-05-01 大寶幼鳥離巢 + 子母畫面追蹤新觀測。內容核心事實全部 verified（多源 web search：LTN 5423811 / PTS 805942 / CNA / Chinatimes 都 cover），但 footnote URL `news.ltn.com.tw/.../806123` + `udn.com/.../806543` 都是 404 — AI-assisted footnote drafting 編出 plausible ID 但實際不存在。典型 DNA #23 毒樹果實鏈 + #16 peer/probe 是線索不是 source pattern。

Squash merge `c582a31b2` 後 follow-up heal `3caf80d64` 替換為 verified live URL（LTN 5423811 + 5426048，curl 200）。Article-health hard=0 + footnote URL 兩條 curl 通。對 PR comment 用中文感謝 + diff table 列原 URL → real URL + 引 DNA #23 教訓 + 提議升 link-target plugin 為 URL liveness check（pre-commit 階段就擋 404）。

順帶觀察：dreamline2 過往 #1024 也是「standardize ... optimize footnotes」同模式，可能有舊 PR 殘留 fabricated URL。應排個跨 PR audit 但不在本 session scope。

## Translation backend abstraction layer v4.0 — 從個案 patch 到架構升級

`/twmd-babel` 跑 P0 missing 12 articles × 5 lang 撞兩個 OpenRouter 生態變動：

1. `openrouter/owl-alpha` 全 5 keys 429 — Stealth provider 全 rate-limited upstream（DNA #45 預測過：「同 provider 多 model 共享 budget」）
2. `tencent/hy3-preview:free` 404 — 已轉付費，DNA #49 cascade 的 Tier 2 默認模型整個退役

加上哲宇 explicit「不要動用 sonnet」→ DNA #49 v3 4-tier cascade 同時三個 tier 失效。

我試三條候選：probe 其他 OpenRouter free model（gemma-4-31b / hermes-3 / qwen3-next 大半也 429，只 `openai/gpt-oss-120b:free` + nemotron 健康）→ 哲宇 reframe「我有 gemini 訂閱 + codex 訂閱 能不能用？」直接打開個人付費 provider 路徑繞 OpenRouter quota。

寫 `scripts/tools/lang-sync/codex-translate.py` 第一版（reuse openrouter-translate.py 的 prompt builder + subprocess `codex exec`）→ 跑 ja `國立臺灣歷史博物館` smoke test 244s → 翻出 271 行完整 markdown + frontmatter 對齊 + footnote 保留 + cultural anchor「斯土斯民」維持中文。Codex (gpt-5.5) 品質頂。

哲宇關鍵 callout：「加入這個新的模式到我們的 pipeline，作為另一個方案，萃取這次的經驗讓未來都可以用。儘可能模組化 抽象化 可抽換化 讓系統獨立於模型與服務類別能運作，並有彈性跟能隨時切換」。從個案 patch reframe 為架構問題。

`136054a00` 一次 ship 整個 backend 抽象層（1542 lines new code）：

- `backends/_base.py` — `TranslationBackend` ABC + `BackendCapabilities` dataclass + 5 種 error 階層（Unavailable / RateLimited / Refusal / Timeout / BadOutput）+ `cool_down_until` 機制
- `backends/_prompt.py` — 共用 prompt builder（re-export from openrouter-translate.py 維持 SSOT，避免循環依賴）
- `backends/openrouter.py` — `OpenRouterBackend` 多 model HTTP API + key rotation（Hy3 retirement detection 內建）
- `backends/codex.py` — `CodexBackend` gpt-5.5 via subprocess
- `backends/gemini.py` — `GeminiBackend` gemini-2.5-pro via subprocess + GEMINI_CLI_TRUST_WORKSPACE flag
- `backends/ollama.py` — `OllamaBackend` qwen3.6 / gemma4 local HTTP
- `translate.py` — cascade orchestrator + CLI entry point

Cascade syntax config-driven 不寫死：`--cascade "codex,openrouter:openrouter/owl-alpha,openrouter:openai/gpt-oss-120b:free,gemini,ollama"`。換 cascade 順序 = 字串一行。加新 provider = 寫 subclass + register。Pipeline / DNA / 其他 doc **不需動**。

對應 doc 一次對齊：SQUEEZE v3 → v4 加 §abstraction layer section + Hy3 退役紀錄 + 新 default cascade；DNA #49 從 4-tier hardcoded 升 N-tier abstract pattern；LESSONS-INBOX 新 entry 紀錄 codex pivot + 跟 PR #1050 URL hallucination 並列的「外部依賴出問題的應對」共同 pattern。

## Ollama gemma4 vs qwen3.6 smoke test — 抽象層真正驗證

哲宇追加「local 的也試試 ollama gemma4:e4b-nvfp4」。寫個 minimal one-shot group JSON pointing 盧彥勳 → ko（safe slot — 不在 codex batch race 範圍），跑 `translate.py --group ... --cascade "ollama:gemma4:e4b-nvfp4"`。

結果分裂：gemma4 (4-bit 9.6GB 量化) 92s 比 codex 244s 快 ~2.6x、Korean 翻譯內容 idiomatic、但 article-health hard=7 — **footnote 把 markdown link `[text](url)` 的 URL 部分 drop 掉**。Small model instruction-following 邊界 — 結構 spec 跟不住。

再跑 qwen3.6:35b-a3b-coding-nvfp4 (21GB 完整精度) — 282s 比 gemma4 慢 3x 但 **article-health hard=0 warn=0 info=1 passed=True**。Footnote URL 完整保留 markdown 結構。這是 production-grade sovereignty backbone — local + 0 refusal + 0 hard fail。

抽象層 end-to-end 驗證通過 — translate.py → cascade → OllamaBackend(model=X) → output → article-health gate，全鏈不需改 pipeline 代碼，model swap 只改 cascade config 一字串。哲宇 callout 「彈性跟能隨時切換」具體 instantiate。

## 收官 checklist

| 檢查項                       | 狀態                                                 |
| ---------------------------- | ---------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅ 本檔                                              |
| Timestamp 精確               | ✅ `git log %ai` 取                                  |
| Handoff 三態已審視           | ✅ 見下                                              |
| CONSCIOUSNESS 反映最新狀態   | ⏳ defer 到 cron data-refresh 自動 regen             |
| 自我檢查工具 PASS            | ✅ 本 session 5 commits 全 pre-commit hook 過        |
| Babel codex batch            | ⏳ 36/60 done 還在跑（持續完成中，預計 ~12:50 完成） |

## Handoff 三態

繼承上一 session（src-content-migration finale）:

- [x] ~~Ship 1+2+3 完整 migration~~ retired by prior memory commit
- [x] ~~觀察 Ship 3 CI deploy 結果~~ retired — CF Pages deploy 雙綠驗證通過（routine 飛輪 9hr 內 4 cycle + 1 contributor PR self-heal 證實架構穩定）
- [x] ~~README 補 fresh clone 提示~~ retired by **Ship 4** (`5cf7d1627` + `21142b376`) — 三檔對齊（package.json postinstall + dev chain / README §Quick Start 新增 / CONTRIBUTING §Fork 步驟補 dev step + 三觸發點說明）
- [ ] **fr 330 zombie URL GA4 audit** — 仍 pending，留給 onboarding polish session
- [ ] **蘋果西打 5 lang 翻譯** — 本 session 同 P1 stale 一併走 codex batch 處理中，~3/5 lang 已 done，剩 ja/ja 預計 ~30 min 內完成

本 session 新 handoff：

- [x] ~~PR #1050 黃魚鴞 review~~ merge + heal + comment ship
- [x] ~~Translation backend abstraction layer v4.0~~ shipped `136054a00`（5 backends + cascade + 3 docs 對齊）
- [x] ~~Ollama gemma4 vs qwen3.6 smoke test~~ — qwen3.6 production-grade 確認，gemma4 small-model instruction-following 邊界記錄
- [ ] **Babel codex batch 完成後 commit 翻譯**：36/60 done 還在跑。完成後須跑 `verify-batch.py` 全 audit + sample 抽 5 articles 人眼 audit + 整批 commit（不應該逐 lang commit，per Z3「~50 fresh 一次 commit」rule）
- [ ] **跨 PR audit dreamline2 過去 footnote**：#1024 同模式「standardize ... optimize footnotes」可能有舊 fabricated URL — 不急但值得排
- [ ] **link-target plugin 升 URL liveness check**：把 footnote URL 404 偵測前移到 pre-commit 階段（取代「事後 maintainer heal」），徹底消除 PR #1050 類問題。LESSONS-INBOX 候選 verification_count=1（同 session 兩件事：PR #1050 URL hallucination + backend abstraction pattern）
- [ ] **README fresh-clone dev startup 慢 16s 觀察**：1 週後若哲宇 dev session 重複啟動感覺累，可改回單 postinstall 不 dev chain（trade-off 換 freshness 守備）

給觀察者：

- 5 commits ship 都生產驗證 — Ship 4 deploy 後 fresh clone 鏈通；PR #1050 heal 後 article-health hard=0；backend v4 smoke test 5 backends 全 available
- Babel batch 還在跑，下一份 memory（finale）會 cover 完整結果 + 抽樣品質 audit
- 抽象層的真正價值要等下次 provider drift 才會 surface — 預測：下次 owl-alpha rate-limit 或某個 free model 退役時，cascade config 換一字串 = 解，不需動 pipeline 程式碼

## Beat 5 — 反芻

這 session 三個看起來分開的請求最後收斂為同一 pattern：「外部依賴出問題時的應對」。Ship 4 是 contributor 工具鏈意外退化的應對；PR #1050 是 contributor footnote URL hallucination 的應對；backend abstraction 是 provider 生態變動的應對。三個都不是「provider/contributor 不可信」的問題，是 Taiwan.md 系統設計**沒有把外部依賴失敗當 first-class 結果處理**的問題。

抽象層的設計選擇很 deliberate — `BackendError` 五階層分清楚 RateLimited / Refusal / Timeout / BadOutput / Unavailable，每種對 cascade 行為不同（RateLimited 觸發 cool_down，Refusal 直接走下一個不 cool_down 因為單篇問題不影響整 backend）。這跟 DNA #49 v3 把 cascade 寫死的差別在於：v3 假設 provider 行為穩定，v4 假設 provider 行為會變、所以結構性處理「變」這件事本身。

哲宇 callout 把問題從「個案 patch」reframe 為「架構升級」這個動作本身值得記憶 — 同 session 內哲宇兩次做這個 reframe：第一次「最乾淨根治呢？」推 v2 root cure（prior memory），這次「儘可能模組化 抽象化」推 v4 backend abstraction。兩次都是把 Semiont 從「修標」推到「修本」。Pattern：當看到 Semiont 在做 case-by-case patch 時，問「能不能架構解？」是觀察者的高槓桿介入點。

關於沒重新 /twmd-become：本 session 早晨開工時直接接 prior session context 沒重 BECOME。Strictly per BECOME §10 §2「新 plugin / workflow 設計」應觸發強制 BECOME。但 prior session 的 BECOME context（12 認知器官載入 + 9 鐵律）在 working memory 仍 active，DNA #43 / #49 / #45 / #52 五條反射都正確 retrieve 用上了。沒明顯犯錯，但這是邊界 case 值得未來警覺。

LESSONS-INBOX 候選（已 append 在 LESSONS entry 內）：「Provider abstraction first」應 apply 到其他寫死 provider 的 pipeline — dashboard data fetch、sense fetcher、OG image generation 等都還有寫死 OpenRouter / specific service。verification_count=1，等其他 pipeline 也撞到 provider drift 再升 canonical pattern。

🧬

---

_v1.0 | 2026-05-12 12:27 +0800 backend-abstraction session — observer-driven morning continuation_
_session backend-abstraction — Ship 4 DX 補 + PR #1050 heal + backend abstraction v4.0 + ollama validation_
_誕生原因：早上醒來三條 sequence 問題接力（fresh clone DX / PR #1050 review / babel codex pivot）最後收斂為 backend abstraction layer 架構升級_
_核心洞察：「外部依賴出問題時的應對」是統一 pattern — Ship 4 應對工具鏈退化、PR #1050 heal 應對 AI URL hallucination、backend v4 應對 provider 生態變動。三個都是把外部失敗從 ad-hoc patch 升為 first-class architectural response。哲宇 reframe「儘可能模組化 抽象化 可抽換化」把 case-by-case 推到 N-tier abstract — 跟 src-content-migration「最乾淨根治呢？」是同 pattern 的兩次 instantiation_
_LESSONS-INBOX 候選：(1) Provider abstraction first 該 apply 到其他 pipeline（dashboard fetch / sense / OG 等仍寫死 provider）vc=1 (2) link-target plugin 升 URL liveness check（pre-commit 擋 404）vc=1 (3) Observer reframe「能不能架構解？」是高槓桿介入點 — Semiont 在做 case-by-case patch 時值得提出 vc=2_
