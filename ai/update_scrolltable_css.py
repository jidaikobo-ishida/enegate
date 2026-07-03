# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 旧 .scrolltable .itemspec の定義を、潰れ防止用の .scrolltable table に置換
target = """    /* 仕様テーブルのスマホ表示時の横スクロール化調整 */
    .scrolltable {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: auto !important;
        padding: 0.5rem 0 !important;
        box-sizing: border-box !important;
        -webkit-overflow-scrolling: touch;
    }
    .scrolltable .itemspec {
        min-width: 650px !important; /* 横潰れを防ぐため、最小幅をキープ */
    }"""

replacement = """    /* 仕様テーブルのスマホ表示時の横スクロール化調整 */
    .scrolltable {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: auto !important;
        padding: 0.5rem 0 !important;
        box-sizing: border-box !important;
        -webkit-overflow-scrolling: touch;
    }
    .scrolltable table {
        width: auto !important;
        min-width: 700px !important; /* 横潰れを防ぎ、本来の幅を維持してはみ出させる */
    }"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully updated scrolltable styles to use table wrapper in common.css.")
else:
    # 別の箇所にある可能性を考慮したフォールバック
    if ".scrolltable .itemspec" in content_lf:
        content_lf = content_lf.replace(".scrolltable .itemspec {\n        min-width: 650px !important; /* 横潰れを防ぐため、最小幅をキープ */\n    }", ".scrolltable table {\n        width: auto !important;\n        min-width: 700px !important;\n    }")
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content_lf)
        print("Successfully updated scrolltable style in common.css (fallback).")
    else:
        print("Target scrolltable styles not found in CSS.")
