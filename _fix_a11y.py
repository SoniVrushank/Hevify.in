# -*- coding: utf-8 -*-
"""Fix all WCAG accessibility issues across all HTML files."""
import os
import re

base = r"C:\Users\Vrushh\Downloads\Companies\HV\WEB.FILES"

# ─── 1. Fix Level A: Theme toggle icons ───────────────────────────────
# Replace ☀ / ☾ character spans with SVG icons (icon chars must be aria-hidden)
THEME_TOGGLE_SUN_SVG = '''<svg class="theme-icon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
  <circle cx="12" cy="12" r="5" fill="currentColor"/>
  <line x1="12" y1="1" x2="12" y2="4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <line x1="12" y1="20" x2="12" y2="23" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <line x1="1" y1="12" x2="4" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <line x1="20" y1="12" x2="23" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <line x1="4.22" y1="4.22" x2="6.34" y2="6.34" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <line x1="17.66" y1="17.66" x2="19.78" y2="19.78" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <line x1="4.22" y1="19.78" x2="6.34" y2="17.66" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <line x1="17.66" y1="6.34" x2="19.78" y2="4.22" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>'''

THEME_TOGGLE_MOON_SVG = '''<svg class="theme-icon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" fill="currentColor"/>
</svg>'''

def fix_theme_toggle(content):
    # Sun icon: replace ☀ span (with garbled char)
    content = re.sub(
        r'<span class="theme-toggle__sun"[^>]*>.*?</span>',
        f'<span class="theme-toggle__sun" aria-hidden="true">{THEME_TOGGLE_SUN_SVG}</span>',
        content, flags=re.DOTALL
    )
    # Moon icon: replace ☾ span
    content = re.sub(
        r'<span class="theme-toggle__moon"[^>]*>.*?</span>',
        f'<span class="theme-toggle__moon" aria-hidden="true">{THEME_TOGGLE_MOON_SVG}</span>',
        content, flags=re.DOTALL
    )
    return content

# ─── 2. Fix Level A: glass-dock spark icon ───────────────────────────
# Move ✦ (which renders as &#10022; now) into aria-hidden span, or just aria-hidden the whole spark
def fix_glass_dock_spark(content):
    # The spark text ✦ should be aria-hidden — it's decorative
    content = re.sub(
        r'(<span class="glass-dock__spark"[^>]*)>(&#10022;|&#10022)</span>',
        r'\1 aria-hidden="true">&#10022;</span>',
        content
    )
    return content

# ─── 3. Fix Level A: glass-footer brand "Quick shortcuts" in name ─────
# Remove <small class="glass-footer__tag">Quick shortcuts</small> from inside the link
# The aria-label on the <a> already says "Hevify Labs home" — the <small> is decorative visual only
# But it contributes to the accessible name. Solution: add aria-hidden="true" to the small
GLASS_FOOTER_BRAND_FIX = '''<a class="glass-footer__brand" href="/" aria-label="Hevify Labs home">
        <img src="/favicon.webp" width="40" height="40" alt="Hevify Labs">
        <span>
          <strong>Hevify Labs</strong>
          <small class="glass-footer__tag" aria-hidden="true">Quick shortcuts</small>
        </span>
      </a>'''

def fix_glass_footer_brand(content):
    # Replace brand link: add aria-hidden to the small tag
    content = re.sub(
        r'<a class="glass-footer__brand"[^>]*href="/"[^>]*>.*?<small class="glass-footer__tag">(.*?)</small>.*?</a>',
        lambda m: m.group(0).replace(
            f'<small class="glass-footer__tag">{m.group(1)}</small>',
            f'<small class="glass-footer__tag" aria-hidden="true">{m.group(1)}</small>'
        ),
        content, flags=re.DOTALL
    )
    return content

# ─── 4. Fix Level AAA: btn-outline Contact us too small (97x26px) ────
# Fix in JS: the btn-outline inside folder-actions gets padding that makes it too small
# CSS fix is done separately in site.css — but also need to ensure no min-width in CSS
# For HTML: the "Contact us" buttons that appear inline in service cards need to be bigger
# We'll handle this with CSS fix. For now, ensure they have proper classes.

# ─── 5. Fix Level AAA: Duplicate link text "Learn more" / "Read article" ────
def fix_duplicate_links(content):
    # Count "Learn more" links and add aria-label to each with increasing context
    learn_more_count = content.count('>Learn more</a>')
    if learn_more_count > 1:
        idx = 0
        def replace_learn_more(m):
            nonlocal idx
            idx += 1
            if idx > 1:
                return f'<a{m.group(1)}aria-label="Learn more (article {idx})">{m.group(2)}Learn more</a>'
            return m.group(0)
        content = re.sub(
            r'<a([^>]+)>(Learn more)</a>',
            replace_learn_more,
            content, flags=re.IGNORECASE
        )

    # "Read article" links
    read_article_count = content.count('>Read article</a>')
    if read_article_count > 1:
        idx = 0
        def replace_read_article(m):
            nonlocal idx
            idx += 1
            if idx > 1:
                return f'<a{m.group(1)}aria-label="Read article (article {idx})">{m.group(2)}Read article</a>'
            return m.group(0)
        content = re.sub(
            r'<a([^>]+)>(Read article)</a>',
            replace_read_article,
            content, flags=re.IGNORECASE
        )
    return content

# ─── 6. Fix Level AAA: target="_blank" without warning ──────────────
# Add (opens in new tab) text for Instagram/LinkedIn links
def fix_target_blank(content):
    # Instagram link — add visually hidden text
    content = re.sub(
        r'(<a[^>]*instagram[^>]*target="_blank"[^>]*aria-label=")(Hevify Labs on Instagram)(")',
        r'\1\2 (opens in new tab)\3',
        content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'(<a[^>]*instagram[^>]*target="_blank"[^>]*>)(?!.*aria-label)',
        r'\1 aria-label="Hevify Labs on Instagram (opens in new tab)">',
        content, flags=re.IGNORECASE
    )
    # LinkedIn link
    content = re.sub(
        r'(<a[^>]*linkedin[^>]*target="_blank"[^>]*aria-label=")(Hevify Labs on LinkedIn)(")',
        r'\1\2 (opens in new tab)\3',
        content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'(<a[^>]*linkedin[^>]*target="_blank"[^>]*>)(?!.*aria-label)',
        r'\1 aria-label="Hevify Labs on LinkedIn (opens in new tab)">',
        content, flags=re.IGNORECASE
    )
    # WhatsApp links — add to aria-label
    content = re.sub(
        r'(<a[^>]*href="https://wa\.me[^"]*"[^>]*aria-label=")(Contact on WhatsApp)(")',
        r'\1\2 (opens in new tab)\3',
        content
    )
    content = re.sub(
        r'(<a[^>]*href="https://wa\.me[^"]*"[^>]*>)(?!.*aria-label)(.*?Contact us.*?)</a>',
        r'\1 aria-label="Contact us on WhatsApp (opens in new tab)">\2</a>',
        content, flags=re.DOTALL
    )
    # Other WhatsApp links with btn-primary or btn-whatsapp
    content = re.sub(
        r'(<a[^>]*href="https://wa\.me[^"]*"[^>]*)(>Contact us</a>)',
        r'\1 aria-label="Contact us on WhatsApp (opens in new tab)"\2',
        content
    )
    return content

def process_file(fp, content):
    original = content

    # 1. Theme toggle icons
    content = fix_theme_toggle(content)

    # 2. Glass dock spark
    content = fix_glass_dock_spark(content)

    # 3. Glass footer brand
    content = fix_glass_footer_brand(content)

    # 4. Duplicate link text
    content = fix_duplicate_links(content)

    # 5. target=_blank
    content = fix_target_blank(content)

    return content, content != original

count = 0
for root, dirs, filenames in os.walk(base):
    for fn in filenames:
        if fn.endswith('.html'):
            fp = os.path.join(root, fn)
            for enc in ('utf-8', 'utf-8-sig', 'cp1252'):
                try:
                    with open(fp, 'r', encoding=enc) as f:
                        content = f.read()
                    break
                except (UnicodeDecodeError, UnicodeError):
                    continue

            new_content, changed = process_file(fp, content)
            if changed:
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                rel = fp.replace(base, '')
                print(f"Accessibility fix: {rel}")
                count += 1

print(f"\nTotal files fixed: {count}")
