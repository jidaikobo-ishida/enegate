# -*- coding: utf-8 -*-
import re

print("--- Comment Out #list CSS Rules Start ---")

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 1. 1552〜1559行目付近のPC用 #list 定義をコメントアウト
pc_list_pattern = r'(#list\s+#article\s*\{[^}]*?\}.*?#list\s+#breadcrumbs\s*\{[^}]*?\})'
match1 = re.search(pc_list_pattern, content_lf, re.DOTALL)
if match1:
    block1 = match1.group(1)
    commented_block1 = "/*\n" + block1 + "\n*/"
    content_lf = content_lf.replace(block1, commented_block1)
    print("Commented out PC #list block (1552-1559).")
else:
    # 直接文字列置換フォールバック
    target1 = """#list #article { width:950px; clear:both; }
#list #mainContent {float:right; width:690px; margin:8px 25px 50px 25px !important; font-size:1.1em;}
#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em; float: left; width: 180px;}
#list #breadcrumbs { padding-bottom:20px;font-size:0.78em;}"""
    if target1 in content_lf:
        content_lf = content_lf.replace(target1, f"/*\n{target1}\n*/")
        print("Commented out PC #list block (direct string).")

# 2. 2555〜2590行目付近の body#list 共通新デザインをコメントアウト
design_pattern = r'(body#list\s+\.twocontent\s+\.group\s+\.boxType02.*?body#list\s+\.twocontent\s+\.boxBtm\s*\{[^}]*?display:\s*none\s*!important;\s*\})'
match2 = re.search(design_pattern, content_lf, re.DOTALL)
if match2:
    block2 = match2.group(1)
    commented_block2 = "/*\n" + block2 + "\n*/"
    content_lf = content_lf.replace(block2, commented_block2)
    print("Commented out body#list design block (2555-2590).")

# 3. 2592〜2612行目付近の body#list > table tr / td ブロック化をコメントアウト
trtd_pattern = r'(@media\s+screen\s+and\s*\(max-width:\s*736px\)\s*\{\s*body#list\s+\.twocontent\s+\.group\s+\.boxType02\s+>\s+table\s+tr.*?width:\s*100%\s*!important;\s*\}\s*\})'
# (直系子要素に書き換えた定義に柔軟にマッチ)
match3 = re.search(r'(body#list\s+\.twocontent\s+\.group\s+\.boxType02\s+>\s+table\s+tr.*?width:\s*100%\s*!important;\s*\})', content_lf, re.DOTALL)
if match3:
    block3 = match3.group(1)
    commented_block3 = "/*\n" + block3 + "\n*/"
    content_lf = content_lf.replace(block3, commented_block3)
    print("Commented out body#list child table tr/td block (2592-2612).")

# 4. 3095〜3146行目付近のスマホ用 #list コア調整をコメントアウト
# (先ほど追加した font-size: 1em; などを含む定義にマッチ)
mobile_pattern = r'(#list\s+\.leftsubnav\s*\{.*?#list\s+\.twocontent\s+\.boxTop.*?display:\s*none\s*!important;\s*\})'
match4 = re.search(mobile_pattern, content_lf, re.DOTALL)
if match4:
    block4 = match4.group(1)
    commented_block4 = "/*\n" + block4 + "\n*/"
    content_lf = content_lf.replace(block4, commented_block4)
    print("Commented out mobile #list block (3095-3146).")

# 5. 3225〜3248行目（width解除部分）の #list #article, をコメントアウト（削除）
content_lf = content_lf.replace(
    "#list #article,\n",
    "/* #list #article, */\n"
)
content_lf = content_lf.replace(
    "#list #article,",
    "/* #list #article, */"
)

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("Successfully commented out #list rules in common.css.")
print("--- Comment Out #list CSS Rules End ---")
