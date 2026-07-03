# -*- coding: utf-8 -*-
import re

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# メディアクエリ（@media）の外側にあるPC用スタイルのみを対象にしたいが、
# まずは単純に width: \d+px のうち 760 以上のものを抽出してみる
# セレクタと width の値を抽出する正規表現
# 改行やコメントを考慮しつつスキャン
matches = re.finditer(r'([^{}\n]*)\{[^{}]*?width\s*:\s*(\d+)px', content, re.IGNORECASE)

print("--- Scan width Results ---")
seen = set()
for m in matches:
    selector = m.group(1).strip()
    val = int(m.group(2))
    if val >= 760:
        # 重複や類似パターンを除去
        pair = (selector, val)
        if pair not in seen:
            seen.add(pair)
            print(f"Selector: {selector} | Value: {val}px")
print("--- Scan end ---")
