# -*- coding: utf-8 -*-
"""Add performance optimizations to all HTML heads."""
import os, re

BASE = r"C:\Users\Vrushh\Downloads\Companies\HV\WEB.FILES"

HEAD_INJECT = '''
  <!-- Performance: DNS prefetch -->
  <link rel="dns-prefetch" href="//fonts.googleapis.com">
  <link rel="dns-prefetch" href="//fonts.gstatic.com">
  <!-- Performance: Preconnect to Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <!-- Performance: Preload critical CSS (already in place) -->
  <link rel="preload" href="/assets/css/site.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/assets/css/site.css"></noscript>'''

def fix_head(content):
    # Remove any existing preconnect/dns-prefetch to avoid duplicates
    content = re.sub(r'\s*<link rel="(?:preconnect|dns-prefetch)"[^>]*>', '', content)
    content = re.sub(r'\s*<link rel="preload"[^>]*as="style"[^>]*>', '', content)

    # Find <link rel="icon" ...> line and insert performance hints after it
    icon_line_end = content.find('<link rel="icon"')
    if icon_line_end == -1:
        # insert after <meta name="theme-color"...>
        idx = content.find('<meta name="theme-color"')
        if idx != -1:
            end = content.find('>', idx) + 1
            content = content[:end] + HEAD_INJECT + content[end:]
    else:
        end = content.find('>', icon_line_end) + 1
        content = content[:end] + HEAD_INJECT + content[end:]

    # Fix blog sheet image: use a nice gradient placeholder (no external URL dependency)
    content = content.replace(
        'src="https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=800&q=80"',
        'src="/assets/img/blog-placeholder.png"'
    )
    return content

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
            new_content = fix_head(content)
            if new_content != content:
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Performance head: {fp.replace(BASE, '')}")
                count += 1
print(f"\nTotal: {count}")
