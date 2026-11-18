# ==================== batch C · slides 14-19 of "What is an AI Agent?" (minimal redesign) ====================
AC_WRENCH = '<path d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 005.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>'
AC_LOOK = '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>'
AC_CAB = '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 9h16M4 15h16M10 6h4M10 12h4M10 18h4"/>'
AC_LOOPI = '<path d="M20 12a8 8 0 11-2.3-5.7"/><path d="M20 4v4h-4"/>'
AC_BOOK = '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/>'
AC_SHIELD = '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>'
AC_ARROW = '<path d="M4 12h16M14 6l6 6-6 6"/>'
AC_X = '<path d="M6 6l12 12M18 6L6 18"/>'
AC_CHAT = '<path d="M4 5h16v11H9l-5 4z"/>'

# ---------------- 14 · why agents ----------------
AC_SIX = [(AC_WRENCH, 'Tools', 'to click, send and save'),
          (AC_LOOK, 'Look-up', 'fresh facts, every time'),
          (AC_CAB, 'Memory', 'notes kept outside the brain'),
          (AC_LOOPI, 'A loop', 'try, check, try again'),
          (AC_BOOK, 'Rules', 'your SOP, written down'),
          (AC_SHIELD, 'Permission', 'a person approves')]

slide('19-why-agents', 'Why AI agents were invented', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.six { display:grid; grid-template-columns: repeat(6, 1fr); gap: 36px; margin-top: 74px; position:relative; padding-top: 34px; }
.six::before { content:""; position:absolute; left:0; right:0; top:0; height: 3px; background: var(--ink); transform-origin:left; transform: scaleX(0); animation: mGrow 1.6s cubic-bezier(.65,0,.25,1) .7s forwards; }
html.static .six::before { transform:none; animation:none; }
.six i { display:grid; place-items:center; width: 64px; height: 64px; border-radius: 50%; background: var(--mint); color: var(--green); }
.six b { display:block; font-size: 36px; font-weight: 750; letter-spacing: -.02em; margin-top: 22px; }
.six p { font-size: 26px; line-height: 1.35; color: var(--ink-2); margin-top: 8px; }
.eq { margin-top: auto; margin-bottom: 100px; display:flex; align-items:baseline; gap: 30px; font-size: 54px; font-weight: 750; letter-spacing: -.03em; }
.eq span { color: var(--ink-3); font-weight: 500; }
.eq em { font-style: normal; color: var(--green); }
''', '''
<div class="mk u" style="--d:.05s">From chatbot to agent</div>
<h1 class="mt u" style="--d:.2s">An LLM only talks. 6 things make it <em>work</em>.</h1>
<p class="ml u" style="--d:.4s">People added these 6 things around the brain, 1 gap at a time.</p>
<div class="six">''' + ''.join('<div class="u" style="--d:%.2fs"><i>%s</i><b>%s</b><p>%s</p></div>' % (.9 + k * .2, ic(p, 32, 2), t, s_) for k, (p, t, s_) in enumerate(AC_SIX)) + '''</div>
<div class="eq u" style="--d:2.3s">LLM <span>+</span> 6 things <span>=</span> <em>an AI Agent</em></div>
''',
"\"So here is the honest picture. An LLM on its own is a brilliant talker. It can only talk. So people added 6 things around it, 1 gap at a time.\n\n[Point along the row] 1: tools, hands to click, send and save in real systems. 2: look-up, because its knowledge stops at a cut-off date, so it fetches fresh facts every time. 3: memory, because it forgets after every chat, so notes are kept outside the brain. 4: a loop, so it does not answer in 1 shot; it tries, checks, and tries again until done. 5: rules, your SOP written down, because it does not know how your company works. 6: permission, limits plus a person who approves, so nothing stops it doing the wrong thing.\n\nThe history is short. 2022: ChatGPT, it talks. 2023: tools, it can call a system. 2025: agents, it works in a loop until the job is done.\n\nLLM plus these 6 things: that is an AI Agent. Not a smarter brain. The same brain, with hands, memory, a loop and limits.\"\n\nNote: 2022 = ChatGPT launch; 2023 = tool calling; 2025 = agents like Claude Code and Codex working on their own.\nNext: \"So let me show you what an AI Agent looks like.\"")

# ---------------- 15 · what is an AI agent (robot + 6 in-slide steps) ----------------
AC_PARTS = [  # (name, short label on robot, tag, 1 plain sentence, 1 example)
    ('Brain', 'thinks', '', 'It understands the message and plans the next step.',
     '&ldquo;bwg besar 10kg x ---&rdquo; &rarr; big onions, 10 kg bags. Quantity missing, so it asks.'),
    ('Tools', 'does the work', 'NO TOOLS, NO WORK', 'Each tool is 1 action in a real system. The brain cannot click; tools can.',
     'Check stock &rarr; 42 bags. Create order &rarr; draft ready.'),
    ('Memory', 'knows your data', '', 'The brain forgets after every chat, so it looks up your records.',
     'Jaya Grocer&rsquo;s last price for big onions: RM28 a bag.'),
    ('Rules &amp; skills', 'your SOP', '', 'Your way of working, written down: what never to do, and the steps.',
     'Over the credit limit? Stop and ask the boss.'),
    ('Permission', 'what it may touch', 'KEEPS IT SAFE', 'What it may see and do. Anything important waits for a person.',
     'It can draft an order. It cannot delete an invoice.'),
]
AC_ON1 = [('Brain', 'reads the WhatsApp order'), ('Memory', 'finds the customer and the stock'),
          ('Tools', 'drafts the order in your ERP'), ('Rules', 'asks when an item is unclear'),
          ('Permission', 'you approve before it saves')]

AC_S = 'rgba(0,245,169,.38)'
def AC_lbl(k, x, y, lx, ly, ex, ey, anchor='start'):
    name, short = AC_PARTS[k - 1][0], AC_PARTS[k - 1][1]
    return ('<g class="lb"><path class="ld" d="M%d %dL%d %d" pathLength="1"/><circle class="dot" cx="%d" cy="%d" r="6"/>'
            '<circle class="nb" cx="%d" cy="%d" r="17"/><text class="nn" x="%d" y="%d">%d</text>'
            '<text class="ln" x="%d" y="%d" text-anchor="%s">%s</text><text class="ls" x="%d" y="%d" text-anchor="%s">%s</text></g>'
            % (x, y, ex, ey, x, y, ex, ey, ex, ey + 6, k, lx, ly, anchor, name, lx, ly + 30, anchor, short))

AC_ROBOT = '''<svg class="rbt" viewBox="0 0 820 780" aria-label="An AI agent drawn as a robot, with its 5 parts labelled">
<defs>
 <linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22483F"/><stop offset="1" stop-color="#0B2420"/></linearGradient>
 <linearGradient id="rh" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2B5A50"/><stop offset="1" stop-color="#0D2A25"/></linearGradient>
 <radialGradient id="rg"><stop offset="0" stop-color="#00F5A9" stop-opacity=".55"/><stop offset="1" stop-color="#00F5A9" stop-opacity="0"/></radialGradient>
</defs>
<ellipse cx="380" cy="706" rx="200" ry="28" fill="url(#rg)" opacity=".7"/>
<g class="bob">
 <ellipse class="flame" cx="380" cy="596" rx="30" ry="40" fill="url(#rg)"/>
 <path d="M334 540h92l-14 34h-64z" fill="#0B2420" stroke="''' + AC_S + '''" stroke-width="2"/>
 <ellipse cx="380" cy="576" rx="22" ry="5" fill="#00F5A9" opacity=".85"/>
 <path d="M268 340C212 360 192 408 212 466" fill="none" stroke="''' + AC_S + '''" stroke-width="36" stroke-linecap="round"/>
 <path d="M268 340C212 360 192 408 212 466" fill="none" stroke="#1A3E37" stroke-width="31" stroke-linecap="round"/>
 <path d="M492 340C556 324 590 286 598 232" fill="none" stroke="''' + AC_S + '''" stroke-width="36" stroke-linecap="round"/>
 <path d="M492 340C556 324 590 286 598 232" fill="none" stroke="#1A3E37" stroke-width="31" stroke-linecap="round"/>
 <rect x="262" y="300" width="236" height="246" rx="58" fill="url(#rb)" stroke="''' + AC_S + '''" stroke-width="2"/>
 <path d="M290 320h180" stroke="rgba(242,251,247,.12)" stroke-width="2" stroke-linecap="round"/>
 <rect x="352" y="280" width="56" height="26" rx="8" fill="#0B2420" stroke="''' + AC_S + '''" stroke-width="2"/>
 <line x1="380" y1="86" x2="380" y2="50" stroke="''' + AC_S + '''" stroke-width="5" stroke-linecap="round"/>
 <circle class="ant" cx="380" cy="42" r="11" fill="#00F5A9"/>
 <rect x="248" y="84" width="264" height="204" rx="76" fill="url(#rh)" stroke="''' + AC_S + '''" stroke-width="2"/>
 <circle cx="246" cy="208" r="19" fill="#0B2420" stroke="''' + AC_S + '''" stroke-width="2"/><circle cx="246" cy="208" r="7" fill="#00F5A9" opacity=".6"/>
 <circle cx="514" cy="208" r="19" fill="#0B2420" stroke="''' + AC_S + '''" stroke-width="2"/><circle cx="514" cy="208" r="7" fill="#00F5A9" opacity=".6"/>
 <rect x="284" y="202" width="192" height="60" rx="30" fill="#021A17" stroke="rgba(0,245,169,.5)" stroke-width="2"/>
 <g class="eyes"><rect x="318" y="222" width="34" height="18" rx="9" fill="#00F5A9"/><rect x="408" y="222" width="34" height="18" rx="9" fill="#00F5A9"/></g>

 <g class="pt p1">
  <circle class="ring" cx="380" cy="142" r="84"/>
  <ellipse cx="380" cy="142" rx="76" ry="48" fill="rgba(0,245,169,.07)" stroke="rgba(0,245,169,.45)" stroke-width="2"/>
  <g class="brain" fill="rgba(0,245,169,.16)" stroke="#00F5A9" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
   <path d="M377 106C351 98 327 110 327 131C313 141 317 165 335 169C343 179 364 179 377 172Z"/>
   <path d="M383 106C409 98 433 110 433 131C447 141 443 165 425 169C417 179 396 179 383 172Z"/>
   <path d="M347 125c10 0 16 6 16 14M341 151c10-4 20 0 24 8M413 125c-10 0-16 6-16 14M419 151c-10-4-20 0-24 8" fill="none"/>
  </g>
 </g>
 <g class="pt p2">
  <circle class="ring" cx="606" cy="190" r="70"/>
  <circle cx="598" cy="232" r="22" fill="#0B2420" stroke="#00F5A9" stroke-width="3"/>
  <path transform="translate(588 148) scale(3)" d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 005.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z" fill="#0B2420" stroke="#00F5A9" stroke-width="1.1" stroke-linejoin="round"/>
  <g class="spk" stroke="#00F5A9" stroke-width="3" stroke-linecap="round"><path d="M664 186l16 4M662 206h16M654 224l10 10"/></g>
 </g>
 <g class="pt p3">
  <circle class="ring" cx="380" cy="458" r="80"/>
  <rect x="316" y="404" width="128" height="110" rx="14" fill="#06201C" stroke="#00F5A9" stroke-width="2.5"/>
  <path d="M316 441h128M316 478h128" stroke="#00F5A9" stroke-width="2" opacity=".7"/>
  <g fill="#00F5A9"><rect x="366" y="419" width="28" height="7" rx="3.5"/><rect x="366" y="456" width="28" height="7" rx="3.5"/><rect x="366" y="493" width="28" height="7" rx="3.5"/></g>
 </g>
 <g class="pt p4">
  <circle class="ring" cx="184" cy="478" r="70"/>
  <g transform="rotate(-10 182 478)">
   <rect x="148" y="434" width="70" height="90" rx="8" fill="#0B2420" stroke="#00F5A9" stroke-width="3"/>
   <path d="M160 434v90" stroke="#00F5A9" stroke-width="3"/>
   <path d="M172 462l7 7 14-14M172 492h32M172 506h22" fill="none" stroke="#00F5A9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <circle cx="214" cy="468" r="20" fill="#1A3E37" stroke="''' + AC_S + '''" stroke-width="2"/>
 </g>
 <g class="pt p5">
  <circle class="ring" cx="380" cy="356" r="56"/>
  <path d="M380 324l32 12v20c0 20-14 32-32 40c-18-8-32-20-32-40v-20z" fill="rgba(255,181,71,.16)" stroke="#FFB547" stroke-width="3" stroke-linejoin="round"/>
  <rect x="369" y="352" width="22" height="17" rx="3" fill="#FFB547"/>
  <path d="M373 352v-5a7 7 0 0114 0v5" fill="none" stroke="#FFB547" stroke-width="3"/>
 </g>
</g>
<g class="lbs">
 <g class="pt p1">''' + AC_lbl(1, 304, 128, 176, 120, 200, 128, 'end') + '''</g>
 <g class="pt p2">''' + AC_lbl(2, 628, 162, 656, 100, 628, 106) + '''</g>
 <g class="pt p5">''' + AC_lbl(5, 414, 356, 626, 350, 604, 364) + '''</g>
 <g class="pt p3">''' + AC_lbl(3, 446, 470, 626, 490, 604, 504) + '''</g>
 <g class="pt p4">''' + AC_lbl(4, 160, 528, 30, 660, 112, 604) + '''</g>
</g>
</svg>'''

def AC_detail():
    out = ''
    for i, (name, _, tag, what, eg) in enumerate(AC_PARTS):
        out += ('<div class="dt" data-s="%d"><small class="pn">PART %d OF 5%s</small><h2>%s</h2><p class="what">%s</p>'
                '<div class="eg"><small>EXAMPLE</small><p>%s</p></div></div>'
                % (i + 1, i + 1, (' <span class="tg">' + tag + '</span>') if tag else '', name, what, eg))
    return out

slide('20-what-is-agent', 'What is an AI agent?', SEC[2], 'dark', 'data-sparks="none"', MIN_CSS + '''
.mt { font-size: 66px; }
.wrap { flex:1; display:grid; grid-template-columns: 700px 1fr; gap: 70px; margin-top: 10px; min-height: 0; }
.rbt { width: 700px; height: auto; display:block; overflow: visible; animation: lift .9s cubic-bezier(.2,.8,.2,1) .3s both; }
@keyframes lift { from { opacity: 0; transform: translateY(26px); } to { opacity: 1; transform: none; } }
.bob { animation: bob 4.6s ease-in-out 1.4s infinite; }
@keyframes bob { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-7px); } }
.flame { transform-box: fill-box; transform-origin: 50% 0; animation: flk 1.2s ease-in-out infinite alternate; }
@keyframes flk { from { transform: scaleY(.85); opacity: .75; } to { transform: scaleY(1.1); opacity: 1; } }
.eyes rect { transform-box: fill-box; transform-origin: center; animation: blink 6s 2s infinite; }
@keyframes blink { 0%,95%,100% { transform: scaleY(1); } 97.5% { transform: scaleY(.12); } }
.pt { transition: opacity .5s ease; }
.ring { fill: none; stroke: #00F5A9; stroke-width: 3; opacity: 0; transform-box: fill-box; transform-origin: center; }
.p5 .ring { stroke: #FFB547; }
.lb .ld { fill:none; stroke: rgba(242,251,247,.45); stroke-width: 2; stroke-dasharray: 1; stroke-dashoffset: 1; animation: ld .6s ease forwards; }
.lb .dot { fill: #00F5A9; } .p5 .lb .dot { fill: #FFB547; }
.lb .nb { fill: #021A17; stroke: #00F5A9; stroke-width: 2.5; } .p5 .lb .nb { stroke: #FFB547; }
.lb .nn { font: 700 19px var(--sans); fill: #00F5A9; text-anchor: middle; } .p5 .lb .nn { fill: #FFB547; }
.lb .ln { font: 750 34px var(--sans); fill: var(--on-dark); letter-spacing: -.01em; transition: fill .4s ease; }
.lb .ls { font: 500 23px var(--sans); fill: var(--on-dark-2); }
.lbs .pt { opacity: 0; animation: lin .5s ease forwards; }
''' + ''.join('.lbs .p%d, .lbs .p%d .ld { animation-delay: %.2fs; }\n' % (k, k, .9 + (k - 1) * .2) for k in range(1, 6)) + '''
@keyframes lin { to { opacity: 1; } }
@keyframes ld { to { stroke-dashoffset: 0; } }
''' + ''.join('body[data-s="%d"] .bob .pt:not(.p%d), body[data-s="%d"] .lbs .pt:not(.p%d) > * { opacity: .18; }\n'
              'body[data-s="%d"] .p%d .ring { animation: rng 2.4s ease-out infinite; }\n'
              'body[data-s="%d"] .lbs .p%d .ln { fill: %s; }\n' % (k, k, k, k, k, k, k, k, '#FFB547' if k == 5 else '#00F5A9') for k in range(1, 6)) + '''
@keyframes rng { 0% { opacity: .9; transform: scale(.7); } 100% { opacity: 0; transform: scale(1.25); } }
.stage { position:relative; }
.intro, .dt, .lp { position:absolute; inset: 0; display:flex; flex-direction:column; justify-content:center; transition: opacity .5s ease, transform .6s cubic-bezier(.2,.8,.2,1); }
.dt, .lp { opacity: 0; transform: translateX(24px); pointer-events: none; }
body:not([data-s="0"]) .intro { opacity: 0; transform: translateX(-24px); }
''' + ''.join('body[data-s="%d"] .dt[data-s="%d"] { opacity: 1; transform: none; }\n' % (k, k) for k in range(1, 6)) + '''
body[data-s="6"] .lp { opacity: 1; transform: none; }
.intro > p { font-size: 40px; line-height: 1.35; color: var(--on-dark); max-width: 820px; }
.intro > p b { color: var(--neon); font-weight: 700; }
.vs { margin-top: 44px; display:grid; gap: 0; max-width: 820px; }
.vs div { display:grid; grid-template-columns: 300px 1fr; align-items:baseline; padding: 20px 0; border-top: 1px solid rgba(242,251,247,.18); }
.vs b { font-size: 32px; font-weight: 750; }
.vs span { font-size: 30px; color: var(--on-dark-2); }
.vs .yes b { color: var(--neon); } .vs .yes span { color: var(--on-dark); }
.pn { font-family: var(--mono); font-size: 20px; font-weight: 700; letter-spacing: .14em; color: var(--neon); display:flex; align-items:center; gap: 16px; }
.dt[data-s="5"] .pn { color: #FFB547; }
.tg { padding: 6px 12px; border-radius: 8px; border: 1.5px solid currentColor; letter-spacing: .1em; font-size: 18px; }
.dt h2 { font-size: 76px; font-weight: 750; letter-spacing: -.035em; line-height: 1; margin-top: 18px; }
.dt .what { font-size: 38px; line-height: 1.34; color: var(--on-dark); margin-top: 24px; max-width: 820px; text-wrap: balance; }
.dt .eg { margin-top: 40px; padding-left: 26px; border-left: 3px solid var(--neon); max-width: 820px; }
.dt[data-s="5"] .eg { border-color: #FFB547; }
.dt .eg small { font-family: var(--mono); font-size: 18px; font-weight: 700; letter-spacing: .14em; color: var(--on-dark-3); }
.dt .eg p { font-size: 31px; line-height: 1.38; color: var(--on-dark-2); margin-top: 8px; }
.lp h4 { font-family: var(--mono); font-size: 20px; letter-spacing: .14em; color: var(--neon); font-weight: 700; }
.lp ol { list-style:none; margin-top: 18px; max-width: 840px; }
.lp li { display:grid; grid-template-columns: 56px 220px 1fr; align-items:baseline; padding: 18px 0; border-top: 1px solid rgba(242,251,247,.16); }
.lp li i { font-style: normal; font-family: var(--mono); font-size: 22px; font-weight: 700; color: var(--on-dark-3); }
.lp li b { font-size: 32px; font-weight: 750; color: var(--neon); }
.lp li:last-child b { color: #FFB547; }
.lp li span { font-size: 30px; color: var(--on-dark); }
''', '''
<div class="mk u" style="--d:.05s">The agent</div>
<h1 class="mt u" style="--d:.2s">An AI agent is a brain with hands, and <em>limits</em></h1>
<div class="wrap">
  ''' + AC_ROBOT + '''
  <div class="stage">
    <div class="intro">
      <p class="u" style="--d:1.7s">A brain alone only talks. Give it <b>tools</b>, <b>memory</b>, <b>rules</b> and <b>permission</b>, and it does a real job.</p>
      <div class="vs"><div class="u" style="--d:1.95s"><b>Brain only</b><span>tells you what to do</span></div>
        <div class="yes u" style="--d:2.15s"><b>Brain + 4 parts</b><span>does the work for you</span></div></div>
    </div>
    ''' + AC_detail() + '''
    <div class="lp"><h4>THE 5 PARTS ON 1 WHATSAPP ORDER</h4><ol>''' + ''.join('<li><i>%d</i><b>%s</b><span>%s</span></li>' % (k + 1, p, t) for k, (p, t) in enumerate(AC_ON1)) + '''</ol></div>
  </div>
</div>
<script>
(function () {
  document.body.dataset.s = '0';
  addEventListener('message', function (e) { if (e.data && typeof e.data.deckStep === 'number') document.body.dataset.s = String(e.data.deckStep); });
})();
</script>
''',
"\"If the LLM is the brain, an AI agent is the brain with hands, and with limits. Here it is as a robot with 5 parts. A brain alone only talks; it tells you what to do. Give it the other 4 parts and it does the work for you. Let me take them 1 at a time.\"\n\n(Next) Brain: \"The head is the language model. It understands the message and plans the next step. It understands meaning, not keywords: bwg, bawang and onion are the same thing. Here it reads big onions, 10 kg bags, and sees the quantity is missing, so it asks. But on its own it has never seen your company. Like a smart graduate on day 1.\"\n\n(Next) Tools: \"The hands, and the part people forget. Each tool is 1 action in a real system. Some tools only look: check stock, read an invoice. Some tools act: create an order, send a message. The brain cannot click a button. Without tools, it can only tell you what to do. No tools, no work.\"\n\n(Next) Memory: \"The filing cabinet in its chest. Most people do not know this: the brain forgets everything after each chat. So it looks things up in your records: customers, prices, stock, fresh every time. Jaya Grocer's last price for big onions: RM28 a bag. Which also means: messy records in, wrong answers out.\"\n\n(Next) Rules and skills: \"The rulebook in its hand. Your way of working, written down. Rules say what must never happen: over the credit limit, stop and ask the boss. Skills are the steps for 1 job: read the order, match the items, check stock, draft, send for approval. Plain words, so your manager can read and change them.\"\n\n(Next) Permission: \"The badge on its chest, and what makes it safe. What can it see? Only the data its job needs. What can it do? Only what you allow: draft yes, delete no, move money never. And anything important waits for a person, and every action is logged. This is the difference between a helper and a risk.\"\n\n(Next) \"Put the 5 together on 1 WhatsApp order: the brain reads it, memory finds the customer and the stock, the tools draft the order in your ERP, the rules make it ask when an item is unclear, and permission means you approve before anything is saved.\"\n\nThis slide has 6 extra Next presses.\nNext: \"So how does it actually work? It goes round a loop.\"")

# ---------------- 16 · the agent loop ----------------
AC_NODES = [('Think', -90), ('Act', 30), ('Check', 150)]
AC_ROUNDS = [('1', 'Find the items', 'Big onions, 10 kg. 42 bags in stock.', ''),
             ('2', 'Check the credit', 'Order is RM560. Only RM180 left.', ''),
             ('3', 'Over the limit', 'Rule: the boss decides. It asks, then waits.', 'warn')]
def AC_loop_svg():
    import math
    cx, cy, r = 280, 270, 200
    o = ('<svg class="lps" viewBox="0 0 560 540"><defs><marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">'
         '<path d="M0 0L10 5L0 10z" fill="#00A57A"/></marker></defs>'
         '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="rgba(2,34,31,.08)" stroke-width="2"/>' % (cx, cy, r))
    for k, (_, a) in enumerate(AC_NODES):
        a0, a1 = math.radians(a + 26), math.radians(a + 120 - 26)
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        o += ('<path class="arc" style="--d:%.2fs" d="M%.1f %.1fA%d %d 0 0 1 %.1f %.1f" pathLength="1" fill="none" stroke="#00A57A" stroke-width="4" stroke-linecap="round" marker-end="url(#ah)"/>'
              % (1.0 + k * .35, x0, y0, r, r, x1, y1))
    o += ('<circle class="run" r="9" fill="#00A57A"><animateMotion dur="7s" begin="2.4s" repeatCount="indefinite" path="M%d %d A%d %d 0 1 1 %.1f %d A%d %d 0 1 1 %d %d"/></circle>'
          % (cx, cy - r, r, r, cx, cy + r, r, r, cx, cy - r))
    o += ('<text class="mid" x="%d" y="%d" text-anchor="middle">repeat</text><text class="mid2" x="%d" y="%d" text-anchor="middle">until done</text>'
          % (cx, cy - 4, cx, cy + 34))
    for k, (n, a) in enumerate(AC_NODES):
        x, y = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
        o += ('<g class="nd" style="--d:%.2fs"><circle cx="%.1f" cy="%.1f" r="66" fill="#fff" stroke="#02221F" stroke-width="3"/>'
              '<text class="nn" x="%.1f" y="%.1f" text-anchor="middle">%s</text></g>' % (.6 + k * .35, x, y, x, y + 11, n))
    return o + '</svg>'

slide('21-agent-loop', 'The agent loop', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.wrap { flex:1; display:grid; grid-template-columns: 560px 1fr; gap: 110px; margin-top: 30px; min-height: 0; align-items:center; }
.lps { width: 560px; height: 540px; overflow: visible; display:block; }
.lps .nn { font: 750 32px var(--sans); fill: var(--ink); }
.lps .mid { font: 750 34px var(--sans); fill: var(--green); }
.lps .mid2 { font: 500 26px var(--sans); fill: var(--ink-2); }
.nd { opacity: 0; animation: mFade .7s ease forwards; animation-delay: var(--d); }
.arc { stroke-dasharray: 1; stroke-dashoffset: 1; animation: acd .7s ease forwards; animation-delay: var(--d); }
@keyframes acd { to { stroke-dashoffset: 0; } }
html.static .nd { opacity: 1; animation: none; } html.static .arc { stroke-dashoffset: 0; animation: none; }
html.static .run { display: none; }
.rt { align-self: center; }
.rd { display:grid; grid-template-columns: 80px 1fr; align-items:baseline; padding: 24px 0; border-top: 1px solid var(--line); }
.mk + .rd { border-top: 3px solid var(--ink); }
.rd i { font-style: normal; font-size: 46px; font-weight: 800; color: var(--green); letter-spacing: -.03em; }
.rd b { display:block; font-size: 36px; font-weight: 750; letter-spacing: -.02em; }
.rd p { font-size: 28px; line-height: 1.35; color: var(--ink-2); margin-top: 6px; }
.rd.warn i { color: #C77800; }
.rd.warn b::after { content:""; display:inline-block; width: 12px; height: 12px; border-radius: 50%; background: #FFB547; margin-left: 14px; vertical-align: middle; }
''', '''
<div class="mk u" style="--d:.05s">How an agent works</div>
<h1 class="mt u" style="--d:.2s">It works in a <em>loop</em>, until the job is done</h1>
<p class="ml u" style="--d:.4s">Think, act, check, repeat. It stops when the job is done, or when it needs you.</p>
<div class="wrap">
  ''' + AC_loop_svg() + '''
  <div class="rt"><div class="mk u" style="--d:1.6s;margin-bottom:18px">1 WhatsApp order, 3 rounds</div>''' + ''.join(
      '<div class="rd %s u" style="--d:%.2fs"><i>%s</i><div><b>%s</b><p>%s</p></div></div>' % (c, 1.8 + k * .3, n, t, p) for k, (n, t, p, c) in enumerate(AC_ROUNDS)) + '''</div>
</div>
''',
"\"So how does an agent actually work? It does not answer in 1 shot like a chatbot. It goes round a loop. [Point at the circle] Think: plan the next step. Act: use 1 tool. Check: did it work? Am I done? Is this safe? If not done, round again.\n\nWatch it on 1 WhatsApp order from Jaya Grocer. Round 1: find the items. It searches and finds big onions, 10 kg bags, 42 bags in stock. Round 2: check the credit. The order is RM560, and only RM180 is left on the credit limit. Round 3: over the limit. The rule says the boss decides. So it sends the request for approval and waits.\n\nThat is the whole idea. It loops until the job is done, then reports to you. Or, when it is unsure or the step is risky, it stops and asks a person.\"\n\nNext: \"Think of it like hiring a new graduate.\"")

# ---------------- 17 · brain to staff ----------------
AC_HIRE = [('A job description', 'Instructions', 'the goal, and when it is done'),
           ('Logins and keys', 'Tools', '1 tool for each action'),
           ('The files', 'Memory', 'your records, what you taught it'),
           ('Your SOP', 'Rules &amp; skills', 'how your company works'),
           ('A supervisor', 'Permission', 'who says yes'),
           ('Probation', 'Testing', 'try it on old orders first')]

slide('22-brain-to-staff', 'From brain to staff member', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.wrap { display:grid; grid-template-columns: 1fr 280px; gap: 60px; margin-top: 40px; align-items:end; }
.tb .hd, .tb .hr { display:grid; grid-template-columns: 380px 90px 1fr; align-items:baseline; }
.tb .hd { font-family: var(--mono); font-size: 19px; font-weight: 700; letter-spacing: .14em; color: var(--ink-3); padding-bottom: 14px; border-bottom: 3px solid var(--ink); }
.tb .hd span:last-child { color: var(--green); }
.tb .hr { padding: 15px 0; border-bottom: 1px solid var(--line); }
.tb .hr > span { font-size: 30px; color: var(--ink-2); }
.tb .hr > i { color: var(--emerald); display:flex; align-self:center; }
.tb .hr b { font-size: 32px; font-weight: 750; letter-spacing: -.01em; }
.tb .hr small { font-size: 26px; color: var(--ink-3); margin-left: 16px; }
.av { width: 280px; height: 280px; }
.end { margin-top: auto; margin-bottom: 56px; font-size: 34px; color: var(--ink-2); }
.end b { color: var(--ink); } .end em { font-style: normal; color: var(--green); font-weight: 750; }
''', '''
<div class="mk u" style="--d:.05s">From brain to staff</div>
<h1 class="mt u" style="--d:.2s">Set up an AI Agent like a <em>new hire</em></h1>
<p class="ml u" style="--d:.4s">A smart brain is not enough. It needs what you give any new clerk.</p>
<div class="wrap">
  <div class="tb">
    <div class="hd uf" style="--d:.6s"><span>A NEW CLERK GETS</span><span></span><span>YOUR AI AGENT GETS</span></div>
    ''' + ''.join('<div class="hr u" style="--d:%.2fs"><span>%s</span><i>%s</i><div><b>%s</b><small>%s</small></div></div>' % (.8 + k * .18, a, ic(AC_ARROW, 26, 2.2), b, c) for k, (a, b, c) in enumerate(AC_HIRE)) + '''
  </div>
  <img class="av uf" style="--d:.9s" src="../assets/av/agent-grad.svg" alt="The agent as a new graduate">
</div>
<p class="end u" style="--d:2.1s">The brain plus this setup has a name: <em>the harness</em>.</p>
''',
"\"A brilliant brain alone only talks. Think about hiring a brilliant graduate: talent is not enough. You give them 6 things, and an AI Agent needs the same 6.\n\n[Go down the list] A job description: for the AI, its instructions: the goal, and when the job counts as done. Without it, it does too much, or the wrong job. Logins and keys: its tools, 1 for each action. Without them, it can only give advice. The files: its memory: your records, and what you taught it. Without it, it forgets the customer and guesses the price. Your SOP: its rules and skills. Without them, it does the job its own way. A supervisor: permission, who says yes. Without it, nobody checks before stock or money moves. And probation: testing. You try it on last month's orders first, then you watch it. Without that, the same mistake repeats quietly.\n\nThe brain plus this setup has a name: the harness. Every company can rent the same brain. The harness decides whether it helps or hurts.\"\n\nNext: \"So let me show you why the harness matters more than the brain.\"")

# ---------------- 18 · harness ----------------
AC_RING = ['Tools', 'Memory', 'Rules', 'Permission', 'The loop', 'Tests']
AC_LE = [('The steps', 'what it does, in what order'),
         ('When to stop', 'what &ldquo;done&rdquo; means'),
         ('When to ask a person', 'money, doubt or risk')]
def AC_harness_svg():
    import math
    cx, cy = 350, 320
    o = ('<svg class="hn" viewBox="0 0 700 640"><circle class="hring" cx="%d" cy="%d" r="296" fill="rgba(0,165,122,.07)"/>'
         '<text class="ol" x="%d" y="16" text-anchor="middle">THE HARNESS</text>' % (cx, cy, cx))
    for k, t in enumerate(AC_RING):
        a = math.radians(-90 + k * 60)
        x0, y0 = cx + 108 * math.cos(a), cy + 108 * math.sin(a)
        x1, y1 = cx + 168 * math.cos(a), cy + 168 * math.sin(a)
        c, sn = math.cos(a), math.sin(a)
        if abs(c) < .1:
            x, y, anc = x1, y1 + (-24 if sn < 0 else 44), 'middle'
        else:
            x, y, anc = x1 + (20 if c > 0 else -20), y1 + 10, ('start' if c > 0 else 'end')
        o += ('<path class="sp" style="--d:%.2fs" d="M%.1f %.1fL%.1f %.1f" pathLength="1"/>'
              '<g class="rg" style="--d:%.2fs"><circle cx="%.1f" cy="%.1f" r="7" fill="#00A57A"/>'
              '<text class="rl" x="%.1f" y="%.1f" text-anchor="%s">%s</text></g>'
              % (1.0 + k * .18, x0, y0, x1, y1, 1.2 + k * .18, x1, y1, x, y, anc, t))
    o += ('<circle cx="%d" cy="%d" r="100" fill="#02221F"/><text class="ct" x="%d" y="%d" text-anchor="middle">LLM</text>'
          '<text class="cs" x="%d" y="%d" text-anchor="middle">the brain</text>' % (cx, cy, cx, cy + 6, cx, cy + 40))
    return o + '</svg>'

slide('23-harness', 'Harness and loop engineering', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.wrap { flex:1; display:grid; grid-template-columns: 620px 1fr; gap: 110px; margin-top: 10px; min-height: 0; align-items:center; }
.hn { width: 620px; height: 567px; overflow: visible; display:block; }
.hn .ct { font: 800 48px var(--sans); fill: #00F5A9; }
.hn .cs { font: 600 22px var(--sans); fill: #A9C4BA; }
.hn .ol { font: 700 18px var(--mono); letter-spacing: .16em; fill: #006C48; }
.hn .rl { font: 750 28px var(--sans); fill: #02221F; }
.hn .sp { stroke: #00A57A; stroke-width: 2.5; stroke-dasharray: 1; stroke-dashoffset: 1; animation: acd .5s ease forwards; animation-delay: var(--d); }
.rg { opacity: 0; animation: mFade .6s ease forwards; animation-delay: var(--d); }
@keyframes acd { to { stroke-dashoffset: 0; } }
html.static .hn .sp { stroke-dashoffset: 0; animation: none; } html.static .rg { opacity: 1; animation: none; }
.le .lt { font-size: 34px; line-height: 1.35; color: var(--ink); margin-top: 16px; }
.le ul { list-style: none; margin-top: 24px; }
.le li { padding: 16px 0; border-top: 1px solid var(--line); }
.le li:first-child { border-top: 3px solid var(--ink); }
.le li b { font-size: 32px; font-weight: 750; letter-spacing: -.01em; }
.le li span { font-size: 27px; color: var(--ink-3); margin-left: 14px; }
.rent { margin-top: 48px; font-size: 48px; font-weight: 750; letter-spacing: -.03em; line-height: 1.15; }
.rent em { font-style: normal; color: var(--green); }
''', '''
<div class="mk u" style="--d:.05s">Why the setup matters</div>
<h1 class="mt u" style="--d:.2s">Same brain, <em>different results</em></h1>
<p class="ml u" style="--d:.4s">The setup around the brain decides. It is called the <b>harness</b>.</p>
<div class="wrap">
  <div class="uf" style="--d:.6s">''' + AC_harness_svg() + '''</div>
  <div class="le">
    <div class="mk u" style="--d:2.0s">Loop engineering</div>
    <p class="lt u" style="--d:2.15s">Designing how the agent works, step by step:</p>
    <ul>''' + ''.join('<li class="u" style="--d:%.2fs"><b>%s</b><span>%s</span></li>' % (2.3 + k * .18, t, s_) for k, (t, s_) in enumerate(AC_LE)) + '''</ul>
    <p class="rent u" style="--d:3.0s">The brain is rented.<br><em>The harness is built.</em></p>
  </div>
</div>
''',
"\"Here is the most important idea in AI right now. Everyone can rent the same brain: ChatGPT, Claude, Gemini. So where is the difference? In the setup around the brain. It is called the harness: the tools, the memory, the rules, the permission, the loop, and the tests.\n\nProof: the same brains power the chat apps and the coding tools like Claude Code and Codex. The chat app answers a question. The coding tool can work for hours on its own, writing and testing code. Same brain. Different harness.\n\nAnd the part that matters most is the loop. Designing it has a name: loop engineering. In plain words, 3 questions. The steps: what does it do, in what order, with which small tools? When to stop: what does done mean? Done means the sales order is drafted and sent for approval. And when to ask a person: anything with money, any doubt, any risk. Plus: it checks every step, logs everything, and when a tool fails, it retries once, then reports. Never guesses.\n\nSo remember: the brain is rented. The harness is built. A better harness beats a bigger brain.\"\n\nNext: \"And 1 part of that harness matters more than people think: the tools.\"")

# ---------------- 19 · no tools, no work ----------------
AC_RUN = [('Check stock', '42 bags'), ('Check credit', 'Within limit'), ('Create sales order', 'SO-00451'), ('Send on WhatsApp', 'PDF sent')]

slide('24-tools-and-memory', 'No tools, no work', SEC[2], 'light', 'data-sparks="none"', MIN_CSS + '''
.msg { display:flex; align-items:center; gap: 18px; margin-top: 40px; }
.msg .wa { width: 54px; height: 54px; border-radius: 50%; background: #25D366; color: #fff; display:grid; place-items:center; flex:none; }
.msg .mq b { font-weight: 750; }
.two { display:grid; grid-template-columns: 1fr 1fr; gap: 100px; margin-top: 44px; }
.col h3 { font-size: 38px; font-weight: 750; letter-spacing: -.02em; padding-top: 20px; border-top: 3px solid var(--ink-3); }
.col h3 span { font-size: 26px; font-weight: 500; color: var(--ink-3); margin-left: 12px; }
.col.yes h3 { border-color: var(--green); } .col.yes h3 span { color: var(--green); }
.say { margin-top: 22px; font-size: 28px; line-height: 1.4; color: var(--ink-2); padding: 16px 24px; border-radius: 6px 22px 22px 22px; background: #EFF1EE; }
.col ul { list-style:none; margin-top: 12px; }
.col li { display:flex; justify-content:space-between; align-items:center; padding: 9px 0; border-bottom: 1px solid var(--line); font-size: 28px; }
.col li .rs { display:flex; align-items:center; gap: 8px; font-weight: 700; color: var(--green); }
.vd { margin-top: 22px; display:flex; align-items:center; gap: 12px; font-size: 30px; font-weight: 750; }
.no .vd { color: var(--ink-3); } .yes .vd { color: var(--green); }
.erp { margin-top: auto; margin-bottom: 50px; font-size: 30px; color: var(--ink-2); }
.erp b { color: var(--ink); }
''', '''
<div class="mk u" style="--d:.05s">Tools</div>
<h1 class="mt u" style="--d:.2s">No tools, no <em>work</em></h1>
<p class="ml u" style="--d:.4s">A brain alone gives advice. With tools, it does the job inside your systems.</p>
<div class="msg u" style="--d:.7s"><span class="wa">''' + ic(AC_CHAT, 26) + '''</span><span class="mq"><b>Jaya Grocer:</b> Bwg besar 10kg x 20. Pls deliver be4 12pm</span></div>
<div class="two">
  <div class="col no u" style="--d:1.0s"><h3>Brain only<span>a chatbot</span></h3>
    <div class="say">&ldquo;Open SQL Account, create a sales order for 20 bags, then send it to the customer.&rdquo;</div>
    <div class="vd u" style="--d:1.5s">''' + ic(AC_X, 26, 2.6) + '''You still do all the work.</div></div>
  <div class="col yes u" style="--d:1.2s"><h3>Brain + tools<span>an AI agent</span></h3>
    <ul>''' + ''.join('<li class="u" style="--d:%.2fs"><span>%s</span><span class="rs">%s%s</span></li>' % (1.6 + k * .3, t, r, TICK) for k, (t, r) in enumerate(AC_RUN)) + '''</ul>
    <div class="vd u" style="--d:2.9s">''' + ic(CHECK, 26, 2.6) + '''Done. You just approve.</div></div>
</div>
<p class="erp u" style="--d:3.1s">Every tool works inside your <b>ERP</b>, the core of the company: customers, stock, invoices, money.</p>
''',
"\"Here is the part people forget. The smartest brain in the world, with no tools, can only talk.\n\nSame WhatsApp from Jaya Grocer: 20 bags of big onions before 12. [Point left] A chatbot, a brain only, replies: open SQL Account, create a sales order, send it to the customer. Helpful advice, and you still do all the work.\n\n[Point right] An AI agent, brain plus tools, does it: checks stock, 42 bags. Checks credit, within limit. Creates the sales order. Sends the PDF on WhatsApp. Done; you just approve.\n\nNow look where every one of those tools goes: into your ERP. Your ERP is the core of the company: customers, prices, stock, invoices and money. The agent's memory lives there too. It looks things up fresh every time, so if your records are messy, its answers are wrong.\n\nSo: no ERP, no tools. No tools, no work.\n\nThat is what an AI Agent is. Now let's leave the technology and talk about you.\"\n\nNext: \"Now let's talk about your company. Before I say anything else, I want to hear from you.\"")
