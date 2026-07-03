# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# width: calc(100% + 30px) !important; を width: calc(100% + 15px) !important; に置換
target = "width: calc(100% + 30px) !important;"
replacement = "width: calc(100% + 15px) !important;"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully updated #products .solution .arrowtitle width in common.css.")
else:
    print("Target style pattern for arrowtitle width not found.")
