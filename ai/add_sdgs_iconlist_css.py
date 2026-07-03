# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# .imglg > * の直下に #sdgs .iconlist のレイアウト指定を追記する
target = """    .imglg > * {
        flex: 1 !important;
    }
}"""

replacement = """    .imglg > * {
        flex: 1 !important;
    }
    
    /* スマホ時のSDGs目標アイコンリストの整列調整 */
    #sdgs .iconlist {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: space-between !important;
    }
    #sdgs .iconlist li {
        flex-basis: 23% !important;
        margin: 0 !important;
        float: none !important;
    }
    #sdgs .iconlist::after {
        content: '' !important;
        display: block !important;
        flex-basis: 23% !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added #sdgs .iconlist styles to common.css.")
else:
    print("Target comment marker for .iconlist styles not found.")
