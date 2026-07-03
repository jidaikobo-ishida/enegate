# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 1556行目の #list .leftsubnav の定義を無効化（削除）する
target = "#list .leftsubnav {margin:10px 0 50px 0; float: left; width: 180px;}"

if target in content:
    content = content.replace(target, "")
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully deleted #list .leftsubnav definition from common.css.")
else:
    print("Target #list .leftsubnav definition not found.")
