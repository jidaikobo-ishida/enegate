# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# #google div.main p の直下に h3.box のスマホ調整スタイルを追記する
target = """    /* スマホ時のGoogleマップエリア中央寄せ調整 */
    #google div.main {
        width: auto !important;
    }
    #google div.main p {
        margin: 0 auto !important;
    }
}"""

replacement = """    /* スマホ時のGoogleマップエリア中央寄せ調整 */
    #google div.main {
        width: auto !important;
    }
    #google div.main p {
        margin: 0 auto !important;
    }
    
    /* スマホ時の見出しh3.boxの余白調整 */
    h3.box {
        margin: 1rem 0 !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added h3.box margin style to common.css.")
else:
    print("Target comment marker for h3.box margin style not found.")
