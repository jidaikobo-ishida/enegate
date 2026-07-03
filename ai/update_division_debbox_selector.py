# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# #division .debbox を #division .devbox.debbox に安全に一括置換
updated_content = content_crlf.replace("#division .debbox", "#division .devbox.debbox")

if updated_content != content_crlf:
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(updated_content)
    print("Successfully replaced #division .debbox with #division .devbox.debbox in common.css.")
else:
    print("Error: Target selector patterns not found in common.css.")
