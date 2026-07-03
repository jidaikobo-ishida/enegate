# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# ファイルの末尾にヘッダーとグローバルメニューの調整用メディアクエリを追記
new_block = """

/* ==========================================================
   画面幅950px以下におけるヘッダーサブナビゲーション位置調整
   ========================================================== */
@media screen and (max-width: 950px) {
    #header .hdsub {
        left: auto !important;
        right: 320px !important;
    }
}

/* ==========================================================
   画面幅950px以下からスマホサイズ(737px)までのグローバルメニュー余白調整
   ========================================================== */
@media screen and (max-width: 950px) and (min-width: 737px) {
    #glmenu {
        margin-left: -15px !important;
    }
}
"""

content_lf += new_block

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("Successfully appended header and glmenu responsive styles to common.css.")
