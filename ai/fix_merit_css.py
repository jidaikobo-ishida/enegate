# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 改行コードを LF に統一して置換処理を確実にする
content_lf = content.replace("\r\n", "\n")

target = """    #metainfo .meritl,
    #metainfo .meritr {
        width: 100% !important;
        float: none !important;
        padding-left: 0 !important;
        margin: 15px 0 !important;
        box-sizing: border-box !important;
    }"""

replacement = """    #metainfo .meritl,
    #metainfo .meritr {
        width: 100% !important;
        float: none !important;
        padding-left: 0 !important;
        margin: 15px 0 !important;
        box-sizing: border-box !important;
        clear: both !important;
    }"""

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully patched merit styles in common.css.")
else:
    print("Target style pattern not found in common.css.")
