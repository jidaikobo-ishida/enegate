# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# #header .logo のマージン指定（@media ... 810px ...）の直下に
# .rflt, .lflt の float 解除指定を追記する
target = """/* ==========================================================
   画面幅810px以下から737pxまでのヘッダーロゴマージン調整
   ========================================================== */
@media screen and (max-width: 810px) and (min-width: 737px) {
    #header .logo {
        margin: 14px 0 27px !important;
    }
}"""

replacement = """/* ==========================================================
   画面幅810px以下から737pxまでのヘッダーロゴマージン調整
   ========================================================== */
@media screen and (max-width: 810px) and (min-width: 737px) {
    #header .logo {
        margin: 14px 0 27px !important;
    }
}

/* ==========================================================
   スマホ表示（736px以下）における左右フロートの一括解除
   ========================================================== */
@media screen and (max-width: 736px) {
    .rflt,
    .lflt {
        float: none !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added .rflt and .lflt float: none style to common.css.")
else:
    print("Target comment marker for floats reset not found.")
