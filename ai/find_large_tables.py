# -*- coding: utf-8 -*-
import os
import re
import glob

print("--- Large Tables Finder Start ---")

# products/ フォルダ以下の HTML ファイルを検索
html_files = glob.glob("products/**/*.html", recursive=True)

found_tables = []

for filepath in html_files:
    try:
        with open(filepath, "r", encoding="cp932", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        continue

    # table class="itemspec" の開始位置を探す
    # テーブルタグ全体の正規表現マッチ
    # tableタグの開始から終了まで
    table_matches = re.finditer(r'<table[^>]*class="[^"]*itemspec[^"]*"[^>]*>(.*?)</table>', content, re.DOTALL | re.IGNORECASE)
    
    for match in table_matches:
        table_html = match.group(0)
        table_inner = match.group(1)
        
        # 1行目（tr）を抽出してカラム数を推定する
        # trタグをすべて抽出
        tr_matches = re.findall(r'<tr[^>]*>(.*?)</tr>', table_inner, re.DOTALL | re.IGNORECASE)
        
        max_cols = 0
        for tr in tr_matches:
            # th もしくは td の数をカウント（colspanも考慮）
            cells = re.findall(r'<(td|th)[^>]*>(.*?)</\1>', tr, re.DOTALL | re.IGNORECASE)
            
            cols_in_row = 0
            for tag, inner in cells:
                # colspan 属性があるか調べる
                colspan_match = re.search(r'colspan\s*=\s*["\']?(\d+)["\']?', tag, re.IGNORECASE)
                # もし td/th 自体の属性に colspan がある場合
                parent_tag_match = re.search(r'<[^>]*colspan\s*=\s*["\']?(\d+)["\']?', table_html) # これはテーブル全体にマッチしてしまうので個別セルに対して調べる
                
                # 正確に個別のセルの開始タグを解析
                cell_start_tag = re.search(r'<(td|th)[^>]*>', table_html) # 正確には cells 内の tag に開始タグが含まれる
                
                # cells の判定において、tag は 'td' もしくは 'th' なので、
                # セル全体の開始タグから colspan を探す必要がある。
                # re.findall(r'<(td|th)([^>]*)>(.*?)</\1>', tr) とすれば、開始タグの属性部分 ([^>]*) が取得できる。
                pass
            
            # 正確なセル属性抽出のための再マッチ
            tr_cells = re.findall(r'<(td|th)([^>]*)>(.*?)</\1>', tr, re.DOTALL | re.IGNORECASE)
            for tag_name, attrs, cell_content in tr_cells:
                colspan_match = re.search(r'colspan\s*=\s*["\']?(\d+)["\']?', attrs, re.IGNORECASE)
                if colspan_match:
                    cols_in_row += int(colspan_match.group(1))
                else:
                    cols_in_row += 1
            
            if cols_in_row > max_cols:
                max_cols = cols_in_row
        
        if max_cols >= 4:
            # 見つかったテーブル情報を保存
            found_tables.append({
                "file": filepath,
                "cols": max_cols,
                "snippet": table_html[:300] + "\n... (略) ..."
            })

# 結果を表示
print(f"Total files scanned: {len(html_files)}")
print(f"Found {len(found_tables)} tables with 4 or more columns:")
for t in found_tables:
    print(f"\n[File] {t['file']} (Max Columns: {t['cols']})")
    print(t['snippet'])

print("--- Large Tables Finder End ---")
