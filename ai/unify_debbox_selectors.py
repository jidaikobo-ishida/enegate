# -*- coding: utf-8 -*-

css_path = "common/css/common.css"

with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

# 全て CRLF 改行のまま処理するために LF を一時的に CRLF に正規化
content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

# 1. PC用の重複する #jigyousyo .debbox 定義ブロック全体(1704〜1755行目付近)を完全に削除する
# (すでに .debbox で一括定義するため、この重複部分は物理的に消去します)
target_jigyousyo_block = """#jigyousyo .debbox { padding:20px 0; margin:0 25px 25px 0; width:230px; float:left; text-align:center; background:#E7EFFB; border:1px solid #DBE4F5; box-sizing: border-box;}
#jigyousyo .debbox:nth-child(3n+5) { margin-right:0;}
#jigyousyo .debbox h3 { padding:15px 0 10px; font-weight:bold;}
#jigyousyo .debbox A.morelink{
	position: relative;
	display: inline-block;
	padding:6px 12px 6px 25px;
	font-size:1.3em;
	color:#2A7CC8;
	background:#FFF;
}

#jigyousyo .debbox A.morelink::before{
  content: '';
  width: 6px;
  height: 6px;
  border: 0px;
  border-top: solid 2px #2A7CC8;
  border-right: solid 2px #2A7CC8;
  -ms-transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  position: absolute;
  top: 50%;
  left: 10px;
  margin-top: -3px;
}
#jigyousyo .debbox A.morelink:hover { color:#FFF; background:#2A7CC8;} 
#jigyousyo .debbox A.morelink:hover::before{
	border-top: solid 2px #FFF;
	border-right: solid 2px #FFF;
}
#jigyousyo .debbox A.nolink{
	position: relative;
	display: inline-block;
	padding:6px 12px 6px 25px;
	font-size:1.3em;
	color:#A3B4CC;
	background:#FFF;
}
#jigyousyo .debbox A.nolink::before{
  content: '';
  width: 6px;
  height: 6px;
  border: 0px;
  border-top: solid 2px #A3B4CC;
  border-right: solid 2px #A3B4CC;
  -ms-transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  position: absolute;
  top: 50%;
  left: 10px;
  margin-top: -3px;
}"""

# 厳格に CRLF でマーカーを構築して削除
target_jigyousyo_crlf = target_jigyousyo_block.replace("\r\n", "\n").replace("\n", "\r\n")

if target_jigyousyo_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_jigyousyo_crlf, "")
    print("Successfully deleted duplicate #jigyousyo .debbox block.")
else:
    print("Warning: Duplicate #jigyousyo .debbox block not found. Checking exact spaces...")

# 2. #division .devbox.debbox を親IDなしの .debbox に一括置換する
# (PC版およびスマホ版両方に適用されます)
content_crlf = content_crlf.replace("#division .devbox.debbox", ".debbox")

# 念のため、置換結果を保存
with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_crlf)

print("Unified .debbox selectors and cleaned up stylesheet.")
