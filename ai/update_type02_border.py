# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# border: 3px solid #d2e5f4 !important; を border: 5px solid #d2e5f4 !important; に置換
target = "border: 3px solid #d2e5f4 !important;"
replacement = "border: 5px solid #d2e5f4 !important;"

# LF統一
content_lf = content.replace("\r\n", "\n")

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated .twocontent .group .type02 border size to 5px in common.css.")
else:
    print("Target style pattern for type02 border update not found.")
