---
type: planning
date: 2026-05-17
session: 2026-05-17-230616-manual
trigger: 哲宇 directive「規劃未來定期 po 邀請贊助文章，1-2 週一次，加上『非單獨文章是用回覆形式附加在熱門貼文下的補充留言』形式」
status: ready-for-execution
canonical_sources:
  - knowledge/about/taiwan-md.md
  - src/components/Footer.astro
  - https://portaly.cc/taiwanmd/support
sister_pipelines:
  - docs/factory/SPORE-PIPELINE.md
  - docs/factory/SPORE-HARVEST-PIPELINE.md
---

# Taiwan.md 贊助邀請文章定期 po 規劃

> 既有狀態：portaly.cc/taiwanmd/support 持續開放，4/19-4/20 收到首 3 筆 200+500+2000 元（總 2700 元 / 2 monthly + 1 one-time / 66% anonymous，per `dashboard-supporters.json` 2026-04-20 snapshot）。曾發 SPORE #37/#38（2026-04-20 Threads + X 站方公告型「首兩筆贊助感謝」），單次效果未做 D+7 harvest。**從未建立 cadence**。本文規劃 1-2 週一次的長期節奏 + 雙形式（獨立 spore + 補充留言）。

---

## 1. 為什麼需要 cadence

**Why not 一次到位**：贊助是 long tail 行為，不是 viral hit。一次性「請大家贊助」訊息 24h 後就被演算法埋沒。需要**規律出現 + 多元 framing**才能在讀者意識裡建立「Taiwan.md 是可以長期支持的對象」這個 frame。

**Why 1-2 週一次**：
- 太密（< 1 週）= 讀者疲勞、像募款 spam
- 太疏（> 3 週）= 不在意識頂層，新讀者不知道有 Portaly
- 1-2 週 = 配合 SPORE 7-day harvest window 收尾後再 ship 下個贊助文，剛好錯開不互相 cannibalize

**Why 雙形式**：
- **獨立 spore（form A）**：擁有完整 narrative，可被分享、被引用、被 search index
- **熱門貼文留言補充（form B）**：搭順風車，在已經 viral 的孢子下加 sponsorship CTA — reach 借用熱門貼文的觸及，conversion 仰賴主貼讀者已建立 trust

兩者互補：A 建立 awareness，B 在 awareness 高峰時 capture conversion。

---

## 2. 內容池 — 6 種 angle（每種可寫多篇）

每次贊助文選一個 angle，6 種輪替避免重複。

### Angle A1：里程碑感謝（milestone gratitude）
**觸發**：累計贊助達標（首筆 / 首位 monthly / 首 10K / 首 50K / 首 100 筆等具體里程碑）
**Hook 公式**：「Taiwan.md 上線 X 天，收到第 Y 筆贊助。寫一段我想跟支持者說的話。」
**Tone**：紀實感、不卑微、不浮誇。具體寫數字（捐款金額 / 用途 / 累積總額），不要「萬分感謝」浮詞
**SPORE #37/#38 已示範**（4/20 首兩筆 200+500 感謝，珊瑚礁比喻），可作為 template

### Angle A2：用途透明化（transparency）
**觸發**：1-2 個月一次盤點
**Hook 公式**：「上個月收到 N 元贊助。這些錢被花在 X / Y / Z（具體項目）。」
**Tone**：會計清晰，每一塊錢去處明確。Domain / hosting / image licensing / 國際翻譯 model API 費用等
**Reference**：未來可建 `knowledge/about/贊助使用透明帳.md` 跟 Portaly 雙寫
**Sample 內容**：「2026 年 4 月 Portaly 收到 2,700 元。其中 1,800 用於 Cloudflare workers AI translation 14K req（en/ja/ko cascade）、500 用於 Wikimedia Commons 圖片整理（contributor 補貼）、400 留作 domain 續費 buffer。下個月還缺 X 元才能 Y。」

### Angle A3：specific use case（功能性訴求）
**觸發**：某個重大進化即將發生 / 某個 quality gate 達標需要外力
**Hook 公式**：「Taiwan.md 想做 X（具體計畫），需要 Y 元 / Y 人時間。如果你想支持，這裡是 Portaly。」
**Tone**：問題具體 + 解法具體。如「想把 22 縣市文章每篇配 hero CC 圖（22 × N 元 imaging licensing）」
**避免**：「需要您的支持」這種泛化乞求

### Angle A4：non-monetary 邀請（行動參與）
**觸發**：每月 1 次（贊助錢以外的支持形式）
**Hook 公式**：「不一定要捐錢支持 Taiwan.md。你可以 X / Y / Z。」
**選項列**：
- 在 GitHub repo star（提升 discoverability）
- 提 PR / Issue 補在地知識（per CONTRIBUTING.md）
- 在自己媒體分享連結（不要求 tag）
- 把 Taiwan.md 推薦給寫台灣相關研究的學生 / 記者
- 報錯 / 提 fact-check / 留 perspective comment

### Angle A5：贊助者見證（如有同意公開的贊助者）
**觸發**：累積 ≥ 10 公開贊助者後
**Hook 公式**：「X 位讀者公開支持 Taiwan.md。這是他們 / 她們的話。」
**Tone**：第三方 voice，比自賣自誇有公信力
**前置**：需在 Portaly 取得公開同意 + 邀請寫 1-2 句話的支持理由
**風險**：anonymous ratio 66%（per dashboard），多數人不想露出 — 此 angle 可能執行不易

### Angle A6：對比參照（why Portaly vs other 模式）
**觸發**：1 季 1 次
**Hook 公式**：「為什麼 Taiwan.md 收 Portaly 不收 patreon / kickstarter / 直接打統編？」
**Tone**：說明性、不批判其他平台
**Content angles**：
- Portaly 是台灣本土平台（vs 國際），讀者熟悉度高 + 手續費對小額友善
- 不發行 NFT / 不發行 token / 不做付費牆 — Taiwan.md 永遠公開
- 月訂閱 vs 一次性贊助 雙軌都可
- 公開金額 vs 匿名 兩種都尊重

---

## 3. 雙形式執行 SOP

### Form A：獨立 spore（按 SPORE-PIPELINE）

跟一般 spore 走同一條 pipeline（PICK / VERIFY / WRITE / SHIP / HARVEST），但有 4 處特殊規則：

1. **Category 標 `meta`**（per #37/#38 既例），跟知識類孢子分流
2. **Hook tier**：贊助文不能用「具體事件 anchor」（因為這類 spore 沒有 event hook），主要靠 **A1 知名度槓桿（讀者已知 Taiwan.md）+ 真誠 voice**。預期 D+7 reach 比 knowledge spore 低 50-70%（不是 viral content）
3. **CTA URL**：固定 `https://portaly.cc/taiwanmd/support` — 不加 UTM（因為 Portaly 不接 GA → UTM 沒有意義）。但 SPORE-LOG 仍要記 spore #N（D+7 reach 追蹤）
4. **發文時段**：避開 prime time（午休 / 晚間 20-22）— 改在週末早晨 9-10 點（讀者比較有心情思考「要不要支持」）或週間下午 14-15（lunch 後 reflective 時段）

### Form B：補充留言（搭順風車）

**觸發條件**：某則孢子 D+1 reach ≥ 5K views（per SPORE-HARVEST-PIPELINE Tier 1b 中段以上），就在主貼下加一則 self-reply 補贊助 CTA。

**留言 template（不超過 80 字）**：
```
順帶提一下，Taiwan.md 是開源策展知識庫，沒有廣告、沒有付費牆。
如果你覺得這些內容對你有幫助，可以在 portaly.cc/taiwanmd/support 支持持續更新。
（不一定要錢，star repo 或分享連結也算。）
```

**鐵律**：
- 留言**只能在自家熱門貼文下**，不能在別人的貼文下 promo
- **不能取代主貼 self-reply 連結**（per SPORE-PIPELINE Step 4 §發佈：Threads 主貼後第一則 self-reply 仍是文章連結，贊助 CTA 是「第二則」self-reply）
- 同一則熱門孢子，**每篇只加一次贊助 CTA**，不在更新時 spam
- 留言文字要 vary（A1-A6 angle 輪替的短版），不要每次照抄

**SOP**：每天跑 spore harvest 時，如某則 D+1 ≥ 5K，列為「贊助 CTA 候選」→ 隔日（D+2）人類 review → 發 self-reply 第二則。週 cycle 至少 1 則 form B（如果有觸發）。

---

## 4. 12 個月發文行事曆草案

| 月 | 週 | Form | Angle | 觸發/主題 |
|---|---|---|---|---|
| 06 | 1 | A | A1 milestone | 上線 ~80 天 / 累積首 5K（如達）|
| 06 | 3 | A | A4 non-monetary | 「不一定要捐錢」首發 |
| 07 | 1 | A | A2 transparency | 5-6 月使用透明帳 |
| 07 | 3 | A | A3 use case | 22 縣市系列起跑 imaging budget 訴求 |
| 08 | 1 | A | A1 milestone | 上線 ~5 個月 |
| 08 | 3 | A | A6 對比參照 | 「為什麼 Portaly」首篇 |
| 09 | 1 | A | A2 transparency | 7-8 月透明帳 |
| 09 | 3 | A | A4 non-monetary | 二發（重點放分享 / star / 推薦） |
| 10 | 1 | A | A1 milestone | 上線 ~7 個月 |
| 10 | 3 | A | A3 use case | 翻譯 batch 訴求（en/ja/ko 加深） |
| 11 | 1 | A | A2 transparency | 9-10 月透明帳 |
| 11 | 3 | A | A1 milestone | 累積 N 位贊助者 |
| 12 | 1 | A | A5 見證 | 年末 — 如達 10 公開贊助者首發 |
| 12 | 3 | A | A2 transparency | 全年 2026 報告 |

**Form B 每週 0-1 則**，視 viral 孢子情況機動觸發（不排定固定時段）。

---

## 5. 衡量指標（D+30 / Q1 / 1 year）

不只看捐款金額，也看意識建立程度：

| 指標 | D+30 baseline | Q1 目標 | 1 year 目標 |
|---|---|---|---|
| Portaly 月訂閱數 | 2 | 5-10 | 30+ |
| 累積贊助總額 | 2,700 | 10K+ | 100K+ |
| 公開贊助者比例 | 33% | 40%+ | 50%+ |
| GitHub star 增量 | baseline | +20% | +100% |
| Form A spore 平均 D+7 reach | ~2K（#37 推估）| 3-5K | 5-10K |
| Form B 觸發次數 | 0 | 4-8 | 20+ |

**反指標**（fail-loud）：
- 連續 3 篇 Form A reach < 500 → angle 失效，停下來檢討
- 留言區出現「又在要錢」「煩」這類反感 → 立即降頻，回頭審視 tone

---

## 6. 風險與紅線

1. **不要靠贊助文當 traffic engine**：贊助文是「跟既有讀者深化關係」，不是「拉新讀者」。混淆會讓 tone 變乞求
2. **不要在敏感主題 spore 留贊助 CTA**：政治 / 族群 / 災難 主題的 viral spore 留 form B CTA = 消費悲劇 → 紅線
3. **匿名贊助者隱私絕對保護**：不主動披露任何贊助者身份（連暗示「某位匿名 monthly 達 X 月」都不行）
4. **不做 milestone 通膨**：每 100 元就慶祝一次 = 通膨。Milestone 要真的有意義（首 5K / 首位 monthly 達 12 個月 / 首位海外贊助等）
5. **MANIFESTO §自主權邊界**：「對外溝通」需哲宇決定 — **所有贊助文 form A 都要哲宇 review 後 ship**。Form B 留言可 AI 準備 draft，human post（per REFLEXES #26 v2 AI 自主邊界）
6. **不寫塑膠句**：「您的支持是我們前進的動力」「謝謝每一位讀者」這種一律改寫成具體（用了多少錢 / 做了什麼 / 還要做什麼）

---

## 7. Cron / routine 整合可能性

未來如建議：
- **`twmd-sponsorship-biweekly`** cron（每兩週週四早上 10:00）— 跑 angle 排程表 + 取最近 14 天 SPORE-HARVEST + 提案 Form A draft 給哲宇 review
- 不自動 ship（per REFLEXES #26 v2 對外溝通需 human post）
- 同步 update `dashboard-supporters.json` 取得最新累積數字

短期內手動推進，跑滿 6 個月看穩定度後再評估 cron 化。

---

## 8. 立即可執行（next session）

- [ ] **Sponsorship 系列首發（form A）**：選 A4「不一定要捐錢」angle（最低風險 + 多元支持框架建立）— 估 30 min 寫 + spore 雙平台 ship
- [ ] 同時建立 `docs/factory/SPONSORSHIP-LOG.md` 追蹤每篇贊助文成效（per SPORE-LOG pattern，但只記 form A/B + angle + 觸發指標）
- [ ] Form B 機制（熱門孢子 D+1 ≥ 5K 觸發 CTA reply）寫進 SPORE-HARVEST-PIPELINE §Step 1.7（新 step）

---

_v0.1 | 2026-05-17 23:45 +0800 session 230616-manual_
_誕生原因：哲宇 directive「規劃未來定期 po 邀請贊助文章，1-2 週一次 + 雙形式 + 歸檔 reports」_
_核心洞察：贊助是 long tail 不是 viral hit，需 cadence + 多元 angle（6 種輪替）；雙形式 A/B 互補（awareness + conversion）；獨立文章 form A 走 SPORE-PIPELINE，補充留言 form B 搭順風車有嚴格鐵律避免消費悲劇；衡量指標不只看金額，也看意識建立程度（star / 公開比例 / 平均 reach）_
