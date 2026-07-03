# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# color を #000 !important; に変更する
target = """    #sdgs .allitem::before {
        content: "持続可能な開発目標（SDGs）への取り組み" !important;
        display: block !important;
        font-size: 1.4em !important;
        font-weight: bold !important;
        color: #2B7CCB !important;
        margin: 15px 0 !important;
    }"""

replacement = """    #sdgs .allitem::before {
        content: "持続可能な開発目標（SDGs）への取り組み" !important;
        display: block !important;
        font-size: 1.4em !important;
        font-weight: bold !important;
        color: #000 !important;
        margin: 15px 0 !important;
    }"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully changed #sdgs .allitem::before color to #000.")
else:
    print("Error: Target style block not found in CSS.")
