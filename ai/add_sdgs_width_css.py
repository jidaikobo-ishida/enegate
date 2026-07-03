# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# table.graytb の直下に #sdgs 関連の 100% 幅指定スタイルを追記する
target = """    /* スマホ時の年表テーブル横幅調整 */
    .scrolltable table.graytb {
        width: 810px !important;
    }
}"""

replacement = """    /* スマホ時の年表テーブル横幅調整 */
    .scrolltable table.graytb {
        width: 810px !important;
    }
    
    /* スマホ時のSDGs関連要素の1カラム化 */
    #sdgs .img,
    #sdgs .txt,
    #sdgs .txtlg,
    #sdgs .imglg {
        width: 100% !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added #sdgs width styles to common.css.")
else:
    print("Target comment marker for #sdgs width not found.")
