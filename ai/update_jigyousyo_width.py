# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# max-width: 100% !important; を width: 100% !important; に置換
# 全体で2箇所あるため、すべて置換
content_lf = content.replace("\r\n", "\n")

target1 = """    /* スマホ時の#jigyousyo関連要素の最大幅流動化 */
    #jigyousyo .sctxt,
    #jigyousyo .infotxt .txtbox {
        max-width: 100% !important;
    }"""

replacement1 = """    /* スマホ時の#jigyousyo関連要素の最大幅流動化 */
    #jigyousyo .sctxt,
    #jigyousyo .infotxt .txtbox {
        width: 100% !important;
    }"""

target2 = """    /* スマホ時の#jigyousyo先輩の声テキストボックス調整 */
    #jigyousyo .voicebox .txtbox {
        max-width: 100% !important;
        float: none !important;
        margin: 0 20px 20px !important;
    }"""

replacement2 = """    /* スマホ時の#jigyousyo先輩の声テキストボックス調整 */
    #jigyousyo .voicebox .txtbox {
        width: 100% !important;
        float: none !important;
        margin: 0 20px 20px !important;
    }"""

if target1 in content_lf:
    content_lf = content_lf.replace(target1, replacement1)
if target2 in content_lf:
    content_lf = content_lf.replace(target2, replacement2)

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("Successfully updated #jigyousyo styles from max-width to width: 100% in common.css.")
