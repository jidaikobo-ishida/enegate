# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# ファイルの末尾に、画面幅950px以下の時の width リセット用メディアクエリを追記
new_block = """

/* ==========================================================
   画面幅950px以下における大枠の固定横幅(width)解除
   ========================================================== */
@media screen and (max-width: 950px) {
    .inner,
    .inner900,
    #content,
    #globalnav ul,
    #Imgnav .Imgnavwrap,
    #productsnav .prosnavwrap,
    #allproductsnav .prosnavwrap,
    #fnav,
    #footer .fwrap,
    #list #article,
    #iteminfo .section,
    #iteminfo .ecobanner,
    #jirei .section,
    #jireisin .section,
    #metainfo .section,
    #eco .section {
        width: auto !important;
    }
}
"""

content_lf += new_block

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("Successfully appended width reset media query to common.css.")
