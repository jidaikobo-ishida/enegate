# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 1. `#sdgs .allitem .iconlist { ... }` の定義ブロックを削除
target_allitem = """    #sdgs .allitem .iconlist {
        justify-content: space-around !important;
        gap: 1.5% !important;
    }"""

# 2. `#sdgs .iconlist li` および `::after` の flex-basis: 31% を width/flex-basis: 23% に戻す
target_iconlist = """    #sdgs .iconlist li {
        margin: 1.5% 0 !important;
        float: none !important;
        flex-basis: 31% !important;
    }
    #sdgs .iconlist::after {
        content: "" !important;
        flex-basis: 31% !important;
    }"""

replacement_iconlist = """    #sdgs .iconlist li {
        width: 23% !important;
        margin: 1.5% 0 !important;
        float: none !important;
    }
    #sdgs .iconlist::after {
        content: "" !important;
        flex-basis: 23% !important;
    }"""

# 厳格に CRLF でマーカーを構築
target_allitem_crlf = target_allitem.replace("\r\n", "\n").replace("\n", "\r\n")
target_iconlist_crlf = target_iconlist.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_iconlist_crlf = replacement_iconlist.replace("\r\n", "\n").replace("\n", "\r\n")

repaired_count = 0

if target_allitem_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_allitem_crlf, "")
    print("Successfully removed #sdgs .allitem .iconlist styles.")
    repaired_count += 1
else:
    print("Warning: target_allitem not found in CSS.")

if target_iconlist_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_iconlist_crlf, replacement_iconlist_crlf)
    print("Successfully restored #sdgs .iconlist li styles to 23% width.")
    repaired_count += 1
else:
    print("Warning: target_iconlist not found in CSS.")

if repaired_count > 0:
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)

print(f"--- Rollback Completed. Repaired {repaired_count} block(s). ---")
