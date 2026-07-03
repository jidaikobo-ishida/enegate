# -*- coding: utf-8 -*-
import re

print("--- Restore Lost CSS Changes Start ---")

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 1. 2546行目付近の table.graytb th, table.graytb td の縦並び化指定を削除
target_graytb_block = """table.graytb th,
table.graytb td {
	width: 100% !important;
	display: block;
	 box-sizing: border-box;
}"""

target_graytb_block_lf = target_graytb_block.replace("\r\n", "\n")

if target_graytb_block_lf in content_lf:
    content_lf = content_lf.replace(target_graytb_block_lf, "")
    print("Successfully deleted target table.graytb th/td display:block style.")
else:
    # 柔軟な正規表現での削除
    pattern = r'table\.graytb th,\s*table\.graytb td\s*\{\s*width:\s*100%\s*!important;\s*display:\s*block;\s*box-sizing:\s*border-box;\s*\}'
    content_lf, count = re.subn(pattern, "", content_lf, flags=re.IGNORECASE)
    if count > 0:
         print(f"Successfully deleted {count} table.graytb display:block style(s) via regex.")
    else:
         print("Warning: table.graytb display:block style not found.")

# 2. スマホ用追記CSSの末尾（h3.boxの余白調整の直下）に、失われていたSDGsの調整と歩み年表の画像調整を再統合
target_tail = """    /* スマホ時の見出しh3.boxの余白調整 */
    h3.box {
        margin: 1rem 0 !important;
    }
}"""

replacement_tail = """    /* スマホ時の見出しh3.boxの余白調整 */
    h3.box {
        margin: 1rem 0 !important;
    }
    
    /* スマホ時の歩み年表画像縮小防止 */
    table.graytb td img {
        max-width: inherit !important;
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
}"""

target_tail_lf = target_tail.replace("\r\n", "\n")
replacement_tail_lf = replacement_tail.replace("\r\n", "\n")

if target_tail_lf in content_lf:
    content_lf = content_lf.replace(target_tail_lf, replacement_tail_lf)
    print("Successfully restored SDGs and graytb image styles to the CSS tail.")
else:
    print("Warning: CSS tail target marker not found.")

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("--- Restore Lost CSS Changes Completed ---")
