# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 1行ずつスキャンして、コメントのネストや、閉じられていないコメント、余計な閉じコメントを探す
lines = content_lf.split("\n")
comment_level = 0

for i, line in enumerate(lines):
    # 行内の /* と */ をカウント
    # 複数ある場合を考慮して、左から右へスキャン
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
                print(f"Mismatch: Extra */ found at line {i+1}: {line}")
                comment_level = 0 # リセットして続ける

if comment_level > 0:
    print(f"Mismatch: CSS ends with unclosed comments! Level: {comment_level}")
else:
    print("Comment scan complete.")
