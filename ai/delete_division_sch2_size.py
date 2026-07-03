# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 2509行目の定義から width:100%; height: auto; を削除する
target = """#division .sch2 { width:100%; height: auto; margin-bottom:15px; padding:10px; font-size:1.5em; float:none;}"""
replacement = """#division .sch2 { margin-bottom:15px; padding:10px; font-size:1.5em; float:none;}"""

# 厳格に CRLF でマーカーを構築
target_crlf = target.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully deleted width and height from #division .sch2 in common.css.")
else:
    # 部分一致（スペースの差異など）に備えてフォールバック
    target_fallback = """#division .sch2 { width:100%; height:auto; margin-bottom:15px; padding:10px; font-size:1.5em; float:none;}"""
    target_fallback_crlf = target_fallback.replace("\r\n", "\n").replace("\n", "\r\n")
    if target_fallback_crlf in content_crlf:
        content_crlf = content_crlf.replace(target_fallback_crlf, replacement_crlf)
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content_crlf)
        print("Successfully deleted width and height (fallback match) in common.css.")
    else:
        print("Error: Target marker not found in common.css.")
