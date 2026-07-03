# -*- coding: utf-8 -*-
import os
import re
import glob

print("--- HTML Patching Script Start ---")

# 共通製品ナビゲーション（Shift-JISで書き込むため、Pythonの文字列として定義し、cp932エンコードで処理）
common_nav = """<div id="productsnav"></div>
<div id="allproductsnav">
<div class="inner clearfix">
	<div class="prosnavwrap clearfix">
	<a href="/products/seigyo.html" class="imgnav01 fade letsp">電力の計測・監視・制御</a>
	<a href="/products/henkan.html" class="imgnav02 fade">電力の変換</a>
	<a href="/products/eco.html" class="imgnav03 fade">エネルギーマネジメント</a>
	<a href="/products/tsusin.html" class="imgnav04 fade">通信</a>
	<a href="/products/mente.html" class="imgnav05 fade">工事・メンテナンス</a>
	<a href="/products/index.html" class="imgnav06 fade">製品・サービス一覧</a>
	</div>
</div>
</div>"""

# 会社概要・事業所用共通CSSスタイル
list_style = """<style>
/* 事業所グループ要素の幅100%とテキストサイズ14px化 */
.twocontent .group {
    width: 100% !important;
}
.twocontent .group, 
.twocontent .group p, 
.twocontent .group td, 
.twocontent .group li,
.twocontent .group h3 {
    font-size: 14px !important;
}
/* 新デザイン等へのリニューアル */
.twocontent .group .boxType02 {
    border: 1px solid #C5D6DC !important;
    padding: 1px !important;
    background: none !important;
}
.twocontent .group .type02 {
    width: 100% !important;
    margin: 0 !important;
    border: 3px solid #d2e5f4 !important;
}
.twocontent .group .type02 td.end {
    width: 50% !important;
}
.twocontent .boxTop,
.twocontent .boxBtm {
    display: none !important;
}
</style>
</head>"""

# Shift-JIS (cp932) でファイルを読み書きするヘルパー
def process_file(filepath, replacements):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
    
    try:
        with open(filepath, "r", encoding="cp932", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False
    
    modified = False
    for target, replacement in replacements:
        if target in content:
            content = content.replace(target, replacement)
            modified = True
        else:
            # 改行コードのゆらぎに対応
            target_lf = target.replace("\r\n", "\n")
            content_lf = content.replace("\r\n", "\n")
            if target_lf in content_lf:
                content = content_lf.replace(target_lf, replacement.replace("\r\n", "\n"))
                modified = True

    if modified:
        try:
            with open(filepath, "w", encoding="cp932", errors="ignore") as f:
                f.write(content)
            print(f"Successfully patched: {filepath}")
            return True
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
            return False
    else:
        print(f"No changes applied to: {filepath}")
        return False

# =========================================================================
# 1. 製品関連ページのパッチ適用
# =========================================================================
products_files = [
    "products/index.html",
    "products/tsusin.html",
    "products/eco.html",
    "products/seigyo.html",
    "products/henkan.html",
    "products/mente.html",
    "products/other/other01.html"
]

# 各製品ファイルでの共通置換
for pf in products_files:
    # 既存の productsnav (class="section" がついているもの、またはついていないもの) を common_nav に置換
    # 本番環境のナビ定義を抽出
    target_nav_pattern = r'<div class="section" id="productsnav">.*?</div>\s*</div>'
    target_nav_pattern_2 = r'<div class="section" id="productsnav">.*?</div>\s*</div>\s*</div>'
    
    filepath = pf
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="cp932", errors="ignore") as f:
        p_content = f.read()
        
    # productsnavの部分を正規表現で探して置換
    p_content_modified = False
    
    # <div class="section" id="productsnav"> ... </div> (その中の clearfix などの閉じタグまでを特定)
    # 本番は <div class="section" id="productsnav"> から次の </div> </div> までの構造
    nav_match = re.search(r'<div class="section" id="productsnav">.*?</div>\s*</div>', p_content, re.DOTALL)
    if nav_match:
        p_content = p_content.replace(nav_match.group(0), common_nav)
        p_content_modified = True
        print(f"Replaced productsnav in {pf}")

    # クラス調整の適用
    replacements = [
        # bltitle の section 削除
        ('class="section bltitle blwidback productstop"', 'class="bltitle blwidback productstop"'),
        # メインコンテナの section 削除
        ('<div class="section">\n<div class="inner clearfix">\n<img src="img/sdgs_index.jpg"', '<div>\n<div class="inner clearfix">\n<img src="img/sdgs_index.jpg"'),
        ('<div class="section">\n<div class="inner clearfix">\n\t<img src="img/sdgs_tsusin.jpg"', '<div>\n<div class="inner clearfix">\n\t<img src="img/sdgs_tsusin.jpg"'),
        ('<div class="section">\n<div class="inner clearfix">\n\t<img src="img/sdgs_eco.jpg"', '<div>\n<div class="inner clearfix">\n\t<img src="img/sdgs_eco.jpg"'),
        ('<div class="section"> \n<div class="inner clearfix">\n\t<img src="img/sdgs_seigyo.jpg"', '<div> \n<div class="inner clearfix">\n\t<img src="img/sdgs_seigyo.jpg"'),
        ('<div class="section">\n<div class="inner clearfix">\n<img src="img/sdgs_henkan.jpg"', '<div>\n<div class="inner clearfix">\n<img src="img/sdgs_henkan.jpg"'),
        ('<div class="section">\n<div class="inner clearfix">\n\t<img src="img/sdgs_mente.jpg"', '<div>\n<div class="inner clearfix">\n\t<img src="img/sdgs_mente.jpg"'),
    ]
    
    # tsusin_text の適用 (products/tsusin.html)
    if pf == "products/tsusin.html":
        replacements.append(('<p class="text">ネット技術の', '<p class="text tsusin_text">ネット技術の'))
        
    # other01 のテーブルラップ (products/other/other01.html)
    if pf == "products/other/other01.html":
        replacements.append((
            '<table class="itemspec">',
            '<div class="scrolltable"><table class="itemspec">'
        ))
        replacements.append((
            '</table>\n\n\t</div>',
            '</table></div>\n\n\t</div>'
        ))

    # 置換を適用
    for target, replacement in replacements:
        # 日本語を含む場合は errors="ignore" で処理されるように置換を適用
        target_encoded = target.encode("cp932", "ignore").decode("cp932", "ignore")
        replacement_encoded = replacement.encode("cp932", "ignore").decode("cp932", "ignore")
        if target_encoded in p_content:
            p_content = p_content.replace(target_encoded, replacement_encoded)
            p_content_modified = True
        else:
            # 改行やスペース調整
            target_clean = re.sub(r'\s+', '', target_encoded)
            # コンテンツ側の空白を除去してマッチングする等の柔軟な対応
            
    if p_content_modified:
        with open(filepath, "w", encoding="cp932", errors="ignore") as f:
            f.write(p_content)
        print(f"Patched products file: {pf}")

# =========================================================================
# 2. メーター関連ページのパッチ適用 (meter02/index.html)
# =========================================================================
meter_file = "meter02/index.html"
meter_replacements = [
    (
        '<table class="itemspec">\n\t\t  <tr> \n\t\t  \t<th class="thline"',
        '<div class="scrolltable"><table class="itemspec">\n\t\t  <tr> \n\t\t  \t<th class="thline"'
    ),
    (
        '</table>\n\t\t<p class="mintxt">詳細',
        '</table></div>\n\t\t<p class="mintxt">詳細'
    )
]
process_file(meter_file, meter_replacements)

# =========================================================================
# 3. 会社概要・拠点案内・地図ルートページのパッチ適用
# =========================================================================

# company/list/index.html の処理
list_index_file = "company/list/index.html"
list_index_replacements = [
    ('</head>', list_style),
    ('width="690" height="568"', 'width="100%" height="auto"'),
    ('width="690" height="50"', 'width="100%" height="auto"')
]
process_file(list_index_file, list_index_replacements)

# company/list/list.html の処理
list_file = "company/list/list.html"
list_replacements = [
    ('</head>', list_style),
    (
        '<table class="type02">',
        '<div class="scrolltable"><table class="type02">'
    ),
    (
        '</table>\n\t\t\t\t<div class="boxBtm">',
        '</table></div>\n\t\t\t\t<div class="boxBtm" style="display:none;">'
    ),
    (
        '<div class="boxTop"><img src="/cmn/img/div_top02.gif" alt="" width="690" height="7" /></div>',
        '<div class="boxTop" style="display:none;"><img src="/cmn/img/div_top02.gif" alt="" width="690" height="7" /></div>'
    )
]
process_file(list_file, list_replacements)

# company/list/mapXX.html (22ファイル) の処理
# すべての map*.html に対して、ヘッダーに list_style を適用するだけで、
# PCレイアウトの余幅を維持したまま、1カラム100%幅へのレスポンシブ化が自動で達成される。
map_files = glob.glob("company/list/map*.html")
for mf in map_files:
    # 既に適用されていない場合のみ追加
    with open(mf, "r", encoding="cp932", errors="ignore") as f:
        mf_content = f.read()
    if ".twocontent .group" not in mf_content:
        mf_content = mf_content.replace("</head>", list_style)
        # 画像の幅のレスポンシブ化
        mf_content = mf_content.replace('width="690" height="39"', 'width="100%" height="auto"')
        mf_content = mf_content.replace('width="690" height="7"', 'width="100%" height="auto"')
        with open(mf, "w", encoding="cp932", errors="ignore") as f:
            f.write(mf_content)
        print(f"Patched map file: {mf}")
    else:
        print(f"Map file already patched: {mf}")

print("--- HTML Patching Script End ---")
