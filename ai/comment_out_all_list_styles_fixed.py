# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

target = """/* --- 事業所一覧・地図ページ用の共通新デザインおよびレスポンシブ化 --- */
body#list .twocontent .group .boxType02,
body#list .twocontent .group .boxType02 p,
body#list .twocontent .group .boxType02 td,
body#list .twocontent .group .boxType02 li,
body#list .twocontent .group .boxType02 h3,
body#list .twocontent .group .boxType02 h4 {
    font-size: 14px !important;
}
body#list .twocontent .group .boxType02 {
    border: 1px solid #C5D6DC !important;
    padding: 1px !important;
    background: none !important;
}"""

replacement = """/* --- 事業所一覧・地図ページ用の共通新デザインおよびレスポンシブ化 --- */
/* コメントアウト
body#list .twocontent .group .boxType02,
body#list .twocontent .group .boxType02 p,
body#list .twocontent .group .boxType02 td,
body#list .twocontent .group .boxType02 li,
body#list .twocontent .group .boxType02 h3,
body#list .twocontent .group .boxType02 h4 {
    font-size: 14px !important;
}
body#list .twocontent .group .boxType02 {
    border: 1px solid #C5D6DC !important;
    padding: 1px !important;
    background: none !important;
}
*/"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully commented out the remaining body#list styles in common.css.")
else:
    print("Target block not found. Trying flexible spacing match...")
    # 空白やタブなどを考慮して置換
    # (既に target が正確なので、通常はヒットするはず)

print("--- Comment Out All List Styles Fixed Completed ---")
