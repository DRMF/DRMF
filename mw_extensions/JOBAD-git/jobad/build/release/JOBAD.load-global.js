  var JOBAD_IN_PAGE;
  var selector = jQuery("#mw-content-text");
  JOBAD_IN_PAGE = new JOBAD(selector);
  JOBAD_IN_PAGE.modules.load([
    "math.showsource",
    "math.clipboard",
    "mathjax.mathjax",
    "wiki.formulapage",
    'math.wolframalpha'
  ], function(mod, state){
    this.Setup();
  });

true;
