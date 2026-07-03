# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# .scrolltable::after を .scrolltable::before, .scrolltable::after に置換
target = "    .scrolltable::after {"
replacement = "    .scrolltable::before,\n    .scrolltable::after {"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully added .scrolltable::before to common.css.")
else:
    # インデントや空白のゆらぎに対応
    import re
    pattern = r'\.scrolltable::after\s*\{'
    if re.search(pattern, content):
        content = re.sub(pattern, '.scrolltable::before, .scrolltable::after {', content)
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content)
        print("Successfully added .scrolltable::before to common.css (regex).")
    else:
        print("Target style pattern for .scrolltable::after not found.")
