# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 以前個別に追記していた padding 指定や余白調整ブロックを検索し、一括定義に置換・整理する
target_section = """    /* スマホ時の#jigyousyo先輩の声テキストボックスの余白・中央寄せ調整 */
    #jigyousyo .voicebox .txtbox {
        margin: 0 auto !important;
        float: none !important;
    }
    #jigyousyo .voicebox {
        padding: 15px !important;
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
    /* スマホ時の事業内容管理部門(#division #kanri .voicebox)のパディング調整 */
    #division #kanri .voicebox {
        padding: 15px !important;
    }"""

replacement_section = """    /* スマホ時の先輩の声(.voicebox)一括パディング・余白リセット調整 */
    .voicebox {
        padding: 15px !important;
        box-sizing: border-box !important;
    }
    .voicebox .txtbox,
    .voicebox .imgbox {
        margin: 0 auto !important;
        float: none !important;
        width: 100% !important;
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
    }"""

# 厳格に CRLF でマーカーを構築
target_section_crlf = target_section.replace("\r\n", "\n").replace("\n", "\r\n")
replacement_section_crlf = replacement_section.replace("\r\n", "\n").replace("\n", "\r\n")

if target_section_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_section_crlf, replacement_section_crlf)
    # 書き込み (厳格に cp932 エンコーディング)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_crlf)
    print("Successfully applied unified mobile .voicebox styles to common.css.")
else:
    print("Error: Target style block not found in common.css.")
