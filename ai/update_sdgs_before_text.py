# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# content: '株式会社エネゲートの取り組む目標' !important; を
# content: '持続可能な開発目標（SDGs）への取り組み' !important; に置換
target = "content: '株式会社エネゲートの取り組む目標' !important;"
replacement = "content: '持続可能な開発目標（SDGs）への取り組み' !important;"

# LF統一
content_lf = content.replace("\r\n", "\n")

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated SDGs before title to option 3 in common.css.")
else:
    print("Target style pattern for SDGs title update not found.")
