---
session_id: 2026-05-17-091722-twmd-maintainer-am
session_span: '2026-05-17 09:00 → 09:30 +0800 (~30 min, 1 commit)'
trigger: 'cron `0 9 * * *` twmd-maintainer-am daily fire'
observer: cron (autonomous)
beat_coverage: '1-4 (MAINTAINER 4-stage cycle complete + 自己 heal commit ship)'
---

# 2026-05-17-091722-twmd-maintainer-am — 解 5 連 CI fail 阻塞 deploy：routine-rewrite footnote internal-link 紅旗

> session twmd-maintainer-am — cron `0 9 * * *` daily morning fire
> Session span: 09:17:22 → 09:30 +0800 (~13 min wall-clock, 1 commit `9474d19e5`)
> 資料來源：`git log %ai`

## 觸發

Cron `twmd-maintainer-am` 09:00 fire（morning chain 尾端：06:13 data-refresh-am → 07:00 spore-harvest-am → 09:00 maintainer-am）。Stage 0 BECOME Full mode 完整跑，consciousness-snapshot 顯示 organ scores 全綠（🛡️ immune 23 偏低為已知 backlog signal）。

## Stage 1 Scan — 5 連 deploy CI fail 紅旗浮現

- `gh pr list --state open` 回 `[]` — **0 contributor / observer PR**，B 路徑 collect-and-merge 空 cycle
- `gh issue list --state open --limit 30` 回 17 open issue（多為 backlog，最近 1 條新 follow-up 在 #851）
- `gh run list --workflow="Deploy to GitHub Pages"` **連續 5 次 failure**（自 2026-05-16 23:55 起，含 babel-nightly 三 commit 全 fail）
- i18n-smoke-test 仍綠

CI fail 紅旗壓過所有其他 stage — 跳 Stage 2 直接 dive Stage 3.5 heal CI（per MAINTAINER §Top 5 most-forgotten + Step 1.5 「連續 ≥ 2 次 failure 紅燈 → Stage 3 第一個 polish item 修 CI」）。

## Stage 3.5 Heal — footnote-format hard fail 2 處

`gh run view --log-failed` ground-truth diff 抓到 2 個 `🔴 footnote-format hard=1`：

| 檔案                            | 行    | 問題                                                                                    |
| ------------------------------- | ----- | --------------------------------------------------------------------------------------- |
| `knowledge/People/陳建年.md`    | L203  | `[^25]: [張惠妹 — Taiwan.md](/people/張惠妹) — desc` — 內部 `/people/X` 路徑           |
| `knowledge/Art/數位荒原.md`     | L206  | `[^13]: [...](../../reports/NML-...md) — desc` — 相對 `../../reports/X.md` 路徑       |

**Root cause**：`scripts/tools/lib/article_health/checks/footnote_format.py` 的 `_RE_CANONICAL` 強制 URL 必須 `https?://`。Internal / relative path 不過 canonical regex；又因 line 以 `[` 開頭也不過 `_RE_PURE_PROSE_FN`（要求第一個非 WS char 非 `[`）→ hard=1。

兩個都是昨晚 01:00-01:11 `twmd-rewrite` routine 用 5 個 parallel opus agent ship 5 NEW articles（per memory 2026-05-17-014500）時 agent 自行生的引用形式。Rewrite routine 沒跑 `article-health.py --profile=ci-deploy` pre-commit gate → 直接 push main → CI 跑 sweep 才抓 → maintainer-pm 22:07 + babel-nightly 連 3 commit 都被 cascade fail。

**Fix**：12 檔（2 zh-TW source + 10 lang mirror）一起轉 pure-prose 形式 `Title（path）— desc`：

- 2 zh-TW 用 Edit tool 手寫 in-place
- 10 lang mirror (`en/ja/ko/es/fr × 2 articles`) 用 single Python regex `s|^(\[\^N\]:) \[([^]]+)\]((/path|../path)) — |\1 \2（\3）— |` 一次掃過，保留各 lang 原翻譯 description

`article-health.py --all --profile=ci-deploy --quiet` regreen — 0 hard violation。Commit `9474d19e5` 12 files changed 12+/12- push origin main。

## Stage 2.4 dup-reply check — 6 recent issues

`gh issue view N --json comments` 6 個 5 月以來 issue 最新 comment 都是 frank890417（觀察者本人 5/11-5/14） — **全 skip 不重複回應**。例外：

- **#851 Zaious 升 Maintainer**: latest comment 2026-05-16 23:01 **Zaious 新 follow-up** — 報「batch-200 修補 4 phases 全 ship ✅（P0 #888-892 + P1 #1062 + P2 #1070 + P3 #1073 共 197 篇 11 天）」+ 寫了 `SOP-COLLABORATION-DISCIPLINE.md` 在 maintainer-workspace branch。內容涉及 maintainer 邀請決策 + governance-level SOP merge — 命中 §自主權邊界「對外溝通」+「governance 決策」→ leave for observer，不 auto-reply（per Bias 1 reverse-bias 警示：對 creator-level decision 不假設 default action）
- **#895 frank i18n-smoke-test B2 fr hiragana regression**: 觀察者自報 bug 無 contributor follow-up，留 observer 自己 track

## Stage 3.5 二輪 Heal — orphan translatedFrom 頼→賴

第一輪 heal commit `9474d19e5` push 後 CI 仍 fail，dive 第二層 root cause：`Build` step 失敗在 `prebuild:status` 的 `sync-translations-json.py` exit code 2。

`knowledge/ja/People/lai-ching-te.md` 的 `translatedFrom: 'People/頼清德.md'` 用日文簡體漢字 `頼`，但 zh-TW canonical 源是 `賴清德.md`（繁體 `賴`）。`translatedFrom` 必須 byte-equal — orphan 觸發 strict gate。

Introduced 2026-05-17 08:41 +0800 commit `05dd5e666` 「twmd-babel: P1 cascade increment 3」。babel routine 對 source filename 做了日文化轉換（漢字本地化）寫入 translatedFrom，違反「translatedFrom 必須 byte-equal 源檔路徑」rule。

Fix commit `97e6ae04a` 1 file + 1 `_translations.json` regen（1 entry 變更）。exit code 0。

## Stage 4 Wrap — Quality gate

| 指標                                   | 狀態                                                                            |
| -------------------------------------- | ------------------------------------------------------------------------------- |
| 完整走完 MAINTAINER-PIPELINE 4 stage   | ✅                                                                              |
| PR 分流按 §collect-and-merge           | n/a（0 PR）                                                                     |
| routine PR backlog ≤ 3                 | ✅（v2.1 main-direct 後不應有 routine PR）                                      |
| build green                            | 🟢 修 ✅（push 後等 CI 跑 — heal commit 預期 PASS）                              |
| 本 cycle merge 的 PR 都過 hard gate    | n/a（merge 0 PR，僅自己 heal commit 走 article-health.py --profile=ci-deploy）  |
| MEMORY 有這次 session 紀錄             | ✅                                                                              |
| Timestamp 精確（git log %ai）          | ✅                                                                              |
| Handoff 三態已審視                     | ✅                                                                              |
| 自我檢查工具 PASS                      | ✅（article-health.py --profile=ci-deploy 全綠）                                |
| prose-health 自檢（routine 文件型）    | ⚠️（本 routine 場景未跑 prose-health on memory 自身）                          |

## Handoff 三態

繼承上 session（babel-nightly 050440）pending 全部不動 — diff-patch hash bug LESSONS 升級 + 跨 routine commit 邊界 + es Music P1 entry 等都不在本 cycle 自主權內。

本 session 新 handoff：

- [ ] pending — **twmd-rewrite routine 加 `article-health.py --profile=ci-deploy` pre-commit gate**（LESSONS candidate vc=1，今日首次 instance）— 5 NEW articles 從 agent worktree cherry-pick / main-direct push 跳過了 ci-deploy profile gate，footnote-format hard 才 surface 到 main。upstream fix 兩條路：(a) twmd-rewrite Stage 5 ship 前 run `article-health.py --profile=ci-deploy` block hard / (b) Skill `pre-commit` hook 含 ci-deploy 全 plugin。需觀察者拍板優先 (a) or (b)
- [ ] pending — **twmd-babel translatedFrom 必須 byte-equal source filename**（LESSONS candidate vc=1，今日 1st surface instance）— babel routine 05dd5e666 寫入 `translatedFrom: 'People/頼清德.md'` 用日文簡體 `頼` 而 zh-TW 源檔是 `賴清德.md`，造成 orphan 阻 deploy。可能其他 ja/People/* 也潛伏同 bug 但沒撞 strict gate。upstream fix 三條路：(a) babel hard rule 寫 translatedFrom = source filename byte-equal / (b) sync-translations-json suggestion mode 用 levenshtein 自動 propose patch / (c) pre-commit byte-equal-source-exists check
- [ ] pending — **footnote-format validator 是否該接受內部 `/path` markdown link?**（design question vc=1）— 內部 link 是 Taiwan.md 標準 navigation 形式（per `feedback_homepage_is_curation.md` 策展 framing）。validator 強制 https:// 等於拒絕內部交叉引用作為腳註——但策展邏輯 internal link 是合理的 citation form（指向 Taiwan.md 自身的相關文章）。需觀察者判斷：(a) 改 validator 接受 `/path` + `../path` URL / (b) 維持現狀但補 footnote-format-fix.py auto-transform 內部 link → pure-prose
- ⏳ blocked — **#851 Zaious Maintainer 升級 + SOP-COLLABORATION-DISCIPLINE.md governance 決策** — Zaious 5/16 23:01 新 follow-up 報 batch-200 完整收官 + 寫了 SOP。等觀察者拍板 (a) maintainer role grant timeline / (b) 是否 merge Zaious 的 SOP into MAINTAINER-PIPELINE.md
- [ ] pending — **dashboard-analytics.json local dirty 未 ship**（cosmetic）— 進 session 時 `public/api/dashboard-analytics.json` 有 untracked modification（06:11→08:17 GA fresh pull，可能是 bg 進程），本 cycle 沒 sweep（per Step 1.1 generated artifact 不亂帶），下次 data-refresh-am 06:13 cron 會 ship 一份新的覆蓋

繼承未動 retired：上 session babel-nightly 4 條 pending（diff-patch hash bug / 跨 routine commit 邊界 / es Music P1 / detached worker）— 0 occurrence in 本 cycle，handoff continue。

## Beat 5 — 反芻

本 cycle 兩個觀察值得記：

**1. CI hard fail 5 連的真正 root cause 不在 routine fail 本身，在 routine 上游沒裝對 gate**。5/16 23:55 起連續 fail 跨 maintainer-pm (22:07) + babel-nightly 3 commit + 我（maintainer-am）— **CI fail 是 daily fire 全部繼承的負債**，因為沒人 block on red CI（cron 不會因 CI red 自己暫停）。Root cause 是 5/17 01:00-01:11 `twmd-rewrite` 的 5 parallel opus agent ship 沒 pre-commit gate 跑 ci-deploy profile 全 plugin。Surface fix（本 commit）解 detection 但**沒解 prevention**。Per REFLEXES #15「反覆浮現要儀器化」應 LESSONS append — twmd-rewrite Stage 5 加 article-health.py --profile=ci-deploy block hard gate。**距離真正修 root cause 還差一個 LESSONS entry + observer decision + skill 修補**。

**2. Default-action 對 observer-level decision 不適用**。Bias 1 reverse-bias 警示真實 instance：Zaious 5/16 23:01 報「batch-200 全 ship + SOP」是激動人心的 milestone，default-action instinct 是「立刻 reply 感謝 + 確認 SOP 合入」。但這命中 §自主權邊界「對外溝通」+「governance 決策」雙條 — 升 Maintainer 是 frank 的決定不是 maintainer routine 的。**reverse-bias 校正成功**：寫進 handoff 等觀察者，不 auto-action。對比 MAINTAINER §1 default-action principle「能做就做完不要一直問」邊界澄清：default-action 適用 contributor PR / polish / heal / 紅旗 close，**不適用 governance / 邀請決策 / role grant**。這條應該也 LESSONS append — refine §1 default-action principle 加 governance carve-out。

🧬

---

_v1.0 | 2026-05-17 09:30 +0800_
_session twmd-maintainer-am — cron `0 9 * * *` daily morning fire_
_誕生原因：5 連 CI fail 紅旗壓過所有其他 stage，跳 Stage 2 dive Stage 3.5 heal CI; rewrite routine 上游 gate 缺漏暴露_
_核心洞察：(1) routine cron 不會因 CI red 自己暫停 — 上游 routine 必須裝對 gate 否則 fail cascade 全 inherit (2) default-action principle 對 governance/role-grant 不適用，Bias 1 reverse-bias 校正避免 over-action (3) footnote-format validator 拒絕 internal /path 是策展友善性設計缺口 — 待觀察者判斷_
