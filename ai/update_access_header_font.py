# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

target = """    .type02c h4.access::before {
        content: 'ACCESS' !important;
        font-size: 1.2em !important;
        color: #4055b2 !important;
        background: #dceffd !important;
        display: block !important;
        padding: 0.2rem 0.5rem !important;
    }"""

replacement = """    .type02c h4.access::before {
        content: 'ACCESS' !important;
        font-size: 1em !important;
        font-weight: bold !important;
        color: #4055b2 !important;
        background: #dceffd !important;
        display: block !important;
        padding: 0.2rem 0.5rem !important;
    }"""

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated .type02c h4.access::before font styles in common.css.")
else:
    print("Target style pattern for access heading update not found.")
