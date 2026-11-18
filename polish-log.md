# Polish log

Every slide rendered at 1920×1080 after its animations finish, checked as contact sheets.

## Round 1 — worst three
1. Break (21) and closing (33): the agent avatar was invisible. Two animations on one element (`pop` + `float`) overrode each other. Fixed by wrapping the image.
2. Demo day (19): labels sat on the sun arc and crossed it; the sun covered "5:45 pm". Rebuilt as dots on the arc with plumb lines down to one shared label row.
3. AI team (18): names wrapped ("Collection / AI"). Cards made wider, then vertical.

Also: sparkles moved off titles (5, 6, 7, 11, 19, 25); worksheet tab no longer wraps (25); slide 16 sync screen enlarged and columns sized to content; slide 24 house icons enlarged; slide 30 timeline centred and line ends at the last dot; slide 7 formula and result enlarged.

## Round 2 — worst three
1. Poll slide (5): the shimmering tracks read like full bars (fake data). Made them faint so they read as empty, and spread options down the card.
2. Typed three times (6): flow block sat high with a dead lower half. Taller nodes, block centred.
3. Lint: `--ink-3` grey on small labels was 4.3:1. Darkened to #4F635C; cover kicker raised to 26px.

## Lint (design_lint.py, deck floors 24px body / 16px labels)
No red flags. Remaining yellow: the "[Date] · [Venue] · 2:00 to 5:00 pm" line is syllabus content; relative image paths are intended (multi-file deck).
