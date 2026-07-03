# -*- coding: utf-8 -*-
import re

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 行番号 3198 から 3280 付近の max-width: 950px に関連する5つのメディアクエリブロックを正確にコメントアウト
start_marker = "/* ==========================================================\n   画面幅950px以下における大枠の固定最小幅(min-width)解除"
end_marker = "    #header .logo {\n        margin: 14px 0 27px !important;\n    }\n}"

idx_start = content_lf.find(start_marker)
idx_end = content_lf.find(end_marker)

if idx_start != -1 and idx_end != -1:
    end_pos = idx_end + len(end_marker)
    sub_block = content_lf[idx_start:end_pos]
    
    # 内側の */ を無効化して安全にコメントアウト
    safe_sub = sub_block.replace("*/", "* /")
    replacement_sub = f"/* COMMENTED OUT TEMPORARILY BY USER REQUEST\n{safe_sub}\nEND COMMENTED OUT */"
    
    content_lf = content_lf.replace(sub_block, replacement_sub)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully commented out max-width: 950px media queries in common.css.")
else:
    print("Failed to locate target markers in CSS.")
