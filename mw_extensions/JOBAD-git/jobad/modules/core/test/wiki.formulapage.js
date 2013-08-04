(function($){
  JOBAD.modules.register({
    info:{
      'identifier': 'wiki.formulapage',
      'title':  'Formula page redirects for MediaWiki',
      'author': 'Janelle Williams',
      'description':  'Simple link to proof page from MediaWiki',
    },
    contextMenuEntries: function(target){
      if(target.is('#nomenu,#nomenu *')){ //no menu for these elements
        return false;
      }
      var math = target.closest('math');
      if (! math.is('math')) { return false;}
      
      return[
        ["Formula page", function(element){
          /*     var link = target.closest('a').attr('href');
          window.location.href = link; */
          var math_key = 'title';
          var txt = math.find('annotation[encoding="application/x-tex"]').text();
          var math_value= encodeURIComponent(txt).replace(/\(/g, "%28").replace(/\\\\/g,"\\").replace(/\)/g,"%29").replace(/\*/g,"%@A").replace(/\\/g,"%5C");        

          var url_page=window.location.search.substr(1);
          var new_url = url_page+"boilerplate=Template%3ADRMF";//&title=" + math_value;
          //alert(new_url);
          //alert(decodeURIComponent(math_value));
          window.location.href = new_url;
        }]
      ];
    }
  });
})(JOBAD.refs.$);
