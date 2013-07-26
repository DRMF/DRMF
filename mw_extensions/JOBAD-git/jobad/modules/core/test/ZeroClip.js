JOBAD.modules.register({
	info:{
		'identifier':	'test.zero.clipboard',
		'title':	'Test Module: Flash Clipboard',
		'author':	'Janelle Williams',
		'description':	'Small flash video attached to menu content',
	},

	contextMenuEntries: function(target){
		if(target.is('#nomenu,#nomenu *')){ //no menu for these elements
			return false;
		}


  var math = target.closest('math');
		    if (! math.is('math')) { return false;}
		    // 1. we create a hidden button anywhere
		    var $hidden_button = $("<button id='hiddenbutton' >button </button>");
		    var $hidden_text = $("<div id='hiddenmathtocopy'>some starting text</div><br><br>");
		    
		    $('body').append($hidden_button);
		    $('body').append($hidden_text);
		    // $hidden_text.hide();
		    //$hidden_button.hide();
		    // 2. we add the zclip functionality to that button
		    /*		    $hidden_button.style ='none';
                    ZeroClipboard.setMoviePath('ZeroClipboard.swf');
                    var clip = new ZeroClipboard.Client(); 
                    clip.addEventListener('mouseDown', function (client) {
			  $hidden_button.trigger('mousedown');
			});			
		    clip.glue($hidden_button[0], $hidden_button.parent()[0]);
					
		    //$(window).bind('load resize',function(){clip.reposition();});
 */
 
		    return [
			    ["Copy TeX Source", function(element){
				    var tex = math.find('annotation[encoding="application/x-tex"]').text();
				    
				    $hidden_text.text(tex);
				    $hidden_button.zclip({
					    path:'examples/Zeroclipboard.swf',
					    copy:$hidden_text.text(),
				    //				    $hidden_text.text(tex);
				    //   clip.setText(tex);
				    //clip.receiveEvent('mouseDown', null);
					});
				}]
			    ];
		}





    });