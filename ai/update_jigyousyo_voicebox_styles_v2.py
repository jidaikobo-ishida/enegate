# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

target = """    /* .voicebox h3.bldottitle のスマホ版調整 */
    .voicebox h3.bldottitle {
        width: -webkit-calc(100% - 20px) !important;
        width: calc(100% - 20px) !important;
        margin: 20px 10px 10px !important;
    }"""

replacement = """    /* .voicebox h3.bldottitle のスマホ版調整 */
    .voicebox h3.bldottitle {
        width: -webkit-calc(100% - 20px) !important;
        width: calc(100% - 20px) !important;
        margin: 0 auto 10px !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_crlf = target.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully updated .voicebox h3.bldottitle margin to 0 auto 10px.")
else:
    print("Error: Target marker not found in common.css.")
