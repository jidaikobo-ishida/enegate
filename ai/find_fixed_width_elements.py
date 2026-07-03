# -*- coding: utf-8 -*-
import re

print("--- Find Fixed Width Elements (>= 734px) Start ---")

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# メディアクエリの外側（PC用グローバル領域）のみをパースするため、
# スマホ用メディアクエリ（@media only screen and (max-width:736px)）の開始位置を取得し、
# それ以前のテキストを対象とする
sp_media_marker = "@media only screen and (max-width:736px)"
if sp_media_marker in content:
    pc_content = content[:content.index(sp_media_marker)]
    print("Parsing only PC-side global styles (before max-width:736px query).")
else:
    pc_content = content
    print("Warning: max-width:736px marker not found, parsing entire file.")

# 正規表現で selector { ... width: XXXpx; ... } を探す
# 単純に「数数値 px」を検索して、それが 734 以上のものを抽出する
# (width や min-width が対象)
matches = re.finditer(r'([^{}\n]+)\{[^{}]*?(width|min-width)\s*:\s*(\d+)px', pc_content, flags=re.IGNORECASE | re.DOTALL)

found_elements = []

for m in matches:
    selector = m.group(1).strip()
    prop = m.group(2).strip().lower()
    value = int(m.group(3))
    
    if value >= 734:
        # コメントアウトされた行に入っているものは除外
        # (簡易的なチェック)
        if "/*" in selector or "*/" in selector:
            continue
        # 1行にまとめる
        selector_clean = " ".join(selector.split())
        found_elements.append((selector_clean, prop, value))

# 重複を排除して綺麗に出力
seen = set()
unique_elements = []
for item in found_elements:
    key = (item[0], item[1], item[2])
    if key not in seen:
        seen.add(key)
        unique_elements.append(item)

print(f"\nFound {len(unique_elements)} elements with fixed width/min-width >= 734px:")
for idx, (sel, prop, val) in enumerate(unique_elements, 1):
    print(f"{idx:02d}. Selector: `{sel}`\n    Property: `{prop}: {val}px;`\n")

print("--- Find Fixed Width Elements Completed ---")
