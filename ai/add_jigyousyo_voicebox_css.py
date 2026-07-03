# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# #jigyousyo .infotxt .txtbox の直下に
# #jigyousyo .voicebox .txtbox スタイルを追記する
target = """    /* スマホ時の#jigyousyo関連要素の最大幅流動化 */
    #jigyousyo .sctxt,
    #jigyousyo .infotxt .txtbox {
        max-width: 100% !important;
    }
}"""

replacement = """    /* スマホ時の#jigyousyo関連要素の最大幅流動化 */
    #jigyousyo .sctxt,
    #jigyousyo .infotxt .txtbox {
        max-width: 100% !important;
    }
    
    /* スマホ時の#jigyousyo先輩の声テキストボックス調整 */
    #jigyousyo .voicebox .txtbox {
        max-width: 100% !important;
        float: none !important;
        margin: 0 20px 20px !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added #jigyousyo voicebox styles to common.css.")
else:
    print("Target comment marker for #jigyousyo voicebox styles not found.")
