# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 1. #jigyousyo .infotxt .txtbox の width: 100% !important; を削除
target_infotxt = """    #jigyousyo .sctxt,
    #jigyousyo .infotxt .txtbox {
        width: 100% !important;
    }"""

replacement_infotxt = """    #jigyousyo .sctxt {
        width: 100% !important;
    }"""

# 2. #jigyousyo .voicebox .txtbox の width: 100% !important; を削除
target_voicebox = """    #jigyousyo .voicebox .txtbox {
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 20px 20px !important;
    }"""

replacement_voicebox = """    #jigyousyo .voicebox .txtbox {
        float: none !important;
        margin: 0 !important;
        padding: 0 20px 20px !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_infotxt_crlf = target_infotxt.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_infotxt_crlf = replacement_infotxt.replace("\r\n", "\n").replace("\n", "\r\n")
target_voicebox_crlf = target_voicebox.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_voicebox_crlf = replacement_voicebox.replace("\r\n", "\n").replace("\n", "\r\n")

repaired_count = 0

if target_infotxt_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_infotxt_crlf, replacement_infotxt_crlf)
    print("Successfully deleted width from jigyousyo infotxt txtbox.")
    repaired_count += 1
else:
    print("Warning: target_infotxt not found in CSS.")

if target_voicebox_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_voicebox_crlf, replacement_voicebox_crlf)
    print("Successfully deleted width from jigyousyo voicebox txtbox.")
    repaired_count += 1
else:
    print("Warning: target_voicebox not found in CSS.")

if repaired_count > 0:
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)

print(f"--- Delete jigyousyo txtbox width completed. Repaired {repaired_count} block(s). ---")
