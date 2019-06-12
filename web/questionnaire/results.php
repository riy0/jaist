<?php

$file=fopen("./text.csv", "r");

$name=array();
$sex=array();
$season=array();
$reason=array();

if($file){
  while($line = fgetcsv($file)){
    array_push($name, $line[0]);
    array_push($sex, $line[1]);
    array_push($season, $line[2]);
    array_push($reason, $line[3]);
  }
}
fclose($file);
?>


<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>アンケート</title>
</head>
<body>

  <h1>アンケート結果</h1>
  <table border="1">
    <tr>
      <td>名前 </td>
      <td>性別 </td>
      <td>好きな季節 </td>
      <td>理由 </td>
    </tr>
    <tr>
      <?php
      $cnt= 0;
      for($i=0; $i <count($name); $i++){
        echo '<td>'.$name[$i].'</td>';
        if ($sex[$i] == 'man'){
          $cnt++;
          echo '<td>男</td>';
        }
        else{ echo '<td>女</td>';}
        echo '<td>'.$season[$i].'</td>';;
        echo '<td>'.$reason[$i].'</td>';
        echo'</tr><tr>';

      }
      echo "回答数：". $i."（男性：".$cnt. "，女性：".($i - $cnt)."）";
      ?>
    </tr>
  </table>

  <p><input type="button" onclick='history.back()' value="戻る"></p>

</body>
</html>
