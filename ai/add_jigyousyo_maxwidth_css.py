# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# .twocontent .boxBtm { display: none !important; } の直下に
# #jigyousyo 関連の max-width: 100% スタイルを追記する
target = """    .twocontent .boxTop,
    .twocontent .boxBtm {
        display: none !important;
    }
}"""

replacement = """    .twocontent .boxTop,
    .twocontent .boxBtm {
        display: none !important;
    }
    
    /* スマホ時の#jigyousyo関連要素の最大幅流動化 */
    #jigyousyo .sctxt,
    #jigyousyo .infotxt .txtbox {
        max-width: 100% !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added #jigyousyo styles to common.css.")
else:
    print("Target comment marker for #jigyousyo styles not found.")
