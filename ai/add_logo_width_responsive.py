# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# #header .hdsub の指定がある @media screen and (max-width: 950px) ブロックを探して、
# その直下に #header .logo { width: 250px !important; } を追記する
target = """/* ==========================================================
   画面幅950px以下におけるヘッダーサブナビゲーション位置調整
   ========================================================== */
@media screen and (max-width: 950px) {
    #header .hdsub {
        left: auto !important;
        right: 320px !important;
    }
}"""

replacement = """/* ==========================================================
   画面幅950px以下におけるヘッダーサブナビゲーション位置調整
   ========================================================== */
@media screen and (max-width: 950px) {
    #header .hdsub {
        left: auto !important;
        right: 320px !important;
    }
    #header .logo {
        width: 250px !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added #header .logo width style to common.css.")
else:
    print("Target comment marker for logo width not found.")
