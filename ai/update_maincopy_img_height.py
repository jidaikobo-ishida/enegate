# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# height: 40px !important; を
# height: 35px !important; に置換
target = "height: 40px !important;"
replacement = "height: 35px !important;"

# LF統一
content_lf = content.replace("\r\n", "\n")

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated .maincopy > img height to 35px in common.css.")
else:
    print("Target style pattern for .maincopy height update not found.")
