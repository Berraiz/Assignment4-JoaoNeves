<?php
$x = escapeshellarg($_POST['a']);
$y = escapeshellarg($_POST['b']);
$z = escapeshellarg($_POST['c']);

$command = escapeshellcmd("python3 process_input.py $a $b $c");
$output = shell_exec($command);

echo "<h2>Assignment 4:</h2>";
echo "<div>$output</div>";
?>