<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['a']) && isset($_POST['b']) && isset($_POST['c'])) {
        $a = escapeshellarg($_POST['a']);
        $b = escapeshellarg($_POST['b']);
        $c = escapeshellarg($_POST['c']);

        $command = "python3 calculate.py $a $b $c";
        $output = shell_exec($command);

        echo "<h2>Calculation Result</h2>";
        echo $output;
    } else {
        echo "<h3>Error: Missing input values.</h3>";
    }
}
?>
