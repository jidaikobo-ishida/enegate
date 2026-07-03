# -*- coding: utf-8 -*-

filepath = "company/list/list.html"

with open(filepath, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# LFに統一
content_lf = content.replace("\r\n", "\n")

# scrolltable の囲みを取り除く
target = '<div class="scrolltable"><table class="type02">'
replacement = '<table class="type02">'

if target in content_lf:
    content_lf = content_lf.replace(target, replacement)
    
    # 閉じタグ </table></div> を </table> に戻す
    # 最初の </table></div> のみを置換するため、注意して置換
    # (今回テーブルは1つしかないので直接置換でも安全)
    content_lf = content_lf.replace('</table></div>', '</table>')
    
    with open(filepath, "w", encoding="cp932", errors="ignore") as f:
        f.write(content_lf)
    print("Successfully removed scrolltable wrapper from list.html.")
else:
    print("scrolltable wrapper not found in list.html.")
