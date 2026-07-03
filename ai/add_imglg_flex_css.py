# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# #sdgs .imglg 関連定義の直下に .imglg の flex 指定を追記する
target = """    /* スマホ時のSDGs関連要素の1カラム化 */
    #sdgs .img,
    #sdgs .txt,
    #sdgs .txtlg,
    #sdgs .imglg {
        width: 100% !important;
    }
}"""

replacement = """    /* スマホ時のSDGs関連要素の1カラム化 */
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
        justify-content: space-between !important;
        gap: 1rem !important;
        flex-wrap: nowrap !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added .imglg flex styles to common.css.")
else:
    print("Target comment marker for .imglg flex not found.")
