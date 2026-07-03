# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# #jigyousyo .voicebox .txtbox の直下に
# .type02c h4.access のスマホ調整スタイルを追記する
target = """    /* スマホ時の#jigyousyo先輩の声テキストボックス調整 */
    #jigyousyo .voicebox .txtbox {
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 20px 20px !important;
    }
}"""

replacement = """    /* スマホ時の#jigyousyo先輩の声テキストボックス調整 */
    #jigyousyo .voicebox .txtbox {
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 20px 20px !important;
    }
    
    /* スマホ時の地図ページ.type02cアクセス見出し調整 */
    .type02c h4.access img {
        display: none !important;
    }
    .type02c h4.access::before {
        content: 'ACCESS' !important;
        font-size: 1.2em !important;
        color: #4055b2 !important;
        background: #dceffd !important;
        display: block !important;
        padding: 0.2rem 0.5rem !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added .type02c h4.access styles to common.css.")
else:
    print("Target comment marker for .type02c h4.access styles not found.")
