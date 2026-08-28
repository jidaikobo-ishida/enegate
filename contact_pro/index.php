<?php

/**
 * PHP5
 * 問い合わせフォーム-ファイル処理 [index.php]
 */

if ($_POST["sendok"] == null || $_POST["sendok"] =="") {
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NZ276ZFV');</script>
<!-- End Google Tag Manager -->
<meta charset="Shift_JIS">
<meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
	<script>
		(function () {
			var meta = document.getElementById('viewport');
			function switchViewport() {
				var isTouch = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);
				var currentWidth;
				if (isTouch && screen && screen.width) {
					var isLandscape = window.innerWidth > window.innerHeight;
					currentWidth = isLandscape ? Math.max(screen.width, screen.height) : Math.min(screen.width, screen.height);
				} else {
					currentWidth = window.innerWidth;
				}
				var target = (currentWidth > 736) ? 'width=970' : 'width=device-width, initial-scale=1.0';
				if (meta.getAttribute('content') !== target) {
					meta.setAttribute('content', target);
				}
			}
			switchViewport();
			window.addEventListener('resize', switchViewport, false);
			window.addEventListener('orientationchange', function () {
				setTimeout(switchViewport, 100);
			}, false);
		})();
	</script>
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
<title>製品についてのお問い合わせ｜株式会社エネゲート</title>
<meta name="description" content="エネゲートへの製品のお問い合わせ、ご意見、ご要望はこちらから。" />
<meta name="keywords" content="エネゲート,製品のお問い合わせ" />
<link rel="stylesheet" href="/common/css/reset.css" media="all">
<link rel="stylesheet" href="/common/css/common.css" media="all">
<link rel="stylesheet" href="/cmn/css/print.css" media="print">
<!--
<script type="text/javascript" src="./js/check.js"></script>
-->
<script type="text/javascript">
<!--

//submitの2度押し防止
function disableButton(){
  //document.form1.button1.disabled = true;　
  submit(document.form1);
}
function submit(formName){
	var retval;
	retval=check(formName);
	    
	if(retval){
		    formName.sendok.value='ok';
			formName.submit();
	 }else{
		 //alert("sendErr");
		    //document.forms[formName].sendok.value="";
			formName.sendok.value="";
	 }
}
function check(formName){
	
	var flag = 0;
	// 設定開始（必須にする項目を設定してください）
	if(formName.email.value == ""){ // 「メールチェック」の入力をチェック
		flag = 1;
	}
	if(formName.telNo.value == ""){ // 「電話番号」の入力をチェック
		flag = 1;
	}
	// 設定終了
	if(flag){
		window.alert('必須項目に未入力がありました'); // 入力漏れがあれば警告ダイアログを表示
		return false; // 送信を中止
	}else{
		return true; // 送信を実行
	}
}
//メールチェック
function chkRegEmail(str)
{
        /* E-mail形式の正規表現パターン */
        /* @が含まれていて、最後が .(ドット)でないなら正しいとする */
          var Seiki=/[!#-9A-~]+@+[a-z0-9]+.+[^.]$/i;
        /* 入力された値がパターンにマッチするか調べる */
        if(str!="")
        {
            if(str.match(Seiki))
            {
                //alert(str.match(Seiki)+"\n\nメールアドレスの形式は正しいです");
                return true;
            }else{
                alert("メールアドレスの形式が不正です","エラーメッセージ");
                return false;
            }
        }else{
            /* 何も入力されていない場合はアラート表示 */
            alert("メールアドレスを入力してください","エラーメッセージ");
            return false;
        }
}
// -->
</script>
</head>
<body id="form">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NZ276ZFV"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
<?php
include($_SERVER['DOCUMENT_ROOT'] . '/common/block/header.html');
?>

<div id="breadcrumbs" class="inner">
	<ol class="breadcrumbslist"><li><a href="/">HOME</a></li><li>製品についてのお問い合わせ</li></ol>
</div>

<div class="inner clearfix">
<div class="section">

		<h1 class="grytitle">製品についてのお問い合わせ</h1>
		<p class="text">当ウェブサイトのお問い合わせフォームには、プライバシー保護のため、SSL暗号化通信を採用（導入）しています。</p>

		<!-- 入力フォーム -->
		<form action="index.php" method="post" id="form1" name="form1" onSubmit="this.button1.disabled = true;">

		<table class="graytb" width="100%">
		<tr>
		<th>製品名</th>
		<td>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="generalcubicle") { ?>
			<input name="productName" value="一般用キュービクル（特別高圧・高圧）" type="text" size=100 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="electriccubicle") { ?>
			<input name="productName" value="電力用キュービクル（22ｋＶ、6.6ｋＶ）" type="text" size=100 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="digitalkadenryuhogo") { ?>
			<input name="productName" value="ディジタル過電流保護リレー" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="digital_houkoukyorihogo") { ?>
			<input name="productName" value="ディジタル形方向距離保護リレー" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="omegac_chirakukadenatu") { ?>
			<input name="productName" value="ωC測定付地絡過電圧リレー" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
					<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="blackstart") { ?>
			<input name="productName" value="ブラックスタート用系統保護リレー" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="vctautomatich") { ?>
			<input name="productName" value="VCT・低圧CT自動試験装置" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="sansoukouryusiken") { ?>
			<input name="productName" value="三相交流試験台" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="digital_henatukihogo") { ?>
			<input name="productName" value="6.6・22kVディジタル形変圧器保護リレー" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="interfaceunit") { ?>
			<input name="productName" value="インターフェイスユニット" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="tirakukensituhyouji") { ?>
			<input name="productName" value="地絡検出表示装置" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
        <!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="haiji") { ?>
			<input name="productName" value="配電線自動運用変電所子局" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="svare") { ?>
			<input name="productName" value="SVaRe（スバレ）" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="info-svare">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="aisolusion") { ?>
			<input name="productName" value="AIソリューション" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="mmcub") { ?>
			<input name="productName" value="MMCub" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
			
        
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="6kvmoldkeikihenatu") { ?>
		<input name="productName2" value="6ｋＶモールド計器用変圧変流器" type="text" size=50 maxlength="100" class="text w202" />
		<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="33kmoldct") { ?>
			<input name="productName" value="22ｋＶ・33ｋＶモールド計器用変圧変流器" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="6kmoldhenryuki") { ?>
			<input name="productName" value="6ｋＶモールド変流器" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="6kmoldsetikei") { ?>
			<input name="productName" value="6ｋＶモールド接地型計器用変圧器" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="22kunyusetigatakeiki") { ?>
			<input name="productName" value="22ｋＶ油入接地型計器用変圧器" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="hikikomikaiheiki") { ?>
			<input name="productName" value="引込開閉器制御電源用変圧器" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="tijyousetigatahenatu") { ?>
			<input name="productName" value="地上設置型変圧器" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="teiatumoldhenatu") { ?>
			<input name="productName" value="低圧モールド変圧器" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="usuteiatuhenatu") { ?>
			<input name="productName" value="薄型低圧変圧器" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="usuhenatukinaizou") { ?>
			<input name="productName" value="薄型変圧器内蔵分電盤" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--　トランス事業部　-->
		<?php if ($_GET["value"]=="shisoukondensa") { ?>
			<input name="productName" value="進相コンデンサー用モールド放電コイル" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_transu">
		<?php } ?>
		<!--	計測関連製品　　　-->
		<!--　計測システム事業部　-->
		<?php if ($_GET["value"]=="kikaisikidenryokukei") { ?>
			<input name="productName" value="機械式電力量計" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keisoku">
		<?php } ?>
		<!--　計測システム事業部　-->
		<?php if ($_GET["value"]=="densisikidenryokukei_kou") { ?>
			<input name="productName" value="電子式電力量計（高圧用）" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keisoku">
		<?php } ?>
		<!--　計測システム事業部　-->
		<?php if ($_GET["value"]=="densisikidenryokukei_tei") { ?>
			<input name="productName" value="電子式電力量計（低圧用）" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keisoku">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="elmeter_b") { ?>
			<input name="productName" value="EL計器(B)（電子式電力量計）" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="elmeter_s") { ?>
			<input name="productName" value="EL計器(S)（電子式電力量計）" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
					<!--　営業開発部　-->
		<?php if ($_GET["value"]=="chokuryumeter") { ?>
			<input name="productName" value="直流電力量計" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　計測システム事業部　-->
		<?php if ($_GET["value"]=="unitpowermeter") { ?>
			<input name="productName" value="ユニット式電力量計" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keisoku">
		<?php } ?>

		<!--	計測関連製品　　　-->
		<!--　計測システム事業部　-->
		<?php if ($_GET["value"]=="haidenkaiheiki") { ?>
			<input name="productName" value="配電自動化開閉器子局" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keisoku">
		<?php } ?>
		<?php if ($_GET["value"]=="hikariyunit") { ?>
			<input name="productName" value="光ユニット子局" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keisoku">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="nssencer") { ?>
			<input name="productName" value="NSセンサー" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		
		<!--　省エネ関連製品　-->
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="hv_gateway") { ?>
			<input name="productName" value="高圧ゲートウェイ" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="elmeter_sencor") { ?>
			<input name="productName" value="ELセンサー" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="ecowatt") { ?>
			<input name="productName" value="エコワット" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="ecowattace") { ?>
			<input name="productName" value="エコワットエース" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="econaviwireless") { ?>
			<input name="productName" value="省エネナビ（無線型）" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="econavi") { ?>
			<input name="productName" value="省エネナビ（有線型）" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="peakseber") { ?>
			<input name="productName" value="ピークセーバー(空調省エネシステム)" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="superdemapiko") { ?>
			<input name="productName" value="スーパーでまぴこ（デマンドコントローラ）" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="totalwatersystem") { ?>
			<input name="productName" value="トータル節水システム" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="ecogesui") { ?>
			<input name="productName" value="下水道料金削減のご提案" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="demandsign") { ?>
			<input name="productName" value="デマンド契約について" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--	エンジニアリング関連製品　　　-->
		<!--　制御機器事業部　-->	
		<?php if ($_GET["value"]=="itvsystem") { ?>
			<input name="productName" value="ITVシステム" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="turbineshaft") { ?>
			<input name="productName" value="タービン軸振動監視装置" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="vibrographwatching") { ?>
			<input name="productName" value="補機振動監視装置" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="waterdisposecontrol") { ?>
			<input name="productName" value="水処理装置制御盤" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="samplinglac") { ?>
			<input name="productName" value="サンプリングラック" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="boilercontrol") { ?>
			<input name="productName" value="所内ボイラ制御盤" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="bousaiwatcher") { ?>
			<input name="productName" value="防災監視盤" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="cleanwaterwatching") { ?>
			<input name="productName" value="浄水場テレメータ・監視システム" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="damwatching") { ?>
			<input name="productName" value="ダム監視操作卓" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--	情報通信関連製品　　　-->
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="acpower") { ?>
			<input name="productName" value="直流電源装置" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="powersupply") { ?>
			<input name="productName" value="電源供給器" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="uninterruptible_power") { ?>
			<input name="productName" value="無停電電源装置" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!-- 現在掲載しておりません -->
		<?php if ($_GET["value"]=="hikarifiberkakusen") { ?>
			<input name="productName" value="光ファイバー架空地線接続箱" type="text" size=50 maxlength="100" class="text w202" />
		<?php } ?>
		<!--　計測システム事業部　-->
		<?php if ($_GET["value"]=="phsgwbox") { ?>
			<input name="productName" value="PHS－GW収容箱" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keisoku">
		<?php } ?>
		<!--	ITソリューション関連製品　　　-->
		<!--　ソリューション　-->
		<?php if ($_GET["value"]=="ontrogytechnology") { ?>
			<input name="productName" value="オントロジー利用技術" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_kenkai">
		<?php } ?>
		<!--　ソリューション　-->
		<?php if ($_GET["value"]=="3dvideo") { ?>
			<input name="productName" value="３Ｄビデオ技術" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_kenkai">
		<?php } ?>
		<!--　　ソリューション-->
		<?php if ($_GET["value"]=="streo_camera") { ?>
			<input name="productName" value="ステレオカメラ" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_kenkai">
		<?php } ?>
		<!--　ソリューション　-->
		<?php if ($_GET["value"]=="eco_qden") { ?>
			<input name="productName" value="エコQ電システム" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_kenkai">
		<?php } ?>
		<?php if ($_GET["value"]=="eco_qden_pl") { ?>
			<input name="productName" value="エコQ電システム" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<?php if ($_GET["value"]=="smartecowatt") { ?>
			<input name="productName" value="スマートエコワット" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		
		<?php if ($_GET["value"]=="smart_elsencor") { ?>
			<input name="productName" value="スマートELセンサ" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
        
        <?php if ($_GET["value"]=="smartgateway") { ?>
			<input name="productName" value="スマートゲートウェイ" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
<?php } ?>
        
        <?php if ($_GET["value"]=="smartseries") { ?>
			<input name="productName" value="スマートシリーズ全般" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
 <?php if ($_GET["value"]=="purchasestudy") { ?>
			<input name="productName" value="スマートシリーズご購入導入検討" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
        <?php if ($_GET["value"]=="smartpulsecounter") { ?>
			<input name="productName" value="スマートパルスカウンター" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
        <?php if ($_GET["value"]=="smartecowatt_for_eo") { ?>
			<input name="productName" value="Smart Ecowatt for eoについて" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>

	
		
		<!--	各種販売製品　　　-->
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="flextender") { ?>
			<input name="productName" value="フレックステンダー" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="oval") { ?>
			<input name="productName" value="オーバルクランプオン形超音波流量計 UC-1" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="chemical") { ?>
			<input name="productName" value="接地抵抗低減剤（導電性コンクリート）" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="airconditioning") { ?>
			<input name="productName" value="空調設備保守点検施工" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="nitrogenextinguish") { ?>
			<input name="productName" value="窒素消火設備点検施工" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		<!--	工事メンテナンス関連　　　-->
		<!--　計器サービス事業部　-->
		<?php if ($_GET["value"]=="powermetermainte") { ?>
			<input name="productName" value="電力量計の修理" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keiki">
		<?php } ?>
		<!--　計器サービス事業部　-->
		<?php if ($_GET["value"]=="inst_trans_metermainte") { ?>
			<input name="productName" value="計器用変成器の修理" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keiki">
		<?php } ?>
		<!--　計器サービス事業部　-->
		<?php if ($_GET["value"]=="powermeter_kentei") { ?>
			<input name="productName" value="電力量計・計器用変成器の検定代弁" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keiki">
		<?php } ?>
		<!--　計器サービス事業部　-->
		<?php if ($_GET["value"]=="powermeter_change") { ?>
			<input name="productName" value="電力量計の取替工事" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keiki">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="submeter_change") { ?>
			<input name="productName" value="子メータの取替工事" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　計器サービス事業部　-->
		<?php if ($_GET["value"]=="fikaricircuitwork") { ?>
			<input name="productName" value="光回線(FTTO・FTTA)工事" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keiki">
		<?php } ?>
        
        <!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="hikaricable") { ?>
			<input name="productName" value="光ケーブル" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
        
		<!--　計器サービス事業部　-->
		<?php if ($_GET["value"]=="supply_inspect") { ?>
			<input name="productName" value="配電塔点検" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keiki">
		<?php } ?>
		<!--　計器サービス事業部　-->
		<?php if ($_GET["value"]=="measurement_test") { ?>
			<input name="productName" value="計測器の校正試験" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keiki">
		<?php } ?>
		<!--　計器サービス事業部　-->
		<?php if ($_GET["value"]=="eco_instrumentwork") { ?>
			<input name="productName" value="省エネ機器取付工事" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="gauge_devicetest") { ?>
			<input name="productName" value="一般電気設備点検" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		<!--　営業開発部　-->
		<?php if ($_GET["value"]=="receivetransmitted") { ?>
			<input name="productName" value="屋内変圧器室点検" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_keiki">
		<?php } ?>
		
		<!--　制御機器事業部　-->
		<?php if ($_GET["value"]=="info07") { ?>
			<input name="productName" value="光配線盤" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_seigyo">
		<?php } ?>
		
		<!--電力関連製品-->
		<?php if ($_GET["value"]=="denryokukanren") { ?>
			<input name="productName" value="電力関連製品" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>
		<!--計測製品-->
		<?php if ($_GET["value"]=="keisokukanren") { ?>
			<input name="productName" value="計測製品" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--省エネ関連製品-->
		<?php if ($_GET["value"]=="syoenekanren") { ?>
			<input name="productName" value="省エネ関連製品" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--エンジニアリング関連製品-->
		<?php if ($_GET["value"]=="engkanren") { ?>
			<input name="productName" value="エンジニアリング関連製品" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--情報通信関連-->
		<?php if ($_GET["value"]=="infocomkanren") { ?>
			<input name="productName" value="情報通信関連" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--ITソリューション関連製品-->
		<?php if ($_GET["value"]=="ITkanren") { ?>
			<input name="productName" value="ITソリューション関連製品" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--各種販売等-->
		<?php if ($_GET["value"]=="otherkanren") { ?>
			<input name="productName" value="各種販売等" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--工事メンテナンス関連-->
		<?php if ($_GET["value"]=="koujikanren") { ?>
			<input name="productName" value="工事メンテナンス関連" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--電力の計量・計測・監視・制御-->
		<?php if ($_GET["value"]=="keiryokeisokuseigyo") { ?>
			<input name="productName" value="電力の計量・計測・監視・制御" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--電力変換-->
		<?php if ($_GET["value"]=="denryokuhenkan") { ?>
			<input name="productName" value="電力変換" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--省エネCO2削減-->
		<?php if ($_GET["value"]=="syoeneco2") { ?>
			<input name="productName" value="省エネCO2削減" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>
		
		<!--製品メンテナンス-->
		<?php if ($_GET["value"]=="seihinmente") { ?>
			<input name="productName" value="製品メンテナンス" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--情報通信-->
		<?php if ($_GET["value"]=="infocom") { ?>
			<input name="productName" value="情報通信" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--研究開発・技術情報-->
		<?php if ($_GET["value"]=="kenkyukaihatu") { ?>
			<input name="productName" value="研究開発・技術情報" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		<!--　営業開発部(日置電機)　-->
		<?php if ($_GET["value"]=="hioki01") { ?>
			<input name="productName" value="メモリハイコーダ 8847" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>

		<!--　営業開発部(日置電機)　-->
		<?php if ($_GET["value"]=="hioki02") { ?>
			<input name="productName" value="電源品質アナライザ 3196" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>
		
		<!--　営業開発部(日置電機)　-->
		<?php if ($_GET["value"]=="hioki03") { ?>
			<input name="productName" value="電源ラインモニタ 3351" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_eigyou">
		<?php } ?>

		<!--　営業開発部(日置電機関連)　-->
		<?php if ($_GET["value"]=="hioki00") { ?>
			<input name="productName" value="日置電機関連製品" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>		

		<!--　　-->
		<?php if ($_GET["value"]=="") { ?>
			<input name="productName" value="該当なし" type="text" size=50 maxlength="100" class="text w202" />
			<input type="hidden" name="mail_to" value="hp_mail_soumu">
		<?php } ?>

		</td></tr>

				<tr>
		<th>お名前</th>
		<td>
		<input name="name"  type="text" size=35 maxlength="100" class="text w202" />
		</td></tr>

<?php if ($_GET["value"]!="smartecowatt_for_eo") { ?>
		<tr>
		<th>会社・団体名</th>
		<td><input name="kaisya"  type="text" size="35" maxlength="100" class="text w202" /></td></tr>

		<tr>
		  <th>所属部署名</th>
		  <td>
		    <input name="syozoku" type="text" size=35 maxlength="100" class="text w202"/></td></tr>
		<tr>
<?php } ?>
		  <th>ご住所</th>
		  <td>
		    
		    <select name="pref" class="w109">
		      <option selected value="">都道府県</option>
		      <option value="北海道">北海道 </option>
		      <option value="青森県">青森県 </option>
		      <option value="岩手県">岩手県 </option>
		      <option value="秋田県">秋田県 </option>
		      <option value="宮城県">宮城県 </option>
		      <option value="山形県">山形県 </option>
		      <option value="福島県">福島県 </option>
		      <option value="茨城県">茨城県 </option>
		      <option value="栃木県">栃木県 </option>
		      <option value="群馬県">群馬県 </option>
		      <option value="埼玉県">埼玉県 </option>
		      <option value="千葉県">千葉県 </option>
		      <option value="東京都">東京都 </option>
		      <option value="神奈川県">神奈川県 </option>
		      <option value="新潟県">新潟県 </option>
		      <option value="山梨県">山梨県 </option>
		      <option value="長野県">長野県 </option>
		      <option value="静岡県">静岡県 </option>
		      <option value="愛知県">愛知県 </option>
		      <option value="岐阜県">岐阜県 </option>
		      <option value="富山県">富山県 </option>
		      <option value="石川県">石川県 </option>
		      <option value="福井県">福井県 </option>
		      <option value="三重県">三重県 </option>
		      <option value="滋賀県">滋賀県 </option>
		      <option value="京都府">京都府 </option>
		      <option value="奈良県">奈良県 </option>
		      <option value="大阪府">大阪府 </option>
		      <option value="和歌山県">和歌山県 </option>
		      <option value="兵庫県">兵庫県 </option>
		      <option value="鳥取県">鳥取県 </option>
		      <option value="岡山県">岡山県 </option>
		      <option value="島根県">島根県 </option>
		      <option value="広島県">広島県 </option>
		      <option value="山口県">山口県 </option>
		      <option value="香川県">香川県 </option>
		      <option value="徳島県">徳島県 </option>
		      <option value="愛媛県">愛媛県 </option>
		      <option value="高知県">高知県 </option>
		      <option value="福岡県">福岡県 </option>
		      <option value="佐賀県">佐賀県 </option>
		      <option value="長崎県">長崎県 </option>
		      <option value="大分県">大分県 </option>
		      <option value="熊本県">熊本県 </option>
		      <option value="宮崎県">宮崎県 </option>
		      <option value="鹿児島県">鹿児島県 </option>
		      <option value="沖縄県">沖縄県 </option>
		      <option value="韓国">韓国</option>
		      <option value="海外その他">海外その他</option>
		      </select>　
		    
		    <input name="city" type="text"  size="10" maxlength="50" class="text w109" />
		    <span id="fcol1">市（郡）</span>
		    <input name="town" type="text"  size="10" maxlength="50" class="text w109" />
		    <span id="fcol2">区（町）</span>
		   
            </td></tr>

		<tr>
		<th>電話番号</th>
		<td><input name="telNo"  type="text" size="35" maxlength="100" class="text w202" />
        <span class="px12_red">※必須項目</span></td></tr>

		<tr>
		<th>メールアドレス</th>
		<td><input name="email" type="text"  size="35" class="text w202" />
		  <span class="px12_red">※必須項目</span></td></tr>
		
        <tr>
            <th>お問合せ種類</th>
            <td>
                <span class="px12_red">※必須項目</span><br />
                <?php if ($_GET["value"]!="smartecowatt_for_eo") { ?>
                <input type="radio" name="detail" value="お見積り依頼"  checked />
                お見積り依頼<br />
                <?php } ?>
                <input type="radio" name="detail" value="資料請求"  />
                資料請求<br />
                <input type="radio" name="detail" value="その他"  />
                その他
            </td>
        </tr>
		<tr>
		<th>お問合せ内容</th>
		<td>
		<textarea name="message" cols="50" rows="6"  class="w398" /></textarea>
		</td></tr>
		</table>

        <!--
		<input name="sendok" type="hidden" />
		-->
        <input name="sendok" type="hidden" />
        <div id="FormButtons"> 
        <!--
          <input name="submit" type="image" src="./img/btn_send.gif" value="送信する" onclick="javascript:Submit('form1');"/>
          <input name="button1" type="image" src="./img/btn_send.gif" value="送信する" onclick="disableButton()"/>  
          <a href="javascript:void(0);" onclick="document.form1.reset()"><img src="./img/btn_reset.gif" alt="リセット" width="113" height="25" /></a>
         --> 
         	<input type="button" name="button1" value=" 送信する " onClick="disableButton()" class="submit_button">
			<input type="reset" name="button1" value=" リセット " class="reset_button">
         
				<!-- DigiCert Seal HTML -->
<!-- Place HTML on your site where the seal should appear -->
<div id="DigiCertClickID_DMYnOAHo"></div>

<!-- DigiCert Seal Code -->
<!-- Place with DigiCert Seal HTML or with other scripts -->
<script type="text/javascript">
        var __dcid = __dcid || [];
 __dcid.push({"cid":"DigiCertClickID_DMYnOAHo","tag":"DMYnOAHo","seal_format":"dynamic"});
        (function(){var cid=document.createElement("script");cid.async=true;cid.src="//seal.digicert.com/seals/cascade/seal.min.js";var s = document.getElementsByTagName("script");var ls = s[(s.length - 1)];ls.parentNode.insertBefore(cid, ls.nextSibling);}());
</script>
          <input name="mode" type="hidden" id="mode" value="conf" />
        </div>

		</form>
		<!-- //入力フォーム -->


</div>
</div>
<?php
include($_SERVER['DOCUMENT_ROOT'] . '/common/block/footer.html');
?>
</body>
</html>
<?php
} elseif ($_POST["sendok"] == "ok") {

	if ($_GET["value"]!="smartecowatt_for_eo") {
			
			//メール送信
			$text_body="ご担当" . "様" . "\r\n" .
		
			"本メールは、お問い合わせメールとして送らさせていただいております。" . "\r\n" .
		
			"【お問い合わせ内容】━━━━━━━━━━━━━━━━━━━━━━━━━" . "\r\n" .
			" 製 品 名:        " . $_POST["productName"] . "\r\n" .
			" 名　　前:　　　　" . $_POST["name"] . "\r\n" .
			" 会社/団体:     　" . $_POST["kaisya"] . "\r\n" .
			" 所属部署名:      " . $_POST["syozoku"] . "\r\n" .		
			" ご住所: 　     　" . $_POST["pref"] . $_POST["city"] . $_POST["town"]  . "\r\n" .
			" 電話番号:  　    " . $_POST["telNo"] . "\r\n" .
			" メ ー ル:　　　　" . $_POST["email"] . "\r\n" .
			" お問合せ種類:　　" . $_POST["detail"] . "\r\n" .
			" お問合せ内容:    " . $_POST["message"]. "\r\n" .
			"\r\n" .
			"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" . "\r\n" .
			"\r\n" .
			"以上、対応よろしくお願い申し上げます。";  
	}else{
		
		//メール送信
			$text_body="ご担当" . "様" . "\r\n" .
		
			"本メールは、お問い合わせメールとして送らさせていただいております。" . "\r\n" .
		
			"【お問い合わせ内容】━━━━━━━━━━━━━━━━━━━━━━━━━" . "\r\n" .
			" 製 品 名:        " . $_POST["productName"] . "\r\n" .
			" 名　　前:　　　　" . $_POST["name"] . "\r\n" .
			" ご住所: 　     　" . $_POST["pref"] . $_POST["city"] . $_POST["town"]  . "\r\n" .
			" 電話番号:  　    " . $_POST["telNo"] . "\r\n" .
			" メ ー ル:　　　　" . $_POST["email"] . "\r\n" .
			" お問合せ種類:　　" . $_POST["detail"] . "\r\n" .
			" お問合せ内容:    " . $_POST["message"]. "\r\n" .
			"\r\n" .
			"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" . "\r\n" .
			"\r\n" .
			"以上、対応よろしくお願い申し上げます。";  
	}
			
	//半角カナを全角カナに変更	
	$text_body=mb_convert_kana($text_body ,"sKV");		
	
	//$subject="一二三四五六七八" ; 全角8文字はエラー
	$subject="お問い合わせ" ;
	$subject2="確認メール" ;
	
	//$to       = 'nakamura@enegate.jp';
	$to       = $_POST["mail_to"];

//セキュリティテストのため　TO は固定アドレスを入れる 2013/03/23 --------------------------
$mail_to_adderss='nakamura.isao@enegate.co.jp';
if($to=="hp_mail_seigyo"){$mail_to_adderss='hp_mail_seigyo@enegate.co.jp';}
if($to=="hp_mail_eigyou"){$mail_to_adderss='hp_mail_eigyou@enegate.co.jp';}
if($to=="hp_mail_transu"){$mail_to_adderss='hp_mail_transu@enegate.co.jp';}
if($to=="hp_mail_keisoku"){$mail_to_adderss='hp_mail_keisoku@enegate.co.jp';}
if($to=="hp_mail_kenkai"){$mail_to_adderss='hp_mail_kenkai@enegate.co.jp';}
if($to=="hp_mail_smarteco"){$mail_to_adderss='hp_mail_smarteco@enegate.co.jp';}
if($to=="hp_mail_keiki"){$mail_to_adderss='hp_mail_keiki@enegate.co.jp';}
if($to=="hp_mail_soumu"){$mail_to_adderss='hp_mail_soumu@enegate.co.jp';}
if($to=="info-svare"){$mail_to_adderss='info-svare@enegate.co.jp';}
//---------------------------------------------------------------------------------------


	//$to       = 'nakamura.isao@enegate.co.jp';
	$from = "From:hp_enegate@enegate.co.jp" . "\r\n" . "Cc:hp_mail_soumu@enegate.co.jp";
	//$from = "From:hp_enegate@enegate.co.jp";

	mb_language("ja");
	mb_internal_encoding("SHIFT-JIS");
	mb_send_mail($mail_to_adderss,$subject, $text_body, $from)
		or die("mail Err\n");
	require("thanks.html");

}
?>