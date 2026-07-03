# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# スマホメディアクエリ（736px以下）の左右フロート解除の直下に、
# 大枠の固定幅を安全に100%幅に解除するスタイルを追加する
target = """/* ==========================================================
   スマホ表示（736px以下）における左右フロートの一括解除
   ========================================================== */
@media screen and (max-width: 736px) {
    .rflt,
    .lflt {
        float: none !important;
    }"""

replacement = """/* ==========================================================
   スマホ表示（736px以下）における左右フロートの一括解除
   ========================================================== */
@media screen and (max-width: 736px) {
    .rflt,
    .lflt {
        float: none !important;
    }
    
    /* スマホ表示（736px以下）時の大枠固定幅解除 */
    .inner {
        width: 100% !important;
        max-width: 100% !important;
        min-width: auto !important;
        box-sizing: border-box !important;
    }
    #content {
        min-width: auto !important;
        width: 100% !important;
    }"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added mobile inner container width overrides in common.css.")
else:
    print("CSS target marker not found.")
