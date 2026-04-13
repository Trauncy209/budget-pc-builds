---
layout: default
title: Budget PC Builds
---

<section class="hero">
  <p class="eyebrow">Hardware value</p>
  <h1>Value hardware</h1>
  <p class="muted">Simple build notes for people who want a good machine without paying for parts that do not change the experience much.</p>
</section>

<div class="split" style="margin-top:20px;">
  <section class="card highlight">
    <h2>Latest posts</h2>
    <ul class="clean">
      {% for post in site.posts limit:5 %}
      <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><div class="muted">{{ post.date | date: "%b %d, %Y" }}</div></li>
      {% endfor %}
    </ul>
  </section>
  <section class="card">
    <h2>What you get here</h2>
    <p>Build pages that explain performance, noise, and cost in plain language.</p>
    <p class="muted">Readable writing, practical recommendations, and enough context to decide whether a topic matters to you.</p>
  </section>
</div>
