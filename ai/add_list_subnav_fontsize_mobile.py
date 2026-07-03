# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

target = """    #list .leftsubnav {
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        box-sizing: border-box !important;
    }"""

replacement = """    #list .leftsubnav {
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        box-sizing: border-box !important;
        font-size: 1em !important;
    }"""

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated #list .leftsubnav mobile font-size to 1em.")
else:
    print("Target style pattern for mobile font-size update not found.")
