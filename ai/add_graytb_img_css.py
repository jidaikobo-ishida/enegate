# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# スマホメディアクエリの末尾（最後の } の直前）に table.graytb td img の設定を追記する
# 事業所・地図のスマホ対応ブロックの最後に追記する
target = """    #list .twocontent .boxTop,
    #list .twocontent .boxBtm,
    .guide .twocontent .boxTop,
    .guide .twocontent .boxBtm {
        display: none !important;
    }
}"""

replacement = """    #list .twocontent .boxTop,
    #list .twocontent .boxBtm,
    .guide .twocontent .boxTop,
    .guide .twocontent .boxBtm {
        display: none !important;
    }
    
    /* スマホ時の年表内画像サイズ制御 */
    table.graytb td img {
        max-width: auto !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added table.graytb td img style to common.css.")
else:
    print("Target comment marker for table.graytb td img not found.")
