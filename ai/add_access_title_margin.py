# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# .type02c h4.access::before の定義に margin: 1rem auto !important; を追加する
target = """    .type02c h4.access::before {
        content: 'ACCESS' !important;               /* ← テキストを表示 */
        font-size: 1em !important;
        font-weight: bold !important;
        color: #4055b2 !important;                  /* ← 文字色：青色 */
        background: #dceffd !important;             /* ← 背景色：水色 */
        display: block !important;
        padding: 0.2rem 0.5rem !important;          /* ← 内側余白を設定 */
    }"""

replacement = """    .type02c h4.access::before {
        content: 'ACCESS' !important;               /* ← テキストを表示 */
        font-size: 1em !important;
        font-weight: bold !important;
        color: #4055b2 !important;                  /* ← 文字色：青色 */
        background: #dceffd !important;             /* ← 背景色：水色 */
        display: block !important;
        padding: 0.2rem 0.5rem !important;          /* ← 内側余白を設定 */
        margin: 1rem auto !important;               /* ← 上下余白 & 中央寄せ */
    }"""

# 厳格に CRLF でマーカーを構築
target_crlf = target.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added margin:1rem auto to .type02c h4.access::before.")
else:
    print("Error: Target marker not found in common.css.")
