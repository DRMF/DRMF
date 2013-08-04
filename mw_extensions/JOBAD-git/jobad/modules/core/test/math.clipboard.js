(function($){
JOBAD.modules.register({
  info:{
    'identifier': 'math.clipboard',
    'title':  'Math Clipboard',
    'author': 'Janelle Williams and Deyan Ginev',
    'description':  'Clipboard for math formulas realized via Zeroclipboard',
  },

  contextMenuEntries: function(target){
    if(target.is('#nomenu,#nomenu *')){ //no menu for these elements
      return false; }
    var math = target.closest('math');
    if (! math.is('math')) { return false;}
    
    if ($("#zeroclipboardbutton").length == 0) {
      // The most important part is here -- attach a Flash ZeroClipboard object
      // to the current menu row, which will only be created __after__ this function has completed
      // in other words add the attachment into an event that will be triggered when the row is created
      var $hidden_button = $("<button id='zeroclipboardbutton'>Copy TeX Source</button>");
      $('#mw-content-text').append($hidden_button);
      ZeroClipboard.setMoviePath('/extensions/JOBAD-git/ZeroClipboard.swf');
      var clip = new ZeroClipboard.Client(); 
      clip.glue($hidden_button[0], $hidden_button.parent()[0]);
      clip.setText("TeXXX");
      $hidden_button.zclip({
        path:'/extensions/JOBAD-git/ZeroClipboard.swf',
        copy:"Tex"});
      $hidden_button.hide();
    }
    var $tex = math.find('annotation[encoding="application/x-tex"]').text();
    
    return [
      ["Copy TeX Source", function(element,object){
        // We really have nothing to do in the actual click,
        // the Flash will capture that event and do the clipboard magic
        // Temporary: just so that we do something
        var $hidden_button = $("#zeroclipboardbutton");
        $hidden_button.click();
      }]
    ];
  }
});
})(JOBAD.refs.$);


