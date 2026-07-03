# -*- coding: utf-8 -*-
import os
import re

print("--- Sync allproductsnav HTML/CSS Start ---")

# 1. products/index.html からお手本の allproductsnav ブロックを抽出
index_path = "products/index.html"
with open(index_path, "r", encoding="cp932", errors="ignore") as f:
    index_content = f.read()

# 改行を LF に統一して検索しやすくする
index_content_lf = index_content.replace("\r\n", "\n")

# allproductsnav ブロック全体の正規表現抽出
nav_pattern = r'(<div id="allproductsnav">.*?</div>\s*</div>\s*</div>)'
match = re.search(nav_pattern, index_content_lf, re.DOTALL)

if not match:
    raise Exception("Could not find allproductsnav block in products/index.html")

common_nav_block = match.group(1)
print("Extracted master allproductsnav block from products/index.html.")

# 2. 他の製品ページの HTML を置換
targets = [
    "products/seigyo.html",
    "products/henkan.html",
    "products/eco.html",
    "products/tsusin.html",
    "products/mente.html",
    "products/other/other01.html"
]

for filepath in targets:
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, "r", encoding="cp932", errors="ignore") as f:
        content = f.read()
        
    content_lf = content.replace("\r\n", "\n")
    
    # 既存の allproductsnav を探す
    # (productsnav + allproductsnav の場合や、単体の場合に対応するため、より柔軟にマッチング)
    existing_match = re.search(nav_pattern, content_lf, re.DOTALL)
    
    if existing_match:
        content_lf = content_lf.replace(existing_match.group(1), common_nav_block)
        with open(filepath, "w", encoding="cp932", errors="ignore") as f:
            f.write(content_lf)
        print(f"Successfully synced allproductsnav in {filepath}")
    else:
        # もし <div id="allproductsnav"> が直接見つからない場合（古い記述のままの場合）
        # <div class="section" id="productsnav">... などのブロックを置換
        old_pattern = r'(<div class="section" id="productsnav">.*?</div>\s*</div>)'
        old_match = re.search(old_pattern, content_lf, re.DOTALL)
        if old_match:
            # breadcrumbs の直下に挿入するなど、お手本の構造に置き換える
            # 今回はすでに apply_html_patches.py で allproductsnav に置換されているはずなので、通常は existing_match でマッチする
            pass
        print(f"Skipping {filepath} (allproductsnav block not found).")

# 3. CSS の更新 (common/css/common.css)
# #allproductsnav a の height を 70px に置換、あわせて親コンテナの高さも 70px に調整
css_path = "common/css/common.css"
with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    css_content = f.read()

css_content_lf = css_content.replace("\r\n", "\n")

# 置換対象 1: #allproductsnav の高さ
css_content_lf = css_content_lf.replace(
    "#allproductsnav { margin-bottom:35px; height:50px;",
    "#allproductsnav { margin-bottom:35px; height:70px;"
)

# 置換対象 2: #allproductsnav a の高さ
css_content_lf = css_content_lf.replace(
    "\theight:50px;\n\tmargin:0;",
    "\theight:70px;\n\tmargin:0;"
)
# (念のためインデント等の違いに対応するため、より柔軟に置換)
css_content_lf = re.sub(
    r'(#allproductsnav\s+a\s*\{[^}]*?height:\s*)50px(;)',
    r'\170px\2',
    css_content_lf,
    flags=re.DOTALL
)

# 置換対象 3: line-height: 50px の調整 (imgnav02, imgnav04 等)
css_content_lf = css_content_lf.replace(
    "#allproductsnav .imgnav02 { background:#000; line-height:50px;}",
    "#allproductsnav .imgnav02 { background:#000; line-height:70px;}"
)
css_content_lf = css_content_lf.replace(
    "#allproductsnav .imgnav04 { background:#000; line-height:50px;}",
    "#allproductsnav .imgnav04 { background:#000; line-height:70px;}"
)

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(css_content_lf)
print("Successfully updated #allproductsnav heights to 70px in common.css.")

print("--- Sync allproductsnav HTML/CSS End ---")
