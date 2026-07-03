# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

target = "#division .debbox { padding:0 0 10px 0; margin:0 5px 10px 5px; width:45%;}"
replacement = "#division .debbox { padding:0 0 10px 0; margin: 2% !important; width: 46% !important;}"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully patched #division .debbox in common.css.")
else:
    # 念のため、改行やスペースのゆらぎに対応
    import re
    pattern = r'#division\s+\.debbox\s*\{\s*padding:\s*0\s+0\s+10px\s+0;\s*margin:\s*0\s+5px\s+10px\s+5px;\s*width:\s*45%;\s*\}'
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content)
        print("Successfully patched #division .debbox in common.css (regex).")
    else:
        print("Target style pattern for #division .debbox not found.")
