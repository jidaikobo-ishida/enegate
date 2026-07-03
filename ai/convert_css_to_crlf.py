# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全ての LF (\n) を CRLF (\r\n) に変換する
# (すでに CRLF になっている箇所が二重に \r\r\n にならないように安全に処理)
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_crlf)

print("Successfully converted common.css line endings to CRLF and saved as cp932.")
