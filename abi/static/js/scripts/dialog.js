// JavaScript Document

/* --------------------------------------------------------------------------------
   [Dialog]
-------------------------------------------------------------------------------- */
function initDialog(){
	$(".showDialog").click(function(e){
		// cancel the link behavior
		e.preventDefault();
		
		// get link target
		var target = $(this).attr('href');
		
		// create page overlay
		$.blockUI();
		
		// set animation effect for non-ie browser
		var effect = null;
		if( !isIE() ) { effect = 'fade'; }
		
		// set dialog class
		var newDialogClassPrefix = target.substring(1);
		var newDialogClass = 'ui-dialog-' + newDialogClassPrefix;
		
		// set dialog width
		var dialogWidth = $(target).children("div.dialogOptions").css('width');

		// start Dialog with targer
		$(target).dialog({
			show:			effect,
			dialogClass:	' g-box-shadow-black ' + newDialogClass,
			width:			dialogWidth,
			close:			function(){
								// destroy page overlay
								$.unblockUI();
								// destroy dialog
								//$(this).dialog('destroy');
							}
		});
		
	})
}


/* --------------------------------------------------------------------------------
   [ON LOAD]
-------------------------------------------------------------------------------- */
jQuery(document).ready(function(){
	initDialog();
});