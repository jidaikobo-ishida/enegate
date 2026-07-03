# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# ファイルの末尾に、画面幅950px以下の時の min-width リセット用メディアクエリを追記
new_block = """

/* ==========================================================
   画面幅950px以下における大枠の固定最小幅(min-width)解除
   ========================================================== */
@media screen and (max-width: 950px) {
    #content,
    #fnav {
        min-width: auto !important;
    }
}
"""

content_lf += new_block

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("Successfully appended min-width reset media query to common.css.")
