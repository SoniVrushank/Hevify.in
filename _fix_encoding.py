# -*- coding: utf-8 -*-
"""Fix encoding issues in all HTML files — handles mixed encodings."""
import os

base = r"C:\Users\Vrushh\Downloads\Companies\HV\WEB.FILES"
files_fixed = 0
files_skipped = 0

# Garbled → clean replacements
replacements = {
    'â˜¼': '&#9788;',   # sun icon
    'â˜¾': '&#9786;',   # moon icon
    'âœ¦': '&#10022;',  # sparkle
    'â†’': '&#8594;',   # right arrow
    'â†' + '¬': '&#8594;', # right arrow (split)
    'Ã—': '&#215;',     # multiply ×
    'Â©': '&#169;',     # copyright ©
}

def try_read(fp):
    """Try UTF-8, fall back to Windows-1252."""
    for enc in ('utf-8', 'utf-8-sig', 'cp1252', 'latin-1'):
        try:
            with open(fp, 'r', encoding=enc) as f:
                return f.read(), enc
        except (UnicodeDecodeError, UnicodeError):
            continue
    return None, None

def fix_content(content):
    original = content
    for garbled, clean in replacements.items():
        content = content.replace(garbled, clean)
    return content, content != original

for root, dirs, filenames in os.walk(base):
    for fn in filenames:
        if fn.endswith('.html'):
            fp = os.path.join(root, fn)
            content, enc = try_read(fp)
            if content is None:
                print(f"SKIPPED (unreadable): {fp}")
                files_skipped += 1
                continue

            content, changed = fix_content(content)
            if changed:
                # Always write as UTF-8
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed ({enc}→UTF-8): {fp}")
                files_fixed += 1

print(f"\nDone. Fixed: {files_fixed}  |  Skipped: {files_skipped}")
