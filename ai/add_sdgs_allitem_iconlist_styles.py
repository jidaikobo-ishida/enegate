# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# #sdgs .allitem .iconlist のスマホ用スタイル定義
allitem_styles = """
    #sdgs .allitem .iconlist {
        justify-content: space-around !important;
        gap: 1.5% !important;
    }"""

# SDGsアイコンリストのダミー要素（::after）定義（3168行目付近）の直後に挿入する
target_marker = """    #sdgs .iconlist::after {
        content: "" !important;
        flex-basis: 31% !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + allitem_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added styles to #sdgs .allitem .iconlist in common.css.")
else:
    print("Error: Target marker not found in common.css.")
