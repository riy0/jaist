<?php

$name = $_POST["name"];
$sex = $_POST["sex"];
$season = $_POST["season"];
$reason = $_POST["reason"];
$name_err ="";

$input_array=array($name, $sex, $season, $reason);

$file= fopen("text.csv", "a");
fputcsv($file,$input_array);
fclose($file);

?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>アンケート</title>
</head>
<body>

  <h1>投稿が完了しました</h1>

  <p>ありがとうございます</p>
  <a href="./results.php">集計結果</a>
  <p><input type="button" onclick='history.back()' value="戻る"></p>

</body>
</html>
