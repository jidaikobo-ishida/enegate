# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# division #kanri .sctxt のスマホ用 100% 幅指定
kanri_sctxt_styles = """
    /* スマホ時の事業内容(#division #kanri)のsctxt要素の100%幅化・フロート解除 */
    #division #kanri .sctxt {
        width: 100% !important;
        float: none !important;
    }"""

# 地図用アクセス表の縦並び化（直前に追記した部分）の直後に挿入する
target_marker = """    /* スマホ時の地図ページアクセス表(table.type02c)のセル縦並び化 */
    body#list .twocontent .group .boxType02 table.type02c td {
        display: block !important;
        width: 100% !important;
        box-sizing: border-box !important;
        border: none !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + kanri_sctxt_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added width:100% to #division #kanri .sctxt in common.css.")
else:
    print("Error: Target marker not found in common.css.")
