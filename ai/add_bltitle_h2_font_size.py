# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# .bltitle h2 に対する font-size: 1.4em !important;
bltitle_styles = """
    /* スマホ時の青帯付き見出し(.bltitle h2)のフォントサイズ調整 */
    .bltitle h2 {
        font-size: 1.4em !important;
    }"""

# 青ドット見出し調整（直前に追記した部分）の直後に挿入する
target_marker = """    /* スマホ時の青丸付き見出し(.bldottitle)のパディング・フロート解除調整 */
    .bldottitle {
        float: none !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + bltitle_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added font-size to .bltitle h2 in common.css.")
else:
    print("Error: Target marker not found in common.css.")
