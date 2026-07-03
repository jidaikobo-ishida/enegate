# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 1. #division .voicebox .txtbox の padding を 0 !important; に変更
# 元の定義：#division .voicebox .txtbox { width:100%; margin:0; padding:10px; float:none;}
# (※ !important を追加して確実に上書きします)
target_txtbox = """#division .voicebox .txtbox { width:100%; margin:0; padding:10px; float:none;}"""
replacement_txtbox = """#division .voicebox .txtbox { width:100% !important; margin:0 !important; padding:0 !important; float:none !important;}"""

# 2. .bldottitle の padding を 0 0 15px !important; に変更
target_bldot = """    /* スマホ時の青丸付き見出し(.bldottitle)のパディング・フロート解除調整 */
    .bldottitle {
        padding: 15px !important;
        float: none !important;
    }"""

replacement_bldot = """    /* スマホ時の青丸付き見出し(.bldottitle)のパディング・フロート解除調整 */
    .bldottitle {
        padding: 0 0 15px !important;
        float: none !important;
    }"""

# 3. #division #kanri .voicebox の padding: 15px !important; をスマホ用追加スタイルの末尾に追記
# (.bldottitle 定義の直後に追記します)
target_voicebox_append = replacement_bldot
replacement_voicebox_append = replacement_bldot + """
    /* スマホ時の事業内容管理部門(#division #kanri .voicebox)のパディング調整 */
    #division #kanri .voicebox {
        padding: 15px !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_txtbox_crlf = target_txtbox.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_txtbox_crlf = replacement_txtbox.replace("\r\n", "\n").replace("\n", "\r\n")
target_bldot_crlf = target_bldot.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_bldot_crlf = replacement_bldot.replace("\r\n", "\n").replace("\n", "\r\n")
target_voicebox_append_crlf = target_voicebox_append.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_voicebox_append_crlf = replacement_voicebox_append.replace("\r\n", "\n").replace("\n", "\r\n")

repaired_count = 0

if target_txtbox_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_txtbox_crlf, replacement_txtbox_crlf)
    print("Successfully updated #division .voicebox .txtbox padding.")
    repaired_count += 1
else:
    print("Warning: target_txtbox not found. Checking alternate spaces...")

if target_bldot_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_bldot_crlf, replacement_bldot_crlf)
    print("Successfully updated .bldottitle padding.")
    repaired_count += 1
else:
    print("Warning: target_bldot not found.")

# padding 追加部分の適用
content_crlf = content_crlf.replace(target_voicebox_append_crlf, replacement_voicebox_append_crlf)
print("Successfully appended #division #kanri .voicebox padding style.")

if repaired_count > 0:
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)

print(f"--- Update Completed. Repaired {repaired_count} block(s). ---")
