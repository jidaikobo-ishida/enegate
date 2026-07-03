# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# #topics .bltitle.underline に対する margin: 0 !important;
topics_title_styles = """
    /* スマホ時のトピックス見出し(#topics .bltitle.underline)の余白リセット */
    #topics .bltitle.underline {
        margin: 0 !important;
    }"""

# トピックスリスト調整（末尾部分）の直後に挿入する
target_marker = """    #topics .topicslist dd a span {
        position: absolute !important;
        left: 0 !important;
        top: 0 !important;
        margin-right: 0 !important; /* PC用の右マージンを解除 */
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + topics_title_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added margin:0 to #topics .bltitle.underline in common.css.")
else:
    print("Error: Target marker not found in common.css.")
