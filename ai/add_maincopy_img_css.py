# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# #sdgs .allitem::before の直下に .maincopy > img のサイズ調整スタイルを追記する
target = """    #sdgs .allitem::before {
        content: '持続可能な開発目標（SDGs）への取り組み' !important;
        color: #000 !important;
        font-size: 1.4em !important;
        display: block !important;
    }
}"""

replacement = """    #sdgs .allitem::before {
        content: '持続可能な開発目標（SDGs）への取り組み' !important;
        color: #000 !important;
        font-size: 1.4em !important;
        display: block !important;
    }
    
    /* スマホ時のメインコピー画像サイズ調整 */
    .maincopy > img {
        width: auto !important;
        height: 40px !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added .maincopy > img styles to common.css.")
else:
    print("Target comment marker for .maincopy > img not found.")
