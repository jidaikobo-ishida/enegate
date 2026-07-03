# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

target = """    #sdgs .iconlist li {
        flex-basis: 23% !important;
        margin: 0 !important;
        float: none !important;
    }"""

replacement = """    #sdgs .iconlist li {
        flex-basis: 23% !important;
        margin: 1.5% 0 !important;
        float: none !important;
    }"""

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated #sdgs .iconlist li margin to 1.5% 0 in common.css.")
else:
    print("Target style pattern for .iconlist li margin not found.")
