# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_lf = content.replace("\r\n", "\n")

# テスト環境から混入した3箇所の文字化け記号を、本番本来の正しい記号に置換修復する
# 1. 笆 -> ■
# 2. 竊 -> →
# 3. 笳 -> ●

corruptions = [
    ("content: '笆';", "content: '■';"),
    ('content: "竊";', 'content: "→";'),
    ("content: '笳';", "content: '●';"),
]

repaired_count = 0

for target, replacement in corruptions:
    if target in content_lf:
        content_lf = content_lf.replace(target, replacement)
        print(f"Repaired: `{target}` -> `{replacement}`")
        repaired_count += 1
    else:
        # 部分一致やスペースの揺れを考慮
        target_clean = target.replace(" ", "")
        # 正規表現での置換
        import re
        pattern = re.escape(target).replace(r"\ ", r"\s*")
        content_lf, count = re.subn(pattern, replacement, content_lf)
        if count > 0:
            print(f"Repaired via regex: `{target}` -> `{replacement}` ({count} occurrence(s))")
            repaired_count += 1
        else:
            print(f"Warning: Target corruption `{target}` not found in CSS.")

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_lf)

print(f"--- CSS Encoding Corruption Fix Completed. Repaired {repaired_count} block(s). ---")
