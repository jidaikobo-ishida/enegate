# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# コメントを除去したクリーンなCSSを作成
temp_css = content_lf
while "/*" in temp_css:
    start = temp_css.find("/*")
    end = temp_css.find("*/")
    if end == -1:
        temp_css = temp_css[:start]
        break
    temp_css = temp_css[:start] + temp_css[end+2:]

# 各行の中括弧ネストレベルを追跡
lines = temp_css.split("\n")
depth = 0

for i, line in enumerate(lines):
    line_stripped = line.strip()
    
    # 1文字ずつスキャンして depth を追跡
    # 行番号を元のファイルの行と対応させるため、空行やコメント除去後の行と突き合わせる必要があるが、
    # 簡易的に、この temp_css の行を調べる。
    orig_depth = depth
    for char in line:
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                print(f"Error: Depth went negative at line {i+1}: {line_stripped}")
                depth = 0
                
    # 2650行目付近（.scrolltableの定義場所）での depth を監視する
    # .scrolltable というキーワードが含まれている行
    if ".scrolltable" in line_stripped:
        print(f"FOUND: .scrolltable at line {i+1} (depth: {depth}, text: {line_stripped[:100]})")
        
    # @media screen and (max-width: 736px) の depth を監視
    if "@media screen and (max-width: 736px)" in line_stripped:
        print(f"MEDIA START: at line {i+1} (depth: {depth})")

