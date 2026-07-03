# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 地図アクセス見出しのスマホ用スタイル定義
access_title_styles = """
    /* スマホ時の地図ページ.type02cアクセス見出し調整 */
    .type02c h4.access img {
        display: none !important; /* ← 画像を非表示 */
    }
    .type02c h4.access::before {
        content: 'ACCESS' !important;               /* ← テキストを表示 */
        font-size: 1em !important;
        color: #4055b2 !important;                  /* ← 文字色：青色 */
        background: #dceffd !important;             /* ← 背景色：水色 */
        display: block !important;
        padding: 0.2rem 0.5rem !important;          /* ← 内側余白を設定 */
    }"""

# Googleマップエリアフロート解除（直前に追記した部分）の直後に挿入する
target_marker = """    #google div.main p {
        margin: 0 auto !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_marker_crlf = target_marker.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = target_marker_crlf + access_title_styles.replace("\r\n", "\n").replace("\n", "\r\n")

if target_marker_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_marker_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully restored type02c access title styles in common.css.")
else:
    print("Error: Target marker not found in common.css.")
