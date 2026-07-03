# -*- coding: utf-8 -*-
import os
import re
import glob

print("--- Rename Table Class (type05 -> type02) in Map Files Start ---")

map_files = glob.glob("company/list/map*.html")

count_modified = 0

for filepath in map_files:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="cp932", errors="ignore") as f:
        content = f.read()
        
    # クラス名 type05 を type02 に置換する
    # tableタグの class 属性を対象にする
    # 例: <table border="0" cellpadding="0" cellspacing="0" class="type05">
    # 柔軟な正規表現で table タグの中の class="type05" を class="type02" に置換
    
    # 1. table タグの開始タグを抽出
    table_pattern = r'(<table[^>]*class="[^"]*)type05([^"]*"[^>]*>)'
    
    new_content, count = re.subn(table_pattern, r'\1type02\2', content, flags=re.IGNORECASE)
    
    # 2. その他、もし tr や td などに type05 的なクラスがあればそれも置換される可能性を考慮し、
    # 基本的にはテーブルタグ自体を置換すればOK。
    
    if count > 0:
        with open(filepath, "w", encoding="cp932", errors="ignore") as f:
            f.write(new_content)
        print(f"Renamed {count} table(s) in: {os.path.basename(filepath)}")
        count_modified += 1
    else:
        # 完全に一致する class="type05" の文字置換フォールバック
        if 'class="type05"' in content:
            new_content = content.replace('class="type05"', 'class="type02"')
            with open(filepath, "w", encoding="cp932", errors="ignore") as f:
                f.write(new_content)
            print(f"Renamed table class (direct string) in: {os.path.basename(filepath)}")
            count_modified += 1

print(f"Modified {count_modified} file(s) out of {len(map_files)} files.")
print("--- Rename Table Class (type05 -> type02) in Map Files End ---")
