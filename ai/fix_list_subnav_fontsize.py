# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# font-size: 0.78em; を除去して通常ページのメニュー文字サイズと揃える
target = "#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em; float: left; width: 180px;}"
replacement = "#list .leftsubnav {margin:10px 0 50px 0; float: left; width: 180px;}"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully removed font-size and aligned subnav styling in common.css.")
else:
    print("Target style pattern for font-size not found.")
