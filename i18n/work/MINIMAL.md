# Brief: redesign the "What is an AI Agent?" chapter (19 slides)

The presenter's words: *"make the slide design clean, minimalist, easy to read and understand, add some smooth animation. For content, make it less technical, but I want them to learn something, easy to understand by layman."*

Audience: Malaysian SME owners and office/warehouse staff (SQL Account users). English is often a 2nd language. They are smart business people, not engineers. Every slide must be understood in 5 seconds and teach 1 thing they remember.

## How you work
- Deck: `/Users/landisoam/Desktop/Seminar slide/agent-seminar-deck/`. All slides live in `build.py` as `slide(file, label, section, theme, attrs, css, html, notes)` calls. Read the current version of each of your slides there (grep `slide('..-<key>'`), and look at `thumbs/NN-<key>.jpg` to see it.
- **Do not edit build.py or any deck file.** Write ONE fragment file: `i18n/work/min-<X>.py` (X = your batch letter). It contains your helper constants and one top-level `slide(...)` call per slide, in the running order. Keep each slide's **file key** (the part after `NN-`, e.g. `'08-machine-learning'` → key `machine-learning`; you may keep the same full first argument), `SEC[2]` as section, and the same label unless a better plain label is obvious.
- Prefix every module-level name you define with `A_` + your batch letter (e.g. `AA_HIST`, `AA_rows()`), so nothing in build.py is overwritten. Available helpers in build.py: `ic(svg_path, size, stroke)` (24×24 line icon), constants `CHECK`, `LOCK`, `PEN`, `TICK`, and `MIN_CSS`.
- Test as often as you like: `python3 i18n/work/try_min.py i18n/work/min-<X>.py` builds into `i18n/work/out-<minX>/` and saves screenshots `shots/<key>.png` (finished) and `shots/<key>-live.png` (2.5 s in). **Open and look at every screenshot** (Read tool on the PNG). Iterate until each slide is clean: nothing overlapping, nothing cut off, nothing touching the footer (bottom ~120px holds the SuDu logo and section name), good balance of space.

## Design system (use it — consistency across all 19 slides matters)
- Start your css with `MIN_CSS + '''...your extra css...'''`. MIN_CSS gives: light paper background (`theme='light'`) or deep green (`theme='dark'`), no decorative glow, and these classes:
  - `.mk` small kicker label · `.mt` big title (78px; `<em>` = green accent word) · `.ml` lead sentence (34px)
  - `.m3` a row of 3 takeaways at the bottom (`<div><b>Title</b><p>line</p></div>` ×3)
  - `.mn` giant number (`<small>` for the unit) · `.mq` a chat-bubble quote · `.mnote` small footnote
  - Motion: `.u` rise + fade, `.uf` fade, `.ux` slide in from left, `.ug` grow a line/bar from the left. Stagger with `style="--d:.4s"`. All of them snap to the end state automatically for thumbnails/PDF.
- Minimalist rules:
  - **1 idea per slide.** A title that says the point (≤ 9 words), 1 lead sentence, then 1 visual or at most 3–5 short items. Cut everything else into the speaker notes.
  - **Readable from the back row:** body text ≥ 26px, labels ≥ 18px, titles 64–80px. No paragraphs on screen; no sentence longer than ~14 words.
  - **Calm:** mostly white space, no boxes inside boxes, no more than 1 accent colour (green; amber `#FFB547` only for a warning/limit). Thin lines and plain type over heavy cards. Icons small and few.
  - Light theme by default. Dark only for the section opener (`section-ai`), the big-number slide (`how-much-it-read`) and at most 1 other "wow" slide in your batch.
  - Motion is smooth and purposeful: elements arrive in reading order (title → lead → items), each ~0.15–0.25 s apart, everything settled by ~3 s. One signature animation per slide at most (a line drawing, a bar growing, a counter, a typewriter). Nothing loops fast or flashes. Never animate `filter: blur` (it flickers).
  - Existing per-slide extras you may keep: `data-count="32" data-delay="1" data-dur="1.5"` count-up on a `<span>`, `data-type="text" data-delay="1" data-cps="14"` typewriter.
- Write numbers as digits ("3x", "5 problems", "1 million"). Plain words; teach 1 term at most per slide and explain it in the same line.
- Do not sell SuDu in this chapter (no "SuDu does X"); generic business examples (a WhatsApp order, stock, a customer who pays late) are good. Keep facts/numbers already on the slides correct; don't invent new statistics.

## Speaker notes (`notes`, the last argument)
A natural spoken script in plain English the presenter reads, as a Python string with `\"` quotes like the existing ones: what to say, in order, matching the screen; short stage directions in brackets; then a final line `Next: "<lead-in to the next slide>"`. Keep any `Note:` with sources that already exists.

## The 19 slides, in order, and the 1 thing each must teach
1. `section-ai` — chapter opener (dark): "What is AI?" and the 3 steps of the chapter: how AI grew up → the brain (LLM) → the agent.
2. `ai-history` — AI did not appear overnight: rules → machine learning → deep learning → LLM → agents. Simple timeline; keep years; at most 1 short line each.
3. `machine-learning` — machine learning = learns a pattern from your past examples and predicts 1 thing (e.g. who will pay late). Model names (random forest, XGBoost, LightGBM, CNN) only as a small "names you may hear" line.
4. `what-is-llm` — an LLM is a machine that predicts the next word, very well. Show it with 1 sentence being completed. ChatGPT / Claude / Gemini / DeepSeek named small.
5. `how-much-it-read` — how much it read (DeepSeek V4: 32 trillion tokens ≈ 240 million books; 13,000 Twin Towers; 50 trips to the Moon; 800 football fields). KEEP the existing tower → Moon animation code and numbers; make the text side minimal (1 hero number + 1 line + at most 3 small facts).
6. `what-it-read` — it read the world (public internet, books, many languages), never your company (your prices, stock, chats). 2 simple columns.
7. `tokens` — it reads in small pieces called tokens; keep the token-splitting animation; 2 plain takeaways: you pay per token, and it can only hold so much at once.
8. `meaning-map` — it stores meaning as a map: words used the same way sit close together (bawang / onion / 洋葱; bwg next to bawang). Keep the map, cut the text.
9. `how-it-learned` — how it learned: guess the next word → check → adjust → repeat trillions of times; then coached by people; then frozen (cut-off date). Make the 4-step loop the visual.
10. `next-word` — how it writes an answer: 1 word at a time, picking the most likely word (nasi lemak … breakfast 82%). Keep the bar chart; end with its 3 limits in plain words.
11. `compare-llms` — not all brains are equal: 7 plain things to compare (how smart, how much it can read at once, cost, speed, thinks step by step, size, how it's built). Very short words each; less technical.
12. `dense-moe` — 2 ways to build the brain, explained ONLY through the office analogy: dense = everyone reads every email; mixture of experts = the receptionist sends each email to the 2 people who know the topic → cheaper and faster. Keep "DeepSeek V4: 1.6T in total, 49B per word" as a small footnote.
13. `makes-things-up` — it sounds sure even when wrong (hallucination): with no facts it guesses; let it look up your records. Keep the 2-chat comparison (RM10,000 made up vs RM5,000 looked up), 3 short rules.
14. `why-agents` — an LLM alone only talks; people added 6 things to make it work: tools, look-up, memory, a loop, rules, permission → an AI Agent. Calm, iconic.
15. `what-is-agent` — the robot with its 5 parts (brain, tools, memory, rules, permission). KEEP the robot SVG and the in-slide step mechanism: the slide must keep 6 Next-steps driven by `addEventListener('message', ...)` setting `document.body.dataset.s` 0–6 (0 = all parts, 1–5 = 1 part highlighted with a short plain explanation + example, 6 = the 5 parts on 1 order). Simplify the text panel: 1 plain sentence + 1 example per part.
16. `agent-loop` — it works in a loop: think → act → check → repeat, until done or until it needs you. Keep the loop; 1 short worked example (a WhatsApp order, 3 rounds) in very few words.
17. `brain-to-staff` — you set up an AI Agent like a new hire: job description, logins, files, SOP, a supervisor, probation. Simple 2-column mapping, short.
18. `harness` — same brain, different results: the setup around it ("harness") decides. 1 clean visual (brain in the middle, 6 parts around), 1 line on "loop engineering" in plain words (design the steps, when to stop, when to ask a person). "The brain is rented. The harness is built."
19. `tools-and-memory` — no tools, no work: a brain alone gives advice; with tools it does the job inside your systems (ERP = the core of the company). Same WhatsApp order, 2 outcomes.

## Done = 
Your fragment builds, every slide's 2 screenshots look clean and consistent with the rules above, and you report: the file path, the slide keys, and 1 line per slide on what changed. Keep the report short.
