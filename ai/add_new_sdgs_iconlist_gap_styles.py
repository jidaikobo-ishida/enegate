# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# SDGsアイコンリストの新しい gap & flex-basis スタイル定義
new_iconlist_styles = """
    /* SDGsアイコンリストのグリッド表示 (gap & flex-basis レイアウト) */
    #sdgs .iconlist {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 15px !important;
    }
    #sdgs .iconlist li {
        flex-basis: calc((100% - 45px) / 4) !important;
        margin: 0 !important;
        float: none !important;
    }"""

# imglg a（3150行目付近）の定義の直後に挿入する
target_marker = """    .imglg a {
        flex: 1 !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + new_iconlist_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added new gap & flex-basis styles for #sdgs .iconlist to common.css.")
else:
    print("Error: Target marker not found in common.css.")
