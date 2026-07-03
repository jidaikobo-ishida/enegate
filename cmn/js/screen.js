/*@cc_on _d=document;eval('var document=_d')@*/
var loadingArray = new Array();
loadingArray[0] = '/cmn/js/rollover.js';
loadingArray[1] = '/cmn/js/crir.js';
loadingArray[2] = '/cmn/js/index.js';
/*loadingArray[3] = '/cmn/js/module.js';*/
for( i=0 ; i<loadingArray.length ; i++ ){
	js = document.createElement('script');
	js.src = loadingArray[i];
	head = document.getElementsByTagName('head')[0];
	head.appendChild(js);
}
