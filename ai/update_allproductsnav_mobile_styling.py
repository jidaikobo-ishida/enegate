# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 旧定義ブロック
target = """#allproductsnav .prosnavwrap { width:100%; background:#FFF;}
#allproductsnav a { 
	display: block;
	height:40px;
	width : 33.33333% ;
	width : -webkit-calc(100% / 3) ;
	width : calc(100% / 3) ;
	padding:5px 0 !important;
	line-height:1.6em;
	font-size:1.2em;}
#allproductsnav .imgnav01 { background:#538FD4; padding-top:4px;}
#allproductsnav .imgnav02 { background:#6D6B92; line-height:43px;}
#allproductsnav .imgnav03 { background:#F08263; padding-top:4px;}
#allproductsnav .imgnav04 { background:#E3C05D; line-height:43px;}
#allproductsnav .imgnav05 { background:#EB8CB7; padding-top:4px;}
#allproductsnav .imgnav06 { background:#74C1A4; padding-top:4px;}"""

# 新定義ブロック（背景色削除、width変更、flex/gap追加）
replacement = """#allproductsnav .prosnavwrap {
    width: 100%;
    background: #FFF;
    display: flex;
    flex-wrap: wrap;
    gap: 1px;
}
#allproductsnav a { 
	display: block;
	height:40px;
	width: calc((100% - 2px) / 3) !important;
	padding:5px 0 !important;
	line-height:1.6em;
	font-size:1.2em;}
#allproductsnav .imgnav01 { padding-top:4px;}
#allproductsnav .imgnav02 { line-height:43px;}
#allproductsnav .imgnav03 { padding-top:4px;}
#allproductsnav .imgnav04 { line-height:43px;}
#allproductsnav .imgnav05 { padding-top:4px;}
#allproductsnav .imgnav06 { padding-top:4px;}"""

# 厳格に CRLF でマーカーを構築
target_crlf = target.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully updated #allproductsnav mobile styles in common.css.")
else:
    print("Error: Target marker not found in common.css.")
