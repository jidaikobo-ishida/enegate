# -*- coding: utf-8 -*-
import os
import shutil

print("--- Rebuild Clean common.css (Fixing Shift-JIS & Comments) v2 Start ---")

src_css = "../enegate-test/common/css/common.css"
dst_css = "common/css/common.css"

# 1. テスト環境のクリーンな元ファイルをコピーしてベースとする
shutil.copy2(src_css, dst_css)
print("Restored base common.css from test environment.")

# 2. ベースとなる CSS を読み込む
with open(dst_css, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# --- 変更1: #list および body#list 関連のコメントアウト ---
# 1552行目付近
target_list_pc = """#list #article {
	background: url(../../company/list/img/article_back.gif) no-repeat left top;
}
#list #breadcrumbs {
	background: url(../../company/list/img/breadcrumbs_back.gif) no-repeat left top;
}"""

replacement_list_pc = """/* コメントアウト
#list #article {
	background: url(../../company/list/img/article_back.gif) no-repeat left top;
}
#list #breadcrumbs {
	background: url(../../company/list/img/breadcrumbs_back.gif) no-repeat left top;
}
*/"""

# 2558行目付近のスマホ用 #list 関連
target_list_sp = """body#list .twocontent .group .boxType02 table {
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

replacement_list_sp = """/* コメントアウト
body#list .twocontent .group .boxType02 table {
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
}
*/"""

# 3095行目付近のスマホ用 #list 関連
target_list_sp2 = """body#list .twocontent .group .boxType02 > table tr {
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

replacement_list_sp2 = """/* コメントアウト
body#list .twocontent .group .boxType02 > table tr {
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
    }
*/"""

content_lf = content_lf.replace(target_list_pc, replacement_list_pc)
content_lf = content_lf.replace(target_list_sp, replacement_list_sp)
content_lf = content_lf.replace(target_list_sp2, replacement_list_sp2)


# --- 変更2: #allproductsnav と #allproductsnav a の高さ70px同期 ---
target_nav = """#productsnav + #allproductsnav { height:50px;}
#productsnav + #allproductsnav a { height:50px;}"""

replacement_nav = """#productsnav + #allproductsnav { height:70px;}
#productsnav + #allproductsnav a { height:70px; line-height:70px;}"""

content_lf = content_lf.replace(target_nav, replacement_nav)


# --- 変更3: スマホ用メディアクエリの末尾に、正常なスマホ調整CSSを一括追記 ---
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
       スマホ表示（736px以下）時のレスポンシブ・カスタマイズ追記
       ========================================================== */
    
    /* スマホ表示（736px以下）時の大枠固定幅解除 */
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
    
    /* 仕様・年表等のテーブル横スクロール化（潰れ防止） */
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
    
    /* 歩み年表テーブルのスマホ時横幅固定値 */
    .scrolltable table.graytb {
        width: 810px !important;
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
}"""

sp_end_marker_lf = sp_end_marker.replace("\r\n", "\n")
sp_end_replacement_lf = sp_end_replacement.replace("\r\n", "\n")

if sp_end_marker_lf in content_lf:
    content_lf = content_lf.replace(sp_end_marker_lf, sp_end_replacement_lf)
    print("Successfully rebuilt and appended responsive styles to common.css (v2).")
else:
    print("Error: Target sp_end_marker not found in common.css.")

with open(dst_css, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("--- Rebuild Clean common.css Completed ---")
