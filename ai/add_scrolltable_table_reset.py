# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# table.graytb 横幅調整の直下に、scrolltable内テーブルセルの縦並び化解除用リセットスタイルを追記する
target = """    /* スマホ時の年表テーブル横幅調整 */
    .scrolltable table.graytb {
        width: 810px !important;
    }"""

replacement = """    /* スマホ時の年表テーブル横幅調整 */
    .scrolltable table.graytb {
        width: 810px !important;
    }
    
    /* scrolltable内テーブルセルの縦並び化(display:block)を解除・本来の表表示にリセット */
    .scrolltable table tr {
        display: table-row !important;
    }
    .scrolltable table td,
    .scrolltable table th {
        display: table-cell !important;
        width: auto !important;
    }"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added scrolltable table reset styles to common.css.")
else:
    print("Target comment marker for scrolltable table reset not found.")
