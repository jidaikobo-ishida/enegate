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
	// 1. 左メニュー親タイトル（採用情報、会社情報などの大枠アコーディオン）
	$('.leftsubnav .navtitle a.toggle, .leftsubnav .navtitle .nvliti').on('click', function(e) {
		var $navtitle = $(this).closest('.navtitle');
		var $leftmenu = $navtitle.find('ul.leftmenu');
		if ($leftmenu.length) {
			e.preventDefault();
			$leftmenu.stop(true, true).slideToggle();
			$navtitle.find('.accordion_icon').toggleClass('active');
		}
	});

	// 2. 左メニュー内のサブメニュー項目(新卒採用、経験者採用などの子アコーディオン)
	$('.leftmenu a.dpmenu, .leftmenu li:has(ul) > a').on('click', function(e) {
		if (window.innerWidth <= 736) {
			var $sub = $(this).next('ul');
			if ($sub.length) {
				e.preventDefault();
				$sub.stop(true, true).slideToggle();
				$(this).toggleClass('active');
			}
		}
	});

	// 3. グローバルナビのアコーディオン開閉制御
	$("#globalnav .accordion li a").on("click", function(e) {
		var $sub = $(this).next('ul');
		if ($sub.length) {
			$sub.slideToggle();	
			$(this).children(".accordion_icon").toggleClass('active');
		}
	});
});
  


