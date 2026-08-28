$(function(){
    var ua = navigator.userAgent;
    if((ua.indexOf('iPhone') > 0) || ua.indexOf('iPod') > 0 || (ua.indexOf('Android') > 0 && ua.indexOf('Mobile') > 0)){
        $('head').prepend('<meta name="viewport" content="width=device-width,initial-scale=1">');
    } else {
        $('head').prepend('<meta name="viewport" content="width=950">');
    } 
});


var $win = $(window);
$win.on('load resize', function() {
  var windowWidth = window.innerWidth;
  if (windowWidth > 737) {
  $(function(){
	var id = $("body").attr("id");
	$(".leftsubnav ul."+id).addClass("current");
	$(".leftsubnav ul li."+id).addClass("currentbkc");
	});
  } else {
  
  }
});



 
 $(function(){
  $("#toggle A").on("click",
  function(){
    $("#glmenu").slideToggle();
  });
}); 

  $('a[href^=#]').click(function(){
    var speed = 500;
    var href= $(this).attr("href");
    var target = $(href == "#" || href == "" ? 'html' : href);
    var position = target.offset().top;
    $("html, body").animate({scrollTop:position}, speed, "swing");
    return false;
  });
  
 $(function(){
	// 左メニューのサブメニュー持ち親項目(dpmenu)のスマホタップ開閉（ページ遷移キャンセル）
	$('.leftmenu a.dpmenu, .leftmenu li:has(ul) > a').on('click', function(e) {
		if (window.innerWidth <= 736) {
			var $sub = $(this).next('ul');
			if ($sub.length) {
				e.preventDefault();
				$sub.slideToggle();
				$(this).toggleClass('active');
			}
		}
	});

	// アコーディオンアイコンを持つ項目の開閉制御
	$(".accordion li a.toggle, #globalnav .accordion li a").on("click", function(e) {
		$(this).next().slideToggle();	
		if ($(this).children(".accordion_icon").hasClass('active')) {			
			$(this).children(".accordion_icon").removeClass('active');				
		}
		else {
			$(this).children(".accordion_icon").addClass('active');			
		}			
	});
});
  


