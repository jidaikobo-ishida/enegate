# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# #list .leftsubnav のPC版定義を置換（float: left と width を追加）
target = "#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em;}"
replacement = "#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em; float: left; width: 180px;}"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully patched PC style for #list .leftsubnav in common.css.")
else:
    # 改行やスペースのゆらぎに対応
    import re
    pattern = r'#list\s+\.leftsubnav\s*\{\s*margin:\s*10px\s+0\s+50px\s+0;\s*font-size:\s*0\.78em;\s*\}'
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content)
        print("Successfully patched PC style for #list .leftsubnav in common.css (regex).")
    else:
        print("Target style pattern for #list .leftsubnav not found.")
