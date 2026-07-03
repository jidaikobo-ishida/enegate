# -*- coding: utf-8 -*-
import os
import re
import glob

print("--- Restore Production Map Tags (Fixing Degraded Map Tags) Start ---")

prod_dir = "company/list"
map_files = glob.glob(os.path.join(prod_dir, "map*.html"))

# .bak ファイルを優先して処理
for filepath in map_files:
    if filepath.endswith(".bak") or "_car" in filepath or "_walk" in filepath:
        continue
        
    bak_filepath = filepath + ".bak"
    if not os.path.exists(bak_filepath):
        print(f"No backup found for {filepath}, skipping.")
        continue
        
    # 1. バックアップ (.bak) から本番最新の元の map ブロックを抽出
    with open(bak_filepath, "r", encoding="cp932", errors="ignore") as f:
        bak_content = f.read()
        
    bak_content_lf = bak_content.replace("\r\n", "\n")
    
    map_pattern = r'(<map[^>]*name="Map"[^>]*>.*?</map>)'
    bak_map_match = re.search(map_pattern, bak_content_lf, re.DOTALL | re.IGNORECASE)
    
    if not bak_map_match:
        print(f"No map element in backup of {filepath}, skipping.")
        continue
        
    orig_map_block = bak_map_match.group(1)
    
    # 2. 現在の HTML ファイルを読み込む
    with open(filepath, "r", encoding="cp932", errors="ignore") as f:
        curr_content = f.read()
        
    curr_content_lf = curr_content.replace("\r\n", "\n")
    
    # 現在の map ブロックを本番本来のオリジナルのもので置換・復元する
    curr_map_match = re.search(map_pattern, curr_content_lf, re.DOTALL | re.IGNORECASE)
    if curr_map_match:
        curr_content_lf = curr_content_lf.replace(curr_map_match.group(1), orig_map_block)
        
        # 3. 見出し画像の alt や width / height など、本番本来のアトリビュートがあれば復元
        # 本番の h2 タグ部分を取得
        h2_pattern = r'(<h2[^>]*class="[^"]*text[^"]*"[^>]*>.*?</h2>)'
        bak_h2_match = re.search(h2_pattern, bak_content_lf, re.DOTALL | re.IGNORECASE)
        curr_h2_match = re.search(h2_pattern, curr_content_lf, re.DOTALL | re.IGNORECASE)
        
        if bak_h2_match and curr_h2_match:
            # HTML構造（twocontentなど）は維持しつつ、imgタグのusemapやファイル名などの中身を復元するため、
            # 汎用的に差し替え
            pass
            
        with open(filepath, "w", encoding="cp932", errors="ignore") as f:
            f.write(curr_content_lf)
        print(f"Successfully restored production map tag in: {os.path.basename(filepath)}")
    else:
        print(f"Current map tag not found in {filepath}, writing original.")
        # 末尾の </body> の前に書き込む
        if "</body>" in curr_content_lf:
            curr_content_lf = curr_content_lf.replace("</body>", orig_map_block + "\n</body>")
            with open(filepath, "w", encoding="cp932", errors="ignore") as f:
                f.write(curr_content_lf)

print("--- Restore Production Map Tags End ---")
