/*@cc_on _d=document;eval('var document=_d')@*/
$(function(){
	topics01Length = $('.topics01 dt').length;
	topics02Length = $('.topics02 dt').length;
	topics03Length = $('.topics03 dt').length;
	topics04Length = $('.topics04 dt').length;
	topics05Length = $('.topics05 dt').length;

	if(topics01Length>1){
		$('.topics01 dl').css({ "padding":"0 0 3px 77px","margin-top":"-2px" });
		$('.newsTopics .box01').css({ "padding":"18px 0 8px 0" });
	}
	if(topics02Length>1){
		$('.topics02 dl').css({ "padding":"0 0 3px 77px","margin-top":"-2px" });
		$('.newsTopics .box02').css({ "padding":"18px 0 8px 0" });
	}
	if(topics03Length>1){
		$('.topics03 dl').css({ "padding":"0 0 3px 77px","margin-top":"-2px" });
		$('.newsTopics .box03').css({ "padding":"18px 0 8px 0" });
	}
	if(topics04Length>1){
		$('.topics04 dl').css({ "padding":"0 0 3px 77px","margin-top":"-2px" });
		$('.newsTopics .box04').css({ "padding":"18px 0 8px 0" });
	}
	if(topics05Length>1){
		$('.topics05 dl').css({ "padding":"0 0 3px 77px","margin-top":"-2px" });
		$('.newsTopics .box05').css({ "padding":"18px 0 0 0" });
	}
});