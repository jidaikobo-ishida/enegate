# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# #topics .topicslist dd に border: none !important; および width: 100% !important; を追加する
target = """    #topics .topicslist dd {
        padding: 0 !important;
        margin: 0 0 20px !important;
        text-indent: 0 !important;
    }"""

replacement = """    #topics .topicslist dd {
        padding: 0 !important;
        margin: 0 0 20px !important;
        text-indent: 0 !important;
        border: none !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_crlf = target.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully updated #topics .topicslist dd border and width in common.css.")
else:
    print("Error: Target marker not found in common.css.")
