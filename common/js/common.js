

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
	$(".accordion li a").on("click", function() {
		$(this).next().slideToggle();	
		// activeが存在する場合
		if ($(this).children(".accordion_icon").hasClass('active')) {			
			// activeを削除
			$(this).children(".accordion_icon").removeClass('active');				
		}
		else {
			// activeを追加
			$(this).children(".accordion_icon").addClass('active');			
		}			
	});
});
  


