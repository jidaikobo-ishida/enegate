# -*- coding: utf-8 -*-
import glob
import os

print("--- Rollback map*.html tables to class='type05' Start ---")

# map*.html 22ファイルを対象とする
map_files = glob.glob("company/list/map*.html")
print(f"Found {len(map_files)} map files to inspect.")

rollback_count = 0

for file_path in map_files:
    # Shift-JIS (cp932) で読み込む
    with open(file_path, "r", encoding="cp932", errors="ignore") as f:
        html = f.read()
    
    # table.type02 type02c を table.type05 に戻す
    # (クラスの記述順やスペースの揺れを考慮して安全に置換)
    updated_html = html
    
    # パターン1: class="type02 type02c"
    updated_html = updated_html.replace('class="type02 type02c"', 'class="type05"')
    # パターン2: class="type02c type02"
    updated_html = updated_html.replace('class="type02c type02"', 'class="type05"')
    # パターン3: class="type02" (もし地図ページ内に存在すれば)
    # ただし、他の table.type02 (事業所一覧へのリンク等) を誤って置換しないよう、
    # アクセス表部分のみに限定する (通常 map*.html のアクセス表は table class="type02 type02c" となっています)
    
    if updated_html != html:
        with open(file_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(updated_html)
        print(f"Rolled back table class in {os.path.basename(file_path)}")
        rollback_count += 1

print(f"--- Rollback Completed. Rolled back {rollback_count} file(s). ---")
