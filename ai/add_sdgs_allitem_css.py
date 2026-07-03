# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# .iconlist::after の直下に #sdgs .allitem の見出し非表示・背景画像リセットを追記する
target = """    #sdgs .iconlist::after {
        content: '' !important;
        display: block !important;
        flex-basis: 23% !important;
    }
}"""

replacement = """    #sdgs .iconlist::after {
        content: '' !important;
        display: block !important;
        flex-basis: 23% !important;
    }
    
    /* スマホ時のSDGs .allitem 調整 */
    #sdgs .allitem h2,
    #sdgs .allitem h3 {
        display: none !important;
    }
    #sdgs .allitem {
        background-image: none !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added #sdgs .allitem styles to common.css.")
else:
    print("Target comment marker for .allitem styles not found.")
