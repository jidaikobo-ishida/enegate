# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

sdgs_styles = """
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
    }"""

# スマホメディアクエリの終了ブラケット（最後から1つ手前の } ）の直前に挿入する
# ターゲットとして最後の } の手前を指定
target_marker = """    .maincopy > img {
        width: auto !important;
        height: 35px !important;
    }
}"""

replacement = """    .maincopy > img {
        width: auto !important;
        height: 35px !important;
    }""" + sdgs_styles + "\n}"

target_marker_lf = target_marker.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_marker_lf in content_lf:
    content_lf = content_lf.replace(target_marker_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully restored SDGs responsive styles in common.css.")
else:
    print("Error: Target marker for end of mobile query not found.")
