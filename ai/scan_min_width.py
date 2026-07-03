# -*- coding: utf-8 -*-
import re

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# min-width 指定を検索 (例: min-width: 950px;)
matches = re.finditer(r'([^{}\n]*)\{[^{}]*?min-width\s*:\s*(\d+)px', content, re.IGNORECASE)

print("--- Scan min-width Results ---")
for m in matches:
    selector = m.group(1).strip()
    val = int(m.group(2))
    if val >= 760:
        print(f"Selector: {selector} | Value: {val}px")
print("--- Scan end ---")
