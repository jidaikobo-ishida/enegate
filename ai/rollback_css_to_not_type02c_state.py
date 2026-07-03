# -*- coding: utf-8 -*-
import os
import shutil

print("--- Rollback CSS to not(.type02c) state Start ---")

src_css = "../enegate-test/common/css/common.css"
dst_css = "common/css/common.css"

# 1. テスト環境のベースファイルをコピーしてリセット
shutil.copy2(src_css, dst_css)
print("Copied clean base from test CSS.")

# 2. ベースを読み込む
with open(dst_css, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 3. body#list 固有のスタイルの無効化 (物理的削除)
target_list_sp = """body#list .twocontent .group .boxType02,
body#list .twocontent .group .boxType02 p,
body#list .twocontent .group .boxType02 td,
body#list .twocontent .group .boxType02 li,
body#list .twocontent .group .boxType02 h3,
body#list .twocontent .group .boxType02 h4 {
    font-size: 14px !important;
}
body#list .twocontent .group .boxType02 {
    border: 1px solid #C5D6DC !important;
    padding: 1px !important;
    background: none !important;
}"""

target_list_table = """body#list .twocontent .group .boxType02 table {
    width: 100% !important;
    margin: 0 !important;
    border: 3px solid #d2e5f4 !important;
}
body#list .twocontent .group .boxType02 table td,
body#list .twocontent .group .boxType02 table th {
    padding: 5px 10px !important;
}
body#list .twocontent .group .boxType02 table td.end {
    width: 50% !important;
}
body#list .twocontent .boxTop,
body#list .twocontent .boxBtm {
    display: none !important;
}"""

target_list_tr = """body#list .twocontent .group .boxType02 > table tr {
        display: block !important;
    }
    body#list .twocontent .group .boxType02 > table td {
        display: block !important;
        width: 100% !important;
        box-sizing: border-box !important;
        padding: 10px !important;
    }
    body#list .twocontent .group .boxType02 > table td p.img img {
        width: 100% !important;
        height: auto !important;
    }
    body#list .twocontent .group .boxType02 > table.type02 td.end {
        width: 100% !important;
    }"""

content_lf = content_lf.replace(target_list_sp.replace("\r\n", "\n"), "")
content_lf = content_lf.replace(target_list_table.replace("\r\n", "\n"), "")
content_lf = content_lf.replace(target_list_tr.replace("\r\n", "\n"), "")

# 4. #allproductsnav と #allproductsnav a の高さ70px同期を適用
target_nav = """#productsnav + #allproductsnav { height:50px;}
#productsnav + #allproductsnav a { height:50px;}"""

replacement_nav = """#productsnav + #allproductsnav { height:70px;}
#productsnav + #allproductsnav a { height:70px; line-height:70px;}"""

content_lf = content_lf.replace(target_nav, replacement_nav)

# 5. type02b フォントサイズ適正化指定の挿入
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

# 6. スマホ用追加スタイルの一括追記 (not(.type02c) を含み、地図固有や scrolltable 潰れ防止前の状態)
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
       スマホ表示（736px以下）時の追加レスポンシブ・カスタマイズ
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
    
    /* 仕様表・歩み年表テーブルの横スクロール化調整（初期状態） */
    .scrolltable {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: auto !important;
        padding: 0.5rem 0 !important;
        box-sizing: border-box !important;
        -webkit-overflow-scrolling: touch;
    }
    .scrolltable .itemspec {
        min-width: 650px !important;
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
    .twocontent .group .type02:not(.type02b):not(.type02c) {
        width: 100% !important;
        margin: 0 !important;
        border: 5px solid #d2e5f4 !important;
    }
    .twocontent .group .type02:not(.type02b):not(.type02c) td.end {
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
}"""

sp_end_marker_lf = sp_end_marker.replace("\r\n", "\n")
sp_end_replacement_lf = sp_end_replacement.replace("\r\n", "\n")

# type02b_styles をスマホ用メディアクエリの直前に挿入しつつ、末尾にスマホCSSを追記
if sp_end_marker_lf in content_lf:
    # 追記
    content_lf = content_lf.replace(sp_end_marker_lf, sp_end_replacement_lf)
    # type02b スタイルの挿入
    target_sp_header = """    /* ==========================================================
       スマホ表示（736px以下）時の追加レスポンシブ・カスタマイズ
       ========================================================== */"""
    target_sp_header_lf = target_sp_header.replace("\r\n", "\n")
    if target_sp_header_lf in content_lf:
        content_lf = content_lf.replace(target_sp_header_lf, type02b_styles + "\n\n" + target_sp_header_lf)
        print("Successfully rebuilt and restored CSS to the not(.type02c) changes state.")
    else:
        print("Error: target_sp_header_lf not found.")
else:
    print("Error: Target marker not found in CSS.")

with open(dst_css, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("--- Rollback CSS to not(.type02c) state Completed ---")
