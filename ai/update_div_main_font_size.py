# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# div.main および #google div.main のフォントサイズ 1.4em !important; を適用する
target = """    /* スマホ時のGoogleマップエリア(div.main/div.sub)のフロート解除・中央寄せ調整 */
    div.main,
    #google div.main,
    #google div.sub {
        float: none !important;
        width: auto !important;
    }"""

replacement = """    /* スマホ時のGoogleマップエリア(div.main/div.sub)のフロート解除・中央寄せ調整 */
    div.main,
    #google div.main,
    #google div.sub {
        float: none !important;
        width: auto !important;
    }
    div.main,
    #google div.main {
        font-size: 1.4em !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_crlf = target.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully updated div.main font-size to 1.4em in common.css.")
else:
    print("Error: Target marker not found in common.css.")
