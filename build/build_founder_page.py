# -*- coding: utf-8 -*-
# Run from anywhere — this script always operates relative to the repo root.
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import json

import re as _re
_src = open("build/build_blogs.py", encoding="utf-8").read()
BRAND = _re.search(r'<a class="brand".*?</a>', _src, _re.S).group(0).replace('href="../index.html"', 'href="index.html"')


SCHEMA = {
  "@context":"https://schema.org","@graph":[
    {"@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":"https://hevify.in/"},
      {"@type":"ListItem","position":2,"name":"Vrushank Soni — Founder"}]},
    {"@type":"ProfilePage","dateModified":"2026-08-06",
     "mainEntity":{"@type":"Person","@id":"https://hevify.in/#vrushank-soni","name":"Vrushank Soni",
       "jobTitle":"Founder & Digital Strategist","worksFor":{"@id":"https://hevify.in/#organization"},
       "alumniOf":"BBA (Marketing Management), PGDM (Marketing & Finance)",
       "description":"Vrushank Soni is the founder of Hevify Labs, a performance marketing and social media agency in Ahmedabad, India. He combines a data-analytics background (Power BI, SQL, Python) with hands-on SEO, Meta Ads and Google Ads experience.",
       "knowsAbout":["Performance Marketing","SEO","GEO","Social Media Marketing","Power BI","SQL","Python","Data Analytics"],
       "sameAs":["https://www.linkedin.com/in/vrushanksoni","https://www.instagram.com/vrushh_98/","https://vrushanksoni.netlify.app","https://github.com/SoniVrushank"]}}
  ]}

HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vrushank Soni — Founder of Hevify Labs, Ahmedabad</title>
<meta name="description" content="Vrushank Soni is the founder of Hevify Labs, a performance marketing and social media agency in Ahmedabad. His background in data analytics (Power BI, SQL, Python) shapes Hevify's accountable, numbers-first approach to marketing.">
<meta name="keywords" content="Vrushank Soni, Vrushank Soni Hevify, Hevify Labs founder, Vrushank Soni Ahmedabad, Vrushank Soni digital marketing, Vrushank Soni LinkedIn">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://hevify.in/founder-vrushank-soni.html">
<meta property="og:type" content="profile"><meta property="og:title" content="Vrushank Soni — Founder of Hevify Labs, Ahmedabad">
<meta property="og:description" content="The founder story, background and vision behind Hevify Labs.">
<meta property="og:url" content="https://hevify.in/founder-vrushank-soni.html">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<script type="application/ld+json">{schema}</script>
<link rel="stylesheet" href="assets/style.css">
<script src="assets/site.js" defer></script>
</head><body>
<div class="cursor-ring" id="cRing"></div>
<div class="cursor-dot" id="cDot"></div>
<div class="navb" id="siteNav"><div class="in">
{brand}
<a class="btn" href="https://wa.me/919429428270?text=Hi%20Hevify%20Labs%2C%20I%20want%20to%20discuss%20my%20requirements." target="_blank" rel="noopener" data-hot>Contact us</a>
</div></div>
<div class="wrap">
<p class="crumb"><a href="index.html">Home</a> / Founder</p>
<div class="f-hero reveal">
  <span class="f-avatar">VS</span>
  <div><h1>Vrushank <span class="serif">Soni</span></h1><p class="role">Founder &amp; Digital Strategist, Hevify Labs · Ahmedabad, India</p></div>
</div>
<div class="linkrow reveal">
  <a href="https://www.linkedin.com/in/vrushanksoni" target="_blank" rel="noopener">LinkedIn — Vrushank Soni</a>
  <a href="https://www.instagram.com/vrushh_98/" target="_blank" rel="noopener">Instagram — @vrushh_98</a>
  <a href="https://vrushanksoni.netlify.app" target="_blank" rel="noopener">Personal Portfolio</a>
  <a href="https://github.com/SoniVrushank" target="_blank" rel="noopener">GitHub</a>
</div>
<div class="tldr reveal"><h2>Quick answer</h2><p>Vrushank Soni is the founder of Hevify Labs, a performance marketing and social media agency in Ahmedabad, India. His background is in data analytics — Power BI, SQL and Python — alongside hands-on SEO, Meta Ads and Google Ads experience, which is why Hevify is built around measurable, accountable results rather than vanity metrics.</p></div>
<article>
<h2>Where it started</h2>
<p>Vrushank comes from a business background — growth, customers, marketing and finance were part of everyday conversation long before they were a career. That curiosity turned into a BBA in Marketing Management, followed by a PGDM in Marketing &amp; Finance. Internships and client work sharpened the marketing side; analytics pulled him toward Power BI, SQL and Python — turning business data into decisions people could actually act on.</p>
<h2>What he actually worked on</h2>
<div class="timeline">
<div class="trow"><b>Zero Dimensions — Social Media &amp; SEO</b><span>Internship, 2026</span><p>Owned on-page SEO and worked with the off-page team so content ranked, not just shipped — engagement up 15% through weekly reporting leadership could act on.</p></div>
<div class="trow"><b>Provectus — Marketing Intern</b><span>Internship, 2025</span><p>Grew an advisory firm's LinkedIn presence 30% in six months by reading which content converted and doubling down — B2B positioning driven by analysis, not guesswork.</p></div>
<div class="trow"><b>Freelance &amp; client work — Digital Marketing</b><span>2024 — ongoing</span><p>Ran Meta Ads, content and reporting end-to-end for clients including PhysioEdge, Swarna Shanti, Om Shanti and TruVeda, tying every campaign back to its performance numbers.</p></div>
<div class="trow"><b>Hevify Labs — Founder</b><span>2025 — now</span><p>Built Hevify around the same principle: track first, then spend — performance marketing, social media, SEO &amp; GEO and AI automation for brands in Ahmedabad and beyond.</p></div>
</div>
<h2>Why Hevify looks at marketing this way</h2>
<p>A data background changes how you look at marketing. Before a campaign gets creative, the question is what will actually be measured, and what "working" looks like in numbers. That's the thinking behind Hevify's transparent pricing, its "free extras with every plan" promise, and why every package starts with tracking, not with the ad itself.</p>
<h2>Vision for Hevify Labs</h2>
<p>To be Ahmedabad's most accountable growth partner — starting locally, built to scale across Gujarat and beyond — where every rupee spent has a number attached to it, and every client can see exactly what their marketing is actually doing for the business. Less noise, more growth.</p>
</article>
<div class="cta reveal"><h2>Want to talk <span class="serif">growth</span>?</h2><p>Message Vrushank and the Hevify Labs team directly — no forms, no delays.</p><a class="btn" href="https://wa.me/919429428270?text=Hi%20Hevify%20Labs%2C%20I%20want%20to%20discuss%20my%20requirements." target="_blank" rel="noopener">Message us on WhatsApp →</a></div>
</div>
<footer class="foot">© 2026 Hevify Labs · Performance marketing &amp; social media agency, Ahmedabad, India.</footer>
</body></html>"""

open("founder-vrushank-soni.html", "w", encoding="utf-8").write(
    HTML.format(schema=json.dumps(SCHEMA, ensure_ascii=False), brand=BRAND)
)
print("wrote founder-vrushank-soni.html")
