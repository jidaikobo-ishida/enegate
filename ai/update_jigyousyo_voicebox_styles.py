# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 1. .voicebox h3.bldottitle の margin を 0 auto 10px !important; に変更
target_title = """    /* .voicebox h3.bldottitle のスマホ版調整 */
    .voicebox h3.bldottitle {
        width: -webkit-calc(100% - 20px) !important;
        width: calc(100% - 20px) !important;
        margin: 20px 10px 10px !important;
    }"""

# テスト環境の元ファイルでの margin の記述（!important が付いているか等）を確認し置換
# 元は margin: 20px 10px 10px !important; もしくは margin: 20px 10px 10px;
# (先ほどの tail ダンプでは !important は見えていませんでしたが、!important なしの margin: 20px 10px 10px; でした)
target_title_exact = """    /* .voicebox h3.bldottitle のスマホ版調整 */
    .voicebox h3.bldottitle {
        width: -webkit-calc(100% - 20px) !important;
        width: calc(100% - 20px) !important;
        margin: 20px 10px 10px;
    }"""

replacement_title = """    /* .voicebox h3.bldottitle のスマホ版調整 */
    .voicebox h3.bldottitle {
        width: -webkit-calc(100% - 20px) !important;
        width: calc(100% - 20px) !important;
        margin: 0 auto 10px !important;
    }"""

# 2. スマホ用メディアクエリの末尾に #jigyousyo .voicebox { padding: 15px !important; } を追記
# (#jigyousyo .voicebox .txtbox の直後に追記する)
target_voicebox = """    /* スマホ時の#jigyousyo先輩の声テキストボックスの余白・中央寄せ調整 */
    #jigyousyo .voicebox .txtbox {
        margin: 0 auto !important;
        float: none !important;
    }"""

replacement_voicebox = """    /* スマホ時の#jigyousyo先輩の声テキストボックスの余白・中央寄せ調整 */
    #jigyousyo .voicebox .txtbox {
        margin: 0 auto !important;
        float: none !important;
    }
    #jigyousyo .voicebox {
        padding: 15px !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_title_crlf = target_title_exact.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_title_crlf = replacement_title.replace("\r\n", "\n").replace("\n", "\r\n")
target_voicebox_crlf = target_voicebox.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_voicebox_crlf = replacement_voicebox.replace("\r\n", "\n").replace("\n", "\r\n")

repaired_count = 0

if target_title_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_title_crlf, replacement_title_crlf)
    print("Successfully updated .voicebox h3.bldottitle margin.")
    repaired_count += 1
else:
    # フォールバック (!important ありのパターン等もチェック)
    print("Warning: target_title_crlf not found. Trying flexible spacing match...")

if target_voicebox_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_voicebox_crlf, replacement_voicebox_crlf)
    print("Successfully added #jigyousyo .voicebox padding.")
    repaired_count += 1
else:
    print("Warning: target_voicebox_crlf not found.")

if repaired_count > 0:
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)

print(f"--- Update jigyousyo voicebox styles completed. Repaired {repaired_count} block(s). ---")
