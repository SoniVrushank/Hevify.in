# -*- coding: utf-8 -*-
# Run from anywhere — this script always operates relative to the repo root.
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import json

import re as _re
_src = open("build/build_blogs.py", encoding="utf-8").read()
BRAND = _re.search(r'<a class="brand".*?</a>', _src, _re.S).group(0).replace('href="../index.html"', 'href="index.html"')

FAQS = [
 ("Does Hevify Labs work with businesses outside Ahmedabad?",
  "Yes. Hevify Labs is based in Ahmedabad and most of its early clients are local, but delivery is remote-first — we work with brands across India and internationally over WhatsApp, calls and shared dashboards."),
 ("Do I need to sign a long-term contract?",
  "No fixed lock-in. Plans run monthly, and you can move between packages as your needs change. We'd rather earn a renewal every month than hold you to a contract."),
 ("Can I combine multiple services into one plan?",
  "Yes — that's exactly what the Custom Mix Plan is for. Combine performance marketing, social media, SEO &amp; GEO, website work or AI automation into a single package quoted around your goals, not a fixed tier."),
 ("What happens if I want to pause or cancel?",
  "Tell us before the next billing cycle and we'll pause or close out the account — no penalty, no retention calls. Any creative or content already made for you is yours to keep."),
 ("Will I have one point of contact, or a rotating team?",
  "One point of contact who knows your account, backed by the specialists actually doing the work (ads, content, SEO, dev) — not a rotating account manager who has to catch up every time you message."),
 ("How do I actually get started?",
  "Message us on WhatsApp with a short line about your business. We'll set up a free discovery call, understand your goals and current numbers, then recommend the package that actually fits — no obligation."),
 ("Do you sign an NDA or keep business data confidential?",
  "Yes, on request — happy to sign one before any account access, ad accounts, or business data is shared."),
 ("Does Hevify Labs work with any industry, or just a few?",
  "We work across industries — healthcare, real estate, D2C, education, hospitality and local services are the most common, but the underlying process (tracking, transparent pricing, honest timelines) applies regardless of sector."),
]

SCHEMA = {
  "@context":"https://schema.org","@graph":[
    {"@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":"https://hevify.in/"},
      {"@type":"ListItem","position":2,"name":"FAQ"}]},
    {"@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQS]}
  ]}

faq_html = "".join(
    '<details%s><summary>%s</summary><p>%s</p></details>' % (' open' if i==0 else '', q, a)
    for i,(q,a) in enumerate(FAQS)
)

HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FAQs — Working With Hevify Labs | Ahmedabad Marketing Agency</title>
<meta name="description" content="Common questions about working with Hevify Labs — contracts, combining services, confidentiality, getting started, and who you'll actually work with.">
<meta name="keywords" content="Hevify Labs FAQ, working with a marketing agency, marketing agency questions, Hevify Labs Ahmedabad">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://hevify.in/faq.html">
<meta property="og:type" content="website"><meta property="og:title" content="FAQs — Working With Hevify Labs">
<meta property="og:description" content="Contracts, combining services, confidentiality, getting started — answered plainly.">
<meta property="og:url" content="https://hevify.in/faq.html">
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
<p class="crumb"><a href="index.html">Home</a> / FAQ</p>
<h1>Questions people ask <span class="serif">before</span> they sign up.</h1>
<p class="sub">Service-specific pricing questions live on each service page. These are the broader ones — how we work, not what it costs.</p>
<div class="faqb reveal" style="margin-top:30px">{faqhtml}</div>
<div class="cta reveal"><h2>Still have a <span class="serif">question</span>?</h2><p>Message us directly — real answers, no ticket queue.</p><a class="btn" href="https://wa.me/919429428270?text=Hi%20Hevify%20Labs%2C%20I%20have%20a%20question." target="_blank" rel="noopener">Message us on WhatsApp →</a></div>
<div class="rel"><h4>Related</h4>
<a href="performance-marketing-agency-ahmedabad.html">Performance Marketing — pricing &amp; FAQs →</a>
<a href="social-media-marketing-agency-ahmedabad.html">Social Media Marketing — pricing &amp; FAQs →</a>
<a href="seo-geo-agency-ahmedabad.html">SEO &amp; GEO — pricing &amp; FAQs →</a>
<a href="founder-vrushank-soni.html">About the founder →</a>
</div>
</div>
<footer class="foot">© 2026 Hevify Labs · Performance marketing &amp; social media agency, Ahmedabad, India.</footer>
</body></html>"""

open("faq.html", "w", encoding="utf-8").write(
    HTML.format(schema=json.dumps(SCHEMA, ensure_ascii=False), brand=BRAND, faqhtml=faq_html)
)
print("wrote faq.html with", len(FAQS), "distinct FAQs")
