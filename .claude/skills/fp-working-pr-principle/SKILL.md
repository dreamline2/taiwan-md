---
name: fp-working-pr-principle
description: |
  Taiwan.md fork 工作流：upstream 基準、PR 目標 repo、outline gate、
  SSOT 範圍、避免假巨型 diff、commit credit 與 Cursor trailer 陷阱。
  TRIGGER when: user says "fp working pr", "upstream PR", "fork PR 流程",
  "開 PR 到 upstream", "避免 origin main 假 diff", "PR 衛生", "co-authored Cursor".
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Taiwan.md — FP working PR principle（fork → upstream）

本 skill 來自實務教訓（2026-05）：在 fork 上開 PR 若對錯 base、或未先 outline、或 commit 被注入 `Co-authored-by: Cursor`，會造成維護者時間浪費與 credit 糾紛。以下為**強制順序**，不可跳步。

## 0. 遠端與 PR 目標（先讀再動）

- `upstream` 通常指向 **canonical repo**（例如 `frank890417/taiwan-md`）。
- `origin` 指向 **你的 fork**（例如 `dreamline2/taiwan-md`）。
- **對外 PR 預設開在 `upstream`**，head 為 `fork_owner:branch`（例如 `dreamline2:chore/foo`）。
- 若誤把 PR base 設成 **落後的 `origin/main`**，`gh pr` 會顯示數百 commits、數千檔變更——那是**歷史落後造成的假 diff**，不是內容真的改那麼多。

## 1. 開工前必跑（Bash）

```bash
git fetch upstream
git fetch origin
# 相對 upstream：應只有你的內容 commits（通常 1～少數幾個）
git rev-list --left-right --count upstream/main...HEAD
# 相對 origin/main：若左邊數字很大，代表 fork main 落後，勿用 origin/main 當 PR base
git rev-list --left-right --count origin/main...HEAD
git diff --name-only upstream/main...HEAD
```

**通過條件**：`git diff --name-only upstream/main...HEAD` 僅含本次允許路徑（例如僅 `knowledge/...`），且與任務 SSOT 一致。

## 2. 分支與 rebase

- 工作分支從 **`upstream/main`** 切出或 rebase 到其上：`git rebase upstream/main`。
- 提交前再次確認 diff 範圍；**禁止**把 `src/content/`、實驗檔、untracked 大批檔案 `git add` 進同一 PR。

## 3. Outline gate（人類 review 前不開 Draft PR）

除非使用者明確說「跳過 outline、直接開 PR」，否則：

1. 先交付 **繁體中文 outline**：目標檔案清單、每檔變更型態（時效／腳註／事實更正）、不做的範圍。
2. 等使用者 **ok** 後，才執行 `gh pr create --draft`。

## 4. 開 PR 到 upstream（範例）

```bash
gh pr create --repo frank890417/taiwan-md --draft --base main \
  --head dreamline2:YOUR_BRANCH \
  --title "..." --body-file .github/pull_request_template.md
```

（實際 `upstream` owner／branch 名以 `git remote -v` 為準。）

## 5. SSOT 與 PR 衛生

- **單一來源**：若任務要求僅 `knowledge/`，則 commit 內只應出現該路徑變更。
- **禁止**：把 gitignored 的 `src/content/` 同步產物、或與任務無關的 untracked 檔案塞進 PR。
- PR 描述：專業編輯口吻；**不要**在 PR 正文寫 AI／技能名稱／內部自動化流程字樣（若使用者有「去技能化」要求）。

## 6. Commit message 與 credit（Cursor trailer）

- 預期 author／committer 為**人類貢獻者**；不要主動加入 `Co-authored-by: Cursor`。
- 若環境的 `prepare-commit-msg`／commit hook **自動注入** `Co-authored-by: Cursor <cursoragent@cursor.com>`：
  - `git commit --amend --no-verify` 或 `HUSKY=0` **可能仍無法**阻止該 trailer。
  - **可靠修法**：用相同 tree 與 parent 重建 commit，完全控制 message：

```bash
tree=$(git write-tree)
parent=$(git rev-parse HEAD^)
printf '%s\n' "title" "" "body..." | git commit-tree "$tree" -p "$parent"
# 再 git reset --soft NEW_SHA
```

- amend／rewrite 後一律：`git push --force-with-lease origin YOUR_BRANCH`。

## 7. 錯 PR 處置

- 若已在 **錯誤 repo**（例如僅 fork 的 `origin`）開 PR：應關閉或註記「已改開 upstream #…」，避免雙軌混淆。

---

**故意精簡**：細部 editorial／BECOME 流程仍以專案 canonical pipeline 為準；本檔只鎖「fork → upstream PR」的結構性雷點。
