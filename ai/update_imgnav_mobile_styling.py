# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 旧定義ブロック
target = """    #Imgnav .Imgnavwrap {
        width: 100% !important;
        background: #FFF !important;
        display: flex !important;
        flex-wrap: wrap !important;
    }
    #Imgnav a {
        display: block !important;
        height: 40px !important;
        width: 33.33333% !important;
        width: -webkit-calc(100% / 3) !important;
        width: calc(100% / 3) !important;
        padding: 5px 0 !important;
        font-size: 1.2em !important;
        line-height: 1.6em !important;
        color: #FFF !important;
        text-align: center !important;
        float: left !important;
        z-index: 100 !important;
    }
    #Imgnav span { display: inline !important; }
    #Imgnav img { display: none !important; }
    #Imgnav .imgnav01 { background: #538FD4 !important; }
    #Imgnav .imgnav02 { background: #6D6B92 !important; line-height: 43px !important; }
    #Imgnav .imgnav03 { background: #F08263 !important; }
    #Imgnav .imgnav04 { background: #E3C05D !important; line-height: 43px !important; }
    #Imgnav .imgnav05 { background: #EB8CB7 !important; }
    #Imgnav .imgnav06 { background: #74C1A4 !important; }"""

# 新定義ブロック（背景色削除、width変更、gap追加）
replacement = """    #Imgnav .Imgnavwrap {
        width: 100% !important;
        background: #FFF !important;
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 1px !important;
    }
    #Imgnav a {
        display: block !important;
        height: 40px !important;
        width: calc((100% - 2px) / 3) !important;
        padding: 5px 0 !important;
        font-size: 1.2em !important;
        line-height: 1.6em !important;
        color: #FFF !important;
        text-align: center !important;
        float: left !important;
        z-index: 100 !important;
    }
    #Imgnav span { display: inline !important; }
    #Imgnav img { display: none !important; }
    #Imgnav .imgnav02 { line-height: 43px !important; }
    #Imgnav .imgnav04 { line-height: 43px !important; }"""

# 厳格に CRLF でマーカーを構築
target_crlf = target.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully updated #Imgnav mobile styles in common.css.")
else:
    print("Error: Target marker not found in common.css.")
