# ---- batch B: slides 7-13 of "What is an AI Agent?" (minimal redesign) ----

# ---------------- 7 · tokens ----------------
AB_TOKS = ['Pls', ' arrange', ' delivery', ' be', '4', ' 12', 'pm', ',', ' b', 'wg', ' bes', 'ar', ' 10', 'kg', ' x', ' 20']
slide('08-tokens', 'It reads in tokens', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.msg { margin-top: 64px; font-size: 44px; font-weight: 600; letter-spacing: -.01em; color: var(--ink); }
.msg small { display:block; font-family: var(--mono); font-size: 18px; font-weight: 700; letter-spacing: .14em; color: var(--ink-3); margin-bottom: 12px; }
.tks { display:flex; flex-wrap: wrap; gap: 8px; margin-top: 36px; }
.tks span { font-family: var(--mono); font-size: 38px; font-weight: 600; padding: 10px 6px; border-radius: 10px; white-space: pre;
  opacity: 0; transform: translateY(12px); animation: mUp .5s cubic-bezier(.2,.7,.2,1) forwards; animation-delay: var(--d); }
.tks span:nth-child(odd) { background: var(--mint); color: var(--green); }
.tks span:nth-child(even) { background: #ECEFEC; color: var(--ink); }
.cnt { margin-top: 26px; font-size: 30px; color: var(--ink-2); }
.cnt b { font-size: 44px; font-weight: 800; color: var(--green); letter-spacing: -.02em; margin-right: 8px; }
.m3.two { grid-template-columns: 1fr 1fr; gap: 80px; }
html.static .tks span { opacity: 1; transform: none; animation: none; }
''', '''
<div class="mk u" style="--d:.05s">How it reads</div>
<h1 class="mt u" style="--d:.2s">It reads in small pieces called <em>tokens</em></h1>
<div class="msg u" style="--d:.45s"><small>YOUR MESSAGE</small>Pls arrange delivery be4 12pm, bwg besar 10kg x 20</div>
<div class="tks">''' + ''.join('<span style="--d:%.2fs">%s</span>' % (1.0 + k * .08, t) for k, t in enumerate(AB_TOKS)) + '''</div>
<p class="cnt uf" style="--d:2.3s"><b>%d tokens</b>for 9 words</p>
<div class="m3 two">
  <div class="u" style="--d:2.5s"><b>You pay per token</b><p>Every question and answer is counted, like a phone bill.</p></div>
  <div class="u" style="--d:2.7s"><b>It can only hold so much</b><p>In a very long chat, the early details start to slip.</p></div>
</div>
''' % len(AB_TOKS),
"\"One more thing about how it reads. It does not read words. It cuts your message into small pieces, called tokens.\n\nWatch.\" (let the pieces appear) \"Pls arrange delivery be4 12pm, bwg besar 10 kg times 20. 9 words, about 16 tokens. Common English words are 1 piece. Short forms like be4, and Malay words like bwg, get cut into smaller pieces.\n\nWhy should you care? 2 reasons. First: you pay per token. Every question and every answer is counted, like a phone bill. So a long PDF costs more than a short chat. Roughly, 100 English words is about 130 tokens; Malay and Chinese use a bit more.\n\nSecond: it can only hold so much at once. AI people call this the context window: think of it as the size of its desk. Today that is about 100 thousand to 1 million tokens, a 300-page book or more. But in a very long chat, the early details start to slip. That is why a good AI system does not rely on a long chat: it looks up the fact it needs, fresh, each time.\"\n\nNote: token counts are an illustration; each model's tokenizer differs.\nNext: \"And how does it know what those pieces mean?\"")

# ---------------- 8 · meaning map ----------------
AB_MAP = [  # label, centre, words (dx, dy), highlighted?
    ('Onions', (240, 205), [('bawang', -95, -20), ('bwg', -75, 40), ('onion', 30, -60), ('&#27915;&#33905;', 45, 30)], True),
    ('Drinks', (730, 175), [('Milo', -70, -20), ('Horlicks', 20, -55), ('teh tarik', 30, 25), ('Nescafe', -85, 55)], False),
    ('Money', (250, 485), [('invoice', -95, -25), ('bil', 50, -45), ('bayar', -50, 50), ('payment', 40, 25)], False),
    ('When', (740, 475), [('esok', -80, -25), ('tomorrow', 15, -50), ('pagi', -70, 50), ('be4 12pm', 20, 30)], False),
]
def AB_map_svg():
    out = ''
    for g, (lab, (cx, cy), words, hi) in enumerate(AB_MAP):
        d0 = (.7 if hi else 1.5 + (g - 1) * .3)
        out += '<g class="uf %s" style="--d:%.2fs"><circle class="zone" cx="%d" cy="%d" r="122"/><text class="gl" x="%d" y="%d">%s</text>' % (
            'hi' if hi else 'lo', d0, cx, cy, cx, cy - 138, lab.upper())
        for k, (w, dx, dy) in enumerate(words):
            out += ('<g class="uf" style="--d:%.2fs"><circle class="dot" cx="%d" cy="%d" r="8"/><text class="wd" x="%d" y="%d">%s</text></g>'
                    % (d0 + .15 + k * .12, cx + dx, cy + dy, cx + dx + 16, cy + dy + 10, w))
        out += '</g>'
    return out
slide('08-meaning-map', 'It stores meaning as a map', SEC[2], 'dark', 'data-sparks="none"', MIN_CSS + '''
.wrap { flex:1; display:grid; grid-template-columns: 900px 1fr; gap: 70px; align-items:center; margin-top: 10px; margin-bottom: 20px; }
.mp svg { width: 900px; height: 558px; display:block; overflow: visible; }
.mp text { font-family: var(--sans); }
.mp .wd { font-size: 30px; font-weight: 600; }
.mp .gl { font-family: var(--mono); font-size: 18px; font-weight: 700; letter-spacing: .14em; text-anchor: middle; }
.mp .zone { stroke-dasharray: 4 9; stroke-width: 1.5; }
.mp .hi .zone { fill: rgba(0,245,169,.08); stroke: rgba(0,245,169,.6); }
.mp .hi .dot { fill: var(--neon); } .mp .hi .wd { fill: var(--on-dark); } .mp .hi .gl { fill: var(--neon); }
.mp .lo .zone { fill: rgba(242,251,247,.025); stroke: rgba(242,251,247,.18); }
.mp .lo .dot { fill: var(--on-dark-3); } .mp .lo .wd { fill: var(--on-dark-2); } .mp .lo .gl { fill: var(--on-dark-3); }
.pts { display:grid; gap: 48px; }
.pts div { border-top: 3px solid var(--neon); padding-top: 20px; }
.pts b { display:block; font-size: 40px; font-weight: 750; letter-spacing: -.02em; color: var(--on-dark); }
.pts p { font-size: 28px; line-height: 1.4; color: var(--on-dark-2); margin-top: 8px; }
''', '''
<div class="mk u" style="--d:.05s">How it understands</div>
<h1 class="mt u" style="--d:.2s">It stores meaning as a <em>map</em></h1>
<p class="ml u" style="--d:.4s">Words used the same way sit close together.</p>
<div class="wrap">
  <div class="mp"><svg viewBox="0 0 1000 620">''' + AB_map_svg() + '''</svg></div>
  <div class="pts">
    <div class="u" style="--d:2.4s"><b>Any language</b><p>bawang, onion and &#27915;&#33905; sit in the same spot.</p></div>
    <div class="u" style="--d:2.6s"><b>Short forms too</b><p>bwg lands right next to bawang.</p></div>
  </div>
</div>
''',
"\"So how does it understand bwg besar? Here is the idea. While it reads, every piece gets a place on a giant map of meaning. Words that are used in the same way end up close together.\n\nLook at the onions.\" (point) \"Bawang, onion, and the Chinese word for onion all sit in the same spot, because people use them the same way. And bwg, the short form, lands right next to bawang. That is how it reads rojak, BM, English and Chinese mixed together.\n\nThe same happens everywhere: Milo next to Horlicks and teh tarik. Invoice next to bil and bayar. Esok next to tomorrow.\n\nThis picture is a sketch. The real map does not have 2 directions; it has thousands. But the idea is the same: close on the map means similar in meaning.\"\n\nNote: the map is a simplified sketch of what AI people call embeddings.\nNext: \"So how did it build that map? It trained.\"")

# ---------------- 9 · how it learned ----------------
AB_LOOP = [('Guess', 'the next word'), ('Check', 'the real word'), ('Adjust', 'turn the dials a little'), ('Repeat', 'with the next sentence')]
def AB_loop_svg():
    xs = [190, 610, 1030, 1450]
    out = ('<path class="dr" pathLength="1" style="--d:1.8s" d="M1450 70 C1450 -4, 190 -4, 190 70"/>'
           '<path class="dr" pathLength="1" style="--d:2.4s" d="M178 58 L190 72 L202 58"/>'
           '<g class="uf" style="--d:2.2s"><rect x="680" y="0" width="300" height="40" rx="20" class="pill"/>'
           '<text class="arc" x="830" y="28">trillions of times</text></g>')
    for k, (h, s) in enumerate(AB_LOOP):
        x, d = xs[k], .6 + k * .3
        out += ('<g class="uf" style="--d:%.2fs"><circle class="nd%s" cx="%d" cy="130" r="54"/><text class="num%s" x="%d" y="143">%d</text>'
                '<text class="lb" x="%d" y="240">%s</text><text class="sb" x="%d" y="280">%s</text></g>'
                % (d, ' last' if k == 3 else '', x, ' last' if k == 3 else '', x, k + 1, x, h, x, s))
        if k < 3:
            out += ('<path class="dr" pathLength="1" style="--d:%.2fs" d="M%d 130 H%d M%d 120 L%d 130 L%d 140"/>'
                    % (d + .2, x + 72, x + 348, x + 338, x + 348, x + 338))
    return out
slide('08-how-it-learned', 'How it learned', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.lp { margin-top: 44px; }
.lp svg { width: 1664px; height: 300px; display:block; overflow: visible; }
.lp text { font-family: var(--sans); text-anchor: middle; }
.lp .nd { fill: #fff; stroke: var(--green); stroke-width: 3; }
.lp .nd.last { fill: var(--green); }
.lp .num { font-size: 38px; font-weight: 800; fill: var(--green); } .lp .num.last { fill: #fff; }
.lp .lb { font-size: 38px; font-weight: 750; fill: var(--ink); letter-spacing: -.01em; }
.lp .sb { font-size: 26px; fill: var(--ink-2); }
.lp .dr { fill: none; stroke: var(--emerald); stroke-width: 3; stroke-linecap: round; stroke-linejoin: round;
  stroke-dasharray: 1; stroke-dashoffset: 1; animation: abDraw 1s cubic-bezier(.65,0,.25,1) forwards; animation-delay: var(--d); }
.lp .pill { fill: var(--mint); }
.lp .arc { font-family: var(--mono); font-size: 20px; font-weight: 700; letter-spacing: .08em; fill: var(--green); }
@keyframes abDraw { to { stroke-dashoffset: 0; } }
html.static .lp .dr { stroke-dashoffset: 0; animation: none; }
.m3 b span { font-family: var(--mono); font-size: 22px; color: var(--green); margin-right: 12px; }
''', '''
<div class="mk u" style="--d:.05s">How it learned</div>
<h1 class="mt u" style="--d:.2s">It learned by guessing, <em>trillions of times</em></h1>
<p class="ml u" style="--d:.4s">Inside are billions of tiny dials. Each guess turns them a little.</p>
<div class="lp"><svg viewBox="0 0 1664 300">''' + AB_loop_svg() + '''</svg></div>
<div class="m3">
  <div class="u" style="--d:2.5s"><b><span>1</span>Guess and check</b><p>Months of work on 10,000s of chips.</p></div>
  <div class="u" style="--d:2.65s"><b><span>2</span>Coached by people</b><p>Learns to follow instructions politely.</p></div>
  <div class="u" style="--d:2.8s"><b><span>3</span>Frozen</b><p>Knows nothing after its cut-off date.</p></div>
</div>
''',
"\"So how did it learn? Inside the brain are billions of numbers. Think of them as tiny volume dials. Learning simply means turning those dials, a little at a time, until its guesses come out right.\n\nHere is the loop.\" (follow the steps) \"1: take a sentence, hide the next word, and guess it. 2: check the real word. 3: adjust; turn the dials a tiny bit toward the right answer. 4: repeat with the next sentence. Trillions of times. That takes months, tens of thousands of computer chips, and for the biggest models, over 100 million US dollars.\n\nAfter that loop, 2 more stages. It gets coached by people: people wrote example answers and rated its answers, better or worse, so it learned to follow instructions and to be helpful and polite. Like a graduate on probation.\n\nThen it is frozen. The dials are locked. Its knowledge stops at a cut-off date, and it does not learn from your chat as you talk.\"\n\nNote: costs and chip counts are rough public estimates for the largest models; say \"about\".\nNext: \"So when you ask it something, how does it write the answer?\"")

# ---------------- 10 · next word ----------------
AB_PROBS = [('breakfast', 82), ('lunch', 9), ('dinner', 6), ('supper', 3)]
slide('09-next-word', 'How it writes an answer', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.top { display:grid; grid-template-columns: 820px 1fr; gap: 80px; align-items:center; margin-top: 56px; }
.sent { font-size: 60px; font-weight: 650; letter-spacing: -.025em; line-height: 1.2; }
.blank { display:inline-block; min-width: 250px; border-bottom: 5px solid var(--ink); color: var(--green); }
.pb { display:grid; gap: 18px; }
.pb div { display:grid; grid-template-columns: 180px 1fr 80px; align-items:center; gap: 20px; font-size: 32px; }
.pb div:first-child { font-weight: 750; }
.pb i { display:block; height: 20px; border-radius: 10px; background: #ECEFEC; overflow:hidden; }
.pb i b { display:block; height: 100%; width: var(--w); background: var(--emerald); border-radius: 10px; }
.pb div:first-child i b { background: var(--green); }
.pb em { font-style: normal; font-weight: 700; text-align:right; color: var(--ink-2); }
.pb div:first-child em { color: var(--green); }
.m3 > div { border-color: #FFB547; }
.m3 .lim { font-family: var(--mono); font-size: 18px; font-weight: 700; letter-spacing: .14em; color: #B4451F; margin-bottom: 6px; display:block; }
''', '''
<div class="mk u" style="--d:.05s">How it writes</div>
<h1 class="mt u" style="--d:.2s">It writes <em>1 word at a time</em></h1>
<p class="ml u" style="--d:.4s">Every time, it picks the most likely next word.</p>
<div class="top">
  <div class="sent u" style="--d:.6s">&ldquo;Nasi lemak is usually eaten for <span class="blank"><span data-type="breakfast" data-delay="2.1" data-cps="14"></span></span>&rdquo;</div>
  <div class="pb">''' + ''.join('<div class="ux" style="--d:%.2fs"><span>%s</span><i><b class="ug" style="--w:%d%%;--d:%.2fs"></b></i><em>%d%%</em></div>' % (.9 + k * .15, w, p, 1.0 + k * .15, p) for k, (w, p) in enumerate(AB_PROBS)) + '''</div>
</div>
<div class="m3">
  <div class="u" style="--d:2.6s"><span class="lim">LIMIT 1</span><b>Stopped learning on a date</b><p>It knows nothing newer.</p></div>
  <div class="u" style="--d:2.75s"><span class="lim">LIMIT 2</span><b>Never saw your company</b><p>Not your prices, stock or chats.</p></div>
  <div class="u" style="--d:2.9s"><span class="lim">LIMIT 3</span><b>Sounds sure when wrong</b><p>It picks likely words, not checked facts.</p></div>
</div>
''',
"\"So you ask it a question. How does it write the answer? It plays the same game it trained on. Nasi lemak is usually eaten for...\" (let the room shout) \"...breakfast. It scores every possible next word: breakfast 82 percent, lunch 9, dinner 6. It picks the most likely one, writes it, and then does the same for the next word, and the next. 1 word at a time, dozens of words a second. Sometimes it picks the second choice so it sounds natural; that is why you get a slightly different answer each time.\n\nAnd now its 3 limits make sense. 1: it stopped learning on a certain date, so it knows nothing newer. 2: it has never seen your company: not your prices, your stock or your chats. 3: because it picks the most likely words, not checked facts, it can sound completely sure when it is wrong.\"\n\nNote: the percentages are an illustration.\nNext: \"So how do you tell 1 AI brain from another? 7 things to check.\"")

# ---------------- 11 · compare LLMs ----------------
AB_SPECS = [('How smart', 'Test it on your own real work.'),
            ('How much it reads at once', '1 million tokens is about 7 books.'),
            ('Cost', 'You pay per token, in and out.'),
            ('Speed', 'How fast the words come out.'),
            ('Thinks step by step', 'Slower, but better on hard jobs.'),
            ('Size', 'How many dials inside: billions to trillions.'),
            ('How it is built', 'Everyone works, or only experts: next slide.')]
slide('09-compare-llms', '7 things to compare', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.sp { display:grid; grid-template-columns: 1fr 1fr; grid-template-rows: repeat(4, auto); grid-auto-flow: column; gap: 0 90px; margin-top: 50px; }
.sp div { display:grid; grid-template-columns: 64px 1fr; align-items: baseline; padding: 20px 0 22px; border-top: 1px solid rgba(2,34,31,.14); }
.sp i { font-style: normal; font-family: var(--mono); font-size: 24px; font-weight: 700; color: var(--green); }
.sp b { font-size: 36px; font-weight: 750; letter-spacing: -.015em; }
.sp p { grid-column: 2; font-size: 27px; color: var(--ink-2); margin-top: 4px; }
.sp div:last-child b { color: var(--green); }
''', '''
<div class="mk u" style="--d:.05s">Choosing a brain</div>
<h1 class="mt u" style="--d:.2s">Not all AI brains are <em>equal</em></h1>
<p class="ml u" style="--d:.4s">ChatGPT, Claude, Gemini, DeepSeek: compare them on 7 things.</p>
<div class="sp">''' + ''.join('<div class="u" style="--d:%.2fs"><i>%d</i><b>%s</b><p>%s</p></div>' % (.7 + k * .2, k + 1, t, p) for k, (t, p) in enumerate(AB_SPECS)) + '''</div>
''',
"\"ChatGPT, Claude, Gemini, DeepSeek, Llama. They are not all the same. When you pick one, compare 7 things.\n\n1, how smart it is at your kind of work: writing, maths, reading documents. Do not only trust the rankings; test it on 10 of your own real orders. 2, how much it can read at once. DeepSeek V4 reads 1 million tokens, about 7 books. 3, cost: you pay per token, for what goes in and what comes out, so long PDFs and long chats cost more. 4, speed: how fast the words come out. Fast matters for chat; for an overnight report, slower is fine. 5, whether it thinks step by step before answering. Slower and costs more, but better on hard jobs. 6, size: the number of dials inside. Llama 3 comes in 8 billion or 70 billion; DeepSeek V4 Pro has 1.6 trillion. 7, how it is built. That one deserves its own slide.\"\n\nNote: model figures from Meta (Llama 3) and the DeepSeek-V4 paper (2026). Prices change often, so no prices are on the slide.\nNext: \"So how is the brain built? Think of an office.\"")

# ---------------- 12 · dense vs mixture of experts ----------------
AB_PERSON = '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="7.5" r="4.2"/><path d="M3.5 22c0-4.8 3.8-8.4 8.5-8.4s8.5 3.6 8.5 8.4z"/></svg>'
AB_MAIL = ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>', 64, 1.8)
AB_ARROW = ic('<path d="M5 12h14M13 6l6 6-6 6"/>', 40, 2.2)
def AB_staff(lit, d0, step):
    out = ''
    for k in range(16):
        on = (k in lit) if lit is not None else True
        d = (d0 + k * step) if lit is None else d0
        out += '<span class="p%s" style="--d:%.2fs">%s</span>' % (' on' if on else '', d, AB_PERSON)
    return '<div class="staff">%s</div>' % out
slide('09-dense-moe', '2 ways to build the brain', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.two { display:grid; grid-template-columns: 1fr 1fr; gap: 0; margin-top: 50px; }
.two > div:first-child { padding-right: 70px; border-right: 1px solid rgba(2,34,31,.14); }
.two > div:last-child { padding-left: 70px; }
.cap { font-family: var(--mono); font-size: 20px; font-weight: 700; letter-spacing: .14em; color: var(--ink-3); }
.vz { display:flex; align-items:center; gap: 22px; height: 250px; margin-top: 14px; }
.vz > .ml0 { color: var(--ink); display:flex; }
.vz > .ar { color: var(--ink-3); display:flex; }
.rc { display:flex; flex-direction:column; align-items:center; gap: 6px; }
.rc .p { width: 60px; height: 60px; }
.rc small { font-size: 18px; font-weight: 700; color: var(--green); }
.staff { display:grid; grid-template-columns: repeat(4, 50px); gap: 14px 16px; }
.p { display:block; width: 50px; height: 50px; color: #D3DAD6; }
.p svg { width: 100%; height: 100%; display:block; }
.p.on { animation: abLit .6s ease forwards; animation-delay: var(--d); }
@keyframes abLit { to { color: var(--green); } }
html.static .p.on { color: var(--green); animation: none; }
.two b { display:block; font-size: 40px; font-weight: 750; letter-spacing: -.02em; line-height: 1.15; margin-top: 10px; }
.two p { font-size: 28px; color: var(--ink-2); margin-top: 10px; }
.two p strong { color: var(--green); }
.mnote { margin-top: auto; margin-bottom: 64px; }
''', '''
<div class="mk u" style="--d:.05s">How the brain is built</div>
<h1 class="mt u" style="--d:.2s">2 ways to build the brain</h1>
<p class="ml u" style="--d:.4s">Think of an office that gets 1 email.</p>
<div class="two">
  <div class="u" style="--d:.6s"><span class="cap">DENSE</span>
    <div class="vz"><span class="ml0">''' + AB_MAIL + '''</span><span class="ar">''' + AB_ARROW + '''</span>''' + AB_staff(None, 1.1, .05) + '''</div>
    <b>Everyone reads every email</b><p>All 16 people work on it. Slow and costly.</p></div>
  <div class="u" style="--d:.8s"><span class="cap">MIXTURE OF EXPERTS</span>
    <div class="vz"><span class="ml0">''' + AB_MAIL + '''</span><span class="ar">''' + AB_ARROW + '''</span><span class="rc"><span class="p on" style="--d:2.1s">''' + AB_PERSON + '''</span><small>receptionist</small></span><span class="ar">''' + AB_ARROW + '''</span>''' + AB_staff({5, 10}, 2.5, 0) + '''</div>
    <b>The receptionist picks 2 experts</b><p>Only 2 people work on it. <strong>Cheaper and faster.</strong></p></div>
</div>
<p class="mnote uf" style="--d:2.9s">Real example: DeepSeek V4 has 1.6T dials in total, but only 49B work on each word.</p>
''',
"\"The last thing on the list: how the brain is built. There are 2 ways, and the easiest way to see them is an office.\n\nImagine your office gets 1 email.\n\nThe first way is called dense. Everyone reads every email. All 16 people stop and work on it.\" (point at the people lighting up) \"It works, but it is slow and costly, and the bigger the office, the more every email costs.\n\nThe second way is called mixture of experts. A receptionist reads the email first and sends it only to the 2 people who know the topic. Everyone else keeps working on other things. So you can have a very big office, but each email is cheap and fast.\n\nA real example: DeepSeek V4 has 1.6 trillion dials in total, but only 49 billion of them work on each word. That is why many of the newest models are built this way.\"\n\nNote: figures from Meta (Llama 3) and the DeepSeek-V4 paper (June 2026). Llama 3 70B is dense: all 70B dials work on every word.\nNext: \"Whatever way it is built, every AI brain shares 1 big weakness.\"")

# ---------------- 13 · why it makes things up ----------------
slide('09-makes-things-up', 'Why it makes things up', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.ch { display:grid; grid-template-columns: 1fr 1fr; gap: 90px; margin-top: 44px; }
.ch > div { display:flex; flex-direction:column; gap: 16px; }
.cap { font-family: var(--mono); font-size: 20px; font-weight: 700; letter-spacing: .14em; color: var(--ink-3); }
.ch > div:last-child .cap { color: var(--green); }
.q { align-self:flex-end; font-size: 29px; padding: 12px 22px; border-radius: 22px 22px 6px 22px; background: var(--ink); color: var(--on-dark); }
.an { align-self:flex-start; font-size: 30px; padding: 14px 24px; border-radius: 6px 22px 22px 22px; background: #fff; box-shadow: 0 0 0 1px var(--line), 0 18px 30px -26px rgba(2,34,31,.45); }
.an b { font-weight: 800; }
.lk { align-self:flex-start; display:flex; align-items:center; gap: 10px; font-family: var(--mono); font-size: 19px; font-weight: 700; color: var(--green); }
.vd { display:flex; align-items:center; gap: 10px; font-size: 26px; font-weight: 700; }
.bad .vd { color: #B4451F; } .bad .an b { color: #B4451F; }
.good .vd { color: var(--green); } .good .an b { color: var(--green); }
.m3 b { font-size: 34px; } .m3 p { font-size: 26px; }
''', '''
<div class="mk u" style="--d:.05s">Its biggest weakness</div>
<h1 class="mt u" style="--d:.2s">It sounds sure, even when it is <em>wrong</em></h1>
<p class="ml u" style="--d:.4s">With no facts, it guesses. AI people call this <b>hallucination</b>.</p>
<div class="ch">
  <div class="bad"><span class="cap uf" style="--d:.6s">BRAIN ONLY</span>
    <div class="q u" style="--d:.8s">What is Kedai Ali&rsquo;s credit limit?</div>
    <div class="an u" style="--d:1.3s">Kedai Ali&rsquo;s credit limit is <b>RM10,000</b>.</div>
    <div class="vd uf" style="--d:1.8s">''' + ic('<path d="M12 3l9.5 17h-19z"/><path d="M12 10v4M12 17h.01"/>', 28) + '''Made up. It never saw Kedai Ali.</div></div>
  <div class="good"><span class="cap uf" style="--d:.7s">BRAIN + YOUR RECORDS</span>
    <div class="q u" style="--d:1s">What is Kedai Ali&rsquo;s credit limit?</div>
    <div class="lk uf" style="--d:1.5s">''' + ic('<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>', 22, 2.6) + '''Looked up: customer record</div>
    <div class="an u" style="--d:1.9s"><b>RM5,000.</b> Only RM180 is left.</div>
    <div class="vd uf" style="--d:2.3s">''' + ic(CHECK, 28, 2.6) + '''Correct, and you can see where from.</div></div>
</div>
<div class="m3">
  <div class="u" style="--d:2.5s"><b>Give it facts</b><p>Let it look up your records.</p></div>
  <div class="u" style="--d:2.65s"><b>Ask for the source</b><p>&ldquo;Where is this number from?&rdquo;</p></div>
  <div class="u" style="--d:2.8s"><b>A person checks</b><p>Anything that moves money or stock.</p></div>
</div>
''',
"\"Now you can understand its biggest weakness. Remember: it always picks the most likely next word. It is built to always give an answer. So when it has no facts, it does not stop. It guesses, with words that sound right. AI people call this hallucination.\n\nWatch. Ask a brain with no facts: what is Kedai Ali's credit limit? It answers, very confidently: RM10,000. Completely made up. It has never seen Kedai Ali.\n\nNow the same question, but it is allowed to look up the customer record first. RM5,000. They have already used RM4,820, so only RM180 is left. Correct, and you can see where the number came from.\n\nSo 3 rules for using AI in a business. 1: give it facts; let it look up your records instead of trusting what it remembers. 2: ask for the source; a good answer can show you where the number came from. 3: a person checks anything that moves money or stock.\"\n\nNext: \"A brain alone can only talk, and it guesses. So people added 6 things to the brain to make it work. That is the AI Agent.\"")
