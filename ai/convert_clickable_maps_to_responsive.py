# -*- coding: utf-8 -*-
import os
import re
import glob

print("--- Responsive Clickable Maps Converter Start ---")

map_files = glob.glob("company/list/map*.html")

# 画像の基準サイズ
IMAGE_WIDTH = 690.0
IMAGE_HEIGHT = 39.0

count_files = 0

for filepath in map_files:
    if filepath.endswith(".bak") or "_car" in filepath or "_walk" in filepath:
        continue
        
    with open(filepath, "r", encoding="cp932", errors="ignore") as f:
        content = f.read()
        
    content_lf = content.replace("\r\n", "\n")
    
    # 1. HTML内の <map name="Map"> ... </map> ブロックを抽出して area 要素を解析
    map_pattern = r'(<map[^>]*name="Map"[^>]*>.*?</map>)'
    map_match = re.search(map_pattern, content_lf, re.DOTALL | re.IGNORECASE)
    
    if not map_match:
        print(f"Skipping {filepath} (No map element found).")
        continue
        
    map_block = map_match.group(1)
    # area タグをすべて抽出
    areas = re.findall(r'<area([^>]*)/?>', map_block, re.IGNORECASE)
    
    if not areas:
        print(f"No area elements in {filepath}.")
        continue
        
    # すでに生成済みの map-link があれば一旦削除してクリーンにする
    content_lf = re.sub(r'<a[^>]*class="[^"]*map-link[^"]*"[^>]*>.*?</a>', "", content_lf)
    
    generated_links = []
    
    for area_attr in areas:
        coords_match = re.search(r'coords\s*=\s*["\']?([\d\s,]+)["\']?', area_attr, re.IGNORECASE)
        href_match = re.search(r'href\s*=\s*["\']?([^"\']+)["\']?', area_attr, re.IGNORECASE)
        alt_match = re.search(r'alt\s*=\s*["\']?([^"\']+)["\']?', area_attr, re.IGNORECASE)
        
        if coords_match and href_match:
            coords_str = coords_match.group(1).replace(" ", "")
            href = href_match.group(1)
            alt = alt_match.group(1) if alt_match else "リンク"
            
            coords = [float(x) for x in coords_str.split(",")]
            if len(coords) == 4:
                x1, y1, x2, y2 = coords
                
                left = (x1 / IMAGE_WIDTH) * 100.0
                width = ((x2 - x1) / IMAGE_WIDTH) * 100.0
                top = (y1 / IMAGE_HEIGHT) * 100.0
                height = ((y2 - y1) / IMAGE_HEIGHT) * 100.0
                
                link_tag = f'<a href="{href}" class="map-link" style="position: absolute; top: {top:.2f}%; left: {left:.2f}%; width: {width:.2f}%; height: {height:.2f}%; text-indent: -9999px; overflow: hidden;">{alt}</a>'
                generated_links.append(link_tag)
                
    if generated_links:
        h2_pattern = r'(<h2[^>]*class="[^"]*text[^"]*"[^>]*>.*?)(</h2>)'
        h2_match = re.search(h2_pattern, content_lf, re.DOTALL | re.IGNORECASE)
        if h2_match:
            h2_start_and_inner = h2_match.group(1)
            h2_end = h2_match.group(2)
            
            # class に relative を追加
            if 'relative' not in h2_start_and_inner:
                h2_start_and_inner = h2_start_and_inner.replace('class="text"', 'class="text relative"').replace("class='text'", "class='text relative'")
                
            links_html = "".join(generated_links)
            new_h2 = f"{h2_start_and_inner}{links_html}{h2_end}"
            
            content_lf = content_lf.replace(h2_match.group(0), new_h2)
            
            with open(filepath, "w", encoding="cp932", errors="ignore") as f:
                f.write(content_lf)
            print(f"Successfully processed {len(generated_links)} link(s) in: {os.path.basename(filepath)}")
            count_files += 1

# CSSの調整
css_path = "common/css/common.css"
with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    css_content = f.read()
    
css_lf = css_content.replace("\r\n", "\n")

old_mobile_style = """    /* スマホ時のみ見出し内の絶対配置リンクをアクティブ化し追従させる */
    .text.relative {
        position: relative !important;
    }
    .text.relative a.map-link {
        display: block !important;
        position: absolute !important;
        top: 17.9% !important;
        left: 77.5% !important;
        width: 22.2% !important;
        height: 66.7% !important;
        text-indent: -9999px !important;
        overflow: hidden !important;
        z-index: 10 !important;
    }"""

new_mobile_style = """    /* スマホ時のみ見出し内の絶対配置リンクをアクティブ化し追従させる */
    .text.relative {
        position: relative !important;
    }
    .text.relative a.map-link {
        display: block !important;
        position: absolute !important;
        text-indent: -9999px !important;
        overflow: hidden !important;
        z-index: 10 !important;
    }"""

if old_mobile_style.replace("\r\n", "\n") in css_lf:
    css_lf = css_lf.replace(old_mobile_style.replace("\r\n", "\n"), new_mobile_style.replace("\r\n", "\n"))
    with open(css_path, "w", encoding="cp932", errors="ignore") as f:
        f.write(css_lf)
    print("Successfully updated common.css with generic mobile map-link style.")

print(f"Completed! Responsive links added to {count_files} map files.")
print("--- Responsive Clickable Maps Converter End ---")
