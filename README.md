# Hire Your First AI Agent — HTML deck

77 slides built from `../seminar-syllabus.md` with the huashu-design skill. The SuDu introduction (two speaker slides, who we are, vision, the map, four layers in 3D, five stages) the top 5 issues slide after the poll, one slide per problem, and the What is AI? section (section page, Types of AI, What is an LLM, What is an AI agent, why SuDu if I already have SQL Account) is written fresh, not from the syllabus.
Works offline: fonts, logos, avatars and product screens are all in `assets/`.

Slide 5 is today's agenda in 5 parts; slide 6 is the 3 things people take home (a clear picture of AI, how to plan AI for their business, a free Demo AI Account).

Running order (set in `main()` of `build.py`, 1 list per section): Company intro → Speaker intro → What is an AI Agent? → The problem → SuDu AI (intro + live demo) → Workshop (slide 66 is the Workshop section page; slide 67: "Find your number. Join your group." with 3 big group tiles, 1, 2 and 3 (the number on each name tag), "Your coach guides you here"; groups are in `WG_GROUPS`) → Get started → Questions.

Event: 18/11/2026 & 19/11/2026, Esoft Alor Setar, 10:30 am to 3:30 pm (SuDu team stays until 5:45 pm).

## What is AI? section

Slides 7–14 (What is an AI Agent?): section page; 5 types of AI by what they do (5 steps: Predictive, Vision, Voice, Diffusion, AI Agent); what an LLM is, a guess, then how much it read (2 steps); why we need an AI Agent (picture panels); meet your AI Agent; the robot with 5 parts (6 steps); good agent vs bad agent, Ah Malas (in a tudung, `assets/av/malas-tudung.svg`) vs Ah Rajin (4 steps); set up like a new hire. Slide 15 is your before AI / after AI meme image (`assets/img/meme-before-after.webp`). Slide 16 (Imagine) is the big-vision bridge: AI runs the office today, physical AI walks the floor next, one day the company runs itself; slide 17 plays the Figure AI video "F.03 at BMW" (`assets/video/f03-bmw.mp4`, 1 minute, starts with sound when the slide opens; click it to pause, or to turn the sound on if the browser starts it muted). Slides 18–21 introduce SuDu (vision, the map, 5 stages, 4 layers in 3D). Slide 22 opens The problem (Part 2 section page). Slide 31 (2 inner steps: it opens on "Once you start using AI, are these problems solved?", Next reveals "Not necessarily." / 不一定, Next again shows: AI without tools is just a Guru: 3 confident tips, a 只会讲，不会做 stamp, vs AI with SuDu WMS, MES and SQL Account) and slide 32 (a new way of working: the AI Agent, with the SuDu logo on its head, thinks and executes; you set the rules, monitor and approve) close the problem section. Slide 34 (no tools, no work) opens the SuDu AI section; slide 35 plays the SuDu WMS preview video (`assets/video/wms-preview.mp4`, 3:16, with subtitles); slide 36 is the FAQ intro page; slides 37 (FAQ 1: why SuDu if I have SQL Account) and 38 (FAQ 2: can I connect Claude or Codex straight to SQL Account) follow; slide 40 is your pool meme (`assets/img/meme-pool.webp`) just before the demo; then slide 37 (why SuDu): it opens on a 3-card chain (the brain → the tools → your ERP), then 1 inner step, "No proper ERP, no AI work". Slide 41 opens the live demo (7 parts); slide 66 opens the Workshop (Part 4). Left out of the deck but still in `build.py` (`DROP` in `main()`): 70 years of AI, What is an LLM?, the agent loop, the chatbot-or-agent quiz, SQL Account stays, the foundation (WMS and MES), the AI team, the Setting up intro, the AI readiness QR and check, the closing line.

## Present

Open `index.html` in Chrome.

| Key | Does |
|---|---|
| → / Space | next slide |
| ← | previous slide |
| N | speaker notes (the "Say" script from the syllabus) |
| G / Esc | overview wall of all slides |
| F | full screen |

Slide 21 (four layers) has 5 inner steps: Next flips SQL Account up to face you, then WMS, MES and AI agents each land on top while the earlier layers fall back and blur, then all four fold into the 3D stack.
Slide 8 (types of AI) has 5 inner steps: it opens on the 5 types, then each Next flies a 3D card in (same build as the old 70 years of AI), each with a real-life scene: sales forecast, car park plate reader lifting the barrier, WhatsApp voice note to order, an AI short drama frame coming out of noise (diffusion), agent checklist waiting for approval.
Slide 9 (how much it read) has 2 inner steps: it opens on what an LLM is (Large, Language, Model, trained on a huge amount of text); Next shows a guess (A 10,000 / B 1 million / C 20 million / D 100 million books, each with its stacked height and reading years); Next again reveals that the real answer beats D: 240 million books (big), 32 trillion tokens (small), then the Twin Towers / Moon scene plays from the start. The Mandarin page counts to 2.4 亿 (`data-zh` on the counter).
Slide 37 (why SuDu) has 1 inner step: the question opens big and centred, Next moves it up and brings in the 4 layers.
Slide 10 (why we need an AI Agent): 2 picture panels on Ali's egg order: Mei Ling told what to type by a chatbot, vs the real SuDu approval card the agent drafted. Slide 11 introduces the agent as a new staff member. Slide 12 (the robot) has 6 inner steps: the 5 parts, then the 5 parts on 1 order. Slide 13 (good vs bad agent) has 4 inner steps: 9 am, 11:30 am, 4 pm, then the score (1 job vs 5 jobs).
| 1–9 | jump to slide 1–9 |
| P | print |

Each slide plays its own entrance when it opens (staggered text, count-ups, the house drawing itself, the sun crossing the demo day, the 15-minute break timer). Add `#static` to a slide's URL to see it with every animation finished.

## Mandarin version (中文版)

Open `index-zh.html` in Chrome, or press **L** in either deck to switch language on the same slide.

English is the single source (`build.py`). Every `python3 build.py` also writes the Chinese deck (`slides-zh/`, `index-zh.html`) through `i18n.py`, and prints how many texts and notes still have no Chinese:

```
zh: 77 slides, 0 texts missing, 0 notes missing
```

After an English edit, the new or changed text is listed in `i18n/zh-missing.json` (slide notes in `i18n/zh-notes-missing.json`). Add the Chinese to `i18n/zh.json` (`"English": "中文"`, or `"slide-key::English"` for 1 slide only) and `i18n/zh-notes.json`, rebuild until both counts are 0, then run `python3 make_thumbs.py` (it renders both `thumbs/` and `thumbs-zh/`). Translation style and the terms kept in English (Sales Order, Invoice, PO, SQL Account, WMS, MES, AI Agent, Token…) are in `i18n/work/BRIEF.md`.

## Edit

All slide text lives in `build.py` (one block per slide; `notes` = speaker notes). After an edit:

```bash
python3 build.py
```

This rewrites `slides/*.html` and `index.html`. If a slide's look changed, also run `python3 make_thumbs.py` so the overview pictures in `thumbs/` match (the overview shows pictures, not live slides, so it stays smooth). Where the Chinese needs no space between 2 pieces but English does (e.g. before a highlighted phrase), the source has no space and an English-only CSS rule adds it (`:lang(en) { margin-left: .26em }`). Shared look: `shared/deck.css`; shared behaviour: `shared/deck.js`; deck shell: `shell.html`.

## Blanks still to fill

- Slide 72: Standard is highlighted as the recommended plan (4 plans, Lite dropped) — change if you pick another
- Slide 73: which fees can be claimed under HRDF (Esoft offer) — to confirm
- Slides 70–71: manual cost and savings are an estimate for a wholesaler with about 80 orders a day (Pro plan at RM2,000 a month)

The QR code is on slide 23 (problem poll, `assets/qr-survey.png`). The AI readiness QR and check are left out of the deck.

Slide 68 asks 5 WMS and 5 MES questions; 3 or more yes on a side means that layer is needed from day 1. It is worksheet box 2B, so add those 10 questions to the printed worksheet.

Get started (slides 69–76): onboarding in 3 steps, manual work cost, manual vs AI cost, plans, HRDF claimable (Esoft), next step (free 45-minute Online Demo, 20% off within 14 days), upcoming courses (dark premium cards; 01 Smart Warehouse Bootcamp glows with a running light and shows RM399 per person (`UC_PRICE`), 02 Smart Factory Bootcamp, 03 AI Agent Masterclass; 1 inner step: the cards fade back and card 01's detail panel fades in with 4 modules (`UC_DETAIL`) and what they leave with (`UC_TAKE`); dates, fees and HRDF to confirm), don't wait.

## Live demo

Slides 41–65 follow `../Seminar demo prep.md`: a Live demo section page, meet the 6 agents, then 7 parts (Setting up is 1 slide, with no separate intro) (Setting up, Sales, Inventory, Purchase, Collection, Up Sales, Finance AI). Each part opens with an intro slide (the agent, its use cases, a 7-step progress bar), then 1 slide per use case. Web and mobile jobs show the SuDu AI app (Tasks module look); WhatsApp jobs show a phone chat. Edit them in `build.py` under `USECASES`. A `|` in a use-case title is a line break on that use-case slide only (the intro list and notes show a space).

## Files

- `index-zh.html`, `slides-zh/`, `thumbs-zh/` — the Mandarin deck, generated by `i18n.py` (do not edit by hand)
- `Hire Your First AI Agent.pdf` — every slide with animations finished, for sharing or printing (5 MB; slides are images, so text is not selectable)
- `brand-spec.md`, `direction-approved.md`, `polish-log.md` — huashu-design checkpoints
