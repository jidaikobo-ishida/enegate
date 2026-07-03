# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# SDGs内の画像の width: 100% 挙動を打ち消し（消去）するスタイル
stretch_disable_styles = """
    /* SDGs内画像の引き伸ばし防止 (width: 100% 挙動の消去) */
    #sdgs .img img,
    #sdgs .imglg img {
        width: auto !important;
    }"""

# SDGs見出し差し替え指定の直後に追記する
target_marker = """    #sdgs .allitem {
        background-image: none !important;
    }"""

target_marker_lf = target_marker.replace("\r\n", "\n")
replacement = target_marker + stretch_disable_styles

if target_marker_lf in content_lf:
    content_lf = content_lf.replace(target_marker_lf, replacement.replace("\r\n", "\n"))
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully added stretch disabling styles for SDGs images in common.css.")
else:
    print("Error: Target marker not found in CSS.")
