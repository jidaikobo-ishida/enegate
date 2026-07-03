# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# table.graytb td img の直下に .scrolltable table.graytb の幅調整スタイルを追記する
target = """    /* スマホ時の年表内画像サイズ制御 */
    table.graytb td img {
        max-width: inherit !important;
    }
}"""

replacement = """    /* スマホ時の年表内画像サイズ制御 */
    table.graytb td img {
        max-width: inherit !important;
    }
    
    /* スマホ時の年表テーブル横幅調整 */
    .scrolltable table.graytb {
        width: 810px !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added .scrolltable table.graytb width style to common.css.")
else:
    print("Target comment marker for table.graytb width not found.")
