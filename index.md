---
layout: default
title: Budget PC Builds
---

<p class="eyebrow">Value hardware</p>
<h1>Budget PC Builds</h1>
<p class="muted">Simple build notes for people who want a good machine without paying for parts that don’t change the experience much.</p>

<div class="stack">
  <section class="card">
    <h2 class="section-title">Start here</h2>
    <ul class="clean">
      {% for post in site.posts limit:2 %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <div class="muted">{{ post.date | date: "%b %d, %Y" }}</div>
      </li>
      {% endfor %}
    </ul>
  </section>

  <section class="card">
    <h2 class="section-title">What this site is for</h2>
    <p>Quiet, balanced builds with fewer regrets and fewer unnecessary upgrades.</p>
  </section>

  <section class="card">
    <h2 class="section-title">Recent posts</h2>
    <ul class="clean">
      {% for post in site.posts limit:5 %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <div class="muted">{{ post.date | date: "%b %d, %Y" }}</div>
      </li>
      {% endfor %}
    </ul>
  </section>
</div>
