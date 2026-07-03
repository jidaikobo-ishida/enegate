# -*- coding: utf-8 -*-

html_path = "company/list/list.html"

with open(html_path, "r", encoding="cp932", errors="ignore") as f:
    html = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
html_crlf = html.replace("\r\n", "\n").replace("\n", "\r\n")

# 追加した <div class="scrolltable"> およびその閉じ </div> を削除する
target_start = """						<div class="scrolltable">
						<table class="type02 type02b">"""
replacement_start = """						<table class="type02 type02b">"""

target_end = """						</table>
						</div>
						<div class="boxBtm">"""
replacement_end = """						</table>
						<div class="boxBtm">"""

# 厳格に CRLF でマーカーを構築
target_start_crlf = target_start.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_start_crlf = replacement_start.replace("\r\n", "\n").replace("\n", "\r\n")
target_end_crlf = target_end.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_end_crlf = replacement_end.replace("\r\n", "\n").replace("\n", "\r\n")

if target_start_crlf in html_crlf and target_end_crlf in html_crlf:
    html_crlf = html_crlf.replace(target_start_crlf, replacement_start_crlf)
    html_crlf = html_crlf.replace(target_end_crlf, replacement_end_crlf)
    
    # 書き込み (厳格に cp932 エンコーディング)
    with open(html_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(html_crlf)
    print("Successfully removed div.scrolltable from list.html.")
else:
    print("Error: Target tags to remove not found in list.html.")
