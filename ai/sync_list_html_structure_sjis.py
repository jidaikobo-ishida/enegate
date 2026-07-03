# -*- coding: utf-8 -*-
import os

print("--- Sync list.html HTML Structure (Shift-JIS) Start ---")

test_path = "../enegate-test/company/list/list.html"
prod_path = "company/list/list.html"

if not os.path.exists(test_path):
    print("Test list.html not found.")
    exit(1)

# テスト環境の list.html を cp932 (Shift-JIS) で読み込む
with open(test_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 改行を LF に統一
content_lf = content.replace("\r\n", "\n")

# メインのテーブル（class="type02"）を <div class="scrolltable"> でラップする
target_table_start = '<table class="type02">'
if target_table_start in content_lf:
    table_index = content_lf.find(target_table_start)
    table_end_index = content_lf.find('</table>', table_index)
    if table_end_index != -1:
        table_end_index += len('</table>')
        table_part = content_lf[table_index:table_end_index]
        wrapped_table = f'<div class="scrolltable">{table_part}</div>'
        content_lf = content_lf[:table_index] + wrapped_table + content_lf[table_end_index:]
        print("Successfully wrapped type02 table with scrolltable (cp932).")

# 本番環境へ cp932 で書き出す
with open(prod_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("Successfully overwritten prod list.html with test structure in Shift-JIS.")
print("--- Sync list.html HTML Structure (Shift-JIS) End ---")
