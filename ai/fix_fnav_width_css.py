# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# width: 175px; を width: 47% !important; に置換
target = "#fnav .fsbx, #fnav .scbx, #fnav .thbox, #fnav .fubox, #fnav .lflt { width: 175px; float: none; }"
replacement = "#fnav .fsbx, #fnav .scbx, #fnav .thbox, #fnav .fubox, #fnav .lflt { width: 47% !important; float: none; }"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully updated #fnav child widths in common.css.")
else:
    # インデントなどのゆらぎに対応
    import re
    pattern = r'#fnav\s+\.fsbx,\s*#fnav\s+\.scbx,\s*#fnav\s+\.thbox,\s*#fnav\s+\.fubox,\s*#fnav\s+\.lflt\s*\{\s*width:\s*175px;\s*float:\s*none;\s*\}'
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content)
        print("Successfully updated #fnav child widths in common.css (regex).")
    else:
        print("Target style pattern for #fnav widths not found.")
