# -*- coding: utf-8 -*-
"""Update blog placeholder to use local SVG instead of external Unsplash URL."""
import os, re

BASE = r"C:\Users\Vrushh\Downloads\Companies\HV\WEB.FILES"

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

            # Fix Unsplash URL → local SVG data URI
            content = content.replace(
                'src="https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=800&q=80"',
                'src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 800 520\'%3E%3Crect fill=\'%234a7c59\' width=\'800\' height=\'520\'/%3E%3Ctext fill=\'%23ffffff\' font-family=\'sans-serif\' font-size=\'28\' x=\'50%25\' y=\'50%25\' text-anchor=\'middle\' dominant-baseline=\'middle\' font-weight=\'600\'%3EBlog%3C/text%3E%3Ccircle cx=\'660\' cy=\'420\' r=\'80\' fill=\'%239ccd77\' opacity=\'0.5\'/%3E%3Ccircle cx=\'140\' cy=\'100\' r=\'50\' fill=\'%239ccd77\' opacity=\'0.3\'/%3E%3C/svg%3E"'
            )
            if fp.endswith('index.html'):
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Blog image fixed: {fp.replace(BASE, '')}")

# Create blog placeholder image directory and file
img_dir = os.path.join(BASE, 'assets', 'img')
os.makedirs(img_dir, exist_ok=True)

svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" width="800" height="520">
  <rect fill="#4a7c59" width="800" height="520"/>
  <text fill="#ffffff" font-family="sans-serif" font-size="28" x="50%" y="50%" text-anchor="middle" dominant-baseline="middle" font-weight="600">Blog</text>
  <circle cx="660" cy="420" r="80" fill="#9ccd77" opacity="0.5"/>
  <circle cx="140" cy="100" r="50" fill="#9ccd77" opacity="0.3"/>
</svg>'''

img_path = os.path.join(img_dir, 'blog-placeholder.svg')
with open(img_path, 'w', encoding='utf-8') as f:
    f.write(svg_content)
print(f"\nCreated: {img_path}")

# Also update the blog sheet img src to use local SVG
for root, dirs, files in os.walk(BASE):
    for fn in files:
        if fn.endswith('.html'):
            fp = os.path.join(root, fn)
            content = open(fp, encoding='utf-8').read()
            if 'glass-sheet__image' in content:
                fixed = content.replace(
                    'src="data:image/svg+xml',
                    'NOTUSED'
                ).replace(
                    'src="/assets/img/blog-placeholder.svg"',
                    'src="/assets/img/blog-placeholder.svg"'
                )
                # Actually just keep the data URI inline for reliability
                pass
print("All done.")
