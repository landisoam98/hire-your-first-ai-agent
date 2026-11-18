#!/usr/bin/env python3
"""Try a slide fragment without touching the real deck.

  python3 i18n/work/try_min.py i18n/work/min-A.py          -> builds into i18n/work/out-A/, screenshots each fragment slide
  python3 i18n/work/try_min.py i18n/work/min-A.py --apply  -> (lead only) splices the fragment into build.py

A fragment is plain Python placed into build.py: helper constants (prefix them!) plus top-level
slide('NN-key', ...) calls. Each key it defines replaces the old top-level slide() call with that key.
Shots: out-X/shots/<key>.png (all animations finished) and out-X/shots/<key>-live.png (2.5 s after load).
"""
import ast, os, re, subprocess, sys, shutil

DECK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXE = '/Users/landisoam/Library/Caches/ms-playwright/chromium-1228/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'


def slide_calls(src):
    out = {}
    for n in ast.parse(src).body:
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and getattr(n.value.func, 'id', '') == 'slide':
            a = n.value.args[0]
            if isinstance(a, ast.Constant):
                out[re.sub(r'^\d+-', '', a.value)] = (n.lineno, n.end_lineno)
    return out


def splice(src, frag):
    keys = slide_calls(frag)
    have = slide_calls(src)
    missing = [k for k in keys if k not in have]
    if missing:
        sys.exit('unknown slide keys in fragment: %s' % missing)
    lines = src.split('\n')
    first = min(have[k][0] for k in keys)
    for k in sorted(keys, key=lambda k: -have[k][0]):          # remove bottom-up
        a, b = have[k]
        del lines[a - 1:b]
    removed_before = sum(have[k][1] - have[k][0] + 1 for k in keys if have[k][0] < first)
    lines[first - 1 - removed_before:first - 1 - removed_before] = frag.rstrip('\n').split('\n') + ['']
    return '\n'.join(lines), list(keys)


def main():
    frag_path = sys.argv[1]
    frag = open(frag_path).read()
    src = open(os.path.join(DECK, 'build.py')).read()
    new, keys = splice(src, frag)
    if '--apply' in sys.argv:
        open(os.path.join(DECK, 'build.py'), 'w').write(new)
        print('applied', keys)
        return
    tag = re.sub(r'\W', '', os.path.basename(frag_path)[:-3])
    out = os.path.join(DECK, 'i18n', 'work', 'out-' + tag)
    os.makedirs(out, exist_ok=True)
    for d in ('assets', 'shared'):
        p = os.path.join(out, d)
        if not os.path.exists(p):
            os.symlink(os.path.join(DECK, d), p)
    shutil.copy(os.path.join(DECK, 'shell.html'), out)
    new = new.replace("HERE = os.path.dirname(os.path.abspath(__file__))", "HERE = %r" % out)
    new = new.replace('    import i18n', '    pass').replace('    i18n.build_zh(manifest, raw_shell)', '    pass')
    open(os.path.join(out, 'build_try.py'), 'w').write(new)
    r = subprocess.run([sys.executable, os.path.join(out, 'build_try.py')], capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr[-3000:])
    print(r.stdout.strip())
    from playwright.sync_api import sync_playwright
    os.makedirs(os.path.join(out, 'shots'), exist_ok=True)
    files = {re.sub(r'^\d+-', '', f[:-5]): f for f in os.listdir(os.path.join(out, 'slides'))}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=EXE)
        pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        for k in keys:
            f = os.path.join(out, 'slides', files[k])
            pg.goto('file://' + f + '#static'); pg.wait_for_timeout(900)
            pg.screenshot(path=os.path.join(out, 'shots', k + '.png'))
        live = b.new_page(viewport={'width': 1920, 'height': 1080})
        live.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>false})")
        live.on('pageerror', lambda e: errs.append(str(e)))
        for k in keys:
            live.goto('file://' + os.path.join(out, 'slides', files[k])); live.wait_for_timeout(2500)
            live.screenshot(path=os.path.join(out, 'shots', k + '-live.png'))
        b.close()
    print('shots in', os.path.join(out, 'shots'), 'for', keys)
    if errs:
        print('PAGE ERRORS:', errs)


if __name__ == '__main__':
    main()
