# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# margin と padding を修正
content_lf = content.replace("\r\n", "\n")

target = """    /* スマホ時の#jigyousyo先輩の声テキストボックス調整 */
    #jigyousyo .voicebox .txtbox {
        width: 100% !important;
        float: none !important;
        margin: 0 20px 20px !important;
    }"""

replacement = """    /* スマホ時の#jigyousyo先輩の声テキストボックス調整 */
    #jigyousyo .voicebox .txtbox {
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 20px 20px !important;
    }"""

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated #jigyousyo voicebox margin and padding in common.css.")
else:
    print("Target style pattern for voicebox padding update not found.")
