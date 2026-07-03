# -*- coding: utf-8 -*-
import os
import re
import glob

print("--- Scan Unwrapped Large Tables Start ---")

# サイト全体のすべての HTML ファイルを取得
html_files = glob.glob("**/*.html", recursive=True)

unwrapped_tables = []

for filepath in html_files:
    # _car.html や _walk.html などの印刷用や、バックアップファイル（.bak）などは除外
    if "_car" in filepath or "_walk" in filepath or filepath.endswith(".bak") or "enegate-test" in filepath or "node_modules" in filepath:
        continue
        
    try:
        with open(filepath, "r", encoding="cp932", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        continue
        
    content_lf = content.replace("\r\n", "\n")
    
    # すべての table タグを抽出
    # <table ...> ... </table>
    table_matches = re.finditer(r'(<table[^>]*>(.*?)</table>)', content_lf, re.DOTALL | re.IGNORECASE)
    
    for match in table_matches:
        table_html = match.group(1)
        table_inner = match.group(2)
        
        # 1. カラム数を判定 (tr 内の th/td から最大数を計算)
        tr_matches = re.findall(r'<tr[^>]*>(.*?)</tr>', table_inner, re.DOTALL | re.IGNORECASE)
        max_cols = 0
        
        for tr in tr_matches:
            # cells (td/th) の属性とコンテンツを抽出
            tr_cells = re.findall(r'<(td|th)([^>]*)>(.*?)</\1>', tr, re.DOTALL | re.IGNORECASE)
            cols_in_row = 0
            for tag_name, attrs, cell_content in tr_cells:
                colspan_match = re.search(r'colspan\s*=\s*["\']?(\d+)["\']?', attrs, re.IGNORECASE)
                if colspan_match:
                    cols_in_row += int(colspan_match.group(1))
                else:
                    cols_in_row += 1
            if cols_in_row > max_cols:
                max_cols = cols_in_row
                
        # 2. 4カラム以上であるか？
        if max_cols >= 4:
            # 3. 親要素に scrolltable があるかチェック
            # table_html の直前の 100 文字以内に class="scrolltable" が含まれているか確認する
            # あるいは、テーブル自体が <div class="scrolltable"> で囲まれているかを正規表現で調べる
            # (content_lf の全体の中で、table_html の開始インデックスを取得してその前を確認)
            start_idx = content_lf.find(table_html)
            prefix = content_lf[max(0, start_idx - 100):start_idx]
            
            if 'class="scrolltable"' not in prefix and "class='scrolltable'" not in prefix:
                # scrolltable がない未対応のものとして追加
                unwrapped_tables.append({
                    "file": filepath,
                    "cols": max_cols,
                    "snippet": table_html[:250].strip() + "\n... (略) ..."
                })

print(f"Total files scanned: {len(html_files)}")
print(f"Found {len(unwrapped_tables)} unwrapped table(s) with 4 or more columns:")
for t in unwrapped_tables:
    print(f"\n[File] {t['file']} (Max Columns: {t['cols']})")
    print(t['snippet'])

print("--- Scan Unwrapped Large Tables End ---")
