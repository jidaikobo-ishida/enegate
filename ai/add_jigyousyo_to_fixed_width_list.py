# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# スマホ時の自動幅化リストに #jigyousyo 関連の固定幅要素を追加する
target = """    .inner,
    .inner900,
    .twocontent,
    #globalnav ul,
    #mainimg .mainlogo P,
    #Imgnav .Imgnavwrap,
    #productsnav .prosnavwrap,
    #allproductsnav .prosnavwrap,
    #footer .fwrap,
    #iteminfo .section,
    #iteminfo .ecobanner,
    #jirei .section,
    #jireisin .section,
    #metainfo .section,
    #eco .section {"""

replacement = """    .inner,
    .inner900,
    .twocontent,
    #globalnav ul,
    #mainimg .mainlogo P,
    #Imgnav .Imgnavwrap,
    #productsnav .prosnavwrap,
    #allproductsnav .prosnavwrap,
    #footer .fwrap,
    #iteminfo .section,
    #iteminfo .ecobanner,
    #jirei .section,
    #jireisin .section,
    #metainfo .section,
    #eco .section,
    #jigyousyo .sctxt,
    #jigyousyo .infotxt .txtbox,
    #jigyousyo .infotxt .imgbox,
    #jigyousyo .voicebox .txtbox,
    #jigyousyo .kanribox .kanritxt,
    #jigyousyo #kanri .sctxt {"""

# 厳格に CRLF でマーカーを構築
target_crlf = target.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully added #jigyousyo elements to the auto-width list in common.css.")
else:
    print("Error: Target auto-width list not found in common.css.")
