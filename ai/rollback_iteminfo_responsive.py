# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 追加した CSS ブロックを完全に削除して元に戻す
target_block = """/* ==========================================================
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

target_block_lf = target_block.replace("\r\n", "\n")

if target_block_lf in content_lf:
    content_lf = content_lf.replace(target_block_lf, "")
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully rolled back iteminfo responsive styles in common.css.")
else:
    # 完全に一致しなかった場合の汎用部分一致削除
    if "画面幅950px以下における製品詳細ページ" in content_lf:
        # パターンマッチでの削除
        pattern = r'/\* =+.*?画面幅950px以下における製品詳細ページ.*?\}\s*\}\s*\}'
        content_lf = re.sub(pattern, "", content_lf, flags=re.DOTALL)
        with open(css_path, "w", encoding="cp932", errors="ignore") as f:
            f.write(content_lf)
        print("Successfully rolled back iteminfo responsive styles in common.css (regex).")
    else:
        print("Target rollback block not found in CSS.")
