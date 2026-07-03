# -*- coding: utf-8 -*-
import re

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 以前追加した950px以下のメディアクエリ（5つのブロック）をまとめてコメントアウトする。
# コメント内にネストした */ があるとコメントアウトが壊れるため、
# 安全に内側のコメントを加工しつつ、全体を /* ... */ で包む。

target_blocks = """/* ==========================================================
   画面幅950px以下における各要素のmin-width固定値解除
   ========================================================== */
@media screen and (max-width: 950px) {
    #content,
    #fnav {
        min-width: auto !important;
    }
}


/* ==========================================================
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
   画面幅950px以下におけるヘッダーサブナビゲーション位置調整
   ========================================================== */
@media screen and (max-width: 950px) {
    #header .hdsub {
        left: auto !important;
        right: 320px !important;
    }
    #header .logo {
        width: 250px !important;
    }
}

/* ==========================================================
   画面幅950px以下からスマホサイズ(737px)までのグローバルメニュー余白調整
   ========================================================== */
@media screen and (max-width: 950px) and (min-width: 737px) {
    #glmenu {
        margin-left: -15px !important;
    }
}


/* ==========================================================
   画面幅810px以下から737pxまでのヘッダーロゴマージン調整
   ========================================================== */
@media screen and (max-width: 810px) and (min-width: 737px) {
    #header .logo {
        margin: 14px 0 27px !important;
    }
}"""

# ネストコメントを無効化（ */ を * / に）
safe_target = target_blocks.replace("*/", "* /")

commented_blocks = f"""/* COMMENTED OUT TEMPORARILY BY USER REQUEST
{safe_target}
END COMMENTED OUT */"""

target_blocks_lf = target_blocks.replace("\r\n", "\n")
commented_blocks_lf = commented_blocks.replace("\r\n", "\n")

if target_blocks_lf in content_lf:
    content_lf = content_lf.replace(target_blocks_lf, commented_blocks_lf)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully commented out max-width: 950px media queries in common.css.")
else:
    # 部分一致による置換
    if "画面幅950px以下における各要素のmin-width固定値解除" in content_lf:
        # 手動で正規表現置換
        print("Target block not exact match, trying broader replacement...")
        # 簡易置換のため、特徴的な箇所の前後で置換
        # (3201行目の/* === 画面幅950px以下における各要素のmin-width固定値解除 から
        # 3264行目の最後の } まで)
        # ※ python で安全に文字列インデックスをスキャンして置換する
        start_marker = "/* ==========================================================\n   画面幅950px以下における各要素のmin-width固定値解除"
        end_marker = "    #header .logo {\n        margin: 14px 0 27px !important;\n    }\n}"
        
        idx_start = content_lf.find(start_marker)
        idx_end = content_lf.find(end_marker)
        
        if idx_start != -1 and idx_end != -1:
            end_pos = idx_end + len(end_marker)
            sub_block = content_lf[idx_start:end_pos]
            safe_sub = sub_block.replace("*/", "* /")
            replacement_sub = f"/* COMMENTED OUT TEMPORARILY BY USER REQUEST\n{safe_sub}\nEND COMMENTED OUT */"
            
            content_lf = content_lf.replace(sub_block, replacement_sub)
            with open(css_path, "w", encoding="cp932", errors="ignore") as f:
                f.write(content_lf)
            print("Successfully commented out max-width: 950px media queries in common.css (index match).")
        else:
            print("Markers not found.")
    else:
        print("CSS 950px target block not found at all.")
