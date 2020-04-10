#!/usr/bin/env php
<?php
define("CLI_SCRIPT", 1);
die("This script is not complete.  When it is it will give you the path to a file when given the moodle url\n");

// $moodle_dir = $_ENV['WILD_MOODLE_DIR'];
// include $moodle_dir . "/config.php";
// $conn = mysqli($CFG->dbhost, $CFG->dbuser, $CFG->dbpass, $CFG->dbname);
list($contextid, $component, $filearea, $theme, $filename) = explode('/', $argv[1]);
list($filename) = explode('?', $filename);
print("Contextid: $contextid\nComponent: $component\nFilearea: $filearea\nTheme: $theme\nFilename: $filename\n");
$stmt = $conn->prepare("SELECT * FROM " . $CFG->prefix . "files WHERE component=? and filearea=? and contextid=?");
$stmt->bind_param("sss", $component, $filearea, $contextid);
$stmt->execute();


