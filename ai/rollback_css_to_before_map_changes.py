# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 1. 地図関連のCSSをスマホ用メディアクエリ内から完全に削除する

# 削除対象1: 地図アクセス見出し調整
target_access_title = """    /* スマホ時の地図ページ.type02cアクセス見出し調整 */
    .type02c h4.access img {
        display: none !important;
    }
    .type02c h4.access::before {
        content: 'ACCESS' !important;
        font-size: 1em !important;
        font-weight: bold !important;
        color: #4055b2 !important;
        background: #dceffd !important;
        display: block !important;
        padding: 0.2rem 0.5rem !important;
    }"""

# 削除対象2: アクセス表のセル縦並び化
target_access_table = """    /* スマホ時の地図ページアクセス表のセル縦並び化・線消去 */
    .twocontent .group .type02c td {
        display: block !important;
        width: 100% !important;
        border: none !important;
    }"""

# 削除対象3: 地図絶対配置リンク
target_map_links = """    /* 地図見出し内絶対配置リンクをアクティブ化し追従させる */
    .text.relative {
        position: relative !important;
    }
    .text.relative a.map-link {
        display: block !important;
        position: absolute !important;
        text-indent: -9999px !important;
        overflow: hidden !important;
        z-index: 10 !important;
    }"""

content_lf = content_lf.replace(target_access_title.replace("\r\n", "\n"), "")
content_lf = content_lf.replace(target_access_table.replace("\r\n", "\n"), "")
content_lf = content_lf.replace(target_map_links.replace("\r\n", "\n"), "")

# 2. type02 の除外指定から :not(.type02c) を削除して元の :not(.type02b) に戻す
target_type02_not = """    .twocontent .group .type02:not(.type02b):not(.type02c) {
        width: 100% !important;
        margin: 0 !important;
        border: 5px solid #d2e5f4 !important;
    }
    .twocontent .group .type02:not(.type02b):not(.type02c) td.end {
        width: 50% !important;
    }"""

replacement_type02_not = """    .twocontent .group .type02:not(.type02b) {
        width: 100% !important;
        margin: 0 !important;
        border: 5px solid #d2e5f4 !important;
    }
    .twocontent .group .type02:not(.type02b) td.end {
        width: 50% !important;
    }"""

content_lf = content_lf.replace(target_type02_not.replace("\r\n", "\n"), replacement_type02_not.replace("\r\n", "\n"))

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("--- CSS Rollback to Before Map Changes Completed ---")
