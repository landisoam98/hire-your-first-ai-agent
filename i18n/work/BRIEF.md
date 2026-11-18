# Mandarin translation brief — "Hire Your First AI Agent" seminar deck

You translate one chunk of an HTML slide deck from English into **Simplified Chinese** for a Malaysian audience: owners and accounts/warehouse staff of small and medium companies who use SQL Account (accounting software). They are business people, not engineers.

## Input
`i18n/work/chunk-N.json` → `slides[]`, each with:
- `key`: the slide id (e.g. `typed-three-times`)
- `file`: the English slide (`slides/NN-key.html`). **Read it** to see where each text sits, how texts are split by inline tags (`<b>`, `<em>`, `<span>`), and how much space there is.
- `texts`: the English text pieces that need Chinese (each is the text between 2 HTML tags, whitespace-normalised, entities decoded, or an `alt` / `data-type` attribute, or a page label/section name)
- `notes`: the English speaker notes (a spoken script)

## Output
Write **one JSON file**: `i18n/parts/zh-N.json` (N = your chunk number), UTF-8, shaped exactly:
```json
{
  "texts":     { "<English piece exactly as given>": "<中文>" },
  "overrides": { "<slide key>::<English piece>": "<中文 for this slide only>" },
  "notes":     { "<slide key>": "<中文 speaker notes>" }
}
```
- Every item in every `texts` list must get an entry in `texts` (or `overrides`). Keys must match the English **character for character**.
- Use `overrides` only when the same short English piece needs a different Chinese on a specific slide.
- Validate your file parses as JSON before finishing (e.g. `python3 -c "import json;json.load(open('i18n/parts/zh-N.json'))"`).

## Split sentences
A sentence split across tags (e.g. `Every order is keyed in ` + `<span>by hand</span>`) is translated piece by piece, and the pieces are joined back in the same order. Write the Chinese so the joined result reads naturally, e.g. `每张订单都靠` + `人手输入`. If Chinese word order makes that impossible, put the meaning where it reads well and use `""` (empty string) for a piece that is no longer needed. Keep the emphasised piece (the one in `<b>`/`<span class="sig">`/`<em>`) holding the key words.

## Style
- Plain, spoken, confident. Short. Headlines punchy. No 书面腔 jargon. Malaysian business Mandarin is fine.
- **Numbers stay as digits**: "3x" → "3 倍", "5 problems" → "5 个问题", "2 months" → "2 个月". Keep "RM", amounts, dates, codes, times as they are.
- Chinese must fit the same space: aim for the same or shorter visual length than the English. Labels/chips/buttons especially short.
- Use full-width Chinese punctuation （，。：；“”？！） inside Chinese sentences.
- Small uppercase mono labels (e.g. `HOW IT WORKS`, `PART 2 OF 5`) → short Chinese (`运作方式`, `第 2 部分，共 5 部分` → better `第 2/5 部分`).

## Keep in English (do not translate)
Product, brand and standard business/document terms people already say in English:
SQL Account, SuDu AI, SuDu, WMS, MES, ERP, AI, AI Agent (use "AI Agent" for "AI agent"/"agent"; plural also "AI Agent"), LLM, Token, Context Window (may add 上下文窗口 once), ChatGPT, Claude, Gemini, DeepSeek, OpenAI, Anthropic, Google, Claude Code, Codex, WhatsApp, Excel, PDF, Email, Dashboard, Routine, Task, SOP, KPI, ISO 27001, e-Invoice / e-invoicing (LHDN MyInvois), Sales Order (SO), Invoice, Sales Invoice (SI), Purchase Order (PO), Purchase Invoice (PI), Delivery Order (DO), Goods Delivery, Goods Receiving (GRN), Credit Note, Debit Note, Customer Payment, Supplier Payment, Stock Adjustment, Stock Count, Stock Transfer, Quotation, Picking List, Packing List, Putaway, BOM, Traveller Card, Production Order, QC, P&L, SOA (Statement of Account), UOM, FIFO/FEFO, GRN, Bin, Batch.
Agent names stay English: Sales AI, Inventory AI, Purchase AI, Collection AI, Payment AI, Up Sales AI, Finance AI, and the people/agent names (Sasha, Ivan, Puteri, Cody, Uma, Felix, Mei Ling, Kumar, Rahman, Wong, Jason, Ah Seng, Kak Ros, Landis, Owen, Jordan Lee).
Company, customer, supplier and place names stay as they are (Maju Jaya Foods, Jaya Grocer KL, Kedai Ali, Golden Palm, Petronas Twin Towers → 双峰塔 is OK, Mega Mart...).
Malay / rojak quotes stay exactly as they are (bwg besar 10kg x ---, nasi lemak, hantar esok, Terima kasih, Dah bank in boss, Jumaat saya bayar, bila nak bayar...). Product names (Milo, Maggi, Horlicks) stay.

## Preferred Chinese terms
customer 客户 · supplier 供应商 · stock / inventory 库存 · warehouse 仓库 · factory 工厂 · order 订单 (but "Sales Order" stays English) · approve/approval 批准 · credit limit 信用额度 · overdue 逾期 · payment 付款 · collect / collection 收款 · price list 价格表 · item code 货品编号 · key in / type in 输入 / 打单 · manual 手动 / 人手 · staff 员工 · boss 老板 · clerk 文员 · accounts 会计 · training 训练 · pre-training 预训练 · fine-tuning 微调 · hallucination 幻觉 · prompt 提示词 · tool 工具 · memory 记忆 · rules & skills 规则与技能 · permission 权限 · brain 大脑 · harness 驾驭框架 (or keep "harness") · workflow 流程 · physical AI 实体 AI · robot 机器人 · seminar 讲座 · worksheet 作业纸 · table host 桌长.

## Speaker notes
Translate as a natural spoken Mandarin script the presenter can read aloud. Keep the structure: `(Next)` → `（下一步）`, `Next:` → `下一页：`, `Do:` → `操作：`, `Note:` → `备注：`, `Prep:` → `准备：`, stage directions in brackets stay in brackets. Quotes of what to say keep the quote marks “ ”. Keep the same English terms as above. Digits for numbers when it's a figure on screen; spoken words are fine for small numbers in the script.

## Don'ts
- Don't edit any file other than your own `i18n/parts/zh-N.json`.
- Don't invent content or drop meaning. Don't add explanations.
