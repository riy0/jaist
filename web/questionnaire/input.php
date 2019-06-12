<?php
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>アンケート</title>
</head>
<body>

  <h1>アンケートにご回答ください</h1>

  <form action="complete.php" method="post">

  <p> お名前</p>
  <input type="text" name="name" size="20" maxlength="30" required>


  <p> 性別</p>
  男<input type="radio" name="sex" value="man" checked>
  女<input type="radio" name="sex" value="woman">


  <p> 好きな季節</p>
  <select name="season">
  <option value="春">春</option>
  <option value="夏">夏</option>
  <option value="秋">秋</option>
  <option value="冬">冬</option>
  </select>

  <p>理由</p>
  <textarea name="reason" cols="40" rows="3" maxlength="100" required></textarea>

  <p><input type="submit" name="go" value=" 送信 "></p>

  </form>

</body>
</html>
