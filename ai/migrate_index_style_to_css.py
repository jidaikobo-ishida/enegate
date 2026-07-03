# -*- coding: utf-8 -*-
import os
import re

print("--- Migrate Index Style to common.css Start ---")

html_path = "company/list/index.html"
css_path = "common/css/common.css"

# 1. common.css にスマホ用スタイルを追記
with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    css_content = f.read()

css_lf = css_content.replace("\r\n", "\n")

# スマホメディアクエリ（736px以下）の左右フロート解除の直下に追記する
target_css_marker = """/* ==========================================================
   スマホ表示（736px以下）における左右フロートの一括解除
   ========================================================== */
@media screen and (max-width: 736px) {
    .rflt,
    .lflt {
        float: none !important;
    }
}"""

inserted_style = """/* ==========================================================
   スマホ表示（736px以下）における左右フロートの一括解除
   ========================================================== */
@media screen and (max-width: 736px) {
    .rflt,
    .lflt {
        float: none !important;
    }
    
    /* 事業所グループ要素の幅100%化とテキストサイズ14px統一 */
    .twocontent .group {
        width: 100% !important;
    }
    .twocontent .group, 
    .twocontent .group p, 
    .twocontent .group td, 
    .twocontent .group li,
    .twocontent .group h3 {
        font-size: 14px !important;
    }
    /* 新しいデザイン構造へのリニューアル */
    .twocontent .group .boxType02 {
        border: 1px solid #C5D6DC !important;
        padding: 1px !important;
        background: none !important;
    }
    .twocontent .group .type02 {
        width: 100% !important;
        margin: 0 !important;
        border: 3px solid #d2e5f4 !important;
    }
    .twocontent .group .type02 td.end {
        width: 50% !important;
    }
    .twocontent .boxTop,
    .twocontent .boxBtm {
        display: none !important;
    }
}"""

target_css_marker_lf = target_css_marker.replace("\r\n", "\n")
inserted_style_lf = inserted_style.replace("\r\n", "\n")

if target_css_marker_lf in css_lf:
    css_lf = css_lf.replace(target_css_marker_lf, inserted_style_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(css_lf)
    print("Successfully added styles to common.css.")
else:
    print("CSS target marker not found.")

# 2. company/list/index.html のインライン <style> タグを削除
if os.path.exists(html_path):
    with open(html_path, "r", encoding="cp932", errors="ignore") as f:
        html_content = f.read()
        
    html_lf = html_content.replace("\r\n", "\n")
    
    # <style> から </style> までのブロックを探して削除
    style_pattern = r'(<style>.*?\.twocontent\s+\.boxBtm\s*\{.*?\}\s*</style>\s*)'
    match_style = re.search(style_pattern, html_lf, re.DOTALL)
    
    if match_style:
        html_lf = html_lf.replace(match_style.group(1), "")
        with open(html_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(html_lf)
        print("Successfully removed inline style block from index.html.")
    else:
        # もう少し広いパターンでのマッチング
        style_pattern_broad = r'(<style>.*?事業所グループ要素.*?display:\s*none\s*!important;\s*\}\s*</style>\s*)'
        match_style_broad = re.search(style_pattern_broad, html_lf, re.DOTALL)
        if match_style_broad:
            html_lf = html_lf.replace(match_style_broad.group(1), "")
            with open(html_path, "w", encoding="cp932", errors="ignore") as f:
                f.write(html_lf)
            print("Successfully removed inline style block from index.html (broad).")
        else:
            print("Inline style block not found in index.html.")
else:
    print("index.html not found.")

print("--- Migrate Index Style to common.css End ---")
