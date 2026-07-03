# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 950px以下大枠解除の直下に、製品詳細用つっかえ棒解除とスクロールテーブルの拡大適用を追記
target = """/* ==========================================================
   画面幅950px以下における大枠の固定横幅(width)解除
   ========================================================== */
@media screen and (max-width: 950px) {
    .inner,
    .inner900,
    #content,
    #globalnav ul,
    #Imgnav .Imgnavwrap,
    #productsnav .prosnavwrap,
    #allproductsnav .prosnavwrap,
    #fnav,
    #footer .fwrap,
    /* /* #list #article, */ */
    #iteminfo .section,
    #iteminfo .ecobanner,
    #jirei .section,
    #jireisin .section,
    #metainfo .section,
    #eco .section {
        width: auto !important;
    }
}"""

replacement = """/* ==========================================================
   画面幅950px以下における大枠の固定横幅(width)解除
   ========================================================== */
@media screen and (max-width: 950px) {
    .inner,
    .inner900,
    #content,
    #globalnav ul,
    #Imgnav .Imgnavwrap,
    #productsnav .prosnavwrap,
    #allproductsnav .prosnavwrap,
    #fnav,
    #footer .fwrap,
    /* /* #list #article, */ */
    #iteminfo .section,
    #iteminfo .ecobanner,
    #jirei .section,
    #jireisin .section,
    #metainfo .section,
    #eco .section {
        width: auto !important;
    }
}

/* ==========================================================
   画面幅950px以下における製品詳細ページ（#iteminfo）の要素流動化（つっかえ棒解除）
   ========================================================== */
@media screen and (max-width: 950px) {
    #iteminfo .section {
        width: 100% !important;
        max-width: 950px !important;
        padding: 15px 0 !important;
        box-sizing: border-box !important;
    }
    #iteminfo .itemoutline {
        display: block !important;
    }
    #iteminfo .itemoutline #gallery {
        display: block !important;
        text-align: center !important;
        margin-bottom: 15px !important;
        width: 100% !important;
    }
    #iteminfo .itemoutline .copy {
        display: block !important;
        width: 100% !important;
        box-sizing: border-box !important;
        padding: 0 15px 15px !important;
    }
    #iteminfo .itemoutline h2 {
        font-size: 2.0em !important;
        margin-top: 0 !important;
    }
    #iteminfo .itemoutline p {
        font-size: 1.6em !important;
    }
    #iteminfo .ecobanner {
        width: 95% !important;
        padding: 5px !important;
        font-size: 1.3em !important;
        text-align: center !important;
        margin: 10px auto !important;
    }
    #iteminfo .ecobanner img {
        margin: 10px auto !important;
        display: block !important;
        vertical-align: middle !important;
    }
    #iteminfo .litemtxt,
    #iteminfo .ritemtxt {
        width: 100% !important;
        float: none !important;
        padding: 0 15px 15px !important;
        box-sizing: border-box !important;
    }
    
    /* 仕様テーブルの横スクロール化調整を950px以下に拡大適用 */
    .scrolltable {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: auto !important;
        padding: 0.5rem 0 !important;
        box-sizing: border-box !important;
        -webkit-overflow-scrolling: touch;
    }
    .scrolltable .itemspec {
        min-width: 650px !important;
    }
    .scrolltable::before,
    .scrolltable::after {
        content: '横スクロールできます。' !important;
        display: block !important;
        font-size: 0.8em !important;
        color: #666 !important;
        text-align: right !important;
        margin-top: 5px !important;
        clear: both !important;
        padding-right: 15px !important;
    }
}"""

target_lf = target.replace("\r\n", "\n")
replacement_lf = replacement.replace("\r\n", "\n")

if target_lf in content_lf:
    content_lf = content_lf.replace(target_lf, replacement_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully fixed iteminfo responsive issues and scrolltable in common.css.")
else:
    print("CSS target marker not found.")
