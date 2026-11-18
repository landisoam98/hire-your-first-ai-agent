# Plain-language pass — brief

The deck is for Malaysian SME owners and their office/warehouse staff. Many use English as a 2nd language. Every on-screen word must be instantly clear to them. The presenter asked: "the language is weird, make it more layman term", starting from the problem-4 title "The book says 40, the shelf says 12" ("book" meaning the accounting record is confusing).

## Your job
Review the slides in your range **page by page**. For each slide, read the rendered English in `slides/NN-name.html` (visible text only; ignore CSS/JS) and find wording that is jargon, an idiom, too abstract, or odd. Propose plain replacements.

You do **not** edit any file except your output. Output: `i18n/work/plain-N.json`:
```json
[
  {"slide": "17", "old": "<exact substring copied from build.py>", "new": "<replacement>", "why": "<3-8 words>"}
]
```
- `old` must be copied **exactly** from `build.py` (the source; on-screen text lives there inside Python strings, often with HTML entities like `&rsquo;` `&ldquo;` `&middot;` and inline tags). Check with Python that `build.py.count(old) == 1`; if it appears more than once, include more surrounding characters until it is unique. Never span across Python string boundaries or code.
- `new` keeps the same HTML entities/tags style and must not break Python quoting (no unescaped `'` inside a '...' string — use `&rsquo;`).
- If an on-screen phrase you change is also quoted in that slide's speaker notes (the long `"\"...\""` string after the slide), add a 2nd item updating the notes too.
- Validate your JSON parses, and that every `old` is unique in build.py.

## Rules for the new wording
- Short, common words. Say what people do and see at work: "the system", "SQL Account", "the shelf", "your records", "your accounts", "the order", "the boss".
- Replace accounting/IT jargon and idioms: "the books" (→ "your accounts"/"SQL Account"), "posting/posted" (→ "saved into SQL Account"/"recorded"), "ledger", "debtors" (→ "customers who owe you"), "reconcile", "variance", "putaway" (→ "put on the shelf"), "FIFO/FEFO" (→ "oldest stock first"), "sync", "harness" only where it is explained, "single source of truth", "end to end", "visibility", "leverage", "workflow" (→ "the steps"), "master mind", etc.
- Keep these standard terms as they are (people use them daily): SQL Account, WMS, MES, ERP, AI, AI Agent, LLM, Token, WhatsApp, Excel, PDF, Sales Order, Invoice, PO / Purchase Order, Delivery Order, Credit Note, Customer Payment, Stock Count, BOM, SOP, Dashboard, credit limit. A term that a slide deliberately teaches (Token, Context Window, hallucination, harness, loop engineering) stays, because the slide explains it.
- Keep every number, fact, name and quote (customer chat, Malay/rojak text, sample documents) unchanged. Numbers stay digits ("3x", "5 problems").
- Keep the length the same or shorter: slides have fixed space. Titles stay punchy.
- Don't rewrite text that is already clear. It is fine to propose few changes on a good slide. No new content, no marketing tone.
- Leave the live-demo screen mock-ups (fake app/WhatsApp screens) alone, except headings/steps around them.

When done, report: how many changes, and the 3 most important ones.
