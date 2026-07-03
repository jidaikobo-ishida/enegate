# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 1. /* と */ のペア数をチェック
open_comments = content_lf.count("/*")
close_comments = content_lf.count("*/")
print(f"/* count: {open_comments}, */ count: {close_comments}")

# コメントアウトが壊れている（ネストされている）箇所がないか調べる
# コメントをすべて空文字に置換し、中括弧 { } の不整合をチェックする
# 単純な正規表現でコメントを除去（ただしネストは考慮できないので、標準的な非グリーディマッチ）
# /* から */ までのマッチを除去
temp_css = content_lf
# コメント削除ループ（ネストしていないコメントを一掃）
while "/*" in temp_css:
    # 最初の /* と 最初の */ を探して除去
    start = temp_css.find("/*")
    end = temp_css.find("*/")
    if end == -1:
        print("Error: Found unmatched /* comment start without */")
        break
    if end < start:
        print(f"Warning: Found unmatched */ before /* at position {end}")
        # その */ を一時的に退避
        temp_css = temp_css[:end] + " [CLOSE_ERR] " + temp_css[end+2:]
        continue
    temp_css = temp_css[:start] + temp_css[end+2:]

# 残った中括弧 { } の数をチェック
open_braces = temp_css.count("{")
close_braces = temp_css.count("}")
print(f"{{ count: {open_braces}, }} count: {close_braces}")

if open_braces != close_braces:
    print(f"Error: Braces mismatch! Open: {open_braces}, Close: {close_braces}")
    
    # どこでズレているか特定するための簡易インデント・パーサ
    indent = 0
    lines = temp_css.split("\n")
    for i, line in enumerate(lines):
        line = line.strip()
        o = line.count("{")
        c = line.count("}")
        indent += o - c
        if indent < 0:
            print(f"Braces went negative at line {i+1}: {line}")
            indent = 0
else:
    print("Braces matched successfully.")

