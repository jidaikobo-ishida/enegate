# -*- coding: utf-8 -*-

filepath = "company/list/index.html"

with open(filepath, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 1. 地図画像を本番最新（20260616）にする
content = content.replace("img_map20251210.jpg", "img_map20260616.jpg")

# 2. 部署名を本番最新（品質保証・環境）にする
content = content.replace('kanri.html#hinsitu">品質保証', 'kanri.html#hinsitu">品質保証・環境')

with open(filepath, "w", encoding="cp932", errors="ignore") as f:
    f.write(content)

print("Successfully merged honban data into restored index.html")
