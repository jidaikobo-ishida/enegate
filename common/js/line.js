var userAgent = window.navigator.userAgent.toLowerCase();
    
if(userAgent.indexOf('firefox') != -1 || userAgent.indexOf('trident') != -1) {
    $(function(){
	var speed01 = 6;
	var speed02 = 5;
	var speed03 = 6;
	var posX01 = 0;
	var posX02 = 0;
	var posX03 = 0;
	var imgWidth = 1900;

	setInterval(function(){
			if (posX01 >= imgWidth) posX01= 0;
			posX01 += speed01;
			$('#line1').css("background-position",posX01+"px top");
	}, 1);

	setInterval(function(){
			if (posX02 >= imgWidth) posX02= 0;
			posX02 += speed02;
			$('#line2').css("background-position",posX02+"px bottom");
	}, 1);
	
	setInterval(function(){
			if (posX03 >= imgWidth) posX03= 0;
			posX03 += speed03;
			$('#line3').css("background-position",posX03+"px top");
	}, 1);
});

}else{
    $(function(){
	var speed01 = 1.5;
	var speed02 = 0.75;
	var speed03 = 1.5;
	var posX01 = 0;
	var posX02 = 0;
	var posX03 = 0;
	var imgWidth = 1900;

	setInterval(function(){
			if (posX01 >= imgWidth) posX01= 0;
			posX01 += speed01;
			$('#line1').css("background-position",posX01+"px top");
	}, 1);

	setInterval(function(){
			if (posX02 >= imgWidth) posX02= 0;
			posX02 += speed02;
			$('#line2').css("background-position",posX02+"px bottom");
	}, 1);
	
	setInterval(function(){
			if (posX03 >= imgWidth) posX03= 0;
			posX03 += speed03;
			$('#line3').css("background-position",posX03+"px top");
	}, 1);
});

}



