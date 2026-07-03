# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# margin: 14px 0 !important; を
# margin: 14px 0 27px !important; に置換
target = "margin: 14px 0 !important;"
replacement = "margin: 14px 0 27px !important;"

# LF統一
content_lf = content.replace("\r\n", "\n")

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated header logo margin to 14px 0 27px in common.css.")
else:
    print("Target style pattern for logo margin update not found.")
