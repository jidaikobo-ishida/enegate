# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

target = """    .imglg {
        display: flex !important;
        align-items: flex-start !important;
        justify-content: space-between !important;
        gap: 1rem !important;
        flex-wrap: nowrap !important;
        flex: 1 !important;
    }"""

replacement = """    .imglg {
        display: flex !important;
        align-items: flex-start !important;
        justify-content: space-between !important;
        gap: 1rem !important;
        flex-wrap: nowrap !important;
    }
    .imglg > * {
        flex: 1 !important;
    }"""

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully corrected flex: 1 to .imglg > * in common.css.")
else:
    print("Target style pattern for .imglg > * correction not found.")
