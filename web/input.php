<?php

$x = "<p>本文</p>"

?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>アンケート</title>
</head>
<body>
  
  <h1>アンケートにご回答ください</h1>
  <p> お名前</p>
  <p> 性別</p>
  <p> 好きなスポーツ</p>
  <select name="example">
  <option value="サンプル1">サンプル1</option>
  <option value="サンプル2">サンプル2</option>
  <option value="サンプル3">サンプル3</option>
  </select>



  <?php print $x;?>

</body>
</html>
