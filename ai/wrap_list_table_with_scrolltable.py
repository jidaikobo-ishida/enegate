# -*- coding: utf-8 -*-

html_path = "company/list/list.html"

with open(html_path, "r", encoding="cp932", errors="ignore") as f:
    html = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
html_crlf = html.replace("\r\n", "\n").replace("\n", "\r\n")

# table.type02b を <div class="scrolltable"> で囲む
# 開始部分の置換
target_start = """						<table class="type02 type02b">"""
replacement_start = """						<div class="scrolltable">
						<table class="type02 type02b">"""

# 終了部分の置換
# (179行目の </table>\n\t\t\t\t\t\t<div class="boxBtm"> 付近)
target_end = """						</table>
						<div class="boxBtm">"""

replacement_end = """						</table>
						</div>
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
    print("Successfully wrapped table.type02b in list.html with div.scrolltable.")
else:
    print("Error: Target table tags not found in list.html.")
