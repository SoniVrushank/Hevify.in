# -*- coding: utf-8 -*-
"""
Comprehensive fix script for all remaining bugs:
1. Stars encoding (â˜… → ★)
2. Broken Instagram/LinkedIn aria-label duplication
3. Nav redesign (remove hamburger, expand pill, theme toggle outside)
4. Glass dock redesign (WhatsApp inline)
5. Blog sheet image fix
6. Theme toggle SVG simplification
"""
import os, re

BASE = r"C:\Users\Vrushh\Downloads\Companies\HV\WEB.FILES"

# ─── NAV: no hamburger, expanded pill, theme toggle separate ───────────────
def build_nav_html():
    return '''  <header class="site-nav liquid-header" aria-label="Primary navigation">
    <a class="brand" href="/" aria-label="Hevify Labs home">
      <img src="/favicon.webp" width="42" height="42" alt="Hevify Labs" class="brand-mark">
      <span><strong>Hevify</strong><small>Labs</small></span>
    </a>
    <div class="nav-shell" role="navigation" aria-label="Quick links">
      <ul id="nav-links" class="nav-links glass-pill">
        <li><a href="/#about">About</a></li>
        <li><a href="/services/">Services</a></li>
        <li><a href="/blog/">Blog</a></li>
      </ul>
    </div>
    <button class="theme-toggle liquid-toggle" type="button" aria-label="Toggle light and dark mode" title="Toggle theme">
      <span class="theme-toggle__sun" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
          <circle cx="12" cy="12" r="5"/>
          <g stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none">
            <line x1="12" y1="1" x2="12" y2="3"/>
            <line x1="12" y1="21" x2="12" y2="23"/>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
            <line x1="1" y1="12" x2="3" y2="12"/>
            <line x1="21" y1="12" x2="23" y2="12"/>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
          </g>
        </svg>
      </span>
      <span class="theme-toggle__moon" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
        </svg>
      </span>
    </button>
  </header>'''

# ─── GLASS DOCK: blog pill + WhatsApp side by side ────────────────────────
def build_glass_dock():
    return '''
  <div class="glass-dock" role="complementary" aria-label="Quick shortcuts and WhatsApp contact">
    <button class="glass-dock__pill" type="button" data-open-blog-dock aria-label="Open featured blog">
      <span class="glass-dock__spark" aria-hidden="true">&#10022;</span>
      <span class="glass-dock__content">
        <strong data-dock-title>Read: 5 AI Tools Every Marketer Should Be Using in 2025</strong>
        <small data-dock-meta">Featured blog &#183; 4 min read</small>
      </span>
      <span class="glass-dock__arrow" aria-hidden="true">&#8594;</span>
      <span class="glass-dock__progress" aria-hidden="true"><span data-dock-progress></span></span>
    </button>
    <a class="glass-dock__wa" href="https://wa.me/+919429428370?text=Hi%20Hevify%20Labs%2C%20I%20want%20to%20discuss%20my%20requirements." aria-label="Contact on WhatsApp (opens in new tab)" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true">
        <path d="M17.5 14.4c-.3-.1-1.8-.9-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-1.7-.8-2.8-1.8-3.6-3.4-.2-.3 0-.5.1-.7.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4z"/>
        <path d="M12 2.1A9.9 9.9 0 0 0 3.6 17.2l-1 3.6 3.7-1a9.9 9.9 0 1 0 5.7-17.7zm0 17.7c-1.8 0-3.5-.6-4.9-1.6l-.4-.2-2.2.6.6-2.1-.2-.4A7.8 7.8 0 1 1 12 19.8z"/>
      </svg>
    </a>
  </div>'''

# ─── BLOG SHEET: fixed image ─────────────────────────────────────────────
BLOG_SHEET_FIX = '''  <div class="glass-sheet" id="blog-sheet" aria-hidden="true">
    <div class="glass-sheet__backdrop" data-close-blog-dock></div>
    <section class="glass-sheet__panel" role="dialog" aria-modal="true" aria-labelledby="blog-sheet-title">
      <button class="glass-sheet__close" type="button" data-close-blog-dock aria-label="Close featured blog">&#215;</button>
      <p class="glass-sheet__eyebrow">From our blog</p>
      <div class="glass-sheet__image">
        <img data-sheet-image src="https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=800&q=80" width="800" height="520" alt="Featured blog">
      </div>
      <p class="glass-sheet__category" data-sheet-category>Featured Blog</p>
      <h2 id="blog-sheet-title" data-sheet-title>5 AI Tools Every Marketer Should Be Using in 2025</h2>
      <p class="glass-sheet__copy" data-sheet-copy>Discover practical tools that save time, improve productivity, and make marketing workflows lighter.</p>
      <div class="glass-sheet__meta">
        <span data-sheet-reading>4 min read</span>
      </div>
      <a class="btn-primary glass-sheet__cta" data-sheet-cta href="/blog/">Read Full Article &#8594;</a>
    </section>
  </div>'''

WA_SHEET = '''  <div class="glass-sheet" id="wa-sheet" aria-hidden="true">
    <div class="glass-sheet__backdrop" data-close-wa-dock></div>
    <section class="glass-sheet__panel glass-sheet__panel--compact" role="dialog" aria-modal="true" aria-labelledby="wa-sheet-title">
      <button class="glass-sheet__close" type="button" data-close-wa-dock aria-label="Close WhatsApp form">&#215;</button>
      <p class="glass-sheet__eyebrow">Chat with us on WhatsApp</p>
      <h2 id="wa-sheet-title">Send a quick note</h2>
      <form class="glass-form" id="wa-sheet-form">
        <label>Name<input id="wa-name" name="name" autocomplete="name" required></label>
        <label>Company<input id="wa-company" name="company" autocomplete="organization"></label>
        <label>Message<textarea id="wa-message" name="message" rows="4" required>Hi Hevify,
I would like to know more about your marketing services.</textarea></label>
        <button class="btn-primary" type="submit">Send Message</button>
      </form>
    </section>
  </div>'''

GLASS_FOOTER_FIX = '''
  <footer class="glass-footer" aria-label="Quick shortcuts">
    <div class="glass-footer__inner">
      <a class="glass-footer__brand" href="/" aria-label="Hevify Labs home">
        <img src="/favicon.webp" width="40" height="40" alt="Hevify Labs">
        <span>
          <strong>Hevify Labs</strong>
          <small class="glass-footer__tag" aria-hidden="true">Quick shortcuts</small>
        </span>
      </a>
      <nav class="glass-footer__shortcuts" aria-label="Footer shortcuts">
        <a class="glass-footer__link" href="/services/">Services</a>
        <a class="glass-footer__link" href="/blog/">Blog</a>
        <a class="glass-footer__link" href="/packages/">Packages</a>
        <a class="glass-footer__link" href="/#contact">Contact</a>
        <a class="glass-footer__wa" href="https://wa.me/+919429428370?text=Hi%20Hevify%20Labs%2C%20I%20want%20to%20discuss%20my%20requirements." target="_blank" rel="noopener" aria-label="Contact on WhatsApp (opens in new tab)">
          <svg class="wa-icon" viewBox="0 0 24 24" aria-hidden="true" width="16" height="16" fill="currentColor">
            <path d="M17.5 14.4c-.3-.1-1.8-.9-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-1.7-.8-2.8-1.8-3.6-3.4-.2-.3 0-.5.1-.7.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4z"/>
            <path d="M12 2.1A9.9 9.9 0 0 0 3.6 17.2l-1 3.6 3.7-1a9.9 9.9 0 1 0 5.7-17.7zm0 17.7c-1.8 0-3.5-.6-4.9-1.6l-.4-.2-2.2.6.6-2.1-.2-.4A7.8 7.8 0 1 1 12 19.8z"/>
          </svg>
          WhatsApp
        </a>
      </nav>
    </div>
  </footer>'''

def is_root_homepage(fp):
    n = fp.replace('/', '\\')
    return n.endswith('WEB.FILES\\index.html')

def fix_file(fp, content):
    original = content
    changes = []

    # ── 1. Fix garbled stars in reviews: â˜… → ★ HTML entity ─────────────
    content = content.replace('&#185;&#568;&#188;', '&#9733;')
    content = content.replace('&#65533;&#568;&#65533;', '&#9733;')
    # Direct byte-level fix for ★ encoded as UTF-8 read as cp1252
    content = content.replace('â˜…', '&#9733;')

    # ── 2. Fix broken Instagram/LinkedIn aria-label duplication ─────────────
    # These links have "> aria-label="...">Text</a>" — fix to proper single aria-label
    # Pattern: </a>...<a ... instagram ... target="_blank" rel="noopener"> aria-label="...">Text</a>
    # Fix: remove the spurious "> aria-label="..." part

    # Fix Instagram links
    content = re.sub(
        r'(<a\b[^>]*instagram[^>]*target="_blank"[^>]*>) aria-label="[^"]*"(\s*>)',
        r'\1',
        content, flags=re.IGNORECASE
    )
    # Fix LinkedIn links
    content = re.sub(
        r'(<a\b[^>]*linkedin[^>]*target="_blank"[^>]*>) aria-label="[^"]*"(\s*>)',
        r'\1',
        content, flags=re.IGNORECASE
    )
    # Also fix WhatsApp btn-outline duplicate aria-label
    content = re.sub(
        r'(<a\b[^>]*wa\.me[^>]*>) aria-label="[^"]*"(\s*>)',
        r'\1',
        content, flags=re.IGNORECASE
    )
    if 'aria-label="Hevify Labs on Instagram (opens in new tab)"' in content:
        # If still has "(opens in new tab)" clean it up - just use the base name
        content = content.replace(
            'aria-label="Hevify Labs on Instagram (opens in new tab)"',
            'aria-label="Hevify Labs on Instagram"'
        )
        content = content.replace(
            'aria-label="Hevify Labs on LinkedIn (opens in new tab)"',
            'aria-label="Hevify Labs on LinkedIn"'
        )
        content = content.replace(
            'aria-label="Contact on WhatsApp (opens in new tab)"',
            'aria-label="Contact on WhatsApp"'
        )
        content = content.replace(
            'aria-label="Contact us on WhatsApp (opens in new tab)"',
            'aria-label="Contact us on WhatsApp"'
        )
        changes.append("aria-label cleanup")

    # Check if stars changed
    if '&#9733;' in content and 'â˜…' not in content:
        changes.append("stars fixed")

    # ── 3. Replace nav header ─────────────────────────────────────────────
    content = re.sub(
        r'  <header class="site-nav[^>]*>.*?</header>',
        build_nav_html(),
        content, flags=re.DOTALL
    )
    if 'nav-hamburger' not in content:
        changes.append("nav fixed")

    # ── 4. Replace glass-dock + blog sheet + wa sheet (homepage) ───────────
    if is_root_homepage(fp):
        # Remove old glass-dock, blog-sheet, wa-sheet
        content = re.sub(r'\s*<div class="glass-dock"[^>]*>.*?</div>\s*<div class="glass-sheet"[^>]*id="blog-sheet"[^>]*>.*?</div>\s*<div class="glass-sheet"[^>]*id="wa-sheet"[^>]*>.*?</div>', '', content, flags=re.DOTALL)
        # Also handle old footer glass-dock/glass-footer
        content = re.sub(r'\s*<footer class="glass-footer"[^>]*>.*?</footer>', '', content, flags=re.DOTALL)
        # Insert new glass dock + blog sheet + wa sheet before </body>
        content = content.replace('</body>', build_glass_dock() + BLOG_SHEET_FIX + WA_SHEET + '\n</body>')
        changes.append("glass-dock + blog sheet")

    # ── 5. Replace glass-footer for inner pages ───────────────────────────
    else:
        content = re.sub(r'\s*<footer class="glass-footer"[^>]*>.*?</footer>', '', content, flags=re.DOTALL)
        content = content.replace('</body>', GLASS_FOOTER_FIX + '\n</body>')
        changes.append("glass-footer")

    return content, changes, content != original


# ─── Process all files ───────────────────────────────────────────────────
count = 0
for root, dirs, files in os.walk(BASE):
    for fn in files:
        if fn.endswith('.html'):
            fp = os.path.join(root, fn)
            for enc in ('utf-8', 'utf-8-sig', 'cp1252'):
                try:
                    with open(fp, 'r', encoding=enc) as f:
                        content = f.read()
                    break
                except:
                    continue

            new_content, changes, changed = fix_file(fp, content)
            if changed:
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                rel = fp.replace(BASE, '')
                print(f"Updated [{', '.join(changes)}]: {rel}")
                count += 1

print(f"\nTotal files updated: {count}")
