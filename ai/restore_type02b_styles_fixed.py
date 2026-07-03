# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

type02b_styles = """
/* ==========================================================
   事業所・地図ページ（#list）の通常テキスト・テーブルフォントサイズ適正化
   ========================================================== */
#list .twocontent p,
#list .twocontent h3,
#list .twocontent ul,
#list .twocontent .type02b td,
#list .twocontent .type02b th
{
    font-size: 1.4em !important;
}

#list .twocontent ul p{
    font-size: initial;
}"""

target_marker = """/* ==========================================================
   スマホ表示（736px以下）時の追加レスポンシブ・カスタマイズ
   ========================================================== */"""

target_marker_lf = target_marker.replace("\r\n", "\n")

if target_marker_lf in content_lf:
    content_lf = content_lf.replace(target_marker_lf, type02b_styles + "\n\n" + target_marker_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully restored type02b font styles in common.css.")
else:
    print("Error: Target marker not found in common.css.")
