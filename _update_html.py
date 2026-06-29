# -*- coding: utf-8 -*-
"""Update all HTML files: add hamburger menu, unify glass-dock/footer."""
import os
import re

base = r"C:\Users\Vrushh\Downloads\Companies\HV\WEB.FILES"

HAMBURGER_BTN = '''    <button class="nav-hamburger" type="button" aria-label="Toggle navigation" aria-expanded="false">
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <line x1="3" y1="6" x2="21" y2="6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        <line x1="3" y1="12" x2="21" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        <line x1="3" y1="18" x2="21" y2="18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
      </svg>
    </button>'''

GLASS_DOCK_HTML = '''
  <div class="glass-dock" role="complementary" aria-label="Quick shortcuts and WhatsApp contact">
    <button class="glass-dock__pill" type="button" data-open-blog-dock aria-label="Open featured blog">
      <span class="glass-dock__spark" aria-hidden="true">&#10022;</span>
      <span class="glass-dock__content">
        <strong data-dock-title>Read: 5 AI Tools Every Marketer Should Be Using in 2025</strong>
        <small data-dock-meta>Featured blog &#183; 4 min read</small>
      </span>
      <span class="glass-dock__arrow" aria-hidden="true">&#8594;</span>
      <span class="glass-dock__progress" aria-hidden="true"><span data-dock-progress></span></span>
    </button>
    <button class="glass-dock__wa" type="button" data-open-wa-dock aria-label="Open WhatsApp message form">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-1.7-.8-2.8-1.8-3.6-3.4-.2-.3 0-.5.1-.7.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4z"></path><path d="M12 2.1A9.9 9.9 0 0 0 3.6 17.2l-1 3.6 3.7-1a9.9 9.9 0 1 0 5.7-17.7zm0 17.7c-1.8 0-3.5-.6-4.9-1.6l-.4-.2-2.2.6.6-2.1-.2-.4A7.8 7.8 0 1 1 12 19.8z"></path></svg>
    </button>
  </div>
  <div class="glass-sheet" id="blog-sheet" aria-hidden="true">
    <div class="glass-sheet__backdrop" data-close-blog-dock></div>
    <section class="glass-sheet__panel" role="dialog" aria-modal="true" aria-labelledby="blog-sheet-title">
      <button class="glass-sheet__close" type="button" data-close-blog-dock aria-label="Close featured blog">&#215;</button>
      <p class="glass-sheet__eyebrow">From our blog</p>
      <div class="glass-sheet__image">
        <img data-sheet-image src="/favicon.webp" width="800" height="520" alt="Featured blog preview">
      </div>
      <p class="glass-sheet__category" data-sheet-category>Featured Blog</p>
      <h2 id="blog-sheet-title" data-sheet-title>5 AI Tools Every Marketer Should Be Using in 2025</h2>
      <p class="glass-sheet__copy" data-sheet-copy>Discover practical tools that save time, improve productivity, and make marketing workflows lighter.</p>
      <div class="glass-sheet__meta">
        <span data-sheet-reading>4 min read</span>
      </div>
      <a class="btn-primary glass-sheet__cta" data-sheet-cta href="/blog/">Read Full Article &#8594;</a>
    </section>
  </div>
  <div class="glass-sheet" id="wa-sheet" aria-hidden="true">
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

GLASS_FOOTER_HTML = '''
  <footer class="glass-footer" aria-label="Quick shortcuts">
    <div class="glass-footer__inner">
      <a class="glass-footer__brand" href="/" aria-label="Hevify Labs home">
        <img src="/favicon.webp" width="40" height="40" alt="Hevify Labs">
        <span>
          <strong>Hevify Labs</strong>
          <small class="glass-footer__tag">Quick shortcuts</small>
        </span>
      </a>
      <nav class="glass-footer__shortcuts" aria-label="Footer shortcuts">
        <a class="glass-footer__link" href="/services/">Services</a>
        <a class="glass-footer__link" href="/blog/">Blog</a>
        <a class="glass-footer__link" href="/packages/">Packages</a>
        <a class="glass-footer__link" href="/#contact">Contact</a>
        <a class="glass-footer__wa" href="https://wa.me/+919429428370?text=Hi%20Hevify%20Labs%2C%20I%20want%20to%20discuss%20my%20requirements." target="_blank" rel="noopener" aria-label="Contact on WhatsApp">
          <svg class="wa-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-1.7-.8-2.8-1.8-3.6-3.4-.2-.3 0-.5.1-.7.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4z"></path><path d="M12 2.1A9.9 9.9 0 0 0 3.6 17.2l-1 3.6 3.7-1a9.9 9.9 0 1 0 5.7-17.7zm0 17.7c-1.8 0-3.5-.6-4.9-1.6l-.4-.2-2.2.6.6-2.1-.2-.4A7.8 7.8 0 1 1 12 19.8z"></path></svg>
          WhatsApp
        </a>
      </nav>
    </div>
  </footer>'''

def is_homepage(fp):
    """True only for the root index.html"""
    return fp.endswith(r'\index.html') or fp.endswith('/index.html')

def process_file(fp, content):
    changes = []
    original = content

    # 1. Add hamburger button after nav-shell div, before theme-toggle
    if 'nav-hamburger' not in content:
        # Match: nav-shell closing div followed by theme-toggle button
        pattern = r'(    <div class="nav-shell"[^>]*>.*?</div>\n)(    <button class="theme-toggle")'
        replacement = r'\1' + HAMBURGER_BTN + r'\2'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            changes.append("hamburger")
            content = new_content
            original = content

    # 2. Remove any existing glass-footer or glass-dock+glass-sheets
    content = re.sub(r'\s*<footer class="glass-footer"[^>]*>.*?</footer>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<div class="glass-dock"[^>]*>.*?</div>\s*<div class="glass-sheet"[^>]*>.*?</div>\s*<div class="glass-sheet"[^>]*>.*?</div>', '', content, flags=re.DOTALL)

    # 3. Add footer before </body>
    if '</body>' in content:
        if is_homepage(fp):
            content = content.replace('</body>', GLASS_DOCK_HTML + '\n</body>')
            changes.append("glass-dock")
        else:
            content = content.replace('</body>', GLASS_FOOTER_HTML + '\n</body>')
            changes.append("glass-footer")
        original = content

    return content, changes

count = 0
for root, dirs, filenames in os.walk(base):
    for fn in filenames:
        if fn.endswith('.html'):
            fp = os.path.join(root, fn)
            enc = 'utf-8'
            try:
                with open(fp, 'r', encoding=enc) as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    enc = 'cp1252'
                    with open(fp, 'r', encoding=enc) as f:
                        content = f.read()
                except:
                    print(f"SKIP: {fp}")
                    continue

            new_content, changes = process_file(fp, content)
            if new_content != content:
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                rel = fp.replace(base, '')
                print(f"Updated [{', '.join(changes)}]: {rel}")
                count += 1

print(f"\nTotal files updated: {count}")
