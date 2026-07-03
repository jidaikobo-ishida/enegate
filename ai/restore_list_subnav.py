# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# breadcrumbs定義の直前に元のPC用 #list .leftsubnav 定義を書き戻す
target = "#list #breadcrumbs { padding-bottom:20px;font-size:0.78em;}"
replacement = "#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em; float: left; width: 180px;}\n#list #breadcrumbs { padding-bottom:20px;font-size:0.78em;}"

# LF統一して置換
content_lf = content.replace("\r\n", "\n")
target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully restored #list .leftsubnav to common.css.")
else:
    print("Could not find breadcrumbs target to restore.")
