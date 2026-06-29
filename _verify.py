# -*- coding: utf-8 -*-
"""Fix double aria-hidden and verify all accessibility fixes."""
import os

base = r"C:\Users\Vrushh\Downloads\Companies\HV\WEB.FILES"

for root, dirs, files in os.walk(base):
    for fn in files:
        if fn.endswith('.html'):
            fp = os.path.join(root, fn)
            content = open(fp, encoding='utf-8').read()
            # Fix double aria-hidden on spark
            fixed = content.replace('aria-hidden="true" aria-hidden="true"', 'aria-hidden="true"')
            # Fix missing aria-hidden on moon (if not fixed)
            if fixed != content:
                open(fp, 'w', encoding='utf-8').write(fixed)
                print('Fixed:', fp.replace(base, ''))

# Verify key fixes in homepage
fp = os.path.join(base, 'index.html')
content = open(fp, encoding='utf-8').read()
checks = [
    ('theme-toggle SVG sun', 'theme-toggle__sun' in content and 'aria-hidden="true"' in content),
    ('theme-toggle SVG moon', 'theme-toggle__moon' in content),
    ('spark aria-hidden', 'glass-dock__spark' in content and content.count('aria-hidden="true" aria-hidden="true"') == 0),
    ('hamburger', 'nav-hamburger' in content),
    ('glass-dock', 'glass-dock' in content),
]
print('\n=== Homepage verification ===')
for name, result in checks:
    print(f'  {name}: {"OK" if result else "MISSING"}')
