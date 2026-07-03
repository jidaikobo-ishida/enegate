# -*- coding: utf-8 -*-
import os
import shutil

print("--- Rollback CSS to fnav changes state Start ---")

src_css = "../enegate-test/common/css/common.css"
dst_css = "common/css/common.css"

# 1. テスト環境のベースファイルをコピーしてリセット
shutil.copy2(src_css, dst_css)
print("Copied clean base from test CSS.")

# 2. ベースを読み込む
with open(dst_css, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 3. #allproductsnav と #allproductsnav a の高さ70px同期を適用
target_nav = """#productsnav + #allproductsnav { height:50px;}
#productsnav + #allproductsnav a { height:50px;}"""

replacement_nav = """#productsnav + #allproductsnav { height:70px;}
#productsnav + #allproductsnav a { height:70px; line-height:70px;}"""

content_lf = content_lf.replace(target_nav, replacement_nav)
print("Updated allproductsnav heights.")

# 4. スマホ用メディアクエリの末尾に、fnav変更時点までの追加レスポンシブスタイルを一括追記
# (SDGs、歩み年表、事業所、地図関連などのスタイルはすべて除外します)
sp_end_marker = """    /* tsusin.html専用の導入テキスト余白調整 */
    .tsusin_text {
        padding: 0 15px !important;
    }
}"""

sp_end_replacement = """    /* tsusin.html専用の導入テキスト余白調整 */
    .tsusin_text {
        padding: 0 15px !important;
    }
    
    /* ==========================================================
       スマホ表示（736px以下）時の追加レスポンシブ・カスタマイズ (fnav完了時点)
       ========================================================== */
       
    /* 左右フロートの強制解除 */
    .rflt,
    .lflt {
        float: none !important;
    }
    
    /* 大枠の固定最小幅(min-width)・横幅(width)解除 */
    .inner {
        width: 100% !important;
        max-width: 100% !important;
        min-width: auto !important;
        box-sizing: border-box !important;
    }
    #content {
        min-width: auto !important;
        width: 100% !important;
    }
    
    /* フッターメニューの幅47%化（2列グリッド） */
    #fnav {
        min-width: auto !important;
        max-width: 100% !important;
        padding: 30px 15px !important;
        box-sizing: border-box !important;
    }
    #fnav .inner {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 1rem !important;
    }
    #fnav .fsbx, #fnav .scbx, #fnav .thbox, #fnav .fubox, #fnav .lflt {
        width: 47% !important;
        float: none !important;
    }
    #fnav dl, #fnav dt, #fnav dd {
        float: none !important;
        width: auto !important;
        clear: both !important;
    }
    
    /* 製品一覧・詳細の微調整 */
    #products .solution .arrowtitle {
        width: calc(100% + 15px) !important;
    }
    #products img[src*="sdgs_"],
    #products img[src*="sdgs_"] + .text {
        display: block !important;
        max-width: calc(100% - 30px) !important;
        margin: 0 auto !important;
    }
    .maincopy > img {
        width: auto !important;
        height: 35px !important;
    }
}"""

sp_end_marker_lf = sp_end_marker.replace("\r\n", "\n")
sp_end_replacement_lf = sp_end_replacement.replace("\r\n", "\n")

if sp_end_marker_lf in content_lf:
    content_lf = content_lf.replace(sp_end_marker_lf, sp_end_replacement_lf)
    print("Successfully restored CSS to the fnav changes state.")
else:
    print("Error: Target marker not found in CSS.")

with open(dst_css, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("--- Rollback CSS to fnav changes state Completed ---")
