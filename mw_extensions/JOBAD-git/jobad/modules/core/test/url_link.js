JOBAD.modules.register({
	info:{
		'identifier':	'test.url',
		'title':	'Test Module: Mediawiki Link',
		'author':	'Janelle Williams',
		'description':	'Simple link to proof page from mediawiki',
	},
	contextMenuEntries: function(target){
		if(target.is('#nomenu,#nomenu *')){ //no menu for these elements
			return false;
		}
			var math = target.closest('math');
		if (! math.is('math')) { return false;}
		
		return[
		       ["Url Link", function(element){
			  /*     var link = target.closest('a').attr('href');
				 window.location.href = link; */
				 var math_key = 'title';
				 var txt = math.find('annotation[encoding="application/x-tex"]').text();
				 var math_value= encodeURIComponent(txt).replace(/\(/g, "%28").replace(/\\\\/g,"\\").replace(/\)/g,"%29").replace(/\*/g,"%@A").replace(/\\/g,"%5C");
       				 alert(math_value);
				
				 /*	 var url_tex = window.location.search.substr(1).split('&');
      				 var i=url_tex.length; var x;
				 
				 while(i--){
				     x = url_tex[i].split('=');
				     if(x[0])
				     /*
					 if (x[0]== math){
					 x[1] = math_value;
					 url_tex[i] = x.join('=');
				     
	    	           		break;
				     }
				 }
				 
				 if(i<0) {url_tex[url_tex.length] = [math_key,math_value].join('=');}
   				 window.location.search = url_tex.join('&'); 
				 */
				 var url_page=window.location.search.substr(1);
				 //alert(url_page);
				 var new_url = url_page+"boilerplate=Template%3ADRMF&title=" + math_value;
				 alert(new_url);
				 alert(decodeURIComponent(math_value));
				 window.location.href = new_url;
				   }]
		       ];
	}
    });