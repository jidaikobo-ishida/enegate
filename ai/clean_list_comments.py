# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# 余分なネストコメントをきれいな1組のコメントに置換
target = """/*旧調整用*/
/*
#list #article { width:950px; clear:both; }

#list #mainContent {float:right; width:690px; margin:8px 25px 50px 25px !important; font-size:1.1em;}



/*
#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em; float: left; width: 180px;}
#list #breadcrumbs { padding-bottom:20px;font-size:0.78em;}
*/
/**/"""

replacement = """/*旧調整用*/
/*
#list #article { width:950px; clear:both; }
#list #mainContent {float:right; width:690px; margin:8px 25px 50px 25px !important; font-size:1.1em;}
#list .leftsubnav {margin:10px 0 50px 0; font-size:0.78em; float: left; width: 180px;}
#list #breadcrumbs { padding-bottom:20px;font-size:0.78em;}
*/"""

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully cleaned up PC #list comments.")
else:
    # 柔軟な正規表現置換
    import re
    pattern = r'/\*旧調整用\*/\s*/\*\s*#list\s+#article.*?\*/\s*/\*\*/'
    # パターンでの置換
    content_lf = re.sub(
        r'/\*旧調整用\*/\s*/\*\s*#list\s+#article.*?#list\s+#breadcrumbs\s*\{[^}]*?\}\s*\*/\s*/\*\*/',
        replacement,
        content_lf,
        flags=re.DOTALL
    )
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully cleaned up PC #list comments (regex).")
