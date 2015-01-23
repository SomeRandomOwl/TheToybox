<?php
# Directory Index (dirindex.php)
#
# Reads the current directory's content and displays it as
# HTML.  Useful if file listing is denied by the web server
# configuration.
#
# Installation:
# - Put in any directory you like on your PHP-capable webspace.
# - Rename to 'index.php' if you like it to get called if no
#   file is specified in the URL (e.g. www.example.com/files/).
# - Fit the design to your needs just using HTML and CSS.
#
# Changes since original release (25-Mar-2002):
# - simplified and modernized markup and styles (HTML5, CSS3,
#   list instead of table)
# - more functional programming approach
# - improved configurability
# - escaping of HTML characters
# - license changed from GPL to MIT
# - requires PHP 5.3.0 or later
#
# Version: 25-May-2011
# Copyright (c) 2002, 2011 Jochen Kupperschmidt <http://homework.nwsnet.de/>
# Released under the terms of the MIT license
# <http://www.opensource.org/licenses/mit-license.php>


### configuration

# Show the local path. Disable this for security reasons.
define('SHOW_PATH', FALSE);

# Show a link to the parent directory ('..').
define('SHOW_PARENT_LINK', TRUE);

# Show "hidden" directories and files, i.e. those whose names
# start with a dot.
define('SHOW_HIDDEN_ENTRIES', FALSE);

### /configuration


function get_grouped_entries($path) {
    list($dirs, $files) = collect_directories_and_files($path);
    $dirs = filter_directories($dirs);
    $files = filter_files($files);
    return array_merge(
        array_fill_keys($dirs, TRUE),
        array_fill_keys($files, FALSE));
}

function collect_directories_and_files($path) {
    # Retrieve directories and files inside the given path.
    # Also, `scandir()` already sorts the directory entries.
    $entries = scandir($path);
    return array_partition($entries, function($entry) {
        return is_dir($entry);
    });
}

function array_partition($array, $predicate_callback) {
    # Partition elements of an array into two arrays according
    # to the boolean result from evaluating the predicate.
    $results = array_fill_keys(array(1, 0), array());
    foreach ($array as $element) {
        array_push(
            $results[(int) $predicate_callback($element)],
            $element);
    }
    return array($results[1], $results[0]);
}

function filter_directories($dirs) {
    # Exclude directories. Adjust as necessary.
    return array_filter($dirs, function($dir) {
        return $dir != '.'  # current directory
            && (SHOW_PARENT_LINK || $dir != '..') # parent directory
            && !is_hidden($dir);
    });
}

function filter_files($files) {
    return array_filter($files, function($file) {
        return !is_hidden($file)
            && substr($file, -4) != '.php' # PHP scripts
            && substr($file, -4) != '.settings' #To hide sensitive data
            && substr($file, -4) != '.ftpquota' #To hide ftp Things
            && substr($file, -4) != '*.html'
            && substr($file, -4) != '*.sublime-project'
            && substr($file, -4) != '*.sublime-workspace';
    });
}

function is_hidden($entry) {
    return !SHOW_HIDDEN_ENTRIES
        && substr($entry, 0, 1) == '.'  # Name starts with a dot.
        && $entry != '.'  # Ignore current directory.
        && $entry != '..';  # Ignore parent directory.
}

$path = __DIR__ . '/';
$entries = get_grouped_entries($path);
?>
<!DOCTYPE html>
<html lang="de">
  <head>
  <!--Meta Info-->
  <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
  <meta content="utf-8" http-equiv="encoding">
  <meta property='og:site_name' content='Brony Lug'>
  <meta property='og:title' content='Toybox'>
  <meta property='og:description' content='My toys'>
  <meta property='og:image' content='http://bronylug.com/uploads/3/4/0/5/3405336/1390198763.png'>
  <meta property='og:url' content='http://bronylug.com/secret/toybox/'>
  <title>Toybox</title>
  <!--Asset Loading-->
  <link rel="stylesheet" type="text/css" href="/secret/TheToybox/main.css">
  <script src="/secret/TheToybox/assets/external/jquery/jquery.js"></script>
  <script src="/secret/TheToybox/assets/jquery-ui.js"></script>
  <link rel="stylesheet" href="/secret/TheToybox/assets/jquery-ui.css">
  <script src="/Secret/TheToybox/assets/jquery.scrollbar/jquery.scrollbar.js"></script>
  <script src="/secret/TheToybox/JavaScript/Games/rock.js"></script>
</head>
<html>
  <style type="text/css">
  /*************** SCROLLBAR BASE CSS ***************/
  
  .scroll-wrapper {
  overflow: hidden !important;
  padding: 0 !important;
  position: relative;
  }
  
  .scroll-wrapper > .scroll-content {
  border: none !important;
  box-sizing: content-box !important;
  height: auto;
  left: 0;
  margin: 0;
  max-height: none !important;
  max-width: none !important;
  overflow: scroll !important;
  padding: 0;
  position: relative !important;
  top: 0;
  width: auto !important;
  }
  
  .scroll-wrapper > .scroll-content::-webkit-scrollbar {
  height: 0;
  width: 0;
  }
  
  .scroll-element {
  display: none;
  }
  .scroll-element, .scroll-element div {
  box-sizing: content-box;
  }
  
  .scroll-element.scroll-x.scroll-scrollx_visible,
  .scroll-element.scroll-y.scroll-scrolly_visible {
  display: block;
  }
  
  .scroll-element .scroll-bar,
  .scroll-element .scroll-arrow {
  cursor: default;
  }
  
  .scroll-textarea {
  border: 1px solid #cccccc;
  border-top-color: #999999;
  }
  .scroll-textarea > .scroll-content {
  overflow: hidden !important;
  }
  .scroll-textarea > .scroll-content > textarea {
  border: none !important;
  box-sizing: border-box;
  height: 100% !important;
  margin: 0;
  max-height: none !important;
  max-width: none !important;
  overflow: scroll !important;
  outline: none;
  padding: 2px;
  position: relative !important;
  top: 0;
  width: 100% !important;
  }
  .scroll-textarea > .scroll-content > textarea::-webkit-scrollbar {
  height: 0;
  width: 0;
  }
  
  
  
  
  /*************** SCROLLBAR MAC OS X ***************/
  
  .scrollbar-macosx > .scroll-element,
  .scrollbar-macosx > .scroll-element div
  {
  background: none;
  border: none;
  margin: 0;
  padding: 0;
  position: absolute;
  z-index: 10;
  }
  
  .scrollbar-macosx > .scroll-element div {
  display: block;
  height: 100%;
  left: 0;
  top: 0;
  width: 100%;
  }
  
  .scrollbar-macosx > .scroll-element .scroll-element_track { display: none; }
  .scrollbar-macosx > .scroll-element .scroll-bar {
  background-color: #6C6E71;
  display: block;
  
  -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
  filter: alpha(opacity=0);
  opacity: 0;
  
  -webkit-border-radius: 7px;
  -moz-border-radius: 7px;
  border-radius: 7px;
  
  -webkit-transition: opacity 0.2s linear;
  -moz-transition: opacity 0.2s linear;
  -o-transition: opacity 0.2s linear;
  -ms-transition: opacity 0.2s linear;
  transition: opacity 0.2s linear;
  }
  .scrollbar-macosx:hover > .scroll-element .scroll-bar,
  .scrollbar-macosx > .scroll-element.scroll-draggable .scroll-bar {
  -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=70)";
  filter: alpha(opacity=70);
  opacity: 0.7;
  }
  
  
  .scrollbar-macosx > .scroll-element.scroll-x {
  bottom: 0px;
  height: 0px;
  left: 0;
  min-width: 100%;
  overflow: visible;
  width: 100%;
  }
  
  .scrollbar-macosx > .scroll-element.scroll-y {
  height: 100%;
  min-height: 100%;
  right: 0px;
  top: 0;
  width: 0px;
  }
  
  /* scrollbar height/width & offset from container borders */
  .scrollbar-macosx > .scroll-element.scroll-x .scroll-bar { height: 7px; min-width: 10px; top: -9px; }
  .scrollbar-macosx > .scroll-element.scroll-y .scroll-bar { left: -9px; min-height: 10px; width: 7px; }
  
  .scrollbar-macosx > .scroll-element.scroll-x .scroll-element_outer { left: 2px; }
  .scrollbar-macosx > .scroll-element.scroll-x .scroll-element_size { left: -4px; }
  
  .scrollbar-macosx > .scroll-element.scroll-y .scroll-element_outer { top: 2px; }
  .scrollbar-macosx > .scroll-element.scroll-y .scroll-element_size { top: -4px; }
  
  /* update scrollbar offset if both scrolls are visible */
  .scrollbar-macosx > .scroll-element.scroll-x.scroll-scrolly_visible .scroll-element_size { left: -11px; }
  .scrollbar-macosx > .scroll-element.scroll-y.scroll-scrollx_visible .scroll-element_size { top: -11px; }
  </style>
       <script>
      $(function() {
      $( "input[type=submit]" )
      .button()
      .click(function( event ) {
      start();
      });
      });
      jQuery(document).ready(function(){
      jQuery('.scrollbar-macosx').scrollbar();
      });
      </script>
  <body>
      <h1 align="center"><a href="/secret/TheToybox">The Toybox</a></h1>
      <h2 align="center">Current active script is rock.js</h2>
      <h3 align="center"><input type="submit" value="Start Script">
      <hr>
<div class="scrollbar-macosx" width="100%" height="100%">
    <article>
      <h1 align="Center">Content of <?php echo SHOW_PATH ? '<em>' . $path . '</em>' : 'this directory'; ?></h1>
      <h1 align="center"><p> This is used for Script testing From here you can see all the scripts I've messed with</p></h1>
      <h5 align="center">Alot of my scripts require the console log</h5>
      <h1>
      <ol>
  <div align="left">
<?php
foreach ($entries as $entry => $is_dir) {
    $class_name = $is_dir ? 'directory' : 'file';
    $escaped_entry = htmlspecialchars($entry);
    printf('        <li class="%s"><a href="%s">%s</a></li>' . "\n",
        $class_name, $escaped_entry, $escaped_entry);
}
?>
      </ol>
  </div>
    </article>
</div>
  <footer>
    <h5>Scripts Made By Seth177</h5><br>
    <p>Scripts contain some tidbits from sources I've learned from</p>
  </footer>
    <!--<footer>
      <p>directory index script written by <a href="http://homework.nwsnet.de/">Jochen Kupperschmidt</a></p>
    </footer>-->

  </body>
</html>
