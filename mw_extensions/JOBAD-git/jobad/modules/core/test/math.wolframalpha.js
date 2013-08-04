(function($){
JOBAD.modules.register({
  info:{
    'identifier': 'math.wolframalpha',
    'title':  'Wolfram Alpha redirect',
    'author': 'Deyan Ginev',
    'description':  'Queries Wolfram Alpha for information on the formula',
  },

  contextMenuEntries: function(target){
    if(target.is('#nomenu,#nomenu *')){ //no menu for these elements
      return false; }
    var math = target.closest('math');
    if (! math.is('math')) { return false;}
    
    return [
      ["Consult Wolfram Alpha", function(element){
        var $tex = math.find('annotation[encoding="application/x-tex"]').text();
        $tex = encodeURIComponent($tex).replace(/\(/g, "%28").replace(/\\\\/g,"\\").replace(/\)/g,"%29").replace(/\*/g,"%@A").replace(/\\/g,"%5C");        
        window.location.href = "http://www.wolframalpha.com/input/?i="+$tex;
      }]
    ];
  }
});
})(JOBAD.refs.$);


