# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# ご指定の3と5に関するスマホ用フロート解除スタイル定義
selected_float_styles = """
    /* スマホ時の事業所ページ(#jigyousyo)の各種フロート解除 */
    #jigyousyo .sch2,
    #jigyousyo .sctxt,
    #jigyousyo #kanri .sctxt,
    #jigyousyo .kanribox .kanriimg,
    #jigyousyo .kanribox .kanritxt,
    #jigyousyo .infotxt .txtbox,
    #jigyousyo .infotxt .imgbox,
    #jigyousyo .voicebox .txtbox,
    #jigyousyo .voicebox .imgbox {
        float: none !important;
    }
    
    /* スマホ時の環境・品質ページ(#kankyou/#quality)のフロート解除・自動幅化 */
    #kankyou .noinfo,
    #kankyou .pdfinfo,
    #quality .noinfo,
    #quality .pdfinfo {
        float: none !important;
        width: auto !important;
    }"""

# 先ほど追加した .voicebox 一括パディング（3220行目付近）の直後に挿入する
target_marker = """    /* スマホ時の先輩の声(.voicebox)一括パディング・余白リセット調整 */
    .voicebox {
        padding: 15px !important;
        box-sizing: border-box !important;
    }
    .voicebox .txtbox,
    .voicebox .imgbox {
        margin: 0 auto !important;
        float: none !important;
        width: 100% !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + selected_float_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added selected float:none styles to common.css.")
else:
    print("Error: Target marker not found in common.css.")
