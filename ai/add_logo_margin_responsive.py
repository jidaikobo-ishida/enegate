# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# ファイルの末尾に、指定された画面幅範囲でのヘッダーロゴマージン調整メディアクエリを追記
new_block = """

/* ==========================================================
   画面幅810px以下から737pxまでのヘッダーロゴマージン調整
   ========================================================== */
@media screen and (max-width: 810px) and (min-width: 737px) {
    #header .logo {
        margin: 14px 0 !important;
    }
}
"""

content_lf += new_block

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("Successfully appended header logo margin responsive style to common.css.")
