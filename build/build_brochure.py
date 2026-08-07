# -*- coding: utf-8 -*-
# Run from anywhere — this script always operates relative to the repo root.
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import re

src = open("build_blogs.py", encoding="utf-8").read()
BRAND_IMG = re.search(r'<img src="(data:image/webp;base64,[^"]+)"', src).group(1)

CSS = """
@page { size: A4; margin: 0; }
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',system-ui,sans-serif;color:#111113}
.page{width:1034px;height:1462px;padding:74px 78px;page-break-after:always;position:relative;overflow:hidden}
.page:last-child{page-break-after:auto}
.dots{position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,.09) 1px,transparent 1px);background-size:16px 16px;z-index:0}
.dots.lt{background-image:radial-gradient(circle,rgba(17,17,19,.10) 1px,transparent 1px)}
.rel{position:relative;z-index:1;height:100%;display:flex;flex-direction:column}
.serif{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400}
.mono{font-family:'IBM Plex Mono',monospace}

/* COVER */
.cover{background:#111113;color:#fff}
.cover .kicker{font-family:'IBM Plex Mono',monospace;font-size:10.5px;letter-spacing:.18em;color:#c9c9cc;text-align:center;text-transform:uppercase;margin-top:29px}
.cover .mid{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.cover .logo{width:74px;height:74px;border-radius:50%;background:linear-gradient(135deg,#DDEE8C 0%,#8FB63A 55%,#5F7F1E 100%);display:flex;align-items:center;justify-content:center;margin-bottom:11px;box-shadow:0 6px 22px rgba(0,0,0,.35)}
.cover .logo span{font-family:'Instrument Serif',Georgia,serif;font-style:italic;color:#fff;font-size:34px;font-weight:400}
.cover .word{font-weight:800;font-size:14px;letter-spacing:.14em;margin-bottom:34px}
.cover .word b{color:#C6F24E;font-weight:800}
.cover h1{font-size:46px;line-height:1.1;font-weight:800;letter-spacing:-.01em}
.cover h1 .accent{color:#8FC93A;font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400}
.cover .tag{color:#9a9aa2;font-size:13px;margin-top:20px;letter-spacing:.01em}
.cover .foot{text-align:center;color:#8a8a90;font-size:11.5px;padding-top:10px;border-top:1px solid #29292c;margin-bottom:20px}

/* CONTENT HEADER / FOOTER */
.hdr{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #DEDCCF;padding-bottom:9px;margin-bottom:39px}
.hdr .b{display:flex;align-items:center;gap:7px;font-weight:800;font-size:13px}
.hdr .b img{width:19px;height:19px;border-radius:6px}
.hdr .b b{color:#7CA82A}
.hdr .r{font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:.1em;color:#8a8a80;text-transform:uppercase}
.pfoot{margin-top:auto;display:flex;justify-content:space-between;font-family:'IBM Plex Mono',monospace;font-size:9px;color:#a3a396;border-top:1px solid #E4E2D5;padding-top:8px}

h2.title{font-size:23px;font-weight:800;letter-spacing:-.01em;line-height:1.25}
h2.title .accent{color:#7CA82A;font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400}
p.lead{color:#6b6b62;font-size:11.5px;max-width:82%;margin:6px 0 12px}

/* STATS ROW */
.statrow{display:flex;border-top:1px solid #DEDCCF;border-bottom:1px solid #DEDCCF;padding:11px 0;margin-bottom:39px}
.statrow div{flex:1}
.statrow strong{display:block;font-size:20px;font-weight:800}
.statrow span{font-size:9.5px;color:#7a7a70}

.lbl{font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:.12em;color:#7CA82A;text-transform:uppercase;margin-bottom:8px;font-weight:600}

/* WHY CHOOSE US grid */
.whygrid{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:39px}
.whycard{width:calc(33.333% - 4px);border:1px solid #E4E2D5;border-radius:11px;padding:14px 8px;text-align:center;font-size:11px;font-weight:700}
.whycard:nth-child(2n){background:#EFEDDD}
.whycard:not(:nth-child(2n)){background:#fff}
.whycard i{display:block;width:26px;height:26px;border-radius:50%;background:#DCE6BE;margin:0 auto 8px;font-style:normal;line-height:26px;font-size:12px}

/* HOW WE WORK */
.steprow{display:flex;gap:14px;margin-bottom:39px}
.steprow div{flex:1;padding-left:9px;border-left:2px solid #C6F24E}
.steprow i{font-family:'Instrument Serif',Georgia,serif;font-style:italic;color:#7CA82A;font-size:13px}
.steprow b{display:block;font-size:11.5px;margin:2px 0 3px}
.steprow p{font-size:9.5px;color:#7a7a70}

/* SERVICES LIST */
.svcrow{display:flex;justify-content:space-between;align-items:center;border-radius:11px;padding:11px 16px;margin-bottom:6px;font-size:12px;font-weight:700}
.svcrow:nth-child(odd){background:#fff;border:1px solid #E4E2D5}
.svcrow:nth-child(even){background:#EFEDDD;border:1px solid #E4E2D5}
.svcrow.new{background:#fff;border:1.5px dashed #7CA82A}
.svcrow .l{display:flex;align-items:center;gap:10px}
.svcrow i{width:22px;height:22px;border-radius:50%;background:#DCE6BE;display:inline-flex;align-items:center;justify-content:center;font-style:normal;font-size:11px}
.svcrow small{font-family:'IBM Plex Mono',monospace;font-weight:500;color:#9a9a90;font-size:10px}
.svcrow .tag{font-family:'IBM Plex Mono',monospace;font-size:8.5px;color:#7CA82A;border:1px solid #7CA82A;border-radius:100px;padding:2px 7px;margin-left:8px}

/* PRICING PAGES */
.pricehead{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:39px}
.pricehead h2{font-size:25px;font-weight:800}
.pricehead .sub{font-family:'Instrument Serif',Georgia,serif;font-style:italic;color:#6b6b62;font-size:13px}
table.pricing{width:100%;border-collapse:collapse;border:1px solid #E4E2D5;border-radius:12px;overflow:hidden;font-size:10px;margin-bottom:30px}
table.pricing th{background:#EFEDDD;padding:12px 8px;text-align:center;font-size:12px;border-bottom:2px solid #111113}
table.pricing th.star{color:#7CA82A}
table.pricing th .amt{display:block;font-size:17px;font-weight:800;color:#111113;margin-top:2px}
table.pricing td{padding:8px 8px;border-bottom:1px solid #EAE8DB;text-align:center;color:#3a3a35}
table.pricing td.feat{text-align:left;color:#6b6b62;font-weight:600;font-size:10px}
table.pricing tr:nth-child(even) td{background:#FAFAF2}
table.pricing tr.free td{background:#EAF3D3;font-weight:700;color:#4d6b18;font-size:9.5px}
.note{font-size:9.5px;color:#6b6b62;background:#fff;border:1px solid #E4E2D5;border-radius:9px;padding:9px 13px;display:flex;gap:8px;align-items:flex-start}
.note b{color:#111113}

/* CUSTOM QUOTED PAGE */
.customrow{display:flex;gap:14px;margin-bottom:30px}
.customrow .c{flex:1;background:#fff;border:1px solid #E4E2D5;border-radius:13px;padding:16px}
.customrow .n{font-family:'IBM Plex Mono',monospace;color:#7CA82A;font-size:11px;font-weight:700;margin-bottom:5px}
.customrow h3{font-size:15px;margin-bottom:6px}
.customrow p{font-size:10px;color:#6b6b62;margin-bottom:10px}
.customrow .q{color:#7CA82A;font-weight:800;font-size:11.5px;margin-bottom:8px}
.customrow ul{list-style:none}
.customrow li{font-size:9.5px;padding:4px 0;border-bottom:1px dotted #E4E2D5;color:#3a3a35}
.customrow .c.mix{background:#FAFCF0;border:1px solid #C6F24E}

/* CLIENTS */
.clientgrid{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:39px}
.client{width:calc(33.333% - 6px);box-sizing:border-box;background:#fff;border:1px solid #E4E2D5;border-radius:11px;padding:11px 13px;display:flex;align-items:center;gap:9px;font-size:11px;font-weight:700}
.client i{width:24px;height:24px;border-radius:50%;background:#DCE6BE;color:#4d6b18;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:11px;font-weight:800;flex:none}

/* CONTACT (dark) */
.contactwrap{margin-top:auto;background:#111113;color:#fff;border-radius:16px;padding:22px 24px}
.contactwrap h2{font-size:22px;font-weight:800;margin-bottom:5px}
.contactwrap h2 .accent{color:#C6F24E;font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400}
.contactwrap p.lead2{color:#a5a5aa;font-size:11px;margin-bottom:16px}
.cgrid{display:flex;flex-wrap:wrap;gap:9px;margin-bottom:14px}
.citem{width:calc(50% - 5px);box-sizing:border-box;background:#1c1c1f;border-radius:10px;padding:11px 13px}
.citem .l{font-family:'IBM Plex Mono',monospace;font-size:8.5px;color:#9a9aa0;text-transform:uppercase;letter-spacing:.06em;margin-bottom:3px}
.citem .v{font-size:12px;font-weight:700}
.qrrow{display:flex;align-items:center;gap:12px}
.qrbox{width:52px;height:52px;background:#fff;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:9px;color:#111;font-weight:700;text-align:center}
.qrrow p{font-size:10px;color:#a5a5aa}
"""

def hdr(section):
    return f'<div class="hdr"><div class="b"><img src="{BRAND_IMG}">HEVIFY <b>LABS</b></div><div class="r">{section}</div></div>'

def foot(n):
    return f'<div class="pfoot"><span>Services &amp; Pricing Guide · 2026</span><span>{n:02d} — 07</span></div>'

pages = []

# PAGE 1 — COVER (unchanged from original, just re-set to match precisely)
pages.append(f"""<div class="page cover"><div class="dots"></div><div class="rel">
<div class="kicker">Services &amp; Pricing Guide · 2026</div>
<div class="mid">
<div class="logo"><span>hv</span></div>
<div class="word">HEVIFY <b>LABS</b></div>
<h1>Helping Businesses<br>Grow <span class="accent">Online</span>.</h1>
<div class="tag">Digital Marketing · SEO · Website Development · AI Automation</div>
</div>
<div class="foot">hevify.in &nbsp;·&nbsp; WhatsApp +91 94294 28270 &nbsp;·&nbsp; Ahmedabad, India</div>
</div></div>""")

# PAGE 2 — ABOUT & SERVICES (added: Custom Mix Plan as an 8th simple row, marked NEW)
pages.append(f"""<div class="page"><div class="dots lt"></div><div class="rel">
{hdr("01 · About &amp; Services")}
<h2 class="title">Helping businesses build a <span class="accent">stronger digital presence</span>.</h2>
<p class="lead">We help startups, SMEs, restaurants, doctors, retailers and growing businesses grow online — real results, not just reports.</p>
<div class="statrow">
<div><strong>12+</strong><span>Brands Scaled</span></div>
<div><strong>3.8×</strong><span>Average ROI</span></div>
<div><strong>95%</strong><span>Retention</span></div>
<div><strong>8</strong><span>Services, One Partner</span></div>
</div>
<div class="lbl">Why choose us</div>
<div class="whygrid">
<div class="whycard"><i>$</i>Affordable &amp; Transparent</div><div class="whycard"><i>✦</i>Creative Strategies</div><div class="whycard"><i>◎</i>Performance Focused</div>
<div class="whycard"><i>ai</i>AI Powered</div><div class="whycard"><i>♥</i>Dedicated Support</div><div class="whycard"><i>⚙</i>Custom Solutions</div>
</div>
<div class="lbl">How we work</div>
<div class="steprow">
<div><i>i.</i><b>Discover</b><p>A free call on your goals.</p></div>
<div><i>ii.</i><b>Strategy</b><p>A plan built around outcomes.</p></div>
<div><i>iii.</i><b>Execute</b><p>Shipped weekly, on brand.</p></div>
<div><i>iv.</i><b>Scale</b><p>Double down, report clearly.</p></div>
</div>
<div class="lbl">Our services — 8, each quoted separately</div>
<div class="svcrow"><span class="l"><i>◷</i>Social Media Management</span><small>p.03</small></div>
<div class="svcrow"><span class="l"><i>↗</i>Performance Marketing</span><small>p.04</small></div>
<div class="svcrow"><span class="l"><i>⌕</i>SEO &amp; GEO</span><small>p.05</small></div>
<div class="svcrow"><span class="l"><i>&lt;/&gt;</i>Website Development</span><small>p.06</small></div>
<div class="svcrow"><span class="l"><i>ai</i>AI Automation</span><small>p.06</small></div>
<div class="svcrow"><span class="l"><i>◐</i>Branding &amp; Creative</span><small>p.06</small></div>
<div class="svcrow"><span class="l"><i>▤</i>Content Production</span><small>p.06</small></div>
<div class="svcrow new"><span class="l"><i>★</i>Custom Mix Plan — build your own<span class="tag">NEW</span></span><small>p.06</small></div>
{foot(2)}
</div></div>""")

# PAGE 3 — SOCIAL MEDIA
pages.append(f"""<div class="page"><div class="dots lt"></div><div class="rel">
{hdr("02 · Pricing — Social Media")}
<div class="pricehead"><h2>Social Media Management</h2><span class="sub">Consistent, on-brand content — every week.</span></div>
<table class="pricing">
<tr><th class="feat"></th><th>Starter<span class="amt">₹9,999</span>/mo</th><th class="star">★ Growth<span class="amt">₹14,999</span>/mo</th><th>Premium<span class="amt">₹19,999</span>/mo</th></tr>
<tr><td class="feat">Content Pieces / month</td><td>6 Posts + 2 Reels</td><td>6 Posts + 4 Reels</td><td>6 Posts + 4 Reels</td></tr>
<tr><td class="feat">Reel Concepts</td><td>—</td><td>—</td><td>4 Custom Concepts</td></tr>
<tr><td class="feat">Content Planning &amp; Calendar</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr><td class="feat">Creative Design Quality</td><td>Standard</td><td>Premium</td><td>Premium</td></tr>
<tr><td class="feat">Caption &amp; Hashtag Research</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr><td class="feat">Profile Optimisation</td><td>Basic</td><td>Full</td><td>Full</td></tr>
<tr><td class="feat">Community Management</td><td>—</td><td>✓</td><td>Advanced</td></tr>
<tr><td class="feat">Analytics &amp; Reporting</td><td>Monthly</td><td>Detailed</td><td>Advanced Dashboard</td></tr>
<tr><td class="feat">Strategy Call</td><td>—</td><td>Monthly</td><td>Monthly Consultation</td></tr>
<tr><td class="feat">Support</td><td>WhatsApp</td><td>Priority</td><td>Priority</td></tr>
<tr class="free"><td class="feat">Free with plan</td><td>1-Week Sponsored Promotion</td><td>+ Profile Optimisation + Competitor Analysis</td><td>+ Monthly Growth Consultation</td></tr>
</table>
<div class="note">🎁 <span>Sponsored promotion uses <b>1 selected creative</b>, ad spend covered by Hevify — a free trial of what paid ads can do for you.</span></div>
{foot(3)}
</div></div>""")

# PAGE 4 — PERFORMANCE MARKETING
pages.append(f"""<div class="page"><div class="dots lt"></div><div class="rel">
{hdr("03 · Pricing — Performance Marketing")}
<div class="pricehead"><h2>Performance Marketing</h2><span class="sub">Meta &amp; Google Ads that pay back.</span></div>
<table class="pricing">
<tr><th class="feat"></th><th>Starter<span class="amt">₹7,999</span>/mo</th><th class="star">★ Growth<span class="amt">₹11,999</span>/mo</th><th>Premium<span class="amt">₹15,999</span>/mo</th></tr>
<tr><td class="feat">Meta Ads Management</td><td>✓</td><td>✓</td><td>Advanced</td></tr>
<tr><td class="feat">Google Ads</td><td>—</td><td>If Suitable</td><td>Full</td></tr>
<tr><td class="feat">Campaign Management</td><td>Single</td><td>Multi-Campaign</td><td>Full-Funnel</td></tr>
<tr><td class="feat">A/B Testing &amp; Retargeting</td><td>—</td><td>✓</td><td>Advanced</td></tr>
<tr><td class="feat">Conversion Tracking</td><td>—</td><td>✓</td><td>✓</td></tr>
<tr><td class="feat">Optimisation</td><td>Monthly</td><td>Weekly</td><td>Weekly + Strategy Meeting</td></tr>
<tr><td class="feat">Social Media Posts / month</td><td>4</td><td>6</td><td>8</td></tr>
<tr><td class="feat">Google Business Profile</td><td>Optimisation</td><td>+ 4 Posts/mo</td><td>Full Management + Reputation</td></tr>
<tr class="free"><td class="feat">Free with plan</td><td>Campaign Audit + Best-Platform Recommendation</td><td>+ Audience Research + Landing Page Suggestions</td><td>+ Landing Page Review + CRO Suggestions</td></tr>
</table>
<div class="note">ⓘ <span><b>Ad spend is paid separately by you</b>, directly to Meta/Google. Not sure which platform fits your business? That recommendation is free, even before you sign up.</span></div>
{foot(4)}
</div></div>""")

# PAGE 5 — SEO & GEO
pages.append(f"""<div class="page"><div class="dots lt"></div><div class="rel">
{hdr("04 · Pricing — SEO &amp; GEO")}
<div class="pricehead"><h2>SEO &amp; GEO</h2><span class="sub">Found on Google — and on AI search.</span></div>
<table class="pricing">
<tr><th class="feat"></th><th>Starter<span class="amt">₹5,999</span>/mo</th><th class="star">★ Growth<span class="amt">₹9,999</span>/mo</th><th>Premium<span class="amt">₹13,999</span>/mo</th></tr>
<tr><td class="feat">Keyword Research</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr><td class="feat">On-Page SEO</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr><td class="feat">Google Business Optimisation</td><td>✓</td><td>+ 4 Posts/mo</td><td>Full</td></tr>
<tr><td class="feat">Technical SEO Audit</td><td>✓</td><td>Full Technical SEO</td><td>Advanced</td></tr>
<tr><td class="feat">Local SEO</td><td>—</td><td>✓</td><td>✓</td></tr>
<tr><td class="feat">Blog Optimisation</td><td>—</td><td>✓</td><td>+ Content Strategy</td></tr>
<tr><td class="feat">Competitor Analysis</td><td>—</td><td>✓</td><td>✓</td></tr>
<tr><td class="feat">AI Search Optimisation (GEO)</td><td>—</td><td>—</td><td>✓</td></tr>
<tr><td class="feat">Backlink Strategy</td><td>—</td><td>—</td><td>✓</td></tr>
<tr class="free"><td class="feat">Free with plan</td><td>SEO Audit Report</td><td>+ Competitor SEO Report + Keyword Opportunity Report</td><td>+ 30-Day Keyword Roadmap</td></tr>
</table>
<div class="note">✦ <span><b>GEO</b> (Generative Engine Optimisation) helps AI tools like ChatGPT, Gemini and Perplexity recommend your business when people ask.</span></div>
{foot(5)}
</div></div>""")

# PAGE 6 — CUSTOM-QUOTED SERVICES (added: Custom Mix Plan as a simple 3rd fitted card)
pages.append(f"""<div class="page"><div class="dots lt"></div><div class="rel">
{hdr("05 · Custom-Quoted Services")}
<h2 class="title">Three more ways we build <span class="accent">growth infrastructure</span>.</h2>
<p class="lead">Not every service fits a fixed plan. Here's what's included — each one scoped and quoted around your exact needs after a free discovery call.</p>
<div class="customrow">
<div class="c"><div class="n">01</div><h3>Website Development</h3><p>Fast, SEO-ready websites built to convert visitors into enquiries — designed around how your customers actually search, browse and book.</p><div class="q">Custom Quote</div>
<ul><li>Business Websites</li><li>Landing Pages</li><li>Portfolio Sites</li><li>E-Commerce</li><li>Booking Systems</li><li>SEO Ready</li><li>Fast Loading</li><li>Maintenance Plans</li></ul></div>
<div class="c"><div class="n">02</div><h3>AI Automation</h3><p>Custom AI agents that automate lead follow-up, reporting and scheduling — so your team spends less time on busywork and more time on growth.</p><div class="q">Custom Quote</div>
<ul><li>WhatsApp Automation</li><li>Lead Capture</li><li>CRM Automation</li><li>Email Automation</li><li>AI Chatbot</li><li>Custom Integrations</li><li>Dashboards &amp; Reporting</li><li>Workflow Agents</li></ul></div>
<div class="c mix"><div class="n">★ NEW</div><h3>Custom Mix Plan</h3><p>Most businesses don't fit one plan neatly. Combine pieces from any service in this guide — some ads, some social, a bit of SEO — into one package built around your goals.</p><div class="q">Custom Quote</div>
<ul><li>Mix &amp; match any service</li><li>One quote, one point of contact</li><li>Still includes free-extras promise</li><li>Scoped on a free discovery call</li></ul></div>
</div>
<div class="note">☑ <span>Every website, automation and mix-plan project <b>starts with a free discovery call</b> — no cost, no obligation.</span></div>
{foot(6)}
</div></div>""")

# PAGE 7 — CLIENTS + CONTACT (added LinkedIn + Instagram to contact grid)
CLIENTS = ["B2B One Mart","PhysioEdge","Truveda","NearMeIndia","Zero Dimensions","Provectus Corp Advisors","Swarna Shanti","Om Shanti Jewellers","Shree Shanti Jewellers","Ad Creations"]
client_html = "".join('<div class="client"><i>%s</i>%s</div>' % (c[0], c) for c in CLIENTS)
pages.append(f"""<div class="page"><div class="dots lt"></div><div class="rel">
{hdr("06 · Clients")}
<h2 class="title">Trusted by growing <span class="accent">businesses</span>.</h2>
<p class="lead">A few of the brands we've worked with — and many more to come.</p>
<div class="clientgrid">{client_html}</div>
<div class="contactwrap">
<h2>Let's discuss <span class="accent">your business</span>.</h2>
<p class="lead2">Every business is different — we'll understand your goals first, then recommend what actually fits.</p>
<div class="cgrid">
<div class="citem"><div class="l">Website</div><div class="v">hevify.in</div></div>
<div class="citem"><div class="l">WhatsApp</div><div class="v">+91 94294 28270</div></div>
<div class="citem"><div class="l">Email</div><div class="v">hevify.in@gmail.com</div></div>
<div class="citem"><div class="l">Location</div><div class="v">Ahmedabad, India</div></div>
<div class="citem"><div class="l">LinkedIn — Founder</div><div class="v">Vrushank Soni</div></div>
<div class="citem"><div class="l">Instagram — Founder</div><div class="v">@vrushh_98</div></div>
</div>
<div class="qrrow"><div class="qrbox">QR</div><p>Scan to start a WhatsApp conversation — no forms, no delays.</p></div>
</div>
{foot(7)}
</div></div>""")

open("_brochure.html","w",encoding="utf-8").write(
    "<html><head><meta charset='utf-8'><style>%s</style></head><body>%s</body></html>" % (CSS, "".join(pages))
)
print("wrote _brochure.html,", len(pages), "pages")
