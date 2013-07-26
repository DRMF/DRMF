/*
	mathc_clipboard.js - An example module for JOBAD. 
	Extracts the TeX from a selected MathML formula and shows a tooltip.
*/

JOBAD.modules.register({
	info:{
		'identifier':	'test.math.clip',
		'title':	'Test Module: Math Clipboard',
		'author':	'Deyan Ginev',
		'description':	'Simple math clipboard for MathML formulas.',
	},
	contextMenuEntries: function(target){
		if(target.is('#nomenu,#nomenu *')){ //no menu for these elements
			return false;
		}
		var math = target.closest('math');
		if (! math.is('math')) { return false;}
		return [
			["Display TeX", function(element){
				var txt = math.find('annotation[encoding="application/x-tex"]').text();
				alert(txt);
			}]
		];
	}
});
