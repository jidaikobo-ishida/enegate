# -*- coding: utf-8 -*-
import os
import shutil

print("--- Restore and Rebuild Everything from honban_bak Start ---")

honban_bak = "common/css/common.css.honban_bak"
dst_css = "common/css/common.css"

if not os.path.exists(honban_bak):
    raise Exception("Original backup common.css.honban_bak not found!")

# 1. 本番初期バックアップを現在の common.css に上書き復元する
shutil.copy2(honban_bak, dst_css)
print("Successfully restored base from common.css.honban_bak.")

# 2. 復元した CSS を読み込む
with open(dst_css, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 3. PC版の #list 関連スタイルのコメントアウト
target_list_pc = """#list #article { width:950px; clear:both; }
#list #breadcrumbs { padding-bottom:20px;font-size:0.78em;}
#list #mainContent {float:right; width:690px; margin:8px 25px 50px 25px !important; font-size:1.1em;}
#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em;}"""

replacement_list_pc = """/* コメントアウト
#list #article { width:950px; clear:both; }
#list #breadcrumbs { padding-bottom:20px;font-size:0.78em;}
#list #mainContent {float:right; width:690px; margin:8px 25px 50px 25px !important; font-size:1.1em;}
#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em;}
*/"""

if target_list_pc in content_lf:
    content_lf = content_lf.replace(target_list_pc, replacement_list_pc)
    print("Commented out #list PC styles.")
else:
    # 部分一致でのコメントアウト
    print("Warning: Target #list PC block not found exactly. Attempting line replace.")
    content_lf = content_lf.replace("#list #article { width:950px; clear:both; }", "/* #list #article { width:950px; clear:both; } */")
    content_lf = content_lf.replace("#list #breadcrumbs { padding-bottom:20px;font-size:0.78em;}", "/* #list #breadcrumbs { padding-bottom:20px;font-size:0.78em;} */")
    content_lf = content_lf.replace("#list #mainContent {float:right; width:690px; margin:8px 25px 50px 25px !important; font-size:1.1em;}", "/* #list #mainContent {float:right; width:690px; margin:8px 25px 50px 25px !important; font-size:1.1em;} */")
    content_lf = content_lf.replace("#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em;}", "/* #list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em;} */")

# 4. #allproductsnav と #allproductsnav a の高さ70px同期
target_nav = """#productsnav + #allproductsnav { height:50px;}
#productsnav + #allproductsnav a { height:50px;}"""

replacement_nav = """#productsnav + #allproductsnav { height:70px;}
#productsnav + #allproductsnav a { height:70px; line-height:70px;}"""

content_lf = content_lf.replace(target_nav, replacement_nav)
print("Updated allproductsnav heights.")

# 5. 末尾にクリーンなスマホ用メディアクエリ（max-width: 736px）を追加し、
# これまでに構築・完了したすべての正常なスマホ用CSSを一括追記する
sp_styles = """
/* ==========================================================
   スマホ表示（736px以下）用のレスポンシブ・カスタマイズ
   ========================================================== */
@media screen and (max-width: 736px) {
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
    
    /* 仕様表・歩み年表テーブルの横スクロール化調整（潰れ防止） */
    .scrolltable {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: auto !important;
        padding: 0.5rem 0 !important;
        box-sizing: border-box !important;
        -webkit-overflow-scrolling: touch;
    }
    .scrolltable table {
        width: auto !important;
        min-width: 700px !important;
    }
    .scrolltable::before,
    .scrolltable::after {
        content: '横スクロールできます。' !important;
        display: block !important;
        font-size: 0.8em !important;
        color: #666 !important;
        text-align: right !important;
        margin-top: 5px !important;
        clear: both !important;
        padding-right: 15px !important;
    }
    
    /* 歩み年表テーブルの横幅・画像の縮小防止 */
    .scrolltable table.graytb {
        width: 810px !important;
    }
    table.graytb td img {
        max-width: inherit !important;
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
        border: 5px solid #d2e5f4 !important;
    }
    .twocontent .group .type02:not(.type02b) td.end {
        width: 50% !important;
    }
    .twocontent .boxTop,
    .twocontent .boxBtm {
        display: none !important;
    }
    
    /* スマホ時の#jigyousyo関連要素の最大幅流動化 */
    #jigyousyo .sctxt,
    #jigyousyo .infotxt .txtbox {
        width: 100% !important;
    }
    
    /* スマホ時の#jigyousyo先輩の声テキストボックス調整 */
    #jigyousyo .voicebox .txtbox {
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 20px 20px !important;
    }
    
    /* スマホ時の地図ページ.type02cアクセス見出し調整 */
    .type02c h4.access img {
        display: none !important;
    }
    .type02c h4.access::before {
        content: 'ACCESS' !important;
        font-size: 1em !important;
        font-weight: bold !important;
        color: #4055b2 !important;
        background: #dceffd !important;
        display: block !important;
        padding: 0.2rem 0.5rem !important;
    }
    
    /* スマホ時の地図ページアクセス表のセル縦並び化・線消去 */
    .twocontent .group .type02c td {
        display: block !important;
        width: 100% !important;
        border: none !important;
    }
    
    /* スマホ時のGoogleマップエリア中央寄せ調整 */
    #google div.main {
        width: auto !important;
    }
    #google div.main p {
        margin: 0 auto !important;
    }
    
    /* スマホ時の見出しh3.boxの余白調整 */
    h3.box {
        margin: 1rem 0 !important;
    }
    
    /* スマホ時のSDGs関連要素の1カラム化 */
    #sdgs .img,
    #sdgs .txt,
    #sdgs .txtlg,
    #sdgs .imglg {
        width: 100% !important;
    }
    
    /* スマホ時の.imglg内の横並び調整 */
    .imglg br {
        display: none !important;
    }
    .imglg {
        display: flex !important;
        align-items: flex-start !important;
        flex-wrap: nowrap !important;
    }
    .imglg a {
        flex: 1 !important;
    }
    
    /* SDGsアイコンリストのグリッド表示 */
    #sdgs .iconlist {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: space-between !important;
    }
    #sdgs .iconlist li {
        width: 23% !important;
        margin: 1.5% 0 !important;
        float: none !important;
    }
    #sdgs .iconlist::after {
        content: "" !important;
        flex-basis: 23% !important;
    }
    
    /* スマホ時のSDGs見出し差し替え */
    #sdgs .allitem h2,
    #sdgs .allitem h3 {
        display: none !important;
    }
    #sdgs .allitem::before {
        content: "持続可能な開発目標（SDGs）への取り組み" !important;
        display: block !important;
        font-size: 1.4em !important;
        font-weight: bold !important;
        color: #2B7CCB !important;
        margin: 15px 0 !important;
        padding-left: 15px !important;
        border-left: 5px solid #2B7CCB !important;
    }
    #sdgs .allitem {
        background-image: none !important;
    }
    
    /* 地図見出し内絶対配置リンクをアクティブ化し追従させる */
    .text.relative {
        position: relative !important;
    }
    .text.relative a.map-link {
        display: block !important;
        position: absolute !important;
        text-indent: -9999px !important;
        overflow: hidden !important;
        z-index: 10 !important;
    }
}
"""

content_lf = content_lf + sp_styles
print("Appended complete responsive media query block to CSS tail.")

with open(dst_css, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("--- Restore and Rebuild Everything Completed ---")
