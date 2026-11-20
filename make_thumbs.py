#!/usr/bin/env python3
"""Render every slide, English and Mandarin (animations finished), to thumbs/ and thumbs-zh/ for the overview wall, then rebuild index.html.

Robust by design: old thumbnails are only replaced, never wiped first; each slide gets its own browser
(so 1 heavy page, e.g. a video slide, cannot crash the rest); a failed slide is retried, then reported.
"""
import asyncio, glob, os, subprocess, sys
from playwright.async_api import async_playwright
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
# Use Playwright's own Chromium; fall back to any Chrome for Testing already downloaded on this Mac.
EXE = next(iter(sorted(glob.glob(os.path.expanduser(
    '~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing')), reverse=True)), None)
ARGS = ['--autoplay-policy=user-gesture-required', '--mute-audio']


async def launch(p):
    try:
        return await p.chromium.launch(args=ARGS)
    except Exception:
        return await p.chromium.launch(executable_path=EXE, args=ARGS)


async def main():
    jobs = []
    for src, dst in (('slides', 'thumbs'), ('slides-zh', 'thumbs-zh')):
        os.makedirs(os.path.join(HERE, dst), exist_ok=True)
        keep = {os.path.basename(f).replace('.html', '.jpg') for f in glob.glob(os.path.join(HERE, src, '*.html'))}
        for old in glob.glob(os.path.join(HERE, dst, '*.jpg')):   # drop only pictures of slides that no longer exist
            if os.path.basename(old) not in keep:
                os.remove(old)
        jobs += [(f, dst) for f in sorted(glob.glob(os.path.join(HERE, src, '*.html')))]
    failed = []
    async with async_playwright() as p:
        sem = asyncio.Semaphore(4)

        async def one(job):
            f, dst = job
            out = os.path.join(HERE, dst, os.path.basename(f).replace('.html', '.jpg'))
            async with sem:
                for attempt in range(3):
                    b = None
                    try:
                        b = await launch(p)
                        pg = await b.new_page(viewport={'width': 1920, 'height': 1080})
                        await pg.goto('file://' + f + '#static', wait_until='domcontentloaded', timeout=30000)
                        await pg.wait_for_timeout(1500)
                        png = f + '.tmp.png'
                        await pg.screenshot(path=png, timeout=30000)
                        Image.open(png).convert('RGB').resize((960, 540), Image.LANCZOS).save(out, quality=86)
                        os.remove(png)
                        return
                    except Exception as e:
                        if attempt == 2:
                            failed.append((os.path.relpath(f, HERE), str(e).splitlines()[0][:120]))
                    finally:
                        if b:
                            try:
                                await b.close()
                            except Exception:
                                pass

        await asyncio.gather(*[one(j) for j in jobs])
    print('thumbs: %d of %d' % (len(jobs) - len(failed), len(jobs)))
    for f, err in failed:
        print('  FAILED', f, '-', err)


asyncio.run(main())
subprocess.run([sys.executable, os.path.join(HERE, 'build.py')], check=True)
