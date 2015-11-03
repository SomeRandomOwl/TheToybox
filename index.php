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
define('SHOW_PARENT_LINK', FALSE);
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
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Stuff">
    <meta name="author" content="seth177">
    <title>Testing</title>
    <link rel="stylesheet" type="text/css" href="./assets/main.css">
    <link href="./assets/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="./assets/cover.css" rel="stylesheet">
    <script src="./JavaScript/Games/rock.js"></script>
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <style type="text/css">
    li.directory a:before {
    content: '[ ';
    }
    li.directory a:after {
    content: ' ]';
    }
    </style>
    <div class="site-wrapper">
      <div class="site-wrapper-inner">
        <div class="cover-container">
          <div id="color">
            <div class="masthead clearfix" id="head">
              <div class="inner">
                <h3 class="masthead-brand">Seth177's Random place</h3>
              </div>
              <hr color="#004466">
            </div>
          </div>
        </div>
          <div align="center">
              <h1>Current Active Script: Rock.js</h1>
              <a type="submit" value="Start Script" class="btn btn-lg btn-default">Start Script</a>
          </div>
        <div class="scrollbar-macosx" width="100%" height="100%">
          <article>
          <hr>
            <h1 align="Center">Content of <?php echo SHOW_PATH ? '<em>' . $path . '</em>' : 'this directory'; ?></h1>
            <h1 align="center"><p> This is used for Script testing From here you can see all the scripts I've messed with</p></h1>
            <h5 align="center">Alot of my scripts require the console log</h5>
            <h1>
            <ul>
              <div align="left">
                <?php
                foreach ($entries as $entry => $is_dir) {
                $class_name = $is_dir ? 'directory' : 'file';
                $escaped_entry = htmlspecialchars($entry);
                printf('        <li class="%s"><a href="%s">%s</a></li>' . "\n",
                $class_name, $escaped_entry, $escaped_entry);
                }
                ?>
              </ul>
            </article>
          </div>
          <div>
            <div>
              <hr>
              <p>Made by <a href="http://steamcommunity.com/id/Seth177/" id="steam">seth177</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script>
    $(function() {
    $( "a[type=submit]" )
    .button()
    .click(function( event ) {
    start();
    });
    });
    </script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  </body>
</html>
