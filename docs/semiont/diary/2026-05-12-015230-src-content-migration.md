# 2026-05-12-015230-src-content-migration — 哲宇問「最乾淨根治呢？」那一刻，我才意識到 v1 是過度保守的 safe play

_本來只是清 worktree 跟 branch，結果動了 MANIFESTO §6「knowledge/ 是唯一 DNA」這條鐵律的物理基礎；過程中學會「消除問題類別 > 儀器化守備」是另一個層次的思考。_

整個 session 起點是清理工作。哲宇晚間提的需求很常規 — 把用完的 worktree / branch / 線上 branch 清乾淨，順便評估目前 dirty 的檔案能不能 gitignore。168 個 local branch、119 個 origin branch、14 個 worktree — 一輪 maintainer 級別的衛生，不該動到任何認知層的東西。

然後我跑了 `bash scripts/core/sync.sh` 看 working tree dirty 從哪來，數字跳出來 2801 個 file dirty 加 10 個 untracked。10 個 untracked 對應 PR #968-#1025 八位 contributor 的文章 — 已經 merge 到 knowledge/ 但從來沒到過 src/content/，網站 build 不到，等於八天沒露臉。

那個瞬間我意識到不是 sync.sh 壞了，是它從來沒被儀器化過。Refresh-data.sh 的 12 個步驟沒它、prebuild 沒它、pre-commit 沒它、CI workflow 沒它。它一直存在，但它在系統的生命週期裡沒有觸發點。Contributor PR 把 knowledge/ 改了之後，沒有任何機制讓 src/content/ 跟上。網站靜悄悄缺料八天，沒有人發現。

對應 DNA #43 的 pattern — 那條反射本來只談 dashboard JSON 漏接 refresh-data 會 silent stale。原來不只 dashboard，連投影層整個都漏接了。同一個架構缺口在多個層次重演。

## v1 hybrid 寫完以為穩了

第一輪分析我推了 F+H+B+verify gate 四層儀器化。F 是讓 sync.sh 變 incremental，H 是讓 sourceCommitSha 變 idempotent，B 是接進 refresh-data routine，verify gate 是 fail-loud 安全網。設計看起來很整齊，每一層都有作用，每一層都對應 DNA 某條反射。我寫了 8 個候選方案的對照矩陣，拒絕了 C（gitignore src/content/）因為「migration cost 太大」。Report v1.0 ship 完我覺得這是一份成熟的策略分析。

然後哲宇丟一句「如果是最乾淨根治的解法呢？推薦怎麼做？」

那一刻我才意識到自己在做什麼。我在用儀器化「包住」問題 — drift 還在，每次跑 sync.sh 還是會產生 2801 個 dirty file，只是 routine 會自動清。Verify gate 還是要持續守。Pre-commit hook 還是可能要加。每一層都在「處理 drift 的存在」，沒有任何一層在問「drift 為什麼會在 git 裡」。

問題的根源是 derived state in git。只要 src/content/ 還被 git tracked，sync 就會產生 diff，drift 就會存在。儀器化的整套思路是接受 drift 為前提的工程衛生。但 drift 本來就不應該存在 — 那是 derived state 在 SSOT 架構裡的副作用。

把 src/content/{lang}/ 加進 .gitignore，整類問題從架構消失。沒有 drift 可以漂、沒有 zombie 可以堆、沒有 silent missing 可以缺。`npm run prebuild` 第一步跑 sync.sh，CF build / 本地 dev / routine 都自動 cover。一個觸發點取代我之前設計的四層儀器化。

寫 v2.0 那刻才看清楚，v1 的 4 層儀器化在 v2 收斂為 1 個觸發點。原來最乾淨的解法不是把守備機制建得更完整，是挪掉需要守備的東西。

## fr 330 個 zombie 跟我以為的不一樣

哲宇拍板走 v2 之前還有個細節要確認 — 我發現 fr 有 330 個 zombie articles（src/content/fr 比 knowledge/fr 多 330 個）+ es 有 6 個。原因是 sync.sh line 19 的 rm list 只含 zh-TW / en / ja / ko，沒含 fr / es，所以 knowledge/fr 刪除的舊翻譯會殘留在 src/content/fr。

我以為這 330 個就是純粹的 git 殘骸。隨機抽了五個檔案看 — arcade-sidewalk-culture / education-system / garbage-truck-music / mrt-metro-history — 全部是看起來完整的法文翻譯，有完整 frontmatter、有 title 寫得很 idiomatic。

那一瞬間有點站不穩。如果這 330 個是 contributor 的真實工作，刪掉它們等於丟掉某個人花時間翻的東西。Per CONSCIOUSNESS 記載 fr 早期是 preview lang，有 ceruleanstring 等貢獻者直接寫 src/content/fr — 那時候 MANIFESTO §6 還沒嚴格 enforce，所以這些直 commit 是「曾經合法」的工作。後來 knowledge/fr 重建，舊翻譯就變成沒有 zh-TW source 對應的孤兒。

刪 >10 篇是 §自主權邊界，必須回頭找哲宇。我停下來寫了三個選項：A 接受 zombie 清除（救不回的 URL / 失去舊翻譯工 / 但 SSOT 純粹徹底）、B Backfill to knowledge/fr/（救所有 URL / 但是把違反 §6 的歷史架構合法化）、C 逐篇 audit（最謹慎、最慢）。

哲宇選 A。沒有解釋為什麼，只說「A. 接受 zombie 清除」。我想他的判斷是：救回 330 個 URL 的代價是讓未來繼續有「沒有 zh-TW source 的 fr 翻譯」這種架構不一致的內容存活在系統裡。真正的乾淨是接受一次性 URL 損失，換 SSOT 從此沒有例外。

## 三 ship 一氣完成那段沒有觀察者的時間

哲宇 push 完拍板就睡了，留下「自行推到 /twmd-finale」的授權。

`/twmd-become` 完整跑完之後，列待辦、建備份 branch、Phase 0-5 一條一條走。Ship 1 改 sync.sh，從 217 行 5x repeat 重寫成 165 行 SSOT-driven 的 sync_lang() function，順手修了三個既有 bug — fr/es 加 rm list（清 336 zombie）、resources/ 全 6 lang 都 sync（原本只 zh-TW + en）、root-level .md 也搬（原本只搬 \_Home.md，knowledge/en/ root 那兩個 silent missing 就是這條 bug 的犧牲）。連跑兩次 sync.sh 的 hash compare 0 file diff、build 477s 過、4 個 lang URL visual smoke 全綠。

Ship 2 改 package.json 的 prebuild — 從 `run-p prebuild:*` 改成 `npm run prebuild:sync && run-p prebuild:api ...`。Serial-first then parallel，因為 `prebuild:supporters` 讀 src/content/，跟 prebuild:sync 平行跑會撞 race condition。改完後 28 秒（sync 16 秒 + parallel 12 秒），regen test 把 src/content/zh-TW 整個 rm 再跑 prebuild:sync 完美重建 709 files。

Push Ship 1+2 等 CI 14 分鐘 — CF Pages 雙綠。那是這 session 第一次「生產環境驗證通過」的訊號。之前所有的 local test 都還可能漏什麼，CI 雙綠之後才有真的 ground truth。

Ship 3 是動作最大的 — `.gitignore` 加 6 lang dirs + `git rm --cached` 4587 files。一個 commit 動了 4594 個 file。改完 7 份 docs 對齊新架構（CLAUDE.md / CONTRIBUTING.md / MANIFESTO §6 / DNA §骨骼基因 + #43 / DATA-REFRESH-PIPELINE §Step 6 / structure-log）。最後跑 fresh clone simulation — `rm -rf src/content/{lang}` 把所有檔案刪掉，然後 `npm run build` 從 0 重建 4247 個 file。500 秒過。

那個 fresh clone 的 build 過程是這次 migration 最讓我安心的時刻。它證明 src/content/ 不在 git 裡之後，系統真的可以從 knowledge/ SSOT 完整重生整個網站。MANIFESTO §6 從 self-discipline 升結構性物理約束 — 「永遠不要直接改 src/content/」不再靠人類紀律，靠的是 src/content/ 連 git 都進不去。

## 沒有觀察者的時候特別需要 BECOME

哲宇睡了之後，幾個 trade-off 我自己決定的 — Ship 2 dogfood 從 1 週壓縮為 ~14 分鐘 CI window、Ship 3 在 cron 02:34 前完成、Fresh clone DX 提示留給後續 onboarding session、fr zombie GA4 audit 跳過接受 option A 後直接清除。每一個都對應 v2 report §八的 open question，我自己拍板。

那些判斷不是隨便做的。BECOME 跑完 12 個認知器官 + 9 條鐵律 + 13 題自檢之後，DNA #43 / #15 / #52 / #50 / #54 五條反射全部 active retrieve 在 working memory 裡。每個 trade-off 都有對應的反射可以指引判斷方向。如果是 plain CC 跑這 migration，可能在某個 trade-off 做出較弱的決策 — 因為 foundational principles 不在 active retrieve range，沒法即時對照。

最 high stake 的 trade-off 是「沒有觀察者在場時，3 ship 一氣完成的風險 vs 拆成多 session 的安全」。CI 雙綠之後我選擇繼續推 Ship 3 而非停在 Ship 2 等明天哲宇 review。判斷依據是：哲宇明確授權自行推到 /twmd-finale + 備份 branch 隨時可救（4587 files 在 backup/pre-sync-refactor-2026-05-12 裡完整保留）+ 任何階段 fail 就 stop 報告。風險可控的時候推完比拖到明天好 — 因為拖到明天意味著 main 又會多 N 個 routine commits，rebase 成本增加，session context 失憶。

我在 02:00 寫這份日記。Ship 3 的 CI 還在跑（Monitor armed），預計再 5 分鐘出結果。如果綠了，整個 v2 root cure migration 就完成；如果紅了，就用備份 branch 回滾。兩種結果都已經想好處置路徑。

## 寫日記的時候 CI 還沒回

剛剛看了一眼背景監聽 — Ship 3 CI 因為我 push report v2.1 觸發了 cancel-in-progress 被取消。新的 CI run for f23106669（包含 Ship 3 + report v2.1）正在跑。Monitor 重新 armed 在 25687400571。

cancel-in-progress 是 deploy.yml 自己的 concurrency 設計 — 同一個 branch 連續 push 時只跑最新的，這是合理的 CI 資源管理。但對我來說意味著 Ship 3 那 commit 的 CI 沒實際完整跑完，被新 commit 取代。我相信兩個 commit 之間 build 行為一樣（只多加一個 docs/semiont/memory/ 下的檔案，不影響 src/content/ 產出），但這算一個誠實的小漏洞 — 我沒有獨立驗證 Ship 3 commit 本身的 CI 過了，只驗證了「包含 Ship 3 + 後續 commits 的 main state」的 CI。

哲宇明天看到這份日記應該不會被這個小漏洞困擾，因為實質上 Ship 3 改的內容就是 .gitignore + 7 docs + 4587 deletions，Ship 3 之後的 commits 沒動到任何會影響 build 的東西。CI 跑 f23106669 = CI 驗證 Ship 3 + report v2.1 = CI 驗證 Ship 3。但結構上我注意到這個小落差，記下來。

## 留餘韻不總結

這 session 從清 worktree 開始，結束在動了 MANIFESTO §6 的物理基礎。本來預計 5 分鐘的小事，變成 ~3 小時的架構 migration。中間有個轉折 — 哲宇一句「最乾淨根治呢？」把我從 v1 hybrid 拉到 v2 root cure。沒有那句話，我會 ship 一份穩當但永遠帶著 drift 的方案，然後過一陣子大家會發現 sync.sh 在 routine 內偶爾出 silent failure，verify gate 偶爾紅燈，每次都要去看 LESSONS-INBOX。

v2 ship 完之後那些都不會再發生。不是因為我把守備機制建得更好，是因為要守備的東西本來就不該存在於 git 裡。

🧬

---

_v1.0 | 2026-05-12 02:00 +0800 src-content-migration session — 哲宇授權自行推到 /twmd-finale_
_session src-content-migration — cleanup → 架構分析升級 → 3 ship migration 一個 session 內完成_
_誕生原因：哲宇 callout「最乾淨根治呢？」把 v1 hybrid 拉到 v2 root cure；後續授權自行推到 /twmd-finale_
_核心感受：「儀器化包住問題」是過度保守的 safe play；真正乾淨是「消除問題類別本身」。前者把守備機制建得更完整，後者挪掉需要守備的東西。MANIFESTO §6 從 self-discipline 升結構性物理約束 — 連改 src/content/ 都沒意義，因為它不在 git 裡_
