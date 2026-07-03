# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# 1. 元のスマホ用縦並び化指定を直系子要素指定（> table）に書き換える
# これにより、間に入った .scrolltable 内のテーブルは自動的に除外される
content_lf = content_lf.replace(
    "body#list .twocontent .group .boxType02 table tr {",
    "body#list .twocontent .group .boxType02 > table tr {"
)
content_lf = content_lf.replace(
    "body#list .twocontent .group .boxType02 table td {",
    "body#list .twocontent .group .boxType02 > table td {"
)
content_lf = content_lf.replace(
    "body#list .twocontent .group .boxType02 table td p.img img {",
    "body#list .twocontent .group .boxType02 > table td p.img img {"
)
content_lf = content_lf.replace(
    "body#list .twocontent .group .boxType02 table.type02 td.end {",
    "body#list .twocontent .group .boxType02 > table.type02 td.end {"
)

# 2. 先ほど追加した不要になったリセット記述を削除する
target_reset = """    /* scrolltable内テーブルセルの縦並び化(display:block)を解除・本来 of 表表示にリセット */
    .scrolltable table tr {
        display: table-row !important;
    }
    .scrolltable table td,
    .scrolltable table th {
        display: table-cell !important;
        width: auto !important;
    }"""

# 実際に追加されていた文言にマッチさせるため、安全に置換
# 先ほど追加した正確な記述：
target_reset_exact = """    /* scrolltable内テーブルセルの縦並び化(display:block)を解除・本来の表表示にリセット */
    .scrolltable table tr {
        display: table-row !important;
    }
    .scrolltable table td,
    .scrolltable table th {
        display: table-cell !important;
        width: auto !important;
    }"""

if target_reset_exact in content_lf:
    content_lf = content_lf.replace(target_reset_exact, "")
    print("Removed temporary scrolltable cell resets.")

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("Successfully patched boxType02 child table selectors in common.css.")
