# -*- coding: utf-8 -*-
import os
import shutil
import glob

print("--- Sync All Map Files to twocontent Structure Start ---")

test_dir = "../enegate-test/company/list"
prod_dir = "company/list"

# テスト環境の map*.html ファイルの一覧を取得
test_maps = glob.glob(os.path.join(test_dir, "map*.html"))

for src_file in test_maps:
    filename = os.path.basename(src_file)
    dst_file = os.path.join(prod_dir, filename)
    
    if os.path.exists(dst_file):
        # バックアップをとってからコピーする
        backup_file = dst_file + ".bak"
        shutil.copy2(dst_file, backup_file)
        
        # テスト環境のクリーンな HTML 構造のファイルを本番環境へ上書きコピー
        shutil.copy2(src_file, dst_file)
        print(f"Successfully synced: {filename}")
    else:
        print(f"Skipping {filename} (does not exist in prod).")

print("--- Sync All Map Files to twocontent Structure End ---")
