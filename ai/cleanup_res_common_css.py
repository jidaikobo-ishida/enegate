# -*- coding: utf-8 -*-

css_path = "common/css/res_common.css"
with open(css_path, "r", encoding="cp932", errors="ignore") as f:
    content = f.read()

content_crlf = content.replace("\r\n", "\n").replace("\n", "\r\n")

target_imgnav = """/*Imgnav*/
#Imgnav { height:175px; background:#538FD4; position:relative; overflow:hidden;}
#Imgnav .Imgnavwrap { width:950px; margin:0 auto; background:#FFF url(../img/pnav_back.png) repeat-y top right; overflow:hidden;}
#Imgnav A { 
	display: inline-block;
	width : 16.66666% ;
	width : -webkit-calc(100% / 6) ;
	width : calc(100% / 6) ;
	height:175px; 
	padding:0;
	color:#fff;
	text-align:center;
	z-index: 100;
}
#Imgnav A:last-child{margin-right: 0;}
#Imgnav img { margin:40px 0 6px;}
#Imgnav span { display:block;}
#Imgnav .imgnav01 { background:#538FD4;}
#Imgnav .imgnav02 { background:#6D6B92;}
#Imgnav .imgnav03 { background:#F08263;}
#Imgnav .imgnav04 { background:#E3C05D;}
#Imgnav .imgnav05 { background:#EB8CB7;}
#Imgnav .imgnav06 { background:#74C1A4;}
#Imgnav:before {
    width: 50%;
    height: 100%;
    content: "";
    position: absolute;
    top: 0;
    left: 50%;
    background: #74C1A4;
	z-index:0;
}
#Imgnav .wrap {
    position: absolute;
    left: 50%;
    margin-left: -475px;
}"""

target_imgnav_crlf = target_imgnav.replace("\r\n", "\n").replace("\n", "\r\n")

if target_imgnav_crlf in content_crlf:
    content_crlf = content_crlf.replace(target_imgnav_crlf, "")
    print("Successfully deleted #Imgnav styles from res_common.css.")
else:
    print("Error: #Imgnav target not found in res_common.css.")

with open(css_path, "w", encoding="cp932", errors="ignore") as f:
    f.write(content_crlf)
