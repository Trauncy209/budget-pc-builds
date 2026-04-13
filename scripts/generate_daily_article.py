from pathlib import Path
import datetime as dt
import random

base = Path(__file__).resolve().parents[1]
keywords = [line.strip() for line in (base / 'content' / 'keywords.txt').read_text(encoding='utf-8').splitlines() if line.strip()]
if not keywords:
    raise SystemExit('No keywords found')
keyword = keywords[dt.date.today().toordinal() % len(keywords)]
today = dt.date.today().isoformat()
slug = keyword.lower().replace(' ', '-').replace('/', '-')[:80]
post = base / '_posts' / f'{today}-{slug}.md'
if post.exists():
    print(f'already exists: {post.name}')
    raise SystemExit(0)

openers = [
    'For a budget build, the best move is usually to stay calm and spend where it matters.',
    'The cheapest parts are not always the best value.',
    'A good low-cost PC feels balanced, quiet, and easy to live with.'
]
points = [
    ('Start with the target', 'Decide whether you care about 1080p, 1440p, or productivity first. That decides everything else.'),
    ('Spend on the GPU, not the fluff', 'A flashy board or case rarely changes the feel of the build. A stronger GPU usually does.'),
    ('Use decent power and cooling', 'A boring PSU and sensible airflow save more headaches than RGB ever will.')
]
lead = random.choice(openers)
first, second, third = random.sample(points, 3)
content = f'''---
layout: post
title: "{keyword.title()}"
date: {today} 09:00:00 -0400
---

{lead}

## {first[0]}
{first[1]}

## {second[0]}
{second[1]}

## {third[0]}
{third[1]}

My rule: if two parts are close in price, pick the one that makes the whole machine easier to use, not the one with the most marketing buzz.
'''
post.write_text(content, encoding='utf-8')
print(post)
