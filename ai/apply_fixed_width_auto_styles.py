# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# スマホ表示時に width: 734px 以上の固定幅要素を width: auto に変更するスタイル
fixed_width_auto_styles = """
    /* 画面幅736px以下におけるPC用固定幅要素(734px以上)の自動幅化・つっかえ棒解除 */
    .inner,
    .inner900,
    .twocontent,
    #globalnav ul,
    #mainimg .mainlogo P,
    #Imgnav .Imgnavwrap,
    #productsnav .prosnavwrap,
    #allproductsnav .prosnavwrap,
    #footer .fwrap,
    #iteminfo .section,
    #iteminfo .ecobanner,
    #jirei .section,
    #jireisin .section,
    #metainfo .section,
    #eco .section {
        width: auto !important;
        max-width: 100% !important;
    }
    
    #content,
    #fnav {
        min-width: auto !important;
        width: auto !important;
    }"""

# SDGs 関連スタイルの直後（スマホメディアクエリ終了 } の直前）に挿入する
target_marker = """    #sdgs .allitem {
        background-image: none !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + fixed_width_auto_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully applied fixed width auto styles to common.css.")
else:
    print("Error: Target marker not found in common.css.")

