# -*- coding: utf-8 -*-
import re

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# メディアクエリの開始位置を特定
# スマホ用メディアクエリは通常 2078 行目付近 (@media screen and (max-width: 736px))
media_query_match = re.search(r'@media\s+screen\s+and\s*\(max-width:\s*736px\)', content)
if not media_query_match:
    print("Error: Mobile media query not found.")
    exit(1)

mobile_start_idx = media_query_match.start()
pc_part = content[:mobile_start_idx]
mobile_part = content[mobile_start_idx:]

# 1. PC用パートから float: left/right を含むルールブロックを抽出
# 簡易的な正規表現でセレクタとプロパティを抽出
pc_blocks = []
# セレクタ { プロパティ } のパターン
pattern = r'([^{]+)\{([^}]+)\}'
for match in re.finditer(pattern, pc_part):
    selectors_str = match.group(1).strip()
    properties_str = match.group(2).strip()
    if 'float' in properties_str:
        # float の値を調べる
        float_match = re.search(r'float\s*:\s*(left|right)', properties_str)
        if float_match:
            val = float_match.group(1)
            # 各セレクタに分解
            for sel in selectors_str.split(','):
                sel = re.sub(r'\s+', ' ', sel.strip())
                pc_blocks.append((sel, val))

# 2. スマホ用パートで float: none (または display: none 等) で打ち消されているかチェック
unresolved = []

for sel, val in pc_blocks:
    # スマホ用 CSS の中にそのセレクタが記述されているか
    # セレクタが完全一致するか、あるいは部分一致するか
    # 簡易的に、スマホ用 CSS 内にそのセレクタ名が含まれており、かつ float: none や float: none !important が設定されているか
    escaped_sel = re.escape(sel)
    # スマホ用 CSS の中でそのセレクタの定義ブロックを探す
    block_pattern = escaped_sel + r'\s*\{([^}]+)\}'
    block_matches = re.findall(block_pattern, mobile_part)
    
    resolved = False
    for block in block_matches:
        if 'float' in block and 'none' in block:
            resolved = True
            break
        if 'display' in block and 'none' in block:
            # 非表示になるので解決とする
            resolved = True
            break
        if 'display' in block and 'flex' in block:
            # flexレイアウトに上書きされるので解決とする
            resolved = True
            break
    
    if not resolved:
        unresolved.append((sel, val))

# 重複を排除して表示
unresolved = list(set(unresolved))
unresolved.sort()

print(f"Total PC float selectors: {len(pc_blocks)}")
print(f"Unresolved mobile float selectors: {len(unresolved)}")
print("\n--- Unresolved Float Selectors List ---")
for sel, val in unresolved:
    # 汎用的なクラスや、明らかに影響するセレクタをピックアップ
    print(f"Selector: {sel} (PC Float: {val})")

