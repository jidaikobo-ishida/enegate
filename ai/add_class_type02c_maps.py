# -*- coding: utf-8 -*-
import os
import re
import glob

print("--- Add Table Class type02c in Map Files Start ---")

map_files = glob.glob("company/list/map*.html")

count_modified = 0

for filepath in map_files:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="cp932", errors="ignore") as f:
        content = f.read()
        
    # class="type02" を class="type02 type02c" に置換する
    # tableタグの class 属性を対象にする
    # 例: <table border="0" cellpadding="0" cellspacing="0" class="type02">
    
    # 柔軟な正規表現で table タグの中の class="type02" を class="type02 type02c" に置換
    table_pattern = r'(<table[^>]*class="[^"]*)type02([^"]*"[^>]*>)'
    
    # すでに type02c が入っていないか確認しながら置換
    # (二重追加を防ぐ)
    if 'type02c' in content:
        print(f"Skipping {os.path.basename(filepath)} (type02c already exists).")
        continue
        
    new_content, count = re.subn(table_pattern, r'\1type02 type02c\2', content, flags=re.IGNORECASE)
    
    if count > 0:
        with open(filepath, "w", encoding="cp932", errors="ignore") as f:
            f.write(new_content)
        print(f"Added type02c to {count} table(s) in: {os.path.basename(filepath)}")
        count_modified += 1
    else:
        # 完全に一致する class="type02" の文字置換フォールバック
        if 'class="type02"' in content and 'type02c' not in content:
            new_content = content.replace('class="type02"', 'class="type02 type02c"')
            with open(filepath, "w", encoding="cp932", errors="ignore") as f:
                f.write(new_content)
            print(f"Added type02c (direct string) in: {os.path.basename(filepath)}")
            count_modified += 1

print(f"Modified {count_modified} file(s) out of {len(map_files)} files.")
print("--- Add Table Class type02c in Map Files End ---")
