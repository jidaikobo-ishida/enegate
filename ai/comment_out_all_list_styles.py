# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 2551行目付近の「--- 事業所一覧・地図ページ用の共通新デザインおよびレスポンシブ化 ---」から
# スマホ用メディアクエリ開始（2602行目付近）の直前までの body#list スタイルをすべてコメントアウトする

target = """/* --- 事業所一覧・地図ページ用の共通新デザインおよびレスポンシブ化 --- */
body#list .twocontent .group .boxType02,
body#list .twocontent .group .boxType02 p,
body#list .twocontent .group .boxType02 td,
body#list .twocontent .group .boxType02 li,
body#list .twocontent .group .boxType02 h3,
body#list .twocontent .group .boxType02 h4 {
	font-size:12px;
}
body#list .twocontent .group .boxType02 {
	margin-bottom:15px;
	padding:15px 20px 25px;
	background:url(../../company/list/img/box_back02.gif) no-repeat left bottom;
}"""

replacement = """/* --- 事業所一覧・地図ページ用の共通新デザインおよびレスポンシブ化 --- */
/* コメントアウト
body#list .twocontent .group .boxType02,
body#list .twocontent .group .boxType02 p,
body#list .twocontent .group .boxType02 td,
body#list .twocontent .group .boxType02 li,
body#list .twocontent .group .boxType02 h3,
body#list .twocontent .group .boxType02 h4 {
	font-size:12px;
}
body#list .twocontent .group .boxType02 {
	margin-bottom:15px;
	padding:15px 20px 25px;
	background:url(../../company/list/img/box_back02.gif) no-repeat left bottom;
}
*/"""

# さらに、その直後にある body#list .twocontent .group .boxType02 table { ... } ブロックも
# コメントアウトが正しくつながっているか確認する
# (前回は replacement_list_sp で table 以下のブロックを単体でコメントアウトしていました)

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    print("Successfully commented out the main PC-side body#list style blocks.")
else:
    print("Warning: Target body#list style block not found in CSS.")

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("--- Comment Out All List Styles Completed ---")
