# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

target = "#division .sch2 { width:100%;"
replacement = "#division .sch2 { width:100% !important;"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully patched #division .sch2 in common.css.")
else:
    # 念のため、空白などのゆらぎに対応
    import re
    pattern = r'#division\s+\.sch2\s*\{\s*width:\s*100%;'
    if re.search(pattern, content):
        content = re.sub(pattern, '#division .sch2 { width:100% !important;', content)
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content)
        print("Successfully patched #division .sch2 in common.css (regex).")
    else:
        print("Target style pattern for #division .sch2 not found.")
