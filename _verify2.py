# -*- coding: utf-8 -*-
fp = r"C:\Users\Vrushh\Downloads\Companies\HV\WEB.FILES\index.html"
content = open(fp, encoding='utf-8').read()
checks = [
    ('Stars fixed (&#9733;)', '&#9733;' in content and '\u00e2\u0098\u0099' not in content),
    ('No broken Instagram aria-label', 'aria-label="Hevify Labs on Instagram (opens in new tab)"' not in content),
    ('WhatsApp aria-label clean', 'aria-label="Contact on WhatsApp"' in content),
    ('No hamburger in nav', 'nav-hamburger' not in content),
    ('Nav has About/Services/Blog links', '/#about' in content and '/services/' in content and '/blog/' in content),
    ('Theme toggle has SVG', 'theme-toggle__sun' in content),
    ('Glass-dock WhatsApp is <a> tag', 'glass-dock__wa' in content and 'https://wa.me' in content),
    ('Blog sheet has local image', 'blog-placeholder' in content or 'unsplash' not in content),
    ('Preconnect hints added', 'dns-prefetch' in content),
    ('Blog sheet HTML present', 'blog-sheet' in content),
    ('WA sheet HTML present', 'wa-sheet' in content),
]
print('=== Homepage Verification ===')
for name, result in checks:
    print(f'  {name}: {"OK" if result else "FAIL"}')

# Check footer social links
idx = content.find('instagram.com')
if idx >= 0:
    snippet = content[max(0,idx-50):idx+120]
    print(f'\nFooter Instagram: {snippet}')
idx2 = content.find('linkedin.com')
if idx2 >= 0:
    snippet = content[max(0,idx2-50):idx2+120]
    print(f'Footer LinkedIn: {snippet}')
