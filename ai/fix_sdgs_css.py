# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# セレクタを置換
target = "    #products img[src*=\"sdgs_\"] {"
replacement = "    #products img[src*=\"sdgs_\"],#products img[src*=\"sdgs_\"]+.txt {"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully updated SDGs image and text selectors in common.css.")
else:
    # 空白やインデントのゆらぎに対応
    import re
    pattern = r'#products\s+img\[src\*=\"sdgs_\"\]\s*\{'
    if re.search(pattern, content):
        content = re.sub(pattern, '#products img[src*="sdgs_"],#products img[src*="sdgs_"]+.txt {', content)
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content)
        print("Successfully updated SDGs image and text selectors in common.css (regex).")
    else:
        print("Target style pattern for SDGs image selector not found.")
