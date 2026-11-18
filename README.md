# Hire Your First AI Agent — HTML deck

72 slides built from `../seminar-syllabus.md` with the huashu-design skill. The SuDu introduction (two speaker slides, who we are, vision, the map, the map in detail, four layers in 3D, five stages) the top 5 issues slide after the poll, one slide per problem, and the What is AI? section (section page, What is an LLM, What is an AI agent, why SuDu if I already have SQL Account) is written fresh, not from the syllabus.
Works offline: fonts, logos, avatars and product screens are all in `assets/`.

Slide 5 is the overview of the afternoon: 5 parts and the 3 things people leave with.

Running order (set in `main()` of `build.py`, 1 list per section): Company intro → Speaker intro → What is an AI Agent? → The problem → SuDu AI (intro + live demo) → Workshop → Diagnosis → Questions → Spare.

## What is AI? section

Slides 6–13 (What is an AI Agent?): section page; 70 years of AI (5 steps, 3D cards); an LLM predicts the next word; what a token is (1 step); how much it read; why we need an AI Agent, then the robot (7 steps); the agent loop; set up like a new hire; no tools, no work.

## Present

Open `index.html` in Chrome.

| Key | Does |
|---|---|
| → / Space | next slide |
| ← | previous slide |
| N | speaker notes (the "Say" script from the syllabus) |
| G / Esc | overview wall of all slides |
| F | full screen |

Slide 27 (four layers) has 5 inner steps: Next flips SQL Account up to face you, then WMS, MES and AI agents each land on top while the earlier layers fall back and blur, then all four fold into the 3D stack.
Slide 8 (what is an LLM) has 1 inner step: the sentence splits into tokens.
Slide 7 (70 years of AI) has 5 inner steps: each Next flies a 3D card in over the timeline (Rules, Machine learning, Deep learning, LLM, AI agents), each with its own short animated scene, a "think of it like" comparison, examples, use in your company and its limit.
Slide 23 (why SuDu) has 1 inner step: the question opens big and centred, Next moves it up and brings in the 4 layers.
Slide 10 (what is an AI agent) has 7 inner steps: it opens on why we need an AI Agent (chatbot vs agent on 1 WhatsApp order), then the robot with its 5 parts, then the 5 parts on 1 order.
| 1–9 | jump to slide 1–9 |
| P | print |

Each slide plays its own entrance when it opens (staggered text, count-ups, the house drawing itself, the sun crossing the demo day, the 15-minute break timer). Add `#static` to a slide's URL to see it with every animation finished.

## Mandarin version (中文版)

Open `index-zh.html` in Chrome, or press **L** in either deck to switch language on the same slide.

English is the single source (`build.py`). Every `python3 build.py` also writes the Chinese deck (`slides-zh/`, `index-zh.html`) through `i18n.py`, and prints how many texts and notes still have no Chinese:

```
zh: 75 slides, 0 texts missing, 0 notes missing
```

After an English edit, the new or changed text is listed in `i18n/zh-missing.json` (slide notes in `i18n/zh-notes-missing.json`). Add the Chinese to `i18n/zh.json` (`"English": "中文"`, or `"slide-key::English"` for 1 slide only) and `i18n/zh-notes.json`, rebuild until both counts are 0, then run `python3 make_thumbs.py` (it renders both `thumbs/` and `thumbs-zh/`). Translation style and the terms kept in English (Sales Order, Invoice, PO, SQL Account, WMS, MES, AI Agent, Token…) are in `i18n/work/BRIEF.md`.

## Edit

All slide text lives in `build.py` (one block per slide; `notes` = speaker notes). After an edit:

```bash
python3 build.py
```

This rewrites `slides/*.html` and `index.html`. If a slide's look changed, also run `python3 make_thumbs.py` so the overview pictures in `thumbs/` match (the overview shows pictures, not live slides, so it stays smooth). Shared look: `shared/deck.css`; shared behaviour: `shared/deck.js`; deck shell: `shell.html`.

## Blanks still to fill (shown in teal on the slides)

- Slide 1: [Date], [Venue]
- Slide 14: the QR code
- Slide 32: customer names under −90% and −80% (profile credits Twin Arrow and BHPetrol; BHPetrol's result is AI auto scheduling, not MES — to fix)
- Slide 66: Standard is highlighted as the recommended plan — change if you pick another
- Slide 68: [offer], [N] companies a month
- Slide 71: the 3 data-safety answers from the product team

Slide 61 (after the readiness score) asks 5 WMS and 5 MES questions; 3 or more yes on a side means that layer is needed from day 1. It is worksheet box 2B, so add those 10 questions to the printed worksheet.

## Live demo

Slides 34–58 follow `../Seminar demo prep.md`: a section page, then 7 parts (Setting up, Sales, Inventory, Purchase, Collection, Up Sales, Finance AI). Each part opens with an intro slide (the agent, its use cases, a 7-step progress bar), then 1 slide per use case. Web and mobile jobs show the SuDu AI app (Tasks module look); WhatsApp jobs show a phone chat. Edit them in `build.py` under `USECASES`.

## Files

- `index-zh.html`, `slides-zh/`, `thumbs-zh/` — the Mandarin deck, generated by `i18n.py` (do not edit by hand)
- `Hire Your First AI Agent.pdf` — every slide with animations finished, for sharing or printing (5 MB; slides are images, so text is not selectable)
- `brand-spec.md`, `direction-approved.md`, `polish-log.md` — huashu-design checkpoints
