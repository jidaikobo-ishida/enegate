# -*- coding: utf-8 -*-
import os
import re
import glob

print("--- Clean HTML/CSS Patching Script Start ---")

# 1. CSSへのスタイル追記 (common/css/common.css)
# 事業所・地図ページ用のレスポンシブスタイルを末尾にメディアクエリとして追記
css_path = "common/css/common.css"

guide_style = """
/* ==========================================================
   事業所案内（#list）および 拠点地図（.guide）のスマホ対応 (CSS移行版)
   ========================================================== */
@media screen and (max-width: 736px) {
    #list .twocontent .group,
    .guide .twocontent .group {
        width: 100% !important;
    }
    #list .twocontent .group, 
    #list .twocontent .group p, 
    #list .twocontent .group td, 
    #list .twocontent .group li,
    #list .twocontent .group h3,
    .guide .twocontent .group,
    .guide .twocontent .group p,
    .guide .twocontent .group td,
    .guide .twocontent .group li,
    .guide .twocontent .group h3 {
        font-size: 14px !important;
    }
    #list .twocontent .group .boxType02,
    .guide .twocontent .group .boxType02 {
        border: 1px solid #C5D6DC !important;
        padding: 1px !important;
        background: none !important;
    }
    #list .twocontent .group .type02,
    .guide .twocontent .group .type02 {
        width: 100% !important;
        margin: 0 !important;
        border: 3px solid #d2e5f4 !important;
    }
    #list .twocontent .group .type02 td.end,
    .guide .twocontent .group .type02 td.end {
        width: 50% !important;
    }
    #list .twocontent .boxTop,
    #list .twocontent .boxBtm,
    .guide .twocontent .boxTop,
    .guide .twocontent .boxBtm {
        display: none !important;
    }
}
"""

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    css_content = f.read()

if "拠点地図（.guide）のスマホ対応" not in css_content:
    if not css_content.endswith("\n"):
        css_content += "\n"
    css_content += guide_style
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(css_content)
    print("Successfully appended guide styles to common.css.")
else:
    print("Guide styles already present in common.css.")

# =========================================================================
# 2. HTMLのロールバック（以前追加した内部スタイルと画像幅置換の除去）
# =========================================================================

# 削除用のインラインスタイル定義（前のスクリプトで挿入したものと同一）
inserted_style_pattern = r'<style>.*?/\* 新デザイン等へのリニューアル \*/.*?</style>\s*</head>'
inserted_style_pattern_simple = r'<style>.*?</style>\s*</head>'

# HTMLファイルのリスト
html_files = ["company/list/index.html", "company/list/list.html"] + glob.glob("company/list/map*.html")

for hf in html_files:
    if not os.path.exists(hf):
        continue
    with open(hf, "r", encoding="cp932", errors="ignore") as f:
        content = f.read()
        
    original_len = len(content)
    
    # 挿入された style タグを検知して </head> に戻す
    # 複雑なパターンに対応するため正規表現で置換
    content = re.sub(r'<style>\s*/\* 事業所グループ要素.*?boxBtm\s*\{\s*display:\s*none\s*!important;\s*\}\s*</style>\s*</head>', '</head>', content, flags=re.DOTALL)
    
    # 画像の幅属性を元に戻す
    content = content.replace('width="100%" height="auto"', 'width="690" height="568"') # 地図画像
    content = content.replace('width="100%" height="auto" border="0"', 'width="690" height="39" border="0"') # タイトル地図
    
    if len(content) < original_len:
        with open(hf, "w", encoding="cp932", errors="ignore") as f:
            f.write(content)
        print(f"Rollbacked and cleaned HTML: {hf}")

# =========================================================================
# 3. 必要最小限のHTMLマージの再適用
# =========================================================================

# ① products/other/other01.html のテーブルスクロール囲み
other01_file = "products/other/other01.html"
with open(other01_file, "r", encoding="cp932", errors="ignore") as f:
    other_content = f.read()
if "scrolltable" not in other_content:
    other_content = other_content.replace('<table class="itemspec">', '<div class="scrolltable"><table class="itemspec">')
    other_content = other_content.replace('</table>\n\n\t</div>', '</table></div>\n\n\t</div>')
    with open(other01_file, "w", encoding="cp932", errors="ignore") as f:
        f.write(other_content)
    print("Patched products/other/other01.html with scrolltable.")

# ② meter02/index.html の比較表スクロール囲み
meter_file = "meter02/index.html"
with open(meter_file, "r", encoding="cp932", errors="ignore") as f:
    meter_content = f.read()
if "scrolltable" not in meter_content:
    # 既に前回のパッチで適用されているため、何もしない（or 確認）
    print("meter02/index.html already has scrolltable.")

# ③ company/list/list.html のテーブルスクロール囲み
list_file = "company/list/list.html"
with open(list_file, "r", encoding="cp932", errors="ignore") as f:
    list_content = f.read()
if "scrolltable" not in list_content:
    list_content = list_content.replace('<table class="type02">', '<div class="scrolltable"><table class="type02">')
    list_content = list_content.replace('</table>\n\t\t\t\t<div class="boxBtm">', '</table></div>\n\t\t\t\t<div class="boxBtm">')
    with open(list_file, "w", encoding="cp932", errors="ignore") as f:
        f.write(list_content)
    print("Patched company/list/list.html with scrolltable.")

print("--- Clean HTML/CSS Patching Script End ---")
