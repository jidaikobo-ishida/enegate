# -*- coding: utf-8 -*-
import os
import re

print("--- Wrap Ayumi Table Start ---")

filepath = "now/mater_history/ayumi.html"

if not os.path.exists(filepath):
    print(f"File not found: {filepath}")
    exit(1)

with open(filepath, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# table.graytb を探して scrolltable でラップする
# 二重に囲まないように制御
pattern = r'(?<!<div class="scrolltable">)(<table[^>]*class="[^"]*graytb[^"]*"[^>]*>.*?</table>)'

modified = False
def replacer(match):
    global modified
    modified = True
    return f'<div class="scrolltable">{match.group(1)}</div>'

new_content, count = re.subn(pattern, replacer, content_lf, flags=re.DOTALL | re.IGNORECASE)

if modified:
    with open(filepath, "w", encoding="cp932", errors="ignore") as f:
        f.write(new_content)
    print(f"Successfully wrapped table.graytb in {filepath}")
else:
    print(f"No unwrapped table.graytb found in {filepath}")

print("--- Wrap Ayumi Table End ---")
