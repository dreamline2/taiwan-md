# SOCIAL-POSTING-PIPELINE

> 孢子的最後一哩：從 SPORE-PIPELINE Stage 4 SHIP 接手，自動化發文到 Threads / X。
>
> v0.3 | 2026-05-18 | osascript clipboard paste 突破圖片上傳限制，X + Threads 雙平台全自動化確認

---

## 定位

```
SPORE-PIPELINE Stage 4 SHIP（品檢 + UTM + 配圖 + platform allocation）
        ↓ 交付物：文案 + URL + 圖片
SOCIAL-POSTING-PIPELINE（本文件）
        ↓ 執行發文
平台上線
```

SPORE-PIPELINE Stage 4 負責「準備好要發的東西」；本 pipeline 負責「把東西送上平台」。

**MANIFESTO §自主權邊界現狀**：「Post 新孢子 to Threads/X = Human 必做」。本 pipeline 提供工具但不改變這條邊界——觀察者仍需 confirm 每次發文。

---

## 前置條件

### 帳號

| 平台    | 帳號         | 類型                       | 狀態                            |
| ------- | ------------ | -------------------------- | ------------------------------- |
| X       | @taiwandotmd | Premium（藍勾 ✓）          | ✅ 已登入 Chrome、680 followers  |
| Threads | @taiwandotmd | 連結 Professional IG       | ✅ 已登入 Chrome、3,581 followers |
| IG      | @taiwandotmd | Professional (Creator/Biz) | ✅ 已登入 Chrome、220 followers   |

### Chrome MCP 必要條件

- Claude in Chrome 擴充功能已安裝且連線
- X：browser 已登入 @taiwandotmd ✅
- Threads：browser 已登入 @taiwandotmd ✅（需先在 IG 登入 taiwandotmd 帳號，Threads 會跟隨 IG session）

### API 必要條件（未來穩定自動化）

- X：Developer Portal 帳號 + App + OAuth 2.0 credentials
- Threads：Meta Developer App + App Review 通過

---

## 方法一：Chrome MCP 瀏覽器自動化

### X 發文流程 ✅ 已測試確認可行（含圖片）

```
步驟：
1. osascript 把方形配圖寫進 macOS 剪貼簿
2. navigate → x.com/home
3. left_click compose 區域（"What's happening?"）
4. key cmd+v → 圖片從剪貼簿貼入 compose（自動附加）
5. type 孢子文案（含 inline UTM URL for X）
6. ⚠️ 等待觀察者確認 → left_click Post
7. 等待發文成功
8. navigate → x.com/taiwandotmd → 點進最新 post → 從 URL 欄擷取 post URL
```

**實測結果（2026-05-18）**：

| 測試項目              | 結果                                                               |
| --------------------- | ------------------------------------------------------------------ |
| Compose → type → Post | ✅ 正常，Post 按鈕自動啟用                                         |
| 中文文案輸入          | ✅ 正常，含 emoji、URL 都沒問題                                     |
| Post button 定位      | ✅ `find("Post button")` 或 `read_page(filter: "interactive")`     |
| 圖片上傳 file_upload  | ❌ Chrome MCP `file_upload` 被拒（file input opacity:0, width:0）  |
| **圖片 clipboard paste** | **✅ osascript 寫入剪貼簿 + Cmd+V 貼入成功**                    |
| 字數限制              | ✅ **不是問題**——帳號有 Premium（藍勾），上限 25,000 字元            |
| 字數計數器            | ✅ 200 中文字 + URL 仍有 51 字元餘額                                |

**字數結論**：taiwandotmd 有 X Premium，孢子 150-300 中文字 + URL 完全不會超限。免費帳號上限 280 字元（中文每字算 2），帶 URL 最多約 123 中文字。

**Post URL 結構**：`https://x.com/taiwandotmd/status/{status_id}`

### Threads 發文流程 ✅ 已測試確認可行（含圖片）

**重大發現**：Threads compose 支援**串文模式**——在同一個 compose modal 裡可以寫主貼 + self-reply，一次「發佈」送出。不需要先發主貼再回去 reply。

```
步驟：
1. osascript 把方形配圖寫進 macOS 剪貼簿
2. navigate → threads.net
3. left_click 左側「新串文」或 find compose 按鈕
4. 開啟 compose modal → left_click 第一則輸入框
5. key cmd+v → 圖片從剪貼簿貼入（自動附加）
6. type 孢子主貼文案（不含連結）
7. left_click「新增到串文」→ 出現第二則輸入框 (2/2)
8. type self-reply 連結文案（「完整故事 👉 {UTM URL}」）
9. ⚠️ 等待觀察者確認 → left_click「發佈」
10. 兩則同時發出
11. navigate → threads.com/@taiwandotmd → 點進最新 post → 從 URL 欄擷取 post URL
```

**實測結果（2026-05-18）**：

| 測試項目                 | 結果                                                             |
| ------------------------ | ---------------------------------------------------------------- |
| Compose modal 開啟       | ✅ 左側「新串文」按鈕                                             |
| 文案輸入                 | ✅ 中文正常，Threads 自動識別 URL 為連結                           |
| 串文模式（主貼+reply）   | ✅ 「新增到串文」按鈕新增第二則，顯示 1/2、2/2                     |
| URL 預覽卡              | ✅ self-reply 的 URL 自動展開 OG 預覽（taiwan.md OG tags 正確）    |
| 貼文選項                 | ✅ 「誰可以回覆和引用」：所有人/粉絲/追蹤者                        |
| 草稿功能                 | ✅ 取消時可選「儲存為草稿」/「不儲存」                              |
| 圖片上傳 file_upload     | ❌ Chrome MCP `file_upload` 被拒（Meta CSP 安全策略）              |
| **圖片 clipboard paste** | **✅ osascript 寫入剪貼簿 + Cmd+V 貼入成功**                      |
| 字數限制                 | ✅ 500 chars/post，孢子 150-300 字安全                             |

**Post URL 結構**：`https://www.threads.com/@taiwandotmd/post/{post_code}`

**Threads compose 元素定位**（自動化用）：
- 主貼文字框：`textbox` placeholder「有什麼新鮮事？」
- 第二則文字框：`textbox` placeholder「傳達更多想法......」
- 圖片上傳（第一則）：`find("附加影音內容")` → ref 附近的 `input[type="file"]`
- 圖片上傳（第二則）：第二個 `input[type="file"]`
- 發佈按鈕：compose modal 右下角
- 新增到串文：compose 區域底部

### 圖片上傳：osascript clipboard paste ✅ 已解決

Chrome MCP 的 `file_upload` 無法操作兩個平台的隱藏 file input（CSP 安全限制），但 **clipboard paste 路線完全繞過這個限制**。

| 平台    | file_upload（file input） | clipboard paste（osascript + Cmd+V） |
| ------- | ------------------------- | ------------------------------------- |
| X       | ❌ "Not allowed"         | ✅ 圖片正確貼入 compose                |
| Threads | ❌ "Not allowed"         | ✅ 圖片正確貼入 compose                |

**原理**：`file_upload` 走 file input element 觸發（被平台 CSP 擋），clipboard paste 走瀏覽器 paste event handler（平台接受）。兩條路徑在安全模型裡是不同的。

**osascript 指令**（把 PNG 圖片資料寫入 macOS 剪貼簿）：
```bash
osascript -e 'set the clipboard to (read (POSIX file "/absolute/path/to/image.png") as «class PNGf»)'
```

**注意事項**：
- 路徑必須是絕對路徑
- `«class PNGf»` 把檔案內容當作 PNG 圖片資料放入剪貼簿（而非檔案參考）
- Finder Cmd+C 複製的是檔案參考（file reference），不是圖片 data——瀏覽器收到檔案參考會貼成螢幕截圖或不被接受
- osascript 方式在 Bash tool 裡直接執行，不需要開 Finder
- 此方法僅適用於 macOS（osascript 是 AppleScript）

---

## 方法二：API 自動化

### X API（twitter-api-v2）

**費用**：Pay-per-use
- 文字 tweet：$0.015/則
- 含 URL tweet：$0.20/則
- Media upload：v1.1 chunked（OAuth 1.0a，免費但需 elevated access）

**設定步驟**：
1. developer.x.com → 註冊 developer account
2. 建立 Project + App
3. 設定 OAuth 2.0 (PKCE) — User Authentication Settings
4. 記下 Client ID + Client Secret
5. 設定 callback URL（可用 `http://localhost:3000/callback`）

**Node.js 範例**：
```javascript
import { TwitterApi } from 'twitter-api-v2';

const client = new TwitterApi({
  appKey: process.env.X_API_KEY,
  appSecret: process.env.X_API_SECRET,
  accessToken: process.env.X_ACCESS_TOKEN,
  accessSecret: process.env.X_ACCESS_SECRET,
});

// 發文
const { data } = await client.v2.tweet('孢子文案 + URL');
console.log(`Posted: https://x.com/taiwandotmd/status/${data.id}`);

// 帶圖發文
const mediaId = await client.v1.uploadMedia('./spore-image.png');
await client.v2.tweet({ text: '孢子文案', media: { media_ids: [mediaId] } });
```

**Python 範例（tweepy）**：
```python
import tweepy

client = tweepy.Client(
    consumer_key=os.environ['X_API_KEY'],
    consumer_secret=os.environ['X_API_SECRET'],
    access_token=os.environ['X_ACCESS_TOKEN'],
    access_token_secret=os.environ['X_ACCESS_SECRET'],
)

response = client.create_tweet(text="孢子文案 + URL")
print(f"Posted: https://x.com/taiwandotmd/status/{response.data['id']}")
```

### Threads API（graph.threads.net）

**前置**：
- taiwandotmd IG 必須是 Professional 帳號（已確認是）
- 需建立 Meta Developer App
- 需通過 App Review（`threads_basic`, `threads_content_publish` permissions）
- Dev mode 可先測自己帳號（不需 Review）

**設定步驟**：
1. developers.facebook.com → 建立 App（Business type）
2. Add Product → Threads API
3. Generate User Token（需 IG 帳號授權）
4. Dev mode 下可直接測試 publish

**兩步驟 container 模型**：
```bash
# Step 1: 建立 container
curl -X POST "https://graph.threads.net/v1.0/me/threads" \
  -d "media_type=TEXT" \
  -d "text=孢子主貼文案" \
  -d "access_token=$THREADS_TOKEN"
# → { "id": "container_id" }

# Step 2: 發佈
curl -X POST "https://graph.threads.net/v1.0/me/threads_publish" \
  -d "creation_id=container_id" \
  -d "access_token=$THREADS_TOKEN"
# → { "id": "post_id" }

# Step 3: Self-reply（reply_to_id = 剛發的 post_id）
curl -X POST "https://graph.threads.net/v1.0/me/threads" \
  -d "media_type=TEXT" \
  -d "text=完整故事 👉 URL" \
  -d "reply_to_id=post_id" \
  -d "access_token=$THREADS_TOKEN"
# → container for reply

curl -X POST "https://graph.threads.net/v1.0/me/threads_publish" \
  -d "creation_id=reply_container_id" \
  -d "access_token=$THREADS_TOKEN"
```

**帶圖**：
```bash
curl -X POST "https://graph.threads.net/v1.0/me/threads" \
  -d "media_type=IMAGE" \
  -d "image_url=https://taiwan.md/spore-images/xxx.png" \
  -d "text=孢子文案" \
  -d "access_token=$THREADS_TOKEN"
```
注意：`image_url` 必須是公開可訪問的 URL（不能是 local file）。taiwan.md 的 spore-images 部署後即是公開 URL。

**限制**：
- 250 posts / 24hr
- 500 chars / post
- 圖片需公開 URL
- Rate limit: 250 API calls / user / hour

---

## 整合流程（Chrome MCP 版）

完整的從孢子到發文的 end-to-end 流程：

```
1. SPORE-PIPELINE Stage 4 SHIP 交付：
   - 文案（中文 150-300 字）
   - Threads UTM URL: taiwan.md/.../?utm_source=threads&utm_medium=spore&utm_campaign=s{N}
   - X UTM URL: taiwan.md/.../?utm_source=x&utm_medium=spore&utm_campaign=s{N+1}
   - 配圖（landscape 1600×900 / square 1080×1080）

2. Platform allocation 已決定（per SPORE-PIPELINE §Platform allocation）

3. 觀察者確認文案 + 平台選擇

4. 執行發文（Chrome MCP）：

   a. 圖片準備（共用）：
      - osascript 把 square 配圖寫入剪貼簿
        `osascript -e 'set the clipboard to (read (POSIX file "{abs_path}") as «class PNGf»)'`

   b. IF X：
      - navigate → x.com/home
      - left_click compose 區域
      - key cmd+v → 圖片從剪貼簿貼入
      - type 文案 + inline UTM URL
      - ⚠️ 觀察者確認 → left_click Post
      - navigate → @taiwandotmd profile → 點最新 post → 擷取 URL

   c. IF Threads：
      - navigate → threads.net
      - 點「新串文」→ compose modal
      - left_click 第一則輸入框
      - key cmd+v → 圖片從剪貼簿貼入
      - type 主貼文案（第一則，不含連結）
      - 點「新增到串文」→ 第二則輸入框
      - type self-reply「完整故事 👉 {Threads UTM URL}」
      - ⚠️ 觀察者確認 → 點「發佈」（兩則同時送出）
      - navigate → @taiwandotmd profile → 點最新 post → 擷取 URL

5. 後處理：
   - 記錄到 SPORE-LOG.md（URL 乾淨化：剝掉 query string）
   - 寫回源文章 frontmatter sporeLinks
   - git commit
```

---

## 方法選擇建議

| 需求               | 推薦方法                        | 原因                                        |
| ------------------ | ------------------------------- | ------------------------------------------- |
| 立即可用、不需設定  | Chrome MCP + osascript 貼圖     | 零設定，今天就能用，含圖片全自動              |
| 帶圖自動化         | Chrome MCP + osascript 貼圖     | ✅ 已解決——不需要 API                        |
| 全自動（無人值守）  | API + cron                      | Chrome MCP 需要瀏覽器開啟                    |
| 最低成本           | Chrome MCP + osascript          | API 路線 X 每則 $0.015-0.20                  |
| Threads self-reply | Chrome MCP 串文模式             | 一次送出主貼 + self-reply                    |

**目前推薦**：Chrome MCP + osascript clipboard paste。文字 + 圖片 + URL 全自動，觀察者只需確認後按發佈。零成本、零設定、今天就能用。

---

## 開發優先級

| 優先 | 項目                                        | 前置         | 預估                  |
| ---- | ------------------------------------------- | ------------ | --------------------- |
| P0   | ~~重設 taiwandotmd IG 密碼~~                 | ~~email~~    | ✅ 已解決              |
| P1   | Chrome MCP 文字發文（雙平台）                | 無（已就緒） | ✅ 已測試              |
| P1   | Chrome MCP 圖片上傳（osascript paste）       | 無           | ✅ 已測試（雙平台）    |
| P2   | 第一次實戰走完整流程（下一篇 spore）          | 無           | 下次 /twmd-spore      |
| P3   | X Developer Account 申請（backup）           | 無           | 審核 1-3 天            |
| P3   | Meta Developer App 建立（backup）            | IG 登入      | 設定 1hr + 審核 7-14d  |
| P4   | API 自動化 script（X + Threads）             | P3 完成      | 4hr                   |

---

## 安全與治理

- **觀察者 confirm gate**：每次發文前必須經觀察者確認（MANIFESTO §自主權邊界）
- **不存 credentials 在 repo**：API keys 放 `.env`（gitignored）或系統 keychain
- **Rate limit 遵守**：X 50/day、Threads 250/day，script 內建 counter
- **Dry-run mode**：所有自動化 script 預設 `--dry-run`，加 `--publish` 才真的發
- **回滾**：Threads/X 都支援刪除貼文，但觸及已發生無法收回
- **Threads IG 連動**：登入 IG 帳號 = 自動切換 Threads 帳號，注意不要混用 cheyuwu345 / taiwandotmd

---

## 附錄：平台比較

| 維度             | X                             | Threads                         |
| ---------------- | ----------------------------- | ------------------------------- |
| **帳號**         | @taiwandotmd（Premium ✓）    | @taiwandotmd（Professional IG） |
| **字數**         | 25,000（Premium）/ 280（免費）| 500 chars                       |
| **孢子適合度**   | ✅ 150-300 字 + URL 沒問題    | ✅ 150-300 字 + URL 沒問題      |
| **Self-reply**   | 不需要（單則含 URL）          | 串文模式（1/2 主貼 + 2/2 URL）  |
| **Compose 方式** | Home feed 頂部 inline         | Modal popup                     |
| **URL 預覽**     | 自動展開 OG card              | 自動展開 OG card                |
| **圖片 file_upload** | ❌ 被拒（hidden input）    | ❌ 被拒（hidden input）         |
| **圖片 clipboard** | ✅ osascript + Cmd+V        | ✅ osascript + Cmd+V            |
| **API 費用**     | $0.015-0.20/post              | 免費                            |
| **API 認證**     | OAuth 2.0 PKCE                | OAuth 2.0 via Instagram         |
| **API 圖片**     | Local file upload（v1.1）     | 公開 URL only                   |
| **Rate limit**   | 50 posts / 24hr               | 250 posts / 24hr                |
| **Post URL**     | x.com/.../status/{id}         | threads.com/...post/{code}      |

---

_v0.3 | 2026-05-18 | osascript clipboard paste 突破圖片上傳：X ✅ / Threads ✅ 雙平台全自動化（文字+圖片+URL），觀察者只需確認_
_v0.2 | 2026-05-18 | Chrome MCP 雙平台完整實測：X compose ✅ / Threads compose+串文 ✅ / 圖片上傳雙平台 ❌ / X Premium 字數不受限 / Threads 串文一次送出 self-reply_
_v0.1 | 2026-05-17 | 初版：Chrome MCP X 流程實測 + Threads 架構文件 + API 規格整理_
