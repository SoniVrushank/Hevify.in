# -*- coding: utf-8 -*-
# Run from anywhere — this script always operates relative to the repo root.
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

# Generator for standalone service landing pages (root level, alongside index.html).
# Mirrors build_blogs.py's pattern/design system so everything stays visually consistent.
import html, json, os

import re as _re
_src = open("build/build_blogs.py", encoding="utf-8").read()
BRAND = _re.search(r'<a class="brand".*?</a>', _src, _re.S).group(0).replace('href="../index.html"', 'href="index.html"')


HEAD = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://hevify.in/{slug}.html">
<meta property="og:type" content="website"><meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}"><meta property="og:url" content="https://hevify.in/{slug}.html">
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
<p class="crumb"><a href="index.html">Home</a> / {h1_plain}</p>
<h1>{h1}</h1>
<p class="sub">{sub}</p>
<div class="tldr reveal"><h2>Quick answer</h2><p>{tldr}</p></div>
<div class="key">{keys}</div>
{body}
<div class="pkgwrap reveal"><h2>Packages</h2><div class="pkgrow">{tiers}</div><p class="pkgnote">Every plan includes free extras — that's our promise. <a href="hevify-brochure.pdf" target="_blank" rel="noopener">Full plan details in our brochure (PDF) →</a></p><a class="btn" href="https://wa.me/919429428270?text=Hi%20Hevify%20Labs%2C%20I%20want%20to%20discuss%20my%20requirements." target="_blank" rel="noopener">Message us on WhatsApp →</a></div>
<h2 class="h2">Frequently asked questions</h2><div class="faqb reveal">{faqhtml}</div>
<div class="cta reveal"><h2>Want this done <span class="serif">for you</span>?</h2><p>Hevify Labs builds and runs this for brands in Ahmedabad, across India and globally.</p><a class="btn" href="https://wa.me/919429428270?text=Hi%20Hevify%20Labs%2C%20I%20want%20to%20discuss%20my%20requirements." target="_blank" rel="noopener">Message us on WhatsApp →</a></div>
<div class="rel"><h4>Explore more</h4>{rel}</div>
</div>
<footer class="foot">© 2026 Hevify Labs · Performance marketing &amp; social media agency, Ahmedabad, India.</footer>
</body></html>"""

def schema_for(p):
    return json.dumps({
      "@context":"https://schema.org","@graph":[
        {"@type":"BreadcrumbList","itemListElement":[
          {"@type":"ListItem","position":1,"name":"Home","item":"https://hevify.in/"},
          {"@type":"ListItem","position":2,"name":p["h1_plain"]}]},
        {"@type":"Service","name":p["h1_plain"],"serviceType":p["h1_plain"],
         "provider":{"@id":"https://hevify.in/#organization"},"areaServed":p.get("area","India"),
         "description":p["desc"],"url":"https://hevify.in/"+p["slug"]+".html"},
        {"@type":"FAQPage","mainEntity":[
          {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faqs"]]}
      ]}, ensure_ascii=False)

def tiers_html(p):
    if not p.get("tiers"):
        return '<div class="pkg hi"><span class="pn">Custom Quote</span><span class="pa">Free discovery call</span></div>'
    return "".join(
        '<div class="pkg%s"><span class="pn">%s</span><span class="pa">%s<small>/mo</small></span></div>' % (
            " hi" if t.get("hi") else "", html.escape(t["name"]), html.escape(t["amt"])
        ) for t in p["tiers"]
    )

def render(p, related):
    keys = "".join("<span>%s</span>"%html.escape(k) for k in p["keywords_chips"])
    faqhtml = "".join("<details%s><summary>%s</summary><p>%s</p></details>"%(" open" if i==0 else "", html.escape(q), html.escape(a)) for i,(q,a) in enumerate(p["faqs"]))
    rel = "".join('<a href="%s">%s →</a>'%(href,label) for href,label in related)
    return HEAD.format(title=p["title"],desc=p["desc"],kw=p["kw"],slug=p["slug"],schema=schema_for(p),
        brand=BRAND,h1_plain=p["h1_plain"],h1=p["h1"],sub=p["sub"],tldr=p["tldr"],keys=keys,
        body=p["body"],tiers=tiers_html(p),faqhtml=faqhtml,rel=rel)

PAGES = []

PAGES.append(dict(
 slug="performance-marketing-agency-ahmedabad",
 title="Performance Marketing Agency in Ahmedabad | Hevify Labs",
 desc="Performance marketing agency in Ahmedabad running Meta & Google Ads, retargeting and lead funnels. Packages from ₹8,000/mo. Real ROI, not just reports.",
 kw="performance marketing agency Ahmedabad, best performance marketing agency Ahmedabad, Meta ads agency Ahmedabad, Google Ads agency Ahmedabad, PPC agency Ahmedabad, lead generation agency Ahmedabad",
 keywords_chips=["performance marketing","Meta Ads","Google Ads","retargeting","lead funnels"],
 h1_plain="Performance Marketing Agency in Ahmedabad",
 h1='Performance Marketing Agency in Ahmedabad — <span class="serif">Ads That Pay for Themselves</span>',
 sub="Meta Ads, Google Ads, retargeting and lead funnels — built around one number you actually care about.",
 tldr="Hevify Labs runs performance marketing for brands in Ahmedabad — Meta Ads, Google Ads, retargeting and lead funnels, tracked end-to-end so every rupee is accountable. Packages start at ₹8,000/mo; ad spend is billed separately so you stay in control of your budget.",
 area="Ahmedabad",
 body="""
<h2 class="h2">What's included</h2>
<div class="feat-grid">
<div class="feat"><h3>Meta Ads</h3><p>Facebook & Instagram campaigns built around a clear offer and audience, not just boosted posts.</p></div>
<div class="feat"><h3>Google Ads</h3><p>Search campaigns that catch high-intent buyers actively looking for what you sell.</p></div>
<div class="feat"><h3>Retargeting</h3><p>Bring back the visitors who didn't convert the first time, at a fraction of cold-traffic cost.</p></div>
<div class="feat"><h3>Lead funnels &amp; tracking</h3><p>Landing pages and conversion tracking wired together so you can see exactly what's working.</p></div>
</div>
<h2 class="h2">Why Ahmedabad brands work with us</h2>
<p class="body-p">12+ brands scaled, 3.8× average ROI, 95% client retention. We report against the number that actually matters to your business — not reach or impressions.</p>
""",
 tiers=[{"name":"Starter","amt":"₹7,999"},{"name":"★ Growth","amt":"₹11,999","hi":True},{"name":"Premium","amt":"₹15,999"}],
 faqs=[
   ("How much does performance marketing cost in Ahmedabad?","Hevify Labs packages start at ₹8,000/mo for Performance Marketing, and ₹14,000/mo for the full package. Ad spend is billed separately so you control your own budget."),
   ("How soon will I see results?","Paid ads typically show signal within the first few weeks. We set clear expectations upfront and report against the metrics that matter to your business."),
   ("Do you manage the ad spend directly?","Yes — full campaign management across Meta and Google, with transparent reporting on where every rupee went."),
 ]))

PAGES.append(dict(
 slug="social-media-marketing-agency-ahmedabad",
 title="Social Media Marketing Agency in Ahmedabad | Hevify Labs",
 desc="Social media marketing agency in Ahmedabad for reels, content calendars, captions and community management. Packages from ₹10,000/mo, consistent every week.",
 kw="social media marketing agency Ahmedabad, best social media marketing agency Ahmedabad, Instagram marketing agency Ahmedabad, reels content agency, social media agency Ahmedabad",
 keywords_chips=["social media marketing","Instagram","reels strategy","content calendar","community"],
 h1_plain="Social Media Marketing Agency in Ahmedabad",
 h1='Social Media Marketing Agency in Ahmedabad — <span class="serif">Grow Without the Guesswork</span>',
 sub="Content planning, reels, captions and community — consistent and on-brand, every single week.",
 tldr="Hevify Labs plans, creates and manages social media for brands across Ahmedabad — reels strategy, content calendars, captions and community, delivered consistently every week. Packages start at ₹10,000/mo.",
 area="Ahmedabad",
 body="""
<h2 class="h2">What's included</h2>
<div class="feat-grid">
<div class="feat"><h3>Reels strategy</h3><p>Hooks, pacing and formats built for reach — tested in volume, not guessed.</p></div>
<div class="feat"><h3>Content calendar</h3><p>Planned weekly around clear content pillars, so consistency isn't left to motivation.</p></div>
<div class="feat"><h3>Captions &amp; copy</h3><p>On-brand voice across every post, written to actually get read.</p></div>
<div class="feat"><h3>Community management</h3><p>Comments and DMs handled so no lead or conversation goes cold.</p></div>
</div>
<h2 class="h2">Platforms we manage</h2>
<p class="body-p">Instagram, Facebook and LinkedIn — tailored to where your audience actually is, not every platform at once for its own sake.</p>
""",
 tiers=[{"name":"Starter","amt":"₹9,999"},{"name":"★ Growth","amt":"₹14,999","hi":True},{"name":"Premium","amt":"₹19,999"}],
 faqs=[
   ("What's included in the ₹10,000/mo package?","Content planning, reels, captions, community management and profile optimisation, with a consistent weekly presence."),
   ("Which platforms do you manage?","Instagram, Facebook and LinkedIn, tailored to where your audience actually is."),
   ("Who owns the content after the contract ends?","You do — all creative and copy produced for your brand is yours to keep."),
 ]))

PAGES.append(dict(
 slug="seo-geo-agency-ahmedabad",
 title="SEO & GEO Agency in Ahmedabad | Hevify Labs",
 desc="SEO and GEO (AI search) agency in Ahmedabad. Rank on Google and get recommended by ChatGPT, Gemini and Perplexity. Packages from ₹6,000/mo.",
 kw="SEO agency Ahmedabad, best SEO agency Ahmedabad, GEO agency Ahmedabad, local SEO Ahmedabad, AI search optimization agency, generative engine optimization Ahmedabad",
 keywords_chips=["SEO","GEO","local SEO","AI search visibility","structured data"],
 h1_plain="SEO & GEO Agency in Ahmedabad",
 h1='SEO &amp; GEO Agency in Ahmedabad — <span class="serif">Get Found, Everywhere People Search</span>',
 sub="Rank on Google, and get recommended when people ask ChatGPT, Gemini or Perplexity.",
 tldr="Hevify Labs handles both sides of search — traditional SEO to rank on Google, and GEO (Generative Engine Optimization) to get recommended inside AI answers. Packages start at ₹6,000/mo.",
 area="Ahmedabad",
 body="""
<h2 class="h2">What's included</h2>
<div class="feat-grid">
<div class="feat"><h3>Technical &amp; on-page SEO</h3><p>Titles, meta, structure, internal linking and site speed fixed properly.</p></div>
<div class="feat"><h3>Local SEO</h3><p>Google Business Profile, local keywords and citations to rank in the Ahmedabad map pack.</p></div>
<div class="feat"><h3>GEO (AI search)</h3><p>Answer-first content and structured data so AI tools can find, quote and recommend you.</p></div>
<div class="feat"><h3>Structured data</h3><p>Organization, LocalBusiness and FAQ schema — the same markup that powers rich results.</p></div>
</div>
<h2 class="h2">Why SEO and GEO together</h2>
<p class="body-p">Search is splitting into two channels — Google's links and AI-generated answers. Ranking in one but not the other means half your future customers can't find you.</p>
""",
 tiers=[{"name":"Starter","amt":"₹5,999"},{"name":"★ Growth","amt":"₹9,999","hi":True},{"name":"Premium","amt":"₹13,999"}],
 faqs=[
   ("What is GEO and do I need it?","GEO (Generative Engine Optimization) helps AI tools like ChatGPT, Gemini and Perplexity recommend your brand when people ask them questions. As search shifts toward AI answers, GEO works alongside traditional SEO to keep you visible."),
   ("How long until I see ranking movement?","SEO and GEO typically build over 3–6 months. We set clear expectations and report against the metrics that matter to your business."),
   ("What's the difference between SEO and GEO?","SEO ranks you in Google's search results; GEO gets you cited inside AI-generated answers. They overlap heavily but GEO puts extra weight on clear, quotable, factual content."),
 ]))

PAGES.append(dict(
 slug="ai-automation-agency",
 title="AI Automation Agency | Agentic AI for Business — Hevify Labs",
 desc="Custom AI agents that automate lead follow-ups, reporting and scheduling. Free discovery call to scope your automation.",
 kw="AI automation agency India, agentic AI for small business, AI lead follow-up automation, AI agents for business, WhatsApp automation agency",
 keywords_chips=["AI automation","agentic AI","lead follow-up","reporting","scheduling"],
 h1_plain="AI Automation & Agentic AI Builds",
 h1='AI Automation &amp; Agentic AI Builds — <span class="serif">Give Your Team Its Time Back</span>',
 sub="Custom AI agents that handle the repeat work, so your team spends time on growth instead of busywork.",
 tldr="Hevify Labs builds custom AI agents that handle repeat work — lead follow-ups, reporting, scheduling — so your team spends time on growth instead of busywork. Custom scope, starting with a free discovery call.",
 area="India",
 body="""
<h2 class="h2">What we build</h2>
<div class="feat-grid">
<div class="feat"><h3>Lead follow-ups</h3><p>Instant, on-brand replies via WhatsApp so leads never go cold waiting on a human.</p></div>
<div class="feat"><h3>Reporting</h3><p>Automated weekly summaries pulled straight from your ad accounts and CRM.</p></div>
<div class="feat"><h3>Scheduling</h3><p>Booking and reminder agents that cut the back-and-forth out of setting appointments.</p></div>
<div class="feat"><h3>Custom builds</h3><p>Scoped to your specific workflow — not a one-size-fits-all bot.</p></div>
</div>
<h2 class="h2">How it starts</h2>
<p class="body-p">A free discovery call to understand the repeat work costing your team the most time, then a scoped build with a clear price before anything starts.</p>
""",
 tiers=None,
 faqs=[
   ("What kind of businesses is this for?","Any business with repeat manual work — lead follow-up, reporting or scheduling — that a well-built AI agent can take off your team's plate."),
   ("How is pricing decided?","Every build is scoped individually on a free discovery call, based on the workflow and integrations involved, with a clear price agreed before work starts."),
   ("Do I need existing tools like a CRM?","It helps but isn't required — we can work with what you already use, or recommend a lightweight setup."),
 ]))

order = {p["slug"]: p["h1_plain"] for p in PAGES}
slugs = list(order.keys())
for i, p in enumerate(PAGES):
    others = [(slugs[(i+1)%4]+".html", order[slugs[(i+1)%4]]),
              (slugs[(i+2)%4]+".html", order[slugs[(i+2)%4]]),
              (slugs[(i+3)%4]+".html", order[slugs[(i+3)%4]])]
    open("%s.html"%p["slug"], "w", encoding="utf-8").write(render(p, others))
    print("wrote %s.html"%p["slug"])
print("done", len(PAGES))
