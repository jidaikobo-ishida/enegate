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
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
<title>お問い合わせ｜株式会社エネゲート</title>
<meta name="description" content="エネゲートへのお問い合わせ、ご意見、ご要望はこちらから。" />
<meta name="keywords" content="エネゲート,お問い合わせ" />
<link rel="stylesheet" href="/common/css/reset.css" media="all">
<link rel="stylesheet" href="/common/css/common.css" media="all">
<link rel="stylesheet" href="/cmn/css/print.css" media="print">
<script type="text/javascript">
<!--

//submitの2度押し防止
function disableButton(){
  //document.form1.button1.disabled = true;　
  submit(document.form1);
}
//submitの2度押し防止
function disableButton2(){
  //document.form1.button1.disabled = true;　
  submit2(document.form1);
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
	// 設定終了
	if(flag){
		window.alert('必須項目に未入力がありました'); // 入力漏れがあれば警告ダイアログを表示
		return false; // 送信を中止
	}else{
		return true; // 送信を実行
	}
}
function submit2(formName){
	var retval;
	retval=check2(formName);
	    
	if(retval){
	        formName.sendok.value="ok";
  		    formName.submit();
	 }else{
		    formName.sendok.value=""; 
	 }
}
function check2(formName){
	
	var flag = 0;
	// 設定開始（必須にする項目を設定してください）
	if(formName.email.value == ""){ // 「メールチェック」の入力をチェック
		flag = 1;
	}
	if(formName.pref.value == ""){ // 「住所」の入力をチェック
		flag = 1;
	}
	if(formName.city.value == ""){ // 「市」の入力をチェック　town
		flag = 1;
	}
	if(formName.town.value == ""){ // 「市」の入力をチェック　
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
function submit3(formName){
	var retval;
	retval=check3(formName);
	    
	if(retval){
	        formName.sendok.value="ok";
  		    formName.submit();
	 }else{
		    formName.sendok.value=""; 
	 }
}
function check3(formName){
	
	var flag = 0;
	// 設定開始（必須にする項目を設定してください）
	if(formName.email.value == ""){ // 「メールチェック」の入力をチェック
		flag = 1;
	}
	if(formName.telNo.value == ""){ // 「メールチェック」の入力をチェック
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
	<ol class="breadcrumbslist"><li><a href="/">HOME</a></li><li>お問い合わせ</li></ol>
</div>

<div class="inner clearfix">
<div class="section">
		<h1 class="grytitle">お問い合わせ</h1>
		<p class="text">当ウェブサイトのお問い合わせフォームには、プライバシー保護のため、SSL暗号化通信を採用（導入）しています。</p>


		<!-- 入力フォーム -->
 <!--
        <form action="index115.php" method="post" id="form1" name="form1">
  -->     
        <form action="index.php" method="post" id="form1" name="form1" onsubmit="this.button1.disabled = true;">
        

		<table class="graytb" width="100%">
		<tr>
		<th>お問合せ項目</th>
		<td>
		<select name="naiyou"  class="w202" >
		<?php if ($_GET["value"]=="denkimetertorikae") { ?>
			<option value="">選んでください</option>
			<option value="製品について">製品について</option>
			<option value="電気メータ取替えについて" selected>電気メータ取替について</option>
		<?php }else{ ?>
			<option value="">選んでください</option>
			<option value="製品について">製品について</option>
			<option value="電気メータ取替えについて" >電気メータ取替について</option>
		<?php } ?>
			<option value="EV充電関係について">EV充電関係について</option>
			<option value="EMS関係について">EMS関係について</option>
			<option value="パートナーシップ構築宣言について">パートナーシップ構築宣言について</option>
			<option value="事業継続方針について">事業継続方針について</option>
			<option value="環境について">環境について</option>
			<option value="求人について">求人について</option>
			<option value="その他">その他</option>
		</select>
		</td></tr>

		<tr>
		<th>お名前</th>
		<td>
		<input name="name"  type="text" size=35 maxlength="100" class="text w202" />
		</td></tr>

		<tr>
		<th>会社・団体名</th>
		<td><input name="kaisya"  type="text" size="35" maxlength="100" class="text w202" /></td></tr>

		<tr>
		  <th>所属部署名</th>
		  <td>
		    <input name="syozoku" type="text" size=35 maxlength="100" class="text w202"/></td></tr>
		<tr>
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
		    <?php if ($_GET["value"]=="denkimetertorikae") { ?>
            	<span class="px12_red">※必須項目</span>
            <?php } ?>
            </td></tr>

		<tr>
		<th>電話番号</th>
		<td><input name="telNo"  type="text" size="35" maxlength="100" class="text w202" /></td></tr>

		<tr>
		<th>メールアドレス</th>
		<td><input name="email" type="text"  size="35" class="text w202" />
		  <span class="px12_red">※必須項目</span></td></tr>
		
		<?php if ($_GET["value"]=="denkimetertorikae") { ?>
		<tr>
			<th>お客さま番号</th>
			<td><input name="okyakuno" type="text"  size="35" class="text w202" />
            </td>
        </tr>
        <?php }else{ ?>
        <tr>
            <th>お問合せ種類</th>
            <td>
                <span class="px12_red">※必須項目</span><br />
                <input type="radio" name="detail" value="お見積り依頼"  checked />
                お見積り依頼<br />
                <input type="radio" name="detail" value="資料請求"  />
                資料請求<br />
                <input type="radio" name="detail" value="その他"  />
                その他
            </td>
        </tr>
		<?php } ?>
		<tr>
		<th>お問合せ内容</th>
		<td>
		<textarea name="message" cols="50" rows="6"  class="w398" /></textarea>
		</td></tr>
		</table>

           <!--
                <input name="sendok" type="hidden" value="送信する"/> 
	    -->
                <input name="sendok" type="hidden" value="" />
                <p class="text txtc">記入内容をよくご確認のうえ、「送信」ボタンを押してください。</p>
                <div id="FormButtons">
	<!--
        <input name="submit" type="image" src="./img/btn_send.gif" value="送信する" onclick="javascript:Submit('form1');"/>
	-->

        <?php if ($_GET["value"]=="denkimetertorikae") { ?>
        <!--
        	<input name="button1" type="image" src="./img/btn_send.gif"  value="ok" onclick="javascript:submit2('form1');"/>
        -->
        <input name="button1" type="button" value="送信する" onclick="disableButton2();" class="submit_button">
		<?php }else{ ?>
        <!--
        <input name="button1" type="image" src="./img/btn_send.gif" value="ok"  onclick="disableButton();"/>
        -->
        <input type="button" name="button1" value=" 送信する " onclick="disableButton()" class="submit_button">
	<?php } ?>
		<a href="javascript:void(0);" onclick="document.form1.reset()">
		
        <input type="reset" name="button1" value=" リセット " class="reset_button">
        <!--
		<img src="./img/btn_reset.gif" alt="リセット" width="113" height="25" /></a>
		-->
			
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

	if ($_POST["naiyou"]=="電気メータ取替えについて") { 
		//メール送信
		$text_body="総務ご担当" . "様" . "\r\n" .
		
		"本メールは、お問い合わせメールとして送らさせていただいております。" . "\r\n" .
		
		"【お問い合わせ内容】━━━━━━━━━━━━━━━━━━━━━━━━━" . "\r\n" .
		" お問い合わせ項目:" . $_POST["naiyou"] . "\r\n" .
		" 名　　前:　　　　" . $_POST["name"] . "\r\n" .
		" 会社/団体:     　" . $_POST["kaisya"] . "\r\n" .
		" 所属部署名:      " . $_POST["syozoku"] . "\r\n" .
		" ご住所: 　     　" . $_POST["pref"] . $_POST["city"] . $_POST["town"]  . "\r\n" .
		" 電話番号:  　    " . $_POST["telNo"] . "\r\n" .
		" メ ー ル:　　　　" . $_POST["email"] . "\r\n" .
		" お客さま番号:    " . $_POST["okyakuno"] . "\r\n" .
		" お問合せ内容:    " . $_POST["message"]. "\r\n" .
		"\r\n" .
		"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" . "\r\n" .
		"\r\n" .
		"以上、対応よろしくお願い申し上げます。";  
	
	}else{
		//メール送信
		$text_body="総務ご担当" . "様" . "\r\n" .
		
		"本メールは、お問い合わせメールとして送らさせていただいております。" . "\r\n" .
		
		"【お問い合わせ内容】━━━━━━━━━━━━━━━━━━━━━━━━━" . "\r\n" .
		" お問い合わせ項目:" . $_POST["naiyou"] . "\r\n" .
		" 名　　前:　　　　" . $_POST["name"] . "\r\n" .
		" 会社/団体:     　" . $_POST["kaisya"] . "\r\n" .
		" 所属部署名:      " . $_POST["syozoku"] . "\r\n" . 
		" ご住所: 　     　" . $_POST["pref"] . $_POST["city"] . $_POST["town"]  . "\r\n" .
		" 電話番号:  　    " . $_POST["telNo"] . "\r\n" .
		" メ ー ル:　　　　" . $_POST["email"] . "\r\n" .
		" お問合せ種類:    " . $_POST["detail"] . "\r\n" .
		" お問合せ内容:    " . $_POST["message"]. "\r\n" .
		"\r\n" .
		"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" . "\r\n" .
		"\r\n" .
		"以上、対応よろしくお願い申し上げます。";  	
		
	}
	
	//半角カナを全角カナに変更	
	$text_body=mb_convert_kana($text_body ,"sKV");
	
	//$subject="一二三四五六七八" ; 全角8文字はエラー
	$subject="お問い合わせ" ;
	$subject2="確認メール" ;

	if ($_POST["naiyou"]=="電気メータ取替えについて") { 
		$to       = 'hp_mail_keiki@enegate.co.jp';
		$from = "From:hp_enegate@enegate.co.jp" . "\r\n" . "Cc:hp_mail_soumu@enegate.co.jp";
	}elseif ($_POST["naiyou"]=="EV充電関係について") { 
		$to       = 'hp_mail_eigyou@enegate.co.jp';
		$from = "From:hp_enegate@enegate.co.jp" . "\r\n" . "Cc:hp_mail_soumu@enegate.co.jp";
	}elseif ($_POST["naiyou"]=="EMS関係について") { 
		$to       = 'hp_mail_eigyou@enegate.co.jp';
		$from = "From:hp_enegate@enegate.co.jp" . "\r\n" . "Cc:hp_mail_soumu@enegate.co.jp";
	}elseif ($_POST["naiyou"]=="パートナーシップ構築宣言について") { 
		$to       = 'hp_mail_koubai@enegate.co.jp';
		$from = "From:hp_enegate@enegate.co.jp" . "\r\n" . "Cc:hp_mail_soumu@enegate.co.jp";
	}else{
		$to       = 'hp_mail_soumu@enegate.co.jp';	
		//$to       = 'nakamura.isao@enegate.co.jp';
		$from = "From:hp_enegate@enegate.co.jp";
	}
	
	mb_language("ja");
	mb_internal_encoding("SHIFT-JIS");
	mb_send_mail($to,$subject, $text_body, $from)
		or die("メール送信エラーです。しばらくしてから再度送信してください。\n");
	require("thanks.html");
}
?>