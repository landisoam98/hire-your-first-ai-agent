#!/usr/bin/env python3
"""Fold translated parts (i18n/parts/zh-*.json) into i18n/zh.json and i18n/zh-notes.json.

A part looks like {"texts": {en: zh}, "overrides": {"slide-key::en": zh}, "notes": {slide-key: zh}}.
Notes are stored with the English they were translated from, so a later edit to the English notes
shows up as "notes missing" on the next build.
"""
import glob, json, os, re

D = os.path.dirname(os.path.abspath(__file__))
HERE = os.path.dirname(D)

def load(p, d):
    return json.load(open(p)) if os.path.exists(p) else d

t = load(os.path.join(D, 'zh.json'), {})
n = load(os.path.join(D, 'zh-notes.json'), {})
en_notes = {}
for it in json.loads(re.search(r'window\.DECK_MANIFEST = (\[.*?\n\]);',
                               open(os.path.join(HERE, 'index.html')).read(), re.S).group(1)):
    en_notes[re.sub(r'^\d+-', '', os.path.basename(it['file'])[:-5])] = it['notes']

added = notes_added = 0
for p in sorted(glob.glob(os.path.join(D, 'parts', 'zh-*.json'))):
    part = json.load(open(p))
    for k, v in {**part.get('texts', {}), **part.get('overrides', {})}.items():
        if k not in t:
            added += 1
        t[k] = v
    for k, v in part.get('notes', {}).items():
        if k in en_notes:
            n[k] = {'en': en_notes[k], 'zh': v}
            notes_added += 1

json.dump(dict(sorted(t.items())), open(os.path.join(D, 'zh.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(dict(sorted(n.items())), open(os.path.join(D, 'zh-notes.json'), 'w'), ensure_ascii=False, indent=1)
print('texts: %d total (%d new) · notes: %d updated' % (len(t), added, notes_added))
