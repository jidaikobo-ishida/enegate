# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# .type02c h4.access::before の直下に 
# .twocontent .group .type02c td スタイルを追記する
target = """    .type02c h4.access::before {
        content: 'ACCESS' !important;
        font-size: 1em !important;
        font-weight: bold !important;
        color: #4055b2 !important;
        background: #dceffd !important;
        display: block !important;
        padding: 0.2rem 0.5rem !important;
    }
}"""

replacement = """    .type02c h4.access::before {
        content: 'ACCESS' !important;
        font-size: 1em !important;
        font-weight: bold !important;
        color: #4055b2 !important;
        background: #dceffd !important;
        display: block !important;
        padding: 0.2rem 0.5rem !important;
    }
    
    /* スマホ時の地図ページアクセス表のセル縦並び化・線消去 */
    .twocontent .group .type02c td {
        display: block !important;
        width: 100% !important;
        border: none !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added .type02c td styles to common.css.")
else:
    print("Target comment marker for .type02c td styles not found.")
