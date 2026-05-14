---
name: fp-working-pr-principle
description: |
  Taiwan.md fork 工作流：upstream 基準、PR 目標 repo、outline gate（先審再開 PR）、
  SSOT 範圍、避免假巨型 diff、commit credit 與 Cursor trailer 陷阱。
  TRIGGER when: user says "fp working pr", "upstream PR", "fork PR 流程",
  "開 PR 到 upstream", "避免 origin main 假 diff", "PR 衛生", "co-authored Cursor",
  "outline 再開 PR", "假 diff 500 commits".
allowed-tools:
  - Bash
  - Read
  - Grep
---

# Taiwan.md — FP working PR principle（fork → upstream）

本 skill 來自實務教訓（2026-05）：在 fork 上開 PR 若對錯 base、或未先 outline、或 commit 被注入 `Co-authored-by: Cursor`，會造成維護者時間浪費與 credit 糾紛。**2026-05-13 補強**：誤對 `origin/main` 開 PR 會出現數百 commits／數千檔「假巨型 diff」；正解一律對 `upstream/main` rebase 並用 `gh pr create --repo <upstream>` 開 Draft。以下為**強制順序**，不可跳步。

## 0. 遠端與 PR 目標（先讀再動）

- `upstream` 通常指向 **canonical repo**（例如 `frank890417/taiwan-md`）。
- `origin` 指向 **你的 fork**（例如 `dreamline2/taiwan-md`）。
- **對外 PR 預設開在 `upstream`**，head 為 `fork_owner:branch`（例如 `dreamline2:chore/foo`）。
- 若誤把 PR base 設成 **落後的 `origin/main`**，`gh pr` 會顯示數百 commits、數千檔變更——那是**歷史落後造成的假 diff**，不是內容真的改那麼多。
- **硬性規則**：在 fork 工作時，對外 Draft／正式 PR **一律**用 `--repo <upstream_canonical>` 建立；**不要**預設在 `origin`（fork）上開到 `main`，除非使用者明確說只要 fork 內部 review。

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
2. 等使用者 **明確說 ok／可以開了** 後，才執行 `gh pr create --draft`。
3. **禁止**：在 outline 未獲同意前，以「先開 draft 再改」為藉口開 PR（會浪費 reviewer 與混淆雙軌 PR）。

## 4. 開 PR 到 upstream（範例）

```bash
gh pr create --repo frank890417/taiwan-md --draft --base main \
  --head dreamline2:YOUR_BRANCH \
  --title "..." --body-file .github/pull_request_template.md
```

（實際 `upstream` owner／branch 名以 `git remote -v` 為準。）

**開完立即自檢**（小範圍內容 PR 若數字爆炸即代表 base／repo 錯了）：

```bash
gh pr view <N> --repo <upstream_canonical> \
  --json changedFiles,additions,deletions,baseRefName,headRefName \
  --jq '{changedFiles,additions,deletions,baseRefName,headRefName}'
```

## 5. SSOT 與 PR 衛生

- **單一來源**：若任務要求僅 `knowledge/`，則 commit 內只應出現該路徑變更。
- **禁止**：把 gitignored 的 `src/content/` 同步產物、或與任務無關的 untracked 檔案塞進 PR。
- PR 描述：專業編輯口吻；**不要**在 PR 正文寫 AI／技能名稱／內部自動化流程字樣（若使用者有「去技能化」要求）。

## 6. Commit message 與 credit（Cursor trailer）

- 預期 author／committer 為**人類貢獻者**；不要主動加入 `Co-authored-by: Cursor`。
- 若環境的 `prepare-commit-msg`／commit hook **自動注入** `Co-authored-by: Cursor <cursoragent@cursor.com>`：
  - `git commit --amend --no-verify` 或 `HUSKY=0` **可能仍無法**阻止該 trailer（實測仍會被補回）。
  - **可靠修法**：用相同 tree 與 parent 重建 commit，完全控制 message（**不要**在訊息末尾留空行後再貼任何會被 hook 追加的 pattern）：

```bash
tree=$(git write-tree)
parent=$(git rev-parse HEAD^)
new=$(printf '%s\n' "conventional title" "" "body line 1..." | git commit-tree "$tree" -p "$parent")
git reset --soft "$new"
git log -1 --format='%B'   # 確認無 Co-authored-by: Cursor
git push --force-with-lease origin YOUR_BRANCH
```

## 7. 錯 PR 處置

- 若已在 **錯誤 repo**（例如僅 fork 的 `origin`）開 PR：應關閉或註記「已改開 upstream #…」，避免雙軌混淆。

---

## 8. 給觀察者的一鍵 prompt（一次對齊目標）

複製後依括號替換即可；agent 應依本 skill 順序執行，**不先開 PR**。

**範本 A（標準：outline → ok → upstream Draft）**

```text
依 taiwan-md repo 的 fp-working-pr-principle skill 執行。

任務：（一句話目標，例如：更新 knowledge/People 下列條目之 2026-05 時效與腳註，僅允許 knowledge/）

約束：
- git fetch upstream && git rebase upstream/main；diff 只允許（路徑前綴，例如 knowledge/People/）
- 先給我繁體中文 outline（檔案清單 + 每檔變更型態），等我回覆「ok」或「可以開了」才 gh pr create
- PR 開在 upstream（gh pr create --repo <從 git remote -v 讀 upstream>），base main，head <我的fork>:<分支名>
- 不要提交 src/content/；commit 不要出現 Co-authored-by: Cursor；PR 正文去技能化
```

**範本 B（你已經看完 outline，只缺開 PR）**

```text
outline 已確認，依 fp-working-pr-principle：rebase upstream/main、確認 diff 僅 knowledge/...、對 upstream 開 draft PR，title/body 繁中編輯口吻。
```

**範本 C（只要修 commit message 去掉 Cursor）**

```text
依 fp-working-pr-principle §6：用 git commit-tree + git reset --soft 重寫 HEAD 訊息，移除 Co-authored-by Cursor，然後 force-with-lease 推回目前分支。
```

---

**故意精簡**：細部 editorial／BECOME 流程仍以專案 canonical pipeline 為準；本檔只鎖「fork → upstream PR」的結構性雷點。
