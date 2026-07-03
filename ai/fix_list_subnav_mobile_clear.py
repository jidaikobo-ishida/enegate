# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# スマホメディアクエリの中（「事業所案内（#list）および 拠点地図（.guide）のスマホ対応」の直下）に
# #list .leftsubnav のクリア指定を追加する
target = """/* ==========================================================
   事業所案内（#list）および 拠点地図（.guide）のスマホ対応 (CSS移行版)
   ========================================================== */
@media screen and (max-width: 736px) {"""

replacement = """/* ==========================================================
   事業所案内（#list）および 拠点地図（.guide）のスマホ対応 (CSS移行版)
   ========================================================== */
@media screen and (max-width: 736px) {
    #list .leftsubnav {
        width: 100% !important;
        float: none !important;
        margin: 15px 0 !important;
        box-sizing: border-box !important;
    }"""

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added smartphone clear rules for #list .leftsubnav in common.css.")
else:
    print("Target comment marker for mobile clear not found.")
