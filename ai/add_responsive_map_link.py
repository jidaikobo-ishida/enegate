# -*- coding: utf-8 -*-
import re

print("--- Add Responsive Map Link Start ---")

html_path = "company/list/map01.html"
css_path = "common/css/common.css"

# 1. common.css にスタイルを追記
with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    css_content = f.read()

css_lf = css_content.replace("\r\n", "\n")

# PC用の定義として、デフォルトで a.map-link を非表示にする
# (適当なグローバル定義箇所、例えば .leftsubnav の直前に追加)
pc_style = """
/* レスポンシブ用の見出し内絶対配置リンク（デフォルト非表示） */
.text.relative {
    position: relative;
}
.text.relative a.map-link {
    display: none;
}
"""

if ".leftsubnav{" in css_lf:
    css_lf = css_lf.replace(".leftsubnav{", pc_style + "\n.leftsubnav{")
    print("Added default non-display style for map-link in PC CSS.")

# スマホメディアクエリ（736px以下）の末尾に、スマホ時の絶対配置スタイルを追記
target_mobile_marker = """    /* スマホ時の見出しh3.boxの余白調整 */
    h3.box {
        margin: 1rem 0 !important;
    }
}"""

mobile_style = """    /* スマホ時の見出しh3.boxの余白調整 */
    h3.box {
        margin: 1rem 0 !important;
    }
    
    /* スマホ時のみ見出し内の絶対配置リンクをアクティブ化し追従させる */
    .text.relative {
        position: relative !important;
    }
    .text.relative a.map-link {
        display: block !important;
        position: absolute !important;
        top: 17.9% !important;
        left: 77.5% !important;
        width: 22.2% !important;
        height: 66.7% !important;
        text-indent: -9999px !important;
        overflow: hidden !important;
        z-index: 10 !important;
    }
}"""

target_mobile_marker_lf = target_mobile_marker.replace("\r\n", "\n")
mobile_style_lf = mobile_style.replace("\r\n", "\n")

if target_mobile_marker_lf in css_lf:
    css_lf = css_lf.replace(target_mobile_marker_lf, mobile_style_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(css_lf)
    print("Successfully added mobile responsive map-link styling to common.css.")
else:
    print("CSS target marker not found.")

# 2. map01.html の HTML を書き換える
with open(html_path, "r", encoding="cp932", errors="ignore") as f:
    html_content = f.read()

html_lf = html_content.replace("\r\n", "\n")

# 置換対象：
target_h2 = '<h2 class="text"><img src="./img/h2_map01.gif" alt="本社" width="100%" height="auto" border="0" usemap="#Map" /></h2>'
replacement_h2 = '<h2 class="text relative"><img src="./img/h2_map01.gif" alt="本社" width="100%" height="auto" border="0" usemap="#Map" /><a href="index.html" class="map-link">事業所一覧はこちら</a></h2>'

# 柔軟な正規表現での置換（空白や属性順の違いに対応）
h2_pattern = r'<h2 class="text">\s*<img\s+src="\./img/h2_map01\.gif"[^>]*usemap="#Map"[^>]*>\s*</h2>'

match_h2 = re.search(h2_pattern, html_lf, re.IGNORECASE)
if match_h2:
    html_lf = html_lf.replace(match_h2.group(0), replacement_h2)
    with open(html_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(html_lf)
    print("Successfully patched map01.html with relative wrapper and link (regex).")
elif target_h2 in html_lf:
    html_lf = html_lf.replace(target_h2, replacement_h2)
    with open(html_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(html_lf)
    print("Successfully patched map01.html with relative wrapper and link (string).")
else:
    print("Target H2 tag not found in map01.html.")

print("--- Add Responsive Map Link End ---")
