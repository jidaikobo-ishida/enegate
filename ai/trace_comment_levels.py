# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

lines = content_lf.split("\n")
comment_level = 0

for i, line in enumerate(lines):
    orig_level = comment_level
    pos = 0
    while True:
        next_open = line.find("/*", pos)
        next_close = line.find("*/", pos)
        
        if next_open == -1 and next_close == -1:
            break
            
        if next_open != -1 and (next_close == -1 or next_open < next_close):
            comment_level += 1
            pos = next_open + 2
        else:
            comment_level -= 1
            pos = next_close + 2
            if comment_level < 0:
                comment_level = 0
                
    if comment_level != orig_level:
        # レベルが変わった行を出力
        print(f"Line {i+1}: {orig_level} -> {comment_level} | {line.strip()[:100]}")
