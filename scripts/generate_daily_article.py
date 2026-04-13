from pathlib import Path
    import datetime as dt

    base = Path(__file__).resolve().parents[1]
    keywords = [line.strip() for line in (base / 'content' / 'keywords.txt').read_text(encoding='utf-8').splitlines() if line.strip()]
    if not keywords:
        raise SystemExit('No keywords found')
    keyword = keywords[0]
    today = dt.date.today().isoformat()
    slug = keyword.lower().replace(' ', '-').replace('/', '-')[:80]
    post = base / '_posts' / f'{today}-{slug}.md'
    if post.exists():
        print(f'already exists: {post.name}')
        raise SystemExit(0)
    title = keyword.title()
    content = (
        '---
layout: post
title: "{title}"
date: {date} 09:00:00 -0400
---

'
        '# {title}

'
        'Write a helpful, specific article here. Include real steps, common mistakes, and a clear recommendation.
'
    ).format(title=title, date=today)
    post.write_text(content, encoding='utf-8')
    print(post)
