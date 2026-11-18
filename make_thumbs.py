#!/usr/bin/env python3
"""Render every slide, English and Mandarin (animations finished), to thumbs/ and thumbs-zh/ for the overview wall, then rebuild index.html."""
import asyncio, glob, os, subprocess, sys
from playwright.async_api import async_playwright
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
# Use Playwright's own Chromium; fall back to any Chrome for Testing already downloaded on this Mac.
EXE = next(iter(sorted(glob.glob(os.path.expanduser(
    '~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing')), reverse=True)), None)

async def main():
    jobs = []
    for src, dst in (('slides', 'thumbs'), ('slides-zh', 'thumbs-zh')):
        os.makedirs(os.path.join(HERE, dst), exist_ok=True)
        for old in glob.glob(os.path.join(HERE, dst, '*.jpg')):
            os.remove(old)
        jobs += [(f, dst) for f in sorted(glob.glob(os.path.join(HERE, src, '*.html')))]
    files = jobs
    async with async_playwright() as p:
        try:
            b = await p.chromium.launch()
        except Exception:
            b = await p.chromium.launch(executable_path=EXE)
        sem = asyncio.Semaphore(6)
        async def one(job):
            f, dst = job
            async with sem:
                pg = await b.new_page(viewport={'width': 1920, 'height': 1080})
                await pg.goto('file://' + f + '#static'); await pg.wait_for_timeout(1500)
                png = f + '.tmp.png'
                await pg.screenshot(path=png); await pg.close()
                Image.open(png).convert('RGB').resize((960, 540), Image.LANCZOS).save(
                    os.path.join(HERE, dst, os.path.basename(f).replace('.html', '.jpg')), quality=86)
                os.remove(png)
        await asyncio.gather(*[one(f) for f in files])
        await b.close()
    print('thumbs:', len(files))

asyncio.run(main())
subprocess.run([sys.executable, os.path.join(HERE, 'build.py')], check=True)
