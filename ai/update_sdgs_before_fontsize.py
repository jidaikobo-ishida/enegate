# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# font-size: 1.2em !important; を
# font-size: 1.4em !important; に置換
target = "font-size: 1.2em !important;"
replacement = "font-size: 1.4em !important;"

# LF統一
content_lf = content.replace("\r\n", "\n")

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated SDGs before title font-size to 1.4em in common.css.")
else:
    print("Target style pattern for SDGs font-size update not found.")
