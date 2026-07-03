# -*- coding: utf-8 -*-
import re

filepath = "company/list/list.html"

with open(filepath, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 改行コードを LF に統一して処理
content_lf = content.replace("\r\n", "\n")

# コスメメニューのブロックを正規表現で探す
# <!-- から --> までの include を含む部分を柔軟にマッチ
menu_pattern = r'(<!--\s*コスメニュー\s*-->.*?include\(.*?company_leftmenu.html.*?\);.*?\?>.*?<!--\s*//コスメニュー\s*-->)'

match_menu = re.search(menu_pattern, content_lf, re.DOTALL)
if match_menu:
    menu_block = match_menu.group(1)
    # 元の位置から削除
    content_lf = content_lf.replace(menu_block, "")
    print("Found and removed leftmenu block from original position.")
    
    # breadcrumbs の閉じタグ </div> の後ろに挿入
    # <div id="breadcrumbs" ...> ... </div>
    breadcrumbs_pattern = r'(<div id="breadcrumbs" class="inner">.*?</div>)'
    match_bc = re.search(breadcrumbs_pattern, content_lf, re.DOTALL)
    if match_bc:
        insertion = match_bc.group(1) + "\n\n\t\t" + menu_block
        content_lf = content_lf.replace(match_bc.group(1), insertion)
        
        with open(filepath, "w", encoding="cp932", errors="ignore") as f:
            f.write(content_lf)
        print("Successfully moved leftmenu import to top (below breadcrumbs).")
    else:
        print("Could not find breadcrumbs block to insert.")
else:
    # コメントアウトがない場合のフォールバック（直接 include のみ探す）
    simple_pattern = r'(\s*<\?php\s*include\(.*?company_leftmenu.html.*?\);\s*\?>)'
    match_simple = re.search(simple_pattern, content_lf)
    if match_simple:
        menu_block = match_simple.group(1)
        content_lf = content_lf.replace(menu_block, "")
        
        breadcrumbs_pattern = r'(<div id="breadcrumbs" class="inner">.*?</div>)'
        match_bc = re.search(breadcrumbs_pattern, content_lf, re.DOTALL)
        if match_bc:
            insertion = match_bc.group(1) + "\n\n\t\t" + menu_block
            content_lf = content_lf.replace(match_bc.group(1), insertion)
            with open(filepath, "w", encoding="cp932", errors="ignore") as f:
                f.write(content_lf)
            print("Successfully moved leftmenu import (fallback).")
        else:
            print("Could not find breadcrumbs block in fallback.")
    else:
        print("Could not find leftmenu include in list.html at all.")
