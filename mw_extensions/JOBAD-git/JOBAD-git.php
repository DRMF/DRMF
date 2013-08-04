<?php

  /*
   *Mediawiki JOBAD extension
   *
   *@file
   *@ingroup Extensions
   *@version 1.0
   *@author Janelle Williams & Deyan Ginev
   *
   */


if (!defined('MEDIAWIKI')) {
  die("This is not a valid entry point to MediaWiki.\n");
}

//Extension credits that shows on Sepcial: Version
$wgExtensionCredits['other'][]=array(
  'path'=> __FILE__,
  'name'=> 'JOBAD-git',
  'author'=> 'Janelle Williams and Deyan Ginev',
  'version'=> '1.0',
  'descriptionmsg'=>'JOBAD script insert',
);

global $wgResourceModules, $wgOut;
$wgHooks['BeforePageDisplay'][] = 'addingModules';
function addingModules(&$out ){
  $out->addModules( array ('ext.JOBAD-git') );
  return true;  
}

$moduleTemplate = array(
  'localBasePath' => dirname(__FILE__) . '/jobad/build/release',
  'remoteExtPath' => 'JOBAD-git/jobad/build/release',
  'position' => 'top',
  'group' => 'ext.JOBAD-git',
);

file_put_contents( '/tmp/my-custom-debug.log' , "$wgScriptPath\n");

$wgResourceModules['ext.JOBAD-git'] = $moduleTemplate + array(
  'scripts' => array(
    '../../js/deps/jquery/jquery-ui-1.10.3.js',
    'JOBAD.js',
    '../../modules/core/test/math.showsource.js',
    '../../modules/core/test/ZeroClipboard.js',
    '../../modules/core/test/math.clipboard.js',
    "../../modules/core/test/mathjax.mathjax.js",
    "../../modules/core/test/wiki.formulapage.js",
    "../../modules/core/test/math.wolframalpha.js",
    "JOBAD.load-global.js"
  ),
  'dependencies' =>  array('jquery','jquery.ui.core'),
  'styles' => 'JOBAD.css',
);

?>

           