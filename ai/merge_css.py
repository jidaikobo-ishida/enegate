# -*- coding: utf-8 -*-
import os
import re

test_css_path = "../enegate-test/common/css/common.css"
honban_css_path = "common/css/common.css"

print("--- CSS Merge Script Start ---")

# 1. テスト環境CSSからスマホ用スタイル（/* RESPONSIVE STYLES */ 以降）を取得
with open(test_css_path, "r", encoding="cp932", errors="ignore") as f:
    test_content = f.read()

responsive_marker = "/* RESPONSIVE STYLES */"
if responsive_marker in test_content:
    responsive_styles = test_content[test_content.index(responsive_marker):]
    print("Found responsive styles in test CSS.")
else:
    raise Exception("Responsive marker not found in test CSS")

# 2. 本番CSSを読み込む
with open(honban_css_path, "r", encoding="cp932") as f:
    honban_content = f.read()

print("Loaded honban CSS.")

# 3. 必要な置換を実行

# ① body から min-width: 950px; を削除
body_pattern = r'(body\s*\{[^}]*?)min-width\s*:\s*950px\s*;?\s*'
if re.search(body_pattern, honban_content, flags=re.DOTALL):
    honban_content = re.sub(body_pattern, r'\1', honban_content, flags=re.DOTALL)
    print("① Removed 'min-width: 950px' from body.")
else:
    print("① 'min-width: 950px' not found in body or already removed.")

# ② #article に max-width: 100%; を追加
article_target = "#article {  font-size: 13px; *font-size: small; /* IE7+ */ *font: x-small; /* IE6- */}"
article_replace = "#article {  font-size: 13px; *font-size: small; /* IE7+ */ *font: x-small; /* IE6- */; max-width: 100%;}"
if article_target in honban_content:
    honban_content = honban_content.replace(article_target, article_replace)
    print("② Added 'max-width: 100%' to #article.")
else:
    print("② #article target style not found.")

# ③ @media screen and (max-width: 950px) 内の更新
pattern_950 = r'@media screen and \(max-width:\s*950px\)\s*\{\s*\.full\{\s*min-width:\s*950px;\s*margin-left:0;\s*\}\s*\}'
replacement_950 = """@media screen and (max-width: 950px){
.full{  margin-left:0;}
#content { min-width: auto; }
.inner { width: 100%; max-width: 950px; box-sizing: border-box; }
#header > .inner { padding: 0 15px; box-sizing: border-box; }
.leftsubnav { width: 20%; box-sizing: border-box; }
.twocontent { width: 76%; float: right; box-sizing: border-box; }
img { max-width: 100%; height: auto; }
table.type02 { width: 100% !important; margin: 0 auto !important; }
}"""

if re.search(pattern_950, honban_content):
    honban_content = re.sub(pattern_950, replacement_950, honban_content)
    print("③ Updated @media screen and (max-width: 950px).")
else:
    print("③ @media screen and (max-width: 950px) pattern not matched.")

# ④ #productsnav のコメントアウト化と #allproductsnav のflex化
prosnav_start_marker = "/*ProductsNav*/"
prosnav_end_marker = "#allproductsnav .letsp {letter-spacing:-1px;}"

if prosnav_start_marker in honban_content and prosnav_end_marker in honban_content:
    start_idx = honban_content.index(prosnav_start_marker)
    end_idx_temp = honban_content.index(prosnav_end_marker) + len(prosnav_end_marker)
    end_idx = honban_content.index("}", end_idx_temp) + 1
    
    test_start_idx = test_content.index(prosnav_start_marker)
    test_end_idx_temp = test_content.index(prosnav_end_marker) + len(prosnav_end_marker)
    test_end_idx = test_content.index("}", test_end_idx_temp) + 1
    test_prosnav_block = test_content[test_start_idx:test_end_idx]
    
    honban_content = honban_content[:start_idx] + test_prosnav_block + honban_content[end_idx:]
    print("④ Replaced #productsnav and #allproductsnav block.")
else:
    print("④ Could not find ProductsNav markers.")

# ⑤ #products .cat_link li の line-height 調整
cat_link_target = """#products .cat_link li{
display:block;
padding-left:22px !important;
position: relative;
color: #000;
line-height:2.2;
vertical-align: middle;
text-decoration: none;
font-size:1.5em;
}"""
cat_link_replace = """#products .cat_link li{
display:block;
padding-left:22px !important;
position: relative;
color: #000;
line-height:1.6;
vertical-align: middle;
text-decoration: none;
font-size:1.5em;
margin-bottom:10px;
}"""

if cat_link_target in honban_content:
    honban_content = honban_content.replace(cat_link_target, cat_link_replace)
    print("⑤ Updated #products .cat_link li style.")
else:
    cat_link_pattern = r'#products\s+\.cat_link\s+li\s*\{\s*display:\s*block;\s*padding-left:\s*22px\s*!important;\s*position:\s*relative;\s*color:\s*#000;\s*line-height:\s*2\.2;\s*vertical-align:\s*middle;\s*text-decoration:\s*none;\s*font-size:\s*1\.5em;\s*\}'
    if re.search(cat_link_pattern, honban_content):
        honban_content = re.sub(cat_link_pattern, cat_link_replace, honban_content)
        print("⑤ Updated #products .cat_link li style (regex).")
    else:
        print("⑤ #products .cat_link li style not found.")

# ⑥ #products .catlist に clear:both; を追加
catlist_target = "#products .catlist { width:100%; display:table; padding:30px 0; border-bottom:1px solid #979797;}"
catlist_replace = "#products .catlist { width:100%; display:table; padding:30px 0; border-bottom:1px solid #979797; clear:both;}"
if catlist_target in honban_content:
    honban_content = honban_content.replace(catlist_target, catlist_replace)
    print("⑥ Added clear:both to #products .catlist.")
else:
    catlist_pattern = r'#products\s+\.catlist\s*\{\s*width:\s*100%;\s*display:\s*table;\s*padding:\s*30px\s+0;\s*border-bottom:\s*1px\s+solid\s+#979797;\s*\}'
    if re.search(catlist_pattern, honban_content):
        honban_content = re.sub(catlist_pattern, catlist_replace, honban_content)
        print("⑥ Added clear:both to #products .catlist (regex).")
    else:
        print("⑥ #products .catlist not found.")

# ⑦ #allitem .jireilink の更新
jireilink_target = "#allitem .jireilink { margin-bottom:20px;}"
jireilink_replace = """#allitem .jireilink { margin-bottom:30px !important;}
#allitem .jireilink span { bottom:-20px; top:auto;}"""
if jireilink_target in honban_content:
    honban_content = honban_content.replace(jireilink_target, jireilink_replace)
    print("⑦ Updated #allitem .jireilink.")
else:
    jireilink_pattern = r'#allitem\s+\.jireilink\s*\{\s*margin-bottom:\s*20px;\s*\}'
    if re.search(jireilink_pattern, honban_content):
        honban_content = re.sub(jireilink_pattern, jireilink_replace, honban_content)
        print("⑦ Updated #allitem .jireilink (regex).")
    else:
        print("⑦ #allitem .jireilink not found.")

# ⑧ #metainfo .section と #eco .section に max-width:100% を追加
metainfo_target = "#metainfo .section { width:850px; margin:0 auto; padding:0 0 30px 0;}"
metainfo_replace = "#metainfo .section { width:850px; max-width:100%; margin:0 auto; padding:0 0 30px 0;}"
if metainfo_target in honban_content:
    honban_content = honban_content.replace(metainfo_target, metainfo_replace)
    print("⑧-1 Added max-width to #metainfo .section.")
else:
    metainfo_pattern = r'#metainfo\s+\.section\s*\{\s*width:\s*850px;\s*margin:\s*0\s+auto;\s*padding:\s*0\s+0\s+30px\s+0;\s*\}'
    if re.search(metainfo_pattern, honban_content):
        honban_content = re.sub(metainfo_pattern, metainfo_replace, honban_content)
        print("⑧-1 Added max-width to #metainfo .section (regex).")
    else:
        print("⑧-1 #metainfo .section not found.")

eco_target = "#eco .section { width:850px; margin:0 auto; padding:0 0 25px 0;}"
eco_replace = "#eco .section { width:100%; max-width:850px; margin:0 auto; padding:0 0 25px 0;}"
if eco_target in honban_content:
    honban_content = honban_content.replace(eco_target, eco_replace)
    print("⑧-2 Added max-width to #eco .section.")
else:
    eco_pattern = r'#eco\s+\.section\s*\{\s*width:\s*850px;\s*margin:\s*0\s+auto;\s*padding:\s*0\s+0\s+25px\s+0;\s*\}'
    if re.search(eco_pattern, honban_content):
        honban_content = re.sub(eco_pattern, eco_replace, honban_content)
        print("⑧-2 Added max-width to #eco .section (regex).")
    else:
        print("⑧-2 #eco .section not found.")

# ⑨ スマホ用スタイルを末尾に追記
if not honban_content.endswith("\n"):
    honban_content += "\n"
honban_content += responsive_styles
print("⑨ Appended RESPONSIVE STYLES to the end.")

# 4. 本番CSSを Shift-JIS (cp932) で書き戻す
with open(honban_css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(honban_content)

print("CSS Merged and Saved successfully.")
print("--- CSS Merge Script End ---")
