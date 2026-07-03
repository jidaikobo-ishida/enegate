# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# type02 に対する :not(.type02b) および :not(.type02c) の除外指定を適用
# 3090行目付近にある .twocontent .group .type02 定義箇所を置換

target = """    .twocontent .group .type02 {
        width: 100% !important;
        margin: 0 !important;
        border: 5px solid #d2e5f4 !important;
    }
    .twocontent .group .type02:not(.type02b) td.end {
        width: 50% !important;
    }"""

replacement = """    .twocontent .group .type02:not(.type02b):not(.type02c) {
        width: 100% !important;
        margin: 0 !important;
        border: 5px solid #d2e5f4 !important;
    }
    .twocontent .group .type02:not(.type02b):not(.type02c) td.end {
        width: 50% !important;
    }"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully restored :not(.type02c) exclusions in common.css.")
else:
    print("Error: Target type02 style block not found in CSS.")
