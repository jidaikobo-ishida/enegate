function Submit(formName){
	var retval;
	retval=check(formName);
	    
	if(retval){
		    
	        document.forms[formName].button1.disabled = true;
			document.forms[formName].sendok.value="ok";
			document.forms[formName].action="index115.php";
			document.forms[formName].method="post";
			　
			document.forms[formName].submit();
			
			
			//document.forms[formName].sendok.value="ok";
  		    //document.forms[formName].submit();
			return true; // 送信を実行
	 }else{
		 alert("sendErr");
		    //document.forms[formName].sendok.value="";
			document.forms[formName].sendok.value="";
			return false; // 送信を中止
	 }
}
function check(formName){
	
	var flag = 0;
	// 設定開始（必須にする項目を設定してください）
	if(document.forms[formName].email.value == ""){ // 「メールチェック」の入力をチェック
		flag = 1;
		alert("notinput");
	}
	// 設定終了
	if(flag){
		window.alert('必須項目に未入力がありました'); // 入力漏れがあれば警告ダイアログを表示
		return false; // 送信を中止
	}else{
		return true; // 送信を実行
	}
}
function Submit2(formName){
	var retval;
	retval=check2(formName);
	    
	if(retval){
	        document.form1.button1.disabled = true;　
			document.forms[formName].sendok.value="ok";
  		    document.forms[formName].submit();
	 }else{
		    document.forms[formName].sendok.value=""; 
	 }
}
function check2(formName){
	
	var flag = 0;
	// 設定開始（必須にする項目を設定してください）
	if(document.forms[formName].email.value == ""){ // 「メールチェック」の入力をチェック
		flag = 1;
	}
	if(document.forms[formName].pref.value == ""){ // 「住所」の入力をチェック
		flag = 1;
	}
	if(document.forms[formName].city.value == ""){ // 「市」の入力をチェック　town
		flag = 1;
	}
	if(document.forms[formName].town.value == ""){ // 「市」の入力をチェック　
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
function Submit3(formName){
	var retval;
	retval=check3(formName);
	    
	if(retval){
	        document.form1.button1.disabled = true;　
			document.forms[formName].sendok.value="ok";
  		    document.forms[formName].submit();
	 }else{
		    document.forms[formName].sendok.value=""; 
	 }
}
function check3(formName){
	
	var flag = 0;
	// 設定開始（必須にする項目を設定してください）
	if(document.forms[formName].email.value == ""){ // 「メールチェック」の入力をチェック
		flag = 1;
	}
	if(document.forms[formName].telNo.value == ""){ // 「メールチェック」の入力をチェック
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
function disableButton(){
  document.form1.button1.disabled = true;　
  submitForm();
}
function submitForm(){
  document.form1.submit();
}
