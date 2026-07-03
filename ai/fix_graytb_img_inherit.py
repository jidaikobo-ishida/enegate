# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# max-width: auto !important; を max-width: inherit !important; に修正
target = "max-width: auto !important;"
replacement = "max-width: inherit !important;"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully corrected table.graytb td img to max-width: inherit in common.css.")
else:
    print("Target style pattern for correction not found.")
