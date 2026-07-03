# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# #division #kanri .sctxt に clear: both !important; を追加する
target = """    /* スマホ時の事業内容(#division #kanri)のsctxt要素の100%幅化・フロート解除 */
    #division #kanri .sctxt {
        width: 100% !important;
        float: none !important;
    }"""

replacement = """    /* スマホ時の事業内容(#division #kanri)のsctxt要素の100%幅化・フロート解除 */
    #division #kanri .sctxt {
        width: 100% !important;
        float: none !important;
        clear: both !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_crlf = target.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added clear:both to #division #kanri .sctxt in common.css.")
else:
    print("Error: Target marker not found in common.css.")
