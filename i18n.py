"""Mandarin (Simplified Chinese) version of the deck.

build.py writes the English deck, then calls build_zh(), which makes the Chinese deck from it:
  slides/*.html  -> slides-zh/*.html      index.html -> index-zh.html      thumbs/ -> thumbs-zh/

Translations live in i18n/:
  zh.json        {"English text": "中文"}   every visible text, alt text, typewriter text and label
                 {"14-typed-three-times::English text": "中文"}   optional override for 1 slide only
  zh-notes.json  {"<slide file>": {"en": "<English notes>", "zh": "<中文 notes>"}}
  zh.css         CSS added to every Chinese slide, for the few layouts that need it ("\n" in a translation = line break)

Any English text with no translation (new or edited) is listed in i18n/zh-missing.json, and the build
prints how many. Fill them in, rebuild, and both decks stay in step.
"""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'i18n')
TAG = re.compile(r'(<[^>]+>)')
ATTRS = ('alt', 'data-type', 'aria-label', 'title', 'placeholder', 'data-section')
CJK_FONT = ('<style>:root{--sans:"Figtree","PingFang SC","Hiragino Sans GB","Noto Sans SC","Microsoft YaHei",sans-serif;'
            '--mono:"JetBrains Mono","PingFang SC","Noto Sans SC","Microsoft YaHei",monospace}'
            'html[lang=zh-Hans] body{word-break:normal;line-break:strict}</style>')


def norm(t):
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()


def needs(t):
    """True when a text contains words to translate (not a number, code, amount or brand-only string)."""
    if not re.search(r'[A-Za-z]{2,}', t):
        return False
    if all(re.search(r'\d', w) or not re.search(r'[A-Za-z]{2,}', w) for w in t.split()):
        return False                                   # BWG-CN-10, SO-10231, RM552.00, 12pm: every word is a code
    return True


def load(name, default):
    p = os.path.join(D, name)
    return json.load(open(p)) if os.path.exists(p) else default


class Tr:
    def __init__(self):
        self.t = load('zh.json', {})
        self.missing = {}

    def get(self, text, where):
        k = norm(text)
        if not k:
            return None
        if where + '::' + k in self.t:                  # 1-slide override always wins, even for 1 letter
            return self.t[where + '::' + k]
        if not needs(k):
            return None
        v = self.t.get(k)
        if v is None:
            self.missing.setdefault(k, where)
        return v

    def text_node(self, raw, where):
        v = self.get(raw, where)
        if v is None:
            return raw
        lead = raw[:len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()):]
        return lead + html.escape(v, quote=False).replace('\n', '<br>') + trail

    def tag(self, tag, where):
        def sub(m):
            v = self.get(m.group(2), where)
            return m.group(0) if v is None else '%s="%s"' % (m.group(1), html.escape(v, quote=True))
        return re.sub(r'\b(%s)="([^"]*)"' % '|'.join(ATTRS), sub, tag)

    def script(self, js, where):
        def sub(m):
            q, body = m.group(1), m.group(2)
            if not re.search(r'[A-Za-z]{2,}[ ,][A-Za-z]{2,}', body):
                return m.group(0)
            v = self.get(body, where)
            return m.group(0) if v is None else q + v.replace(q, '\\' + q) + q
        return re.sub(r"(['\"])((?:(?!\1)[^\\\n])+)\1", sub, js)

    def page(self, src, where):
        out, mode = [], None
        for part in TAG.split(src):
            if not part:
                continue
            if part.startswith('<'):
                low = part.lower()
                if low.startswith('<style'): mode = 'style'
                elif low.startswith('<script'): mode = 'script'
                elif low.startswith('</style') or low.startswith('</script'): mode = None
                out.append(self.tag(part, where) if not low.startswith('<!') else part)
            elif mode == 'style':
                out.append(part)
            elif mode == 'script':
                out.append(self.script(part, where))
            else:
                out.append(self.text_node(part, where))
        s = ''.join(out).replace('<html lang="en">', '<html lang="zh-Hans">')
        zcss = os.path.join(D, 'zh.css')                  # Chinese-only layout tweaks (fonts run wider/narrower)
        extra = ('<style>' + open(zcss).read() + '</style>') if os.path.exists(zcss) else ''
        return s.replace('</head>', CJK_FONT + extra + '\n</head>', 1)


SHELL_UI = [('<title>Hire Your First AI Agent · SuDu AI', '<title>聘请你的第一个 AI Agent'),
            ('Hire Your First AI Agent · click any slide to present · N notes · Esc overview', '聘请你的第一个 AI Agent · 点击任意一页开始演示 · N 讲稿 · Esc 总览'),
            ('Hire Your First AI Agent · click any slide to present', '聘请你的第一个 AI Agent · 点击任意一页开始演示'),
            ('▶ Present', '▶ 开始演示'), ('⊞ Overview', '⊞ 总览'), ('<html lang="en">', '<html lang="zh-Hans">')]


def build_zh(manifest, shell):
    tr = Tr()
    notes = load('zh-notes.json', {})
    out_dir = os.path.join(HERE, 'slides-zh')
    os.makedirs(out_dir, exist_ok=True)
    for f in os.listdir(out_dir):
        if f.endswith('.html'):
            os.remove(os.path.join(out_dir, f))
    zman, stale = [], []
    for it in manifest:
        name = os.path.basename(it['file'])
        sid = name[:-5]
        key = re.sub(r'^\d+-', '', sid)
        src = open(os.path.join(HERE, it['file'])).read()
        open(os.path.join(out_dir, name), 'w').write(tr.page(src, key))
        z = dict(it, file='slides-zh/' + name)
        z['label'] = tr.get(it['label'], key) or it['label']
        z['section'] = tr.get(it['section'], key) or it['section']
        n = notes.get(key)
        if n and n.get('en') == it['notes']:
            z['notes'] = n['zh']
        else:
            stale.append(key)
            z['notes'] = (n['zh'] + '\n\n[English notes changed — update zh-notes.json]') if n else it['notes']
        th = os.path.join(HERE, 'thumbs-zh', sid + '.jpg')
        if os.path.exists(th):
            z['thumb'] = 'thumbs-zh/%s.jpg' % sid
        else:
            z.pop('thumb', None)
        zman.append(z)
    s = shell.replace('/*MANIFEST*/', json.dumps(zman, ensure_ascii=False, indent=1))
    for a, b in SHELL_UI:
        s = s.replace(a, b)
    open(os.path.join(HERE, 'index-zh.html'), 'w').write(s)
    os.makedirs(D, exist_ok=True)
    json.dump(tr.missing, open(os.path.join(D, 'zh-missing.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump({k: manifest_notes(manifest, k) for k in stale}, open(os.path.join(D, 'zh-notes-missing.json'), 'w'), ensure_ascii=False, indent=1)
    print('zh: %d slides, %d texts missing, %d notes missing' % (len(zman), len(tr.missing), len(stale)))


def manifest_notes(manifest, key):
    for it in manifest:
        if re.sub(r'^\d+-', '', os.path.basename(it['file'])[:-5]) == key:
            return it['notes']
