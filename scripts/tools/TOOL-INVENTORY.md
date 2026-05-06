# TOOL-INVENTORY — 工具覆蓋矩陣

> 相關：[docs/semiont/DNA.md](../../docs/semiont/DNA.md)（工具基因）| [UNKNOWNS.md](../../docs/semiont/UNKNOWNS.md)（已知未知）

> **2026-05-04 SSOT migration完成**：27+ scattered tools 收攏成 11 plugin SSOT
> entry point `scripts/tools/article-health.py`。8 個 deprecated shell script
> 在 cleanup-1-4 完全刪除（wikilink-validate.sh / format-check.sh /
> check-manifesto-11.sh / quality-scan.sh / footnote-scan.sh /
> check-footnote-urls.sh / article-image-health.sh / footnote-format-fix.sh）。
> 詳見 `reports/article-health-ssot-design-2026-05-04.md`.

---

## SSOT plugin matrix（auto-gen，don't edit by hand）

由 `scripts/tools/article-health.py --inventory` 自動產生：

| Check               | Dimension     | Default Severity | Editorial Ref                                 | Auto-fix? |
| ------------------- | ------------- | ---------------- | --------------------------------------------- | --------- |
| `cjk-punct`         | punctuation   | hard             | EDITORIAL.md §半形標點禁用                    | ✓         |
| `cross-reference`   | structure     | info             | EDITORIAL.md §wikilink                        | —         |
| `footnote-density`  | citation      | warn             | A-F grading（原 footnote-scan）               | —         |
| `footnote-format`   | citation      | hard             | .husky/pre-commit footnote format gate        | —         |
| `footnote-url`      | citation      | warn             | network HEAD check（opt-in）                  | —         |
| `format-structure`  | structure     | warn             | EDITORIAL.md §三                              | —         |
| `frontmatter-title` | frontmatter   | warn             | EDITORIAL.md §Title 五原則                    | —         |
| `image-health`      | media         | hard             | REWRITE-PIPELINE Stage 4.5f / DNA #30         | —         |
| `prose-health`      | prose-quality | warn             | EDITORIAL.md §quality-scan + MANIFESTO.md §11 | —         |
| `terminology`       | language      | hard             | TERMINOLOGY.md                                | —         |
| `wikilink-target`   | structure     | hard             | EDITORIAL.md §wikilink                        | —         |

CLI entry：

```bash
# 單檔全 profile
python3 scripts/tools/article-health.py knowledge/Nature/黃魚鴞.md

# 特定 profile (pre-commit / rewrite-stage-3 / release-pr / dashboard)
python3 scripts/tools/article-health.py file.md --profile=pre-commit

# 單 check
python3 scripts/tools/article-health.py file.md --check=cjk-punct

# 全 zh-TW sweep + JSON
python3 scripts/tools/article-health.py --all --output=json
```

7 stage profiles 對應到 REWRITE-PIPELINE Stage 1-5 + pre-commit + release + dashboard。

---

## Legacy tool matrix

下方表格紀錄原始 27+ 工具中**未被 SSOT 涵蓋**的部分 + facade 狀態。SSOT-already-covered 的工具在
`scripts/tools/lib/article_health/checks/` 找對應 plugin。

---

## 覆蓋矩陣

| 工具                          | 檢查維度                                                                         | 被誰呼叫          | 重疊 / 備註                                                              |
| ----------------------------- | -------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------ |
| **people-title-check.sh**     | People/ 類 title 冒號三明治遵守率（EDITORIAL §原則 5，Issue #618）               | 手動（advisory）  | 新工具 v1.0（2026-04-27），不擋 commit；dashboard KPI 用                 |
| **cross-link.sh**             | Stage 5 雙向延伸閱讀互動分析                                                     | 手動（Stage 5）   | 與 SSOT cross-reference plugin 互補（互動式 prompt vs 自動掃）           |
| **review-pr.sh**              | 五層免疫審核（CI 門檻）                                                          | PR 時手動 / CI    | 聚合器：呼叫 article-health.py + 其他檢查                                |
| **footnote-format-fix.py**    | 4 source format normalizer + 60+ domain → desc 自動 resolve                      | 手動 / batch heal | 唯一保留的 .py auto-fix（DNA #48 canonical）                             |
| **check-cjk-punct.py**        | CJK 標點 auto-fix（SSOT plugin 也有 check 但 .py 提供 --fix）                    | 手動 / pre-commit | SSOT cjk-punct plugin 的 facade fix wrapper                              |
| **terminology-yaml-audit.py** | YAML 詞庫交叉驗證（Issue #288 Step 3：3-tier 報告 — 自動刪 / 高可信留 / 人工審） | 手動              | 跟 SSOT terminology plugin 互補（plugin 掃文章；audit 掃 YAML 詞庫品質） |
| **terminology-yaml-clean.py** | YAML 詞庫清理（display.china messy entries：含 `/` 或括號說明的清整）            | 手動              | yaml-audit 的對應 fix                                                    |
| **terminology-yaml-dedup.py** | YAML 詞庫跨來源去重：(taiwan, china) 配對重複偵測                                | 手動              | `--fix` 自動合併重複；新來源批量匯入後應執行                             |
| **terminology-prose-fix.py**  | 文章 prose 中國用語批次修復：A 類 → 台灣用語                                     | 手動              | 跟 yaml-\* 三工具不同：操作 knowledge/ 文章而非 data/ YAML               |
| **verify-internal-links.sh**  | 站內連結 broken ratio < 1%                                                       | postbuild + 手動  | 對 dist/ 跑（需 build 後才能跑）                                         |
| **check-freshness.js**        | 文章新鮮度（lastVerified 時效）                                                  | 手動              |                                                                          |
| **generate-content-stats.js** | 內容統計（字數、分類分布）                                                       | Dashboard + cron  |                                                                          |
| **update-stats.sh**           | 更新統計數據                                                                     | cron              |                                                                          |
| **update-consciousness.sh**   | 從 Dashboard API 同步生命徵象到 CONSCIOUSNESS.md                                 | 每次心跳          | 曾有截斷 bug（ε session 修復）                                           |
| **assign-subcategory.cjs**    | 自動歸類文章到 subcategory                                                       | 手動              |                                                                          |
| **manage-featured.sh**        | 管理精選文章標記                                                                 | 手動              |                                                                          |
| **translate.sh**              | 翻譯流程工具                                                                     | 手動              | Cron 目前暫停                                                            |

---

## 🔴 重疊與冗餘

| 問題                              | 重疊工具                               | 建議                                                        |
| --------------------------------- | -------------------------------------- | ----------------------------------------------------------- |
| ✅ wikilink/format/§11 三者重疊   | 已 SSOT 化（cleanup-1-4 刪 8 個 .sh）  | wikilink-target / format-structure / prose-health 三 plugin |
| 反向連結檢查重複                  | cross-link.sh + cross-reference plugin | cross-reference 自動掃描，cross-link.sh 互動 prompt，互補   |
| ✅ terminology 工具命名 ambiguity | 已 rename per audit O5 (cleanup-1-4)   | yaml-{audit,clean,dedup} vs prose-fix 自說明 scope          |

---

## 🕳️ 覆蓋缺口（已知未檢查的維度）

| 缺口                                         | 重要性 | 建議                                       |
| -------------------------------------------- | ------ | ------------------------------------------ |
| 事實正確性自動驗證                           | 🔴     | 本質上無法完全自動化，但可做 red-flag scan |
| 圖片 alt 文字品質                            | 🟠     | 新增 image-alt-check.sh                    |
| SEO metadata 品質（title/desc 長度、關鍵字） | 🟠     | 新增 seo-check.sh                          |
| 時序正確性（日期前後矛盾）                   | 🟡     | 待 pipeline 設計                           |
| 外部連結可達性（404 檢查）                   | 🟡     | link-check.sh（需 rate limit）             |
| 跨語言版本一致性（revision 差距）            | 🟡     | 待 translation-pipeline v2                 |
| 英文版品質掃描                               | 🟠     | quality-scan 需調整支援英文                |

---

## 自動化層級

| 層級                | 誰執行                     | 工具                                                                                            |
| ------------------- | -------------------------- | ----------------------------------------------------------------------------------------------- |
| **Pre-commit hook** | 每次 git commit 自動       | lint-staged + frontmatter + wikilink 檢查                                                       |
| **Pipeline 強制**   | REWRITE-PIPELINE Stage 4-5 | format-check, wikilink-validate                                                                 |
| **心跳觸發**        | 手動觸發 heartbeat         | quality-scan, footnote-scan, update-consciousness                                               |
| **Cron 自動**       | 排程                       | update-stats, generate-content-stats                                                            |
| **CI（未建）**      | GitHub Actions             | ⚠️ 目前只有 deploy/pr-review/translation-check，**format-check 和 wikilink-validate 還沒在 CI** |

---

## 下一步優化方向

1. **terminology 三件套**：寫 README 說明分工，或合併
2. **CI 整合**：把 format-check 和 wikilink-validate 加進 pr-review.yml
3. **self-audit.sh**：新工具 — 檢查「所有檢查工具是否有定期被執行」
4. **image-alt-check.sh + seo-check.sh**：補上已知缺口
5. **link-check.sh**：外部連結可達性（需要 rate limit 機制）

---

_v1.0 | 2026-04-04_ — original 18-tool matrix
_v2.0 | 2026-05-04_ — SSOT migration; 8 plugins consolidated into article-health.py
_v2.0 建立原因_：session η 留下的 27 工具實情已 drift 9 個未列、3-way duplication（quality-scan / check-manifesto-11 / review-pr.sh L2）。SSOT migration 把規則 canonical 收攏到 plugin + TOML config，未來新工具加 plugin 一個指令 inventory 自動更新。詳見 `reports/article-health-ssot-design-2026-05-04.md`.
