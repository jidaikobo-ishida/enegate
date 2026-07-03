# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行 of まま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# div.main および #google div.main の float: none !important; スタイル定義
float_none_styles = """
    /* スマホ時のGoogleマップエリア(div.main/div.sub)のフロート解除・中央寄せ調整 */
    div.main,
    #google div.main,
    #google div.sub {
        float: none !important;
        width: auto !important;
    }
    #google div.main p {
        margin: 0 auto !important;
    }"""

# jigyousyo .voicebox の padding（直前に追記した部分）の直後に挿入する
target_marker = """    #jigyousyo .voicebox {
        padding: 15px !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + float_none_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added float:none to div.main in common.css.")
else:
    print("Error: Target marker not found in common.css.")
