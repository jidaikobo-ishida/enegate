# -*- coding: utf-8 -*-
import re

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# 1. 64行目の古いIEハック /*\*//*/ を削除してコメントレベルのズレの根源を解消
if "/*\*//*/" in content_lf:
    content_lf = content_lf.replace("/*\*//*/", "")
    print("Cleaned up old IE comment hack /*\\*//*/.")

# 2. コメントアウトされた950pxメディアクエリブロックを物理的に一時削除する
# (コメントアウトの中に /* が大量に残って閉じられていなかったため、ブラウザがそれ以降の全スマホCSSを無視していました)
start_marker = "/* COMMENTED OUT TEMPORARILY BY USER REQUEST"
end_marker = "END COMMENTED OUT */"

idx_start = content_lf.find(start_marker)
idx_end = content_lf.find(end_marker)

if idx_start != -1 and idx_end != -1:
    end_pos = idx_end + len(end_marker)
    del_block = content_lf[idx_start:end_pos]
    content_lf = content_lf.replace(del_block, "")
    print("Successfully deleted the disabled 950px media queries physically (to prevent browser parsing errors).")
else:
    # 簡易置換フォールバック
    pattern = r'/\* COMMENTED OUT TEMPORARILY BY USER REQUEST.*?END COMMENTED OUT \*/'
    content_lf, count = re.subn(pattern, "", content_lf, flags=re.DOTALL)
    if count > 0:
        print(f"Successfully deleted {count} commented block(s) via regex.")
    else:
        print("Disabled 950px media block not found for physical deletion.")

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print("--- CSS Comment Cleanup Completed ---")
