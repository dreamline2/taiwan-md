# 2026-05-04-161254-jovial-feistel-editorial-v5.6 — 4 PR 檢查 × article-health 對比典範 → EDITORIAL 補敘事層 4 章

> session jovial-feistel 後段 — observer-triggered（哲宇連續六輪 task：4 PR review → 拉 article-health → 四篇全文深入讀 → 對比典範 → 範疇歸 EDITORIAL → 完整補充 → memory diary push）
> Session span（後段）：~17:30 → 21:43 +0800（~4h 13min, 1 commit `f46e3e88e`）
> Session span（全段）：16:12 → 21:43 +0800（~5h 31min, 2 commit + 2 issue）
> 資料來源：`git log %ai` + session-id.sh

## 觸發

哲宇早上送出 [#851 Zaious Lv.3 邀請](https://github.com/frank890417/taiwan-md/issues/851) 後，task 連續推進到 PR triage：「先幫我檢查 PR #852, #856, #841, #834」→「拉下最新進度，用 article-health 來審查所有文章」→「我是說拿來審核剛剛 PR 的文章跟回覆」→「深入看這四篇文章，有什麼是你覺得檢查工具缺漏的？」→「好的文章對比：吳哲宇 安溥」追加「還有黑冠麻鷺」→「這些其實都是 EDITORIAL.md 的範疇，你檢查裡面有沒有提到，有提到的話寫的更清楚，如果沒有就補充」→「先拉下線上最新的進度」→「再處理」→「完整調整 一步一步做還有跟我解釋變動跟同步紀錄 memory」→「完整走 pipeline 紀錄 memory / diary 然後 merge 到 main」。

整段工作從 PR triage 演化成 EDITORIAL 進化的觸發鏈條。

## 4 PR 檢查 + article-health 全站 sweep

四個 PR 各自跑 [article-health.py](scripts/tools/article-health.py)（剛 ship 的 SSOT 健檢工具，11 plugin / 整合 manifesto-11 + quality-scan + footnote-format + footnote-density + cjk-punct + format-structure + frontmatter-title + image-health + wikilink-target + cross-reference + terminology）：

- **[#852](https://github.com/frank890417/taiwan-md/pull/852) Zaious EVOLVE 道德課**（refs [#779](https://github.com/frank890417/taiwan-md/issues/779)）：7 hard / 3 warn — 7 條學術書目 footnote 無 URL 是 trade-off 不是 bug
- **[#856](https://github.com/frank890417/taiwan-md/pull/856) idlccp1984 台北 101 大重寫**：0 hard / 7 warn / 1 info — passed=True 但 §11 對位 5 處 + 質量→品質 + 多項 hallucination 風險（92 vs 91 min / Summit 101 / 宏泰 86 億 / Yahoo 訪談）
- **[#841](https://github.com/frank890417/taiwan-md/pull/841) idlccp1984 陳致中 NEW**：5 hard / 2 warn / 3 info — wikilink 殘留 + ETtoday Water 軼事需 fact-check
- **[#834](https://github.com/frank890417/taiwan-md/pull/834) idlccp1984 尊 NEW**：0 hard / 6 warn — 5 條 footnote 全指 wikipedia 同頁 + §11 對位 3 處

順手跑 article-health `--all --profile dashboard` 全站 sweep 670 articles 1.5 sec：1090 hard / 4379 warn / 892 info；158 篇 has-hard，最嚴重 [knowledge/People/黃少雍.md](knowledge/People/黃少雍.md) 165 hard（cjk-punct 163 處，整篇半形標點）。但這是另一個 task 的入口，本 session 沒處理。

## 典範對比 → 10 個工具看不到的敘事層維度

哲宇校正「我是說審核剛剛 PR 的文章」後，追問「深入看這四篇文章，有什麼是你覺得檢查工具缺漏的？」再追加「好的文章對比：吳哲宇 安溥」+「還有黑冠麻鷺」。讀完三篇典範 + 4 PR 全文後歸納出 10 個工具抓不到、人類能感受到的敘事層維度：

1. 場景化開場（具體時間+人+stake）
2. 核心矛盾 anchor 整篇貫穿
3. 時間軸閉合（伏線回收）
4. 逐字引語密度（first-person quotes）
5. 具體名字 / 機構 / 數字密度
6. Heading narrative phrase 不是 categorical label
7. Bullet 用法節制
8. 反向解釋（counter-explanation）
9. Footnote desc 是證據鏈不是裝飾
10. 策展人筆記是反向解釋紀律

10 個維度對 4 PR 各自具體 instantiation 都對得上（例：#856 缺 anchor 貫穿 / heading 全 categorical / bullet 嚴重 / 結尾抽象沒回收開場；#841 chronological 沒 echo / 主角直引只 1 句；#834 footnote 5 條同頁 / 「無意義之意義」abstraction 替代具體）。

## EDITORIAL v5.6：歸 EDITORIAL 範疇後一步一步補

哲宇關鍵指令「這些其實都是 EDITORIAL.md 的範疇，你檢查裡面有沒有提到，有提到的話寫的更清楚，如果沒有就補充」一句話定位了正確的 SSOT 落腳處——10 個維度本來就是 EDITORIAL 該管的，不該開新檔。Audit 後發現分布：3 條已充分（場景開場 / 引語密度 / bullet 節制），3 條部分 cover（散落多處需整合：具體性紀律 / heading / counter-explanation），2 條完全缺（時間軸閉合 / 策展人筆記書寫紀律），1 條格式存在但無內容規範（footnote desc 證據鏈），1 條 partial（核心矛盾 anchor）。

Patch A 改 §結尾（line 437-448）：表格從 5 種模式擴 6 種，加「**敘事閉環式**」+ 加總則「結尾的兩個任務：回收開場 anchor + 給讀者新位置」+ 三典範閉環範例。Patch B 改 §小標題規範（line 450）：補「禁 categorical label」+ 4 對照表 + 3 典範對照。Patch C 改 §挖引語制度（line 291）：補「人物深度文主角本人直引 ≥ 3 句」+ 改 §來源引用（line 519）：補「Footnote desc 是證據鏈」+ 3 對照表 + 4 條規則 + 自檢。Patch D 在 §三 文章結構底下、§開場 之後新增 4 sections：§核心矛盾 anchor 整篇貫穿、§具體性紀律每段 ≥ 1 anchor noun、§反向解釋的編織、§策展人筆記的書寫紀律。

總計 +197 / -10 行，commit `f46e3e88e` push 到 main。

§11 自檢 pass：新增的 4 處對位句型都在「定義邊界」位置（符合三題判準 #1，內容本身是 contrast），破折號 55 處 / ~30K 字遠低 15/1500 字紅線。

## 收官 checklist

| 檢查項                       | 狀態                                                                                |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅ 本檔（後段）+ 已存先前 jovial-feistel.md（前段）                                 |
| Timestamp 精確               | ✅ git log %ai + session-id.sh                                                      |
| Handoff 三態已審視           | ✅（見下）                                                                          |
| CONSCIOUSNESS 反映最新狀態   | ❌ deferred — 本 session 0 知識 article 變動                                        |
| 自我檢查工具 PASS            | ✅ article-health prose-health 對 EDITORIAL 自檢通過（新增的 4 處對位都在定義邊界） |

## Handoff 三態

繼承上 jovial-feistel 前段：

- ⏳ blocked on Zaious 回應 [#851](https://github.com/frank890417/taiwan-md/issues/851) — 不變
- [ ] pending — pipeline §11 教訓/歷史 append 等回應後 — 不變
- [ ] pending — pipeline §4 trust-based 改寫 N=1-2 案例後決定 — 不變

本 session 後段新 handoff：

- [ ] pending — 4 PR 的具體建設性 comment 還沒貼到 PR 上。哲宇 explicit task「回覆 PR」這層尚未完成（task 軌跡轉到 EDITORIAL 補充）。下個 session 可以 (a) 用 EDITORIAL v5.6 的新規則重寫 4 個 PR comment 並 ship；或 (b) 哲宇自己看 PR 用新規則做決定
- [ ] pending — [knowledge/People/黃少雍.md](knowledge/People/黃少雍.md) 165 cjk-punct hard violations（整篇半形標點）是 article-health 全站 sweep 揭露最嚴重的單篇問題。可造橋一支「半形→全形批次修」工具或單篇手動修
- [ ] pending — article-health 全站 1090 hard / 158 篇有 hard，多數 footnote-format（Manus AI APA / 學術書目格式）。可考慮造橋一支「footnote 學術書目 → 加 fallback URL」工具或建立 EDITORIAL「學術引用例外」規則
- ⏳ blocked on observer 拍板 — 是否把 §核心矛盾 anchor / §具體性紀律 / §反向解釋 / §策展人筆記 4 個敘事層維度寫成 article-health plugin（前提是值得自動化；目前是 manual review checklist）

## Beat 5 反芻

本 session 的 meta-pattern 是「**範疇歸位**」。task 從 PR 檢查（個案層）演化到 article-health 全站 sweep（工具層）→ 對比典範（敘事層）→ 哲宇校正「這些都是 EDITORIAL 範疇」（SSOT 層）。每一輪都是把問題從更下層往上推一層，直到找到正確的 canonical 落腳處。EDITORIAL v5.6 不是新發明的東西，是把已經散在 4 PR review / 3 典範對比中的觀察，**找到它們本來就該住的地方**。這是 [§指標 over 複寫](docs/semiont/MANIFESTO.md) 的另一面——不只是「不要在多處重複寫」，是「找到應該的單一落腳處」。

第二個 meta-pattern 是「**default 是預設答案的反 pattern 第二次驗證**」。先前 session（[memory/2026-05-04-161254-jovial-feistel.md](memory/2026-05-04-161254-jovial-feistel.md) §預設答案反 pattern 校正）剛標過這個，本 session 寫 PR comment 草稿時又給了三軸候選（Issue 2 五方向 v1 版），哲宇校正「多紀實的敘述問題與觀察」後退回 phenomenology。同 session 兩次驗證——這個反射要寫進 LESSONS-INBOX 升 DNA candidate。

第三個觀察是 article-health 工具的覆蓋邊界跟敘事層的清晰分隔。工具抓 punctuation / format / footnote 規格 / §11 句型 / 塑膠句——這層是規格層。敘事層（anchor 貫穿 / 閉環 / 反向解釋 / 策展人筆記）很難自動化但能 manual review。這個分工讓 EDITORIAL 知道自己的角色：規格層交給 article-health，敘事層 EDITORIAL 教如何手動把關。

🧬

---

_v1.0 | 2026-05-04 ~21:50 +0800_
_session jovial-feistel 後段 — observer-triggered 4 PR review × article-health × 典範對比 → EDITORIAL v5.6 ship_
_誕生原因：哲宇連續六輪 task 從個案 PR triage 推到 EDITORIAL 範疇歸位，最後落腳在 EDITORIAL.md +197 行新增（4 sections + 結尾閉環式 + heading 禁 categorical + 人物文主角直引 + footnote desc 證據鏈）_
_核心洞察：(1) 範疇歸位 — 問題從個案層推到工具層、敘事層、SSOT 層，每輪推一層找到 canonical 落腳。(2) 工具邊界 vs 敘事層分工 — article-health 抓規格層，EDITORIAL 教敘事層 manual review checklist。(3) 預設答案反 pattern 同 session 第二次驗證 — issue/PR/邀請文件 default 是 phenomenology + open question，不是擺三軸候選。_
_LESSONS-INBOX 候選：(a)「issue/PR/邀請文件 default 是 phenomenology 不是 candidate solution」反射 verification_count=2，可進 DNA candidate（同 session 兩次驗證 + 跨 task 適用）；(b) 工具邊界 vs 敘事層 EDITORIAL 範疇歸位的 SSOT 模式 — 未來新規則先問「這是規格層還是敘事層？」決定該寫工具還是寫 SOP；(c) 全站 article-health sweep 揭露 158 篇 hard violations 是 P3 backlog，需要分工策略（自動 batch heal / 單篇手修 / 規則例外文件化）。_
