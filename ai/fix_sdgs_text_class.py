# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# .txt を .text に修正
target = "#products img[src*=\"sdgs_\"],#products img[src*=\"sdgs_\"]+.txt"
replacement = "#products img[src*=\"sdgs_\"],#products img[src*=\"sdgs_\"]+.text"

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content)
    print("Successfully corrected .txt to .text for SDGs selector in common.css.")
else:
    print("Target style pattern for SDGs text class correction not found.")
