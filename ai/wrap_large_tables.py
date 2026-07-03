# -*- coding: utf-8 -*-
import os
import re

print("--- Wrap Large Tables Start ---")

targets = [
    "products/info/info02.html",
    "products/denryoku/denryoku22.html",
    "products/denryoku/denryoku02.html",
    "products/denryoku/denryoku04.html",
    "products/denryoku/denryoku11.html",
    "products/denryoku/denryoku10.html"
]

for filepath in targets:
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, "r", encoding="cp932", errors="ignore") as f:
        content = f.read()
        
    content_lf = content.replace("\r\n", "\n")
    
    # <table class="itemspec"> を探す
    # 重複して囲まないように、前に <div class="scrolltable"> がない場合のみ置換
    table_pattern = r'(?<!<div class="scrolltable">)(<table[^>]*class="[^"]*itemspec[^"]*"[^>]*>.*?</table>)'
    
    # リストを使うことで nonlocal 回避
    state = {"modified": False}
    
    def replacer(match):
        state["modified"] = True
        return f'<div class="scrolltable">{match.group(1)}</div>'
        
    new_content, count = re.subn(table_pattern, replacer, content_lf, flags=re.DOTALL | re.IGNORECASE)
    
    if state["modified"]:
        with open(filepath, "w", encoding="cp932", errors="ignore") as f:
            f.write(new_content)
        print(f"Successfully wrapped {count} table(s) in {filepath}")
    else:
        print(f"No unwrapped table found in {filepath}")

print("--- Wrap Large Tables End ---")
