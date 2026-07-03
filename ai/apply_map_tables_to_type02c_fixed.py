# -*- coding: utf-8 -*-
import glob
import os

print("--- Apply map*.html tables to class='type02 type02c' Start ---")

map_files = glob.glob("company/list/map*.html")
print(f"Found {len(map_files)} map files to inspect.")

apply_count = 0

for file_path in map_files:
    # 読み込み (cp932)
    with open(file_path, "r", encoding="cp932", errors="ignore") as f:
        html = f.read()
    
    updated_html = html
    
    # class="type05" を class="type02 type02c" に置換
    # (二重適用を防ぐため、既に type02 type02c になっている場合は置換されません)
    updated_html = updated_html.replace('class="type05"', 'class="type02 type02c"')
    
    if updated_html != html:
        # 書き込み (cp932)
        with open(file_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(updated_html)
        print(f"Applied table class to type02 type02c in {os.path.basename(file_path)}")
        apply_count += 1

print(f"--- Apply Completed. Updated {apply_count} file(s). ---")
