# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 今回追加したスマホ用メディアクエリ内のブロック（末尾部分）
target_block = """    /* スマホ時のGoogleマップエリア(div.main/div.sub)のフロート解除・中央寄せ調整 */
    div.main,
    #google div.main,
    #google div.sub {
        float: none !important;
        width: auto !important;
    }
    div.main,
    #google div.main {
        font-size: 1.4em !important;
    }
    #google div.main p {
        margin: 0 auto !important;
    }
    /* スマホ時の地図ページ.type02cアクセス見出し調整 */
    .type02c h4.access img {
        display: none !important; /* ← 画像を非表示 */
    }
    .type02c h4.access::before {
        content: 'ACCESS' !important;               /* ← テキストを表示 */
        font-size: 1em !important;
        font-weight: bold !important;
        color: #4055b2 !important;                  /* ← 文字色：青色 */
        background: #dceffd !important;             /* ← 背景色：水色 */
        display: block !important;
        padding: 0.2rem 0.5rem !important;          /* ← 内側余白を設定 */
        margin: 1rem auto !important;               /* ← 上下余白 & 中央寄せ */
    }
    /* スマホ時の地図ページアクセス表(table.type02c)のセル縦並び化 */
    body#list .twocontent .group .boxType02 table.type02c td {
        display: block !important;
        width: 100% !important;
        box-sizing: border-box !important;
        border: none !important;
    }
    /* スマホ時の事業内容(#division #kanri)のsctxt要素の100%幅化・フロート解除 */
    #division #kanri .sctxt {
        width: 100% !important;
        float: none !important;
        clear: both !important;
    }
    /* スマホ時の青丸付き見出し(.bldottitle)のパディング・フロート解除調整 */
    .bldottitle {
        float: none !important;
    }
    /* スマホ時の青帯付き見出し(.bltitle h2)のフォントサイズ調整 */
    .bltitle h2 {
        font-size: 1.4em !important;
    }
    /* スマホ時のトピックスリスト(#topics .topicslist)調整 */
    #topics .topicslist dt {
        padding: 20px 0 10px !important;
        float: none !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    #topics .topicslist dd {
        padding: 0 !important;
        margin: 0 0 20px !important;
        text-indent: 0 !important;
        border: none !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    #topics .topicslist dd a {
        display: block !important;
        position: relative !important;
        padding: 0 0 0 80px !important;
    }
    #topics .topicslist dd a span {
        position: absolute !important;
        left: 0 !important;
        top: 0 !important;
        margin-right: 0 !important; /* PC用の右マージンを解除 */
    }
    /* スマホ時のトピックス見出し(#topics .bltitle.underline)の余白リセット */
    #topics .bltitle.underline {
        margin: 0 !important;
    }"""

replacement_block = """    /* スマホ時のGoogleマップエリア(div.main/div.sub)のフロート解除・中央寄せ調整 */
    div.main,
    #google div.main,
    #google div.sub {
        float: none;
        width: auto;
    }
    div.main,
    #google div.main {
        font-size: 1.4em;
    }
    #google div.main p {
        margin: 0 auto;
    }
    /* スマホ時の地図ページ.type02cアクセス見出し調整 */
    .type02c h4.access img {
        display: none; /* ← 画像を非表示 */
    }
    .type02c h4.access::before {
        content: 'ACCESS';               /* ← テキストを表示 */
        font-size: 1em;
        font-weight: bold;
        color: #4055b2;                  /* ← 文字色：青色 */
        background: #dceffd;             /* ← 背景色：水色 */
        display: block;
        padding: 0.2rem 0.5rem;          /* ← 内側余白を設定 */
        margin: 1rem auto;               /* ← 上下余白 & 中央寄せ */
    }
    /* スマホ時の地図ページアクセス表(table.type02c)のセル縦並び化 */
    body#list .twocontent .group .boxType02 table.type02c td {
        display: block;
        width: 100%;
        box-sizing: border-box;
        border: none;
    }
    /* スマホ時の事業内容(#division #kanri)のsctxt要素の100%幅化・フロート解除 */
    #division #kanri .sctxt {
        width: 100%;
        float: none;
        clear: both;
    }
    /* スマホ時の青丸付き見出し(.bldottitle)のパディング・フロート解除調整 */
    .bldottitle {
        float: none;
    }
    /* スマホ時の青帯付き見出し(.bltitle h2)のフォントサイズ調整 */
    .bltitle h2 {
        font-size: 1.4em;
    }
    /* スマホ時のトピックスリスト(#topics .topicslist)調整 */
    #topics .topicslist dt {
        padding: 20px 0 10px;
        float: none;
        width: 100%;
        box-sizing: border-box;
    }
    #topics .topicslist dd {
        padding: 0;
        margin: 0 0 20px;
        text-indent: 0;
        border: none;
        width: 100%;
        box-sizing: border-box;
    }
    #topics .topicslist dd a {
        display: block;
        position: relative;
        padding: 0 0 0 80px;
    }
    #topics .topicslist dd a span {
        position: absolute;
        left: 0;
        top: 0;
        margin-right: 0; /* PC用の右マージンを解除 */
    }
    /* スマホ時のトピックス見出し(#topics .bltitle.underline)の余白リセット */
    #topics .bltitle.underline {
        margin: 0;
    }"""

# 厳格に CRLF でマーカーを構築
target_crlf = target_block.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_crlf = replacement_block.replace("\r\n", "\n").replace("\n", "\r\n")

if target_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_crlf, replacement_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully removed all unnecessary !important declarations from common.css.")
else:
    print("Error: Target marker not found in common.css.")
