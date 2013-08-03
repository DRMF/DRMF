  var JOBAD_IN_PAGE;
  var selector = jQuery("#mw-content-text");
  JOBAD_IN_PAGE = new JOBAD(selector);
  JOBAD_IN_PAGE.modules.load([
  ['test.click', ['green']],
  "test.menu1",
  "test.menu2",
  "test.hover",
  "test.sidebar"
  ], function(mod, state){
    this.Setup();
  });

true;
