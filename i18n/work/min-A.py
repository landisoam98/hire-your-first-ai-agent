# ================= batch A · slides 1-6 of "What is AI?" (minimal redesign) =================
AA_ARR = ic('<path d="M5 12h14M13 6l6 6-6 6"/>', 34, 2.2)

# ---------------- 1 · section opener ----------------
AA_STEPS = [('How AI grew up', 'from rules to agents'), ('The brain', 'what an LLM is'), ('The agent', 'a brain that does the work')]
slide('08-section-ai', 'Section: What is AI?', SEC[2], 'dark bare', 'data-sparks="none"', MIN_CSS + '''
.c { flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }
.big { font-size: 200px; font-weight: 750; letter-spacing: -.055em; line-height: .95; margin-top: 26px; }
.big em { font-style: normal; color: var(--neon); }
.c .ml { margin-top: 26px; }
.path { position:relative; display:grid; grid-template-columns: repeat(3, 420px); margin-top: 96px; }
.path .ln { position:absolute; left: 210px; right: 210px; top: 31px; height: 2px; background: rgba(0,245,169,.5); }
.path .st { position:relative; display:flex; flex-direction:column; align-items:center; }
.path i { font-style: normal; width: 64px; height: 64px; border-radius: 50%; display:grid; place-items:center; background: #03201C; border: 2px solid var(--neon); color: var(--neon); font-size: 28px; font-weight: 750; }
.path b { font-size: 38px; font-weight: 700; letter-spacing: -.015em; margin-top: 22px; }
.path span { font-size: 26px; color: var(--on-dark-2); margin-top: 6px; }
''', '''
<div class="c">
  <div class="mk u" style="--d:.1s">Part 1</div>
  <h1 class="big u" style="--d:.25s">What is <em>AI</em>?</h1>
  <p class="ml u" style="--d:.45s">In plain words. No jargon.</p>
  <div class="path">
    <div class="ln ug" style="--d:.9s"></div>
    ''' + ''.join('<div class="st u" style="--d:%.2fs"><i>%d</i><b>%s</b><span>%s</span></div>' % (.7 + k * .35, k + 1, t, s_) for k, (t, s_) in enumerate(AA_STEPS)) + '''
  </div>
</div>
''',
"\"So what is AI, really? Forget the headlines. We will go in 3 steps, in plain words.\n\nOne: how AI grew up, from hand-written rules to agents. Two: the brain, the thing people call an LLM, and how it learned. Three: the agent, a brain that can actually do the work.\"\n\nNext: \"First, how did we get here? 70 years in 1 slide.\"")

# ---------------- 2 · 70 years of AI ----------------
AA_HIST = [('1950s&ndash;80s', 'Rules', 'People wrote every rule by hand.'),
           ('2000s', 'Machine learning', 'It learns patterns from past examples.'),
           ('2012', 'Deep learning', 'It learns to see photos and hear voices.'),
           ('2018&ndash;20', 'LLM', 'It learns to write like a person.'),
           ('2025', 'AI agents', 'It uses tools and gets work done.')]
slide('08-ai-history', '70 years of AI', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.tl { flex:1; display:flex; flex-direction:column; justify-content:center; padding-bottom: 20px; }
.row { position:relative; display:grid; grid-template-columns: repeat(5, 1fr); gap: 28px; }
.row .ln { position:absolute; left: 0; right: 120px; top: 13px; height: 2px; background: var(--ink); opacity: .85; }
.row .ln.ug { animation-duration: 2.2s; }
.st { position:relative; }
.st i { display:block; width: 28px; height: 28px; border-radius: 50%; background: #FAFAF7; border: 3px solid var(--ink); }
.st small { display:block; font-family: var(--mono); font-size: 22px; font-weight: 700; color: var(--green); margin-top: 30px; }
.st b { display:block; white-space: nowrap; font-size: 37px; font-weight: 750; letter-spacing: -.02em; line-height: 1.1; margin-top: 10px; }
.st p { font-size: 27px; line-height: 1.38; color: var(--ink-2); margin-top: 12px; }
.st.now i { background: var(--green); border-color: var(--green); box-shadow: 0 0 0 8px rgba(0,108,72,.15); }
.st.now b { color: var(--green); }
.st em { display:inline-block; font-style: normal; font-size: 20px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: #fff; background: var(--green); padding: 6px 12px; border-radius: 6px; margin-top: 16px; }
''', '''
<div class="mk u" style="--d:.05s">How AI grew up</div>
<h1 class="mt u" style="--d:.15s">AI did not appear <em>overnight</em></h1>
<p class="ml u" style="--d:.3s">70 years, 5 big steps. Each one stands on the one before.</p>
<div class="tl"><div class="row">
  <div class="ln ug" style="--d:.5s"></div>
  ''' + ''.join('<div class="st u%s" style="--d:%.2fs"><i></i><small>%s</small><b>%s</b><p>%s</p>%s</div>' % (' now' if k == 4 else '', .6 + k * .4, y, t, d_, '<em>You are here</em>' if k == 4 else '') for k, (y, t, d_) in enumerate(AA_HIST)) + '''
</div></div>
''',
"\"Before we open up the brain, 1 minute of history, because ChatGPT did not come from nowhere. 70 years, 5 big steps.\n\nFrom the 1950s to the 80s: rules. People wrote every if-then rule by hand. If the customer is over the credit limit, block the order.\n\nIn the 2000s: machine learning. Instead of writing rules, you show the computer past examples and it finds the pattern. That gave us spam filters and credit scores.\n\n2012: deep learning. Much bigger networks that learn to see photos and hear voices. Through the 2010s that went into everyday apps: Siri, face unlock, 'you may also like'.\n\n2018 to 2020: the LLM. In 2017 a new design called the Transformer appeared, the T in ChatGPT. Trained on the internet, it learns to write like a person. GPT-3 came out in 2020. From 2023 it also reads photos, PDFs and voice notes.\n\nAnd 2025: AI agents. It uses tools and works step by step until the job is done. (point at the green dot) That is where we are today.\"\n\nNext: \"Step 2, machine learning, is still everywhere. Let me show you what it does.\"")

# ---------------- 3 · machine learning ----------------
AA_ML_FLOW = [('You give it', 'Past examples', '3 years of invoices'),
              ('It finds', 'The pattern', 'by itself, no rules typed in'),
              ('It predicts', '1 thing', '&ldquo;Kedai Ali: 80% chance<br>of paying late&rdquo;')]
AA_ML_USE = [('Who will pay late?', 'learned from past invoices'),
             ('How much will we sell?', 'learned from past sales'),
             ('What will run out?', 'learned from stock movements')]
slide('08-machine-learning', 'Machine learning', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.mid { flex:1; display:flex; flex-direction:column; justify-content:center; }
.fl { display:grid; grid-template-columns: 1fr 70px 1fr 70px 1.15fr; align-items:start; }
.cp { font-family: var(--mono); font-size: 19px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-3); margin-bottom: 18px; }
.fl > i { display:flex; justify-content:center; padding-top: 52px; color: var(--ink-3); }
.fl small { display:block; font-family: var(--mono); font-size: 19px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-3); }
.fl b { display:block; font-size: 46px; font-weight: 750; letter-spacing: -.02em; margin-top: 10px; }
.fl p { font-size: 28px; line-height: 1.35; color: var(--ink-2); margin-top: 8px; }
.fl .out small, .fl .out b { color: var(--green); }
.fl .out p { color: var(--ink); font-weight: 600; }
.m3 { margin-top: 0; margin-bottom: 26px; }
.m3 b { font-size: 34px; }
.nm { font-size: 22px; color: var(--ink-3); margin-bottom: 8px; }
.nm b { font-weight: 650; color: var(--ink-2); }
''', '''
<div class="mk u" style="--d:.05s">Step 2 &middot; Machine learning</div>
<h1 class="mt u" style="--d:.15s">It learns from your past and <em>predicts 1 thing</em></h1>
<p class="ml u" style="--d:.3s">No rules written by hand. Show it many past examples, and it finds the pattern.</p>
<div class="mid"><div class="fl">''' + ''.join(
    ('<i class="uf" style="--d:%.2fs">%s</i>' % (.5 + k * .35, AA_ARR) if k else '')
    + '<div class="u%s" style="--d:%.2fs"><small>%s</small><b>%s</b><p>%s</p></div>' % (' out' if k == 2 else '', .55 + k * .35, a, b_, c)
    for k, (a, b_, c) in enumerate(AA_ML_FLOW)) + '''</div></div>
<div class="cp uf" style="--d:1.6s">1 model answers 1 question</div>
<div class="m3">''' + ''.join('<div class="u" style="--d:%.2fs"><b>%s</b><p>%s</p></div>' % (1.7 + k * .2, t, p) for k, (t, p) in enumerate(AA_ML_USE)) + '''</div>
<p class="nm uf" style="--d:2.4s">Names you may hear: <b>random forest &middot; XGBoost &middot; LightGBM &middot; CNN</b></p>
''',
"\"Step 2 on that timeline, machine learning, is still everywhere, so let me show you what it does.\n\nNo rules written by hand. You give it past examples, for example 3 years of invoices. It finds the pattern by itself. And then it predicts 1 thing: Kedai Ali, 80 percent chance of paying late.\n\n(point at the 3 questions) That is the key: 1 model answers 1 question. Who will pay late, from past invoices. How much will we sell next month, from past sales. Which items will run out this week, from stock movements.\n\nYou may hear some names. Random forest: many small decision trees vote. XGBoost and LightGBM: trees that fix each other's mistakes, built for big tables. CNN: a network that looks at pictures, like reading a handwritten order. You don't need to remember them.\n\nThe difference with what comes next: machine learning answers 1 question, from numbers in a table. An LLM answers any question, in plain words.\"\n\nNote: the 80% is an illustration.\nNext: \"Then came the LLM.\"")

# ---------------- 4 · what is an LLM ----------------
slide('08-what-is-llm', 'What is an LLM?', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.ex { flex:1; display:flex; flex-direction:column; justify-content:center; }
.sn { display:flex; align-items:flex-start; gap: 22px; font-size: 76px; font-weight: 700; letter-spacing: -.03em; line-height: 1.1; }
.sn .bl { position:relative; display:inline-block; min-width: 330px; }
.sn .bl > span { color: var(--green); }
.sn .bl::after { content:""; position:absolute; left: 0; right: 0; top: 92px; height: 5px; border-radius: 3px; background: var(--green); }
.op { position:absolute; left: 0; top: 116px; display:grid; gap: 4px; font-size: 32px; font-weight: 600; letter-spacing: 0; }
.op span { color: var(--ink-3); opacity: .55; }
.op span:first-child { color: var(--green); opacity: 1; }
.ft { display:flex; justify-content:space-between; align-items:baseline; gap: 40px; margin-bottom: 8px; }
.ft b { font-size: 34px; font-weight: 700; }
.ft b em { font-style: normal; color: var(--green); }
.ft p { font-size: 22px; color: var(--ink-3); white-space: nowrap; }
.ft p span { font-weight: 650; color: var(--ink-2); }
''', '''
<div class="mk u" style="--d:.05s">Step 2 &middot; The brain</div>
<h1 class="mt u" style="--d:.15s">An LLM predicts the next word. <em>Very well.</em></h1>
<p class="ml u" style="--d:.3s"><b>LLM</b> = large language model. It learned which word usually comes next.</p>
<div class="ex">
  <div class="sn u" style="--d:.6s"><span>&ldquo;Terima kasih, see you</span><span class="bl"><span data-type="tomorrow&rdquo;" data-delay="1.7" data-cps="12"></span>
    <span class="op uf" style="--d:1.1s"><span>tomorrow</span><span>later</span><span>soon</span></span></span></div>
</div>
<div class="ft u" style="--d:2.4s"><b>It does not look answers up. <em>It predicts them, 1 word at a time.</em></b>
  <p>You know it as <span>ChatGPT &middot; Claude &middot; Gemini &middot; DeepSeek</span></p></div>
''',
"\"ChatGPT, Claude, Gemini, DeepSeek. You know the names. Inside each one is the same kind of thing: an LLM, a large language model. Large, because it read a huge amount of text. Language, because words go in and words come out.\n\nWhat does it actually do? Only 1 thing. Let's try. Terima kasih, see you...\" (pause, let the room finish) \"...tomorrow. You did it too. It looked at the words so far and picked the most likely next word. Then the next. Then the next. Done well enough, that looks like understanding.\n\nRemember this sentence: it does not look answers up. It predicts them, 1 word at a time. Everything else today follows from that.\"\n\nNext: \"To predict that well, it had to read. A lot.\"")

# ---------------- 5 · how much it read (scene kept from the original) ----------------
AA_TOWERS = '''<svg class="tw" viewBox="0 0 160 400" fill="none">
<g fill="#0E3A33" stroke="#00F5A9" stroke-width="2.5" stroke-linejoin="round">
<path d="M14 400V120l8-16v-20l6-10 6 10v20l8 16v280z"/><path d="M28 74V20"/>
<path d="M104 400V120l8-16v-20l6-10 6 10v20l8 16v280z"/><path d="M118 74V20"/>
<path d="M42 210h62v14H42z" fill="#00F5A9" fill-opacity=".25"/></g>
<g stroke="rgba(0,245,169,.35)" stroke-width="1.5">''' + ''.join('<path d="M18 %d h20M108 %d h20"/>' % (y, y) for y in range(140, 395, 18)) + '''</g></svg>'''
AA_FACTS = [('13,000', 'Twin Towers high, if you stacked the books', 4.2),
            ('800', 'football fields, if you laid the books flat', 6.6),
            ('50 trips', 'to the Moon, with the pages end to end', 8.8)]
slide('08-how-much-it-read', 'How much an AI has read', SEC[2], 'dark', 'data-sparks="none"', MIN_CSS + '''
.slide { padding-top: 112px; }
.wrap { flex:1; display:grid; grid-template-columns: 1fr 800px; gap: 50px; }
.lf { display:flex; flex-direction:column; }
.h2 { color: var(--on-dark-2); font-weight: 500; font-size: 36px; margin-top: 18px; }
.hero { font-size: 170px; font-weight: 800; letter-spacing: -.055em; line-height: .9; margin-top: 14px; white-space: nowrap; }
.hero small { display:block; font-size: 64px; font-weight: 700; letter-spacing: -.03em; color: var(--neon); margin-top: 6px; }
.bk { font-size: 34px; color: var(--on-dark-2); margin-top: 26px; }
.bk b { color: var(--on-dark); font-weight: 650; }
.facts { margin-top: auto; margin-bottom: 10px; display:grid; gap: 0; }
.fx { display:grid; grid-template-columns: 210px 1fr; align-items:baseline; gap: 20px; padding: 16px 0; border-top: 1px solid rgba(242,251,247,.16); }
.fx b { font-size: 42px; font-weight: 750; letter-spacing: -.02em; color: var(--neon); white-space: nowrap; }
.fx span { font-size: 26px; line-height: 1.3; color: var(--on-dark-2); }
/* the scene */
.sc { position:relative; height: 860px; margin-top: -60px; border-radius: 30px; overflow:hidden;
  background: linear-gradient(to top, rgba(0,245,169,.06), transparent 40%); }
.ground { position:absolute; left: 0; right: 0; bottom: 70px; height: 2px; background: rgba(242,251,247,.25); }
.zoom { position:absolute; left: 0; right: 0; bottom: 72px; top: 0; transform-origin: 20% 100%; }
@keyframes zoomout { to { transform: scale(.1); } }
.tw { position:absolute; left: 180px; bottom: 0; width: 160px; height: 400px; }
.stack { position:absolute; left: 400px; bottom: 0; width: 150px; height: 0;
  background: repeating-linear-gradient(to top, #FFB547 0 18px, #0E3A33 18px 20px, #00C389 20px 40px, #0E3A33 40px 42px, #7C5CFF 42px 60px, #0E3A33 60px 62px, #F2FBF7 62px 80px, #0E3A33 80px 82px, #FF8A5B 82px 100px, #0E3A33 100px 102px);
  border-radius: 4px; box-shadow: 0 0 40px rgba(0,245,169,.25);
  animation: pile 2.4s cubic-bezier(.3,.1,.3,1) .8s forwards, sky 2.6s cubic-bezier(.6,0,.2,1) 3.6s forwards; }
@keyframes pile { to { height: 400px; } }
@keyframes sky { from { height: 400px; } to { height: 8200px; } }
.cap1 { position:absolute; left: 400px; bottom: 490px; font-size: 26px; font-weight: 700; color: var(--on-dark); opacity: 0; animation: fade .5s ease 2.6s forwards, fadeout .4s ease 3.4s forwards; }
@keyframes fadeout { to { opacity: 0; } }
.cnt { position:absolute; right: 40px; top: 40px; text-align:right; opacity: 0; }
.cnt b { display:block; font-size: 120px; font-weight: 800; letter-spacing: -.04em; color: var(--neon); line-height: 1; }
.cnt > span { font-size: 30px; color: var(--on-dark); font-weight: 600; }
.tiny { position:absolute; left: 30%; bottom: 76px; transform: translateX(-50%); font-size: 22px; color: var(--on-dark-2); opacity: 0; white-space: nowrap; }
.ht { position:absolute; right: 40px; top: 230px; text-align:right; opacity: 0; animation: fade .6s ease 6.3s forwards, fadeout .5s ease 7.9s forwards; }
.ht b { display:block; font-size: 76px; font-weight: 800; letter-spacing: -.03em; color: var(--on-dark); line-height: 1; }
.ht span { font-size: 26px; color: var(--on-dark-2); }
.ht em { font-style: normal; color: var(--neon); font-weight: 700; }
.cnt { animation: fade .6s ease 3.8s forwards, fadeout .5s ease 7.9s forwards; }
.tiny { animation: fade .6s ease 5.6s forwards, fadeout .5s ease 7.9s forwards; }
.ground { animation: fadeout .5s ease 7.9s forwards; }
.zoom { animation: zoomout 2.6s cubic-bezier(.6,0,.2,1) 3.6s forwards, fadeout .5s ease 7.9s forwards; }
.space { position:absolute; inset: 0; opacity: 0; animation: fade .9s ease 8.1s forwards;
  background: radial-gradient(1.5px 1.5px at 12% 22%, #fff8, transparent), radial-gradient(1.5px 1.5px at 72% 12%, #fff8, transparent), radial-gradient(1px 1px at 40% 64%, #fff6, transparent), radial-gradient(1px 1px at 86% 70%, #fff6, transparent), radial-gradient(1.5px 1.5px at 58% 38%, #fff7, transparent), radial-gradient(1px 1px at 24% 84%, #fff6, transparent); }
.space svg { position:absolute; inset: 0; width: 100%; height: 100%; }
.space .tl { font: 600 24px var(--sans, Figtree); fill: var(--on-dark-2); }
.space .tb { font: 800 26px var(--sans, Figtree); fill: var(--on-dark); }
.mc { position:absolute; left: 40px; top: 36px; max-width: 560px; }
.mc b { display:block; font-size: 96px; font-weight: 800; letter-spacing: -.04em; color: var(--neon); line-height: 1; }
.mc > span { font-size: 28px; color: var(--on-dark); font-weight: 600; }
html.static .ht, html.static .cnt, html.static .tiny { display:none; }
html.static .zoom { transform: scale(.1); } html.static .stack { height: 8200px; } html.static .cap1 { display:none; }
''', '''
<div class="wrap">
  <div class="lf">
    <div class="mk u" style="--d:.05s">How much it read</div>
    <h2 class="h2 u" style="--d:.15s">DeepSeek V4 (2026) read more than</h2>
    <div class="hero u" style="--d:.3s"><span data-count="32" data-delay=".5" data-dur="1.6">0</span> trillion<small>tokens of text</small></div>
    <p class="bk u" style="--d:.7s">&asymp; <b>240 million books</b> of 400 pages</p>
    <div class="facts">''' + ''.join('<div class="fx u" style="--d:%.1fs"><b>%s</b><span>%s</span></div>' % (d_, n, t) for n, t, d_ in AA_FACTS) + '''</div>
  </div>
  <div class="sc">
    <div class="zoom">''' + AA_TOWERS + '''<div class="stack"></div></div>
    <div class="cap1">= 1 Twin Tower</div>
    <div class="ground"></div>
    <div class="tiny">the Twin Towers, 452 m</div>
    <div class="ht"><b>&asymp; 6,000 km</b><span>tall: <em>15x higher</em> than the space station</span></div>
    <div class="space"><svg viewBox="0 0 800 860">
      <defs><radialGradient id="ea" cx=".35" cy=".35"><stop offset="0" stop-color="#4DA3FF"/><stop offset=".6" stop-color="#0B6E5A"/><stop offset="1" stop-color="#05362D"/></radialGradient>
      <radialGradient id="mo" cx=".35" cy=".35"><stop offset="0" stop-color="#F2F4F3"/><stop offset="1" stop-color="#8A9A95"/></radialGradient></defs>
      <path id="tr" d="M190 660 C 330 420, 470 330, 640 250" fill="none" stroke="rgba(0,245,169,.35)" stroke-width="3" stroke-dasharray="6 10"/>
      <circle cx="150" cy="700" r="100" fill="url(#ea)"/><circle cx="150" cy="700" r="100" fill="none" stroke="rgba(77,163,255,.5)" stroke-width="10" stroke-opacity=".25"/>
      <circle cx="660" cy="240" r="44" fill="url(#mo)"/>
      <circle r="9" fill="#00F5A9"><animateMotion dur="1.4s" begin="8.6s" repeatCount="indefinite" keyPoints="0;1;0" keyTimes="0;.5;1" calcMode="linear"><mpath href="#tr"/></animateMotion></circle>
      <text class="tb" x="150" y="840" text-anchor="middle">Earth</text><text class="tb" x="660" y="320" text-anchor="middle">Moon</text>
      <text class="tl" x="440" y="520" text-anchor="middle" transform="rotate(-33 440 470)">384,400 km</text>
    </svg>
    <div class="mc"><b>&times;<span data-count="50" data-delay="8.6" data-dur="2.2">0</span></b><span>trips to the Moon, with the pages<br>laid end to end</span></div></div>
    <div class="cnt"><b>&times;<span data-count="13000" data-delay="3.8" data-dur="2.4">0</span></b><span>Twin Towers of books</span></div>
  </div>
</div>
''',
"\"How much does an LLM read? Take DeepSeek V4, from 2026. It was trained on more than 32 trillion tokens. A token is a small piece of text; more on that in 2 slides. As books of 400 pages, that is about 240 million books. 2 years earlier, Llama 3 read 15 trillion, about 110 million books, so it doubled in 2 years.\n\nWatch: if you stacked the books...\" (the pile reaches the top of the Twin Towers) \"...that is 1 Twin Tower. Keep going.\" (the view pulls back) \"13,000 Twin Towers. The pile is about 6,000 km tall, 15 times higher than the space station. Laid flat, the books would cover 800 football fields.\" (the view changes to Earth and Moon) \"And if you tore out every page and laid them end to end, they would reach the Moon 50 times over.\"\n\nNote: rough figures from the published token counts (DeepSeek-V4 paper: 32T+ tokens; Meta: Llama 3, 15T+). Working: 1 token = 0.75 word; a 400-page book = 100,000 words, 2.5 cm thick, 12 x 20 cm pages; a football field = 7,140 m2. Say \"about\". The stack itself does not reach the Moon; the pages laid end to end do.\nNext: \"So what exactly did it read?\"")

# ---------------- 6 · what it read, and never saw ----------------
AA_GLOBE = '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'
AA_BOOK = '<path d="M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2z"/><path d="M4 19V5"/>'
AA_NEWS = '<path d="M4 6h13v13H6a2 2 0 01-2-2z"/><path d="M17 9h3v8a2 2 0 01-2 2M8 10h5M8 14h5"/>'
AA_LANG = '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>'
AA_READ = [(AA_GLOBE, 'Public websites'), (AA_BOOK, 'Books'), (AA_NEWS, 'News and Wikipedia'),
           (AA_LANG, 'English, Malay, &#20013;&#25991;, &#2980;&#2990;&#3007;&#2996;&#3021; + 100 more')]
AA_NEVER = ['Your customers and their prices', 'Your stock and your accounts', 'Your WhatsApp chats', 'Your SOP: who approves what']
slide('08-what-it-read', 'What it read, and never saw', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.mid { flex:1; display:flex; flex-direction:column; justify-content:center; padding-bottom: 30px; }
.two { display:grid; grid-template-columns: 1fr 2px 1fr; gap: 80px; }
.two > .vl { background: var(--line); }
.cap { font-family: var(--mono); font-size: 20px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--green); }
.cap.no { color: #B87400; }
.two ul { list-style:none; display:grid; gap: 28px; margin-top: 26px; }
.two li { display:flex; align-items:center; gap: 20px; font-size: 32px; font-weight: 600; line-height: 1.25; }
.two li svg { flex:none; color: var(--green); }
.two .pv li svg { color: #E09A2D; }
.end { padding-top: 28px; border-top: 1px solid var(--line); margin-bottom: 8px; font-size: 34px; font-weight: 700; }
.end em { font-style: normal; color: var(--green); }
''', '''
<div class="mk u" style="--d:.05s">What it read</div>
<h1 class="mt u" style="--d:.15s">It read the world, <em>not your company</em></h1>
<p class="ml u" style="--d:.3s">Everything it knows came from public text. Your business was never in it.</p>
<div class="mid"><div class="two">
  <div><div class="cap u" style="--d:.5s">It read &middot; public</div>
    <ul>''' + ''.join('<li class="ux" style="--d:%.2fs">%s%s</li>' % (.65 + k * .18, ic(p, 34), t) for k, (p, t) in enumerate(AA_READ)) + '''</ul></div>
  <div class="vl uf" style="--d:1.2s"></div>
  <div class="pv"><div class="cap no u" style="--d:1.4s">It never saw &middot; private</div>
    <ul>''' + ''.join('<li class="ux" style="--d:%.2fs">%s%s</li>' % (1.55 + k * .18, ic(LOCK, 34), t) for k, t in enumerate(AA_NEVER)) + '''</ul></div>
</div></div>
<p class="end u" style="--d:2.6s">So you don&rsquo;t retrain it. <em>You let it look things up.</em></p>
''',
"\"So what exactly did it read? Public text. Billions of public websites, books from novels to accounting, news and Wikipedia. In many languages: English, Malay, Chinese, Tamil and 100 more. That is why it understands rojak: boss, 3 karton milo, hantar esok.\n\nNow the important part. (point at the right column) What did it never see? Your customers and their special prices. Your stock and your accounts in SQL Account. Your WhatsApp chats. Your SOP: who approves what, who always pays late. And nothing that happened after its training stopped.\n\nSo how do you make it useful for your company? Many people think you must retrain the brain with your data. You do not; that is slow and expensive. Instead, you let it look things up: each time it needs a fact about your company, it fetches it, then answers. Remember that, because that is exactly what an agent does.\"\n\nNext: \"One more thing about how it reads. It does not read whole words. It reads in small pieces.\"")
