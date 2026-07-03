# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# #sdgs .allitem の直下に ::before の擬似要素指定を追記する
target = """    #sdgs .allitem {
        background-image: none !important;
    }
}"""

replacement = """    #sdgs .allitem {
        background-image: none !important;
    }
    #sdgs .allitem::before {
        content: '株式会社エネゲートの取り組む目標' !important;
        color: #000 !important;
        font-size: 1.2em !important;
        display: block !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added #sdgs .allitem::before styles to common.css.")
else:
    print("Target comment marker for .allitem::before styles not found.")
