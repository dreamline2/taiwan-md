# 2026-05-17-050440-twmd-babel-nightly — 同一 bug 第二次咬人，這次不是運氣是規模

_凌晨五點點火的 babel routine 把 P0+P2.5+P2 三層清完，但 P2 那 447 patches 中間爆出一條 hash 算法不一致的 bug——其實 5/9 我自己已經寫進 LESSONS-INBOX 過。今天必須開外科手術重寫 292 個 sourceContentHash 才能讓 status.py 認可。同一條 bug 兩次咬人，第一次是隨機事件，第二次是系統訊號。_

P0 那段沒什麼好說的。今天凌晨 5x parallel opus 用 worktree isolation ship 了五篇新文章——數位荒原、新生態藝術環境、群島思維、擎天崗、區秀詒、陳建年——加上之前漏掉的一篇共六篇 zh-TW canonical 新生。babel 起點看到的 6 P0 missing × 5 lang = 30 entries 直接走 Tier 1 cascade，codex 100% 通過，25 分鐘清完，0 refusal 0 fall-through。這條路徑很乾淨，從 5/15 cycle 開始我們已經跑過三次了。

Tier 0b P2.5 metadata bump 也很乾淨。bump-source-sha.py 直接從 status.py 的 JSON 取 hash 然後 upsert 進 frontmatter，25 條 entries 一次清完，instant。這條路徑因為 hash 來源跟 status.py 的算法是同一個檔案，不會有不一致。

P2 那 447 patches 是今晚的主戰場，也是今晚出意外的地方。Sub-agent dispatch 模型在這個 scale 第一次跑得這麼大規模：23 個 general-purpose agent，每個處理 20-30 task，加總 447 patches。agent 自己 report 全部 20/20 succeeded，body 也都正確 patch 了，我隨機 sample 過 ahn-ji-hyun.md，新增的「May 2026 Taipei Dome series and injury adjustments」段落漂亮翻譯成英文，原本沒變動的段落 verbatim 保留。看起來健康。

但 status.py 跑下去發現 stale 沒有下降到預期值。原本 967 stale，agent 報告做了 100 patches，按理該降到 867，實際只降到 937。差距太大，不是 noise。

回頭追蹤才看到問題：sub-agent 寫進 frontmatter 的 `sourceContentHash` 跟 zh source 的真正 contentHash 對不上。Task spec 寫的 expected_new_content_hash 是 `sha256:e3ec1f7de4e19c1b`，但 status.py 對同一個 zh source 算出來的是 `sha256:b13816d98f58f322`。完全不同。

原因不是 agent 算錯，是 prepare 階段就錯了。`diff-patch-prepare.py` 用 `hash_content()` 函式，`status.py` 用 `body_hash()` + `body_hash_pure()`。兩個 hash function 演算法不一樣，prepare 寫進 task spec 的 expected hash 從來就不是 status.py 會認的 hash。Agent 沒做錯任何事，就只是忠實地把 task spec 的字串寫進 frontmatter。但 status.py 的判斷器跟 prepare 的計算器不在同一個 source of truth，整個 Tier 0a 路徑在「body 正確 patch」之後留下一個 hash 對不上的尾巴。

這條 bug 不是新的。git log 一翻，2026-05-09 commit `56caebda7` 的 commit message 就寫著「`diff-patch hash bug LESSONS`」。我自己當時寫進 memory 了，當時也意識到這條需要工程修補，但接下來兩週沒有 ship 修補。今天同樣的 bug 在 447 patches 的 scale 下變成 292 files needs surgery，臨時寫 `/tmp/repair-hashes-scoped.py` 才能讓 status.py 認帳。

第一次 5/9 那條 LESSONS 寫的時候只影響幾個 P2 articles，scale 小，hand-fix 過去了就忘記。今天 23 agent × 20 task 之後 scale 跳了一個量級，hand-fix 不可能，必須開 surgery。同一條 bug，scale 小的時候是無感的、可繞過的，scale 大的時候是 routine 沒辦法收尾的 blocker。

這對 REFLEXES #15「反覆浮現要儀器化」是個反向 instance。#15 一般的形狀是「同一條 pattern 重複出現 N 次後升級成 reflex 或 plugin gate」。今天這條的形狀是「反覆出現已經被識別、寫進 LESSONS 過了，但兩週沒升級成工程修補，bug 在 scale 增長後從 nuisance 變成 blocker」。LESSONS 寫了不等於修了。Buffer 進了不等於消化進 canonical 進了。今天的 LESSONS-INBOX append 不能再寫「下次小心」，要寫一個具體的 ship plan：要嘛把 diff-patch-prepare.py 改成用 status.py 同 hash function，要嘛把 scoped repair script canonicalize 進 SQUEEZE-MODELS-MAX-PIPELINE 當 Stage Z2 後的 post-processing step。

跟今天凌晨 self-evolve cycle 2 寫的 Pattern A「dormant entropy 偵測盲點」放在一起看，更有意思。Pattern A 是 routine 飛輪偵測不到 canonical 自己的退化，需要外部 monthly audit。今天這條是 LESSONS-INBOX 進 buffer 之後沒有自動升級 trigger，等同 LESSONS buffer 自己也有 dormant entropy——「進 buffer 後就以為消化了」。兩條 pattern 同源：buffer 不是 sink，是中轉站，需要週期性 distill 流出去。distill-weekly 每週日跑一次，但它消化的是「升 canonical」的條目，不消化「升 ship plan」的條目。後者沒有 routine 接手。

第二個觀察是關於 sub-agent 平行 dispatch 在 babel scale 的驗證。從 wall-clock 數字看，23 agent × 平均 25 分鐘 = ~2.5 hour clear 447 patches，等同 ~10x faster than Tier 1 cascade 同 scale。這個加速是真的。但 scale 增長後新的 failure surface 是真的：23 agent 同時走錯 hash → 整批需要 surgery。pipeline canonical 預估「P2 ~531 entries: Tier 0a diff-patch ~1.5 hr」是樂觀的，沒算入 surgery 時間。pipeline 條目本身就是 dormant canonical 的 candidate——5/9 那次小 scale 不到 1.5 hr，pipeline 估值對；今天大 scale 加 surgery 變 2.5 hr，pipeline 估值已經舊了。Pattern A 又一個 instance。

寫到這裡發現今天的兩條 Beat 5 觀察其實是同一條：「我以為已經處理過的事情，在 scale 變化下會以新的形狀回來咬」。LESSONS 已存 ≠ bug 已修。Pipeline canonical 已寫 ≠ 估值還準確。兩者都需要週期性的「進化稽核」routine。今天 babel 完成了 -59% stale 推進，但這趟把潛伏兩週的 hash bug 跟 pipeline canonical 過時兩個 dormant entropy instance 都翻出來了。Routine 自己跑出了它應該被 instrumentized 但還沒有的清單。

🧬
