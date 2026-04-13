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
sections = [
    ('Start with the target', 'Decide whether you are building for 1080p, a quiet office machine, or something with room to upgrade later.'),
    ('Spend on the right parts', 'The GPU, power supply, cooling, and storage tend to affect the real experience more than cosmetic extras.'),
    ('Use the whole market', 'New parts, open-box parts, and used parts can all be good buys if you compare them honestly.'),
    ('What good value looks like', 'A strong value build feels balanced, quiet, and easy to live with instead of flashy for no reason.'),
]
lead = random.choice([
    'Good budget PC advice should make the build easier to use, not harder to justify.',
    'The best value systems usually look boring on paper but feel great in practice.',
    'A smart build is the one you can keep enjoying after the excitement of buying parts is gone.'
])
body = ['---', 'layout: post', f'title: "{keyword.title()}"', f'date: {today} 09:00:00 -0400', '---', '', lead, '']
for heading, text in sections:
    body += [f'## {heading}', text, '']
body.append('If I were buying today, I would keep the target clear, skip the vanity upgrades, and only spend extra where the build truly improves.')
post.write_text('
'.join(body)+'
', encoding='utf-8')
print(post)
