# -*- coding: utf-8 -*-
import os
import re
import glob

print("--- Map Files Menu Position Fix Start ---")

map_files = glob.glob("company/list/map*.html")

for mf in map_files:
    # _car.html や _walk.html などのサブマップ（ポップアップ用の別ウィンドウ）は
    # そもそもヘッダーやレフトナビが省かれた単機能の印刷用ページ等のため、スキップする
    if "_car" in mf or "_walk" in mf:
        continue
        
    with open(mf, "r", encoding="cp932", errors="ignore") as f:
        content = f.read()
        
    content_lf = content.replace("\r\n", "\n")
    
    # 1. ローカルメニュー (leftmenu) のインクルード部分を探して削除
    menu_pattern = r'(<!--\s*ローカルメニュー\s*-->.*?include\(.*?company_leftmenu.html.*?\);.*?\?>.*?<!--\s*//ローカルメニュー\s*-->)'
    match_menu = re.search(menu_pattern, content_lf, re.DOTALL)
    
    menu_block = ""
    if match_menu:
        menu_block = match_menu.group(1)
        content_lf = content_lf.replace(menu_block, "")
    else:
        # フォールバック (シンプルなインクルードのみ)
        simple_pattern = r'(\s*<\?php\s*include\(.*?company_leftmenu.html.*?\);\s*\?>)'
        match_simple = re.search(simple_pattern, content_lf)
        if match_simple:
            menu_block = match_simple.group(1)
            content_lf = content_lf.replace(menu_block, "")
            
    if not menu_block:
        print(f"Skipping {mf} (leftmenu not found or already moved).")
        continue

    # 2. パンくず (breadcrumbs) の後ろに挿入
    breadcrumbs_pattern = r'(<div id=\"breadcrumbs\" class=\"inner\">.*?</div>)'
    match_bc = re.search(breadcrumbs_pattern, content_lf, re.DOTALL)
    if match_bc:
        insertion = match_bc.group(1) + "\n\n\t\t" + menu_block
        content_lf = content_lf.replace(match_bc.group(1), insertion)
        
        with open(mf, "w", encoding="cp932", errors="ignore") as f:
            f.write(content_lf)
        print(f"Successfully moved leftmenu to top in: {mf}")
    else:
        print(f"Could not find breadcrumbs block in: {mf}")

print("--- Map Files Menu Position Fix End ---")
