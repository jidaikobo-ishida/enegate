# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# jigyousyo .voicebox .txtbox の margin: 0 auto !important; スタイル定義
voicebox_margin_styles = """
    /* スマホ時の#jigyousyo先輩の声テキストボックスの余白・中央寄せ調整 */
    #jigyousyo .voicebox .txtbox {
        margin: 0 auto !important;
        float: none !important;
    }"""

# SDGs画像の引き伸ばし防止（3227行目付近）の直後、スマホメディアクエリ終了の } の直前に挿入する
target_marker = """    #sdgs .img img,
    #sdgs .imglg img {
        width: auto !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + voicebox_margin_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added margin:0 auto to #jigyousyo .voicebox .txtbox in common.css.")
else:
    print("Error: Target marker not found in common.css.")
