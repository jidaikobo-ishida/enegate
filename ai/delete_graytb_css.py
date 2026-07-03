# -*- coding: utf-8 -*-
import re

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# メディアクエリを含めて table.graytb に対する不要な定義全体を削除する
target = """@media only screen and (max-width:736px){
table.graytb th,
table.graytb td {
	width: 100% !important;
	display: block;
	 box-sizing: border-box;
}

}"""

target_lf = target.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, "")
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully deleted table.graytb responsive rules from common.css.")
else:
    # 柔軟な正規表現でのマッチング
    pattern = r'@media\s+only\s+screen\s+and\s*\(max-width:\s*736px\)\s*\{\s*table\.graytb\s+th,\s*table\.graytb\s+td\s*\{\s*width:\s*100%\s*!important;\s*display:\s*block;\s*box-sizing:\s*border-box;\s*\}\s*\}'
    if re.search(pattern, content_lf):
        content_lf = re.sub(pattern, "", content_lf)
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content_lf)
        print("Successfully deleted table.graytb responsive rules from common.css (regex).")
    else:
        print("Target table.graytb style block not found in common.css.")
