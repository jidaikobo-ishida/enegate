# -*- coding: utf-8 -*-
import os
import shutil
import re

print("--- Restore to Scrolltable Debug State Start ---")

src_css = "../enegate-test/common/css/common.css"
dst_css = "common/css/common.css"

# 1. テスト環境のベースファイルをコピーしてリセット
shutil.copy2(src_css, dst_css)
print("Copied clean base from test CSS.")

# 2. ベースを読み込む
with open(dst_css, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# --- 変更1: 2546行目付近の table.graytb th, table.graytb td の縦並び化指定を削除 ---
target_graytb = """table.graytb th,
table.graytb td {
	width: 100% !important;
	display: block;
	 box-sizing: border-box;
}"""

target_graytb_lf = target_graytb.replace("\r\n", "\n")
if target_graytb_lf in content_lf:
    content_lf = content_lf.replace(target_graytb_lf, "")
    print("Deleted table.graytb display:block style.")
else:
    # 正規表現での安全な削除
    pattern = r'table\.graytb th,\s*table\.graytb td\s*\{\s*width:\s*100%\s*!important;\s*display:\s*block;\s*box-sizing:\s*border-box;\s*\}'
    content_lf, count = re.subn(pattern, "", content_lf, flags=re.IGNORECASE)
    print(f"Deleted {count} table.graytb display:block style(s) via regex.")

# --- 変更2: body#list 固有のスタイルの無効化 (物理的削除によるコメント破損防止) ---
# 2551行目付近の新デザイン定義（PC用/スマホ用）
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

# その下の table 定義
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

# 3095行目付近の tr / td 定義
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

# 干渉元であるこれらの body#list 固有指定を、コメント破損を防ぐため物理的に消去する
content_lf = content_lf.replace(target_list_sp.replace("\r\n", "\n"), "")
content_lf = content_lf.replace(target_list_table.replace("\r\n", "\n"), "")
content_lf = content_lf.replace(target_list_tr.replace("\r\n", "\n"), "")
print("Physically removed body#list overrides to prevent specificity conflicts.")

# --- 変更3: #allproductsnav と #allproductsnav a の高さ70px同期 ---
target_nav = """#productsnav + #allproductsnav { height:50px;}
#productsnav + #allproductsnav a { height:50px;}"""

replacement_nav = """#productsnav + #allproductsnav { height:70px;}
#productsnav + #allproductsnav a { height:70px; line-height:70px;}"""

content_lf = content_lf.replace(target_nav, replacement_nav)
print("Updated allproductsnav heights.")

# --- 変更4: スマホ用メディアクエリの末尾に、失われた追加レスポンシブスタイルを一括追記 ---
# (※ scrolltable の調整前＝min-width: 650px!important の初期状態に戻します)
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
        min-width: 650px !important; /* 横潰れを防ぐため、最小幅をキープ */
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
}"""

sp_end_marker_lf = sp_end_marker.replace("\r\n", "\n")
sp_end_replacement_lf = sp_end_replacement.replace("\r\n", "\n")

if sp_end_marker_lf in content_lf:
    content_lf = content_lf.replace(sp_end_marker_lf, sp_end_replacement_lf)
    print("Appended custom styles to end of mobile query.")
else:
    print("Error: Target marker for end of mobile query not found.")

with open(dst_css, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("--- Restore to Scrolltable Debug State Completed ---")
