<?php
header('Content-Type: text/html; charset=UTF-8');

$subject = array("田中", "山田", "中村", "鈴木", "木村", "山本", "高橋", "佐々木");
$test_a = array(45, 98, 34, 56, 67, 88, 76, 70);
$test_b = array(65, 74, 50, 55, 55, 70, 67, 52);

$a_ave = array_sum($test_a)/count($test_a);
$b_ave = array_sum($test_b)/count($test_b);

echo 'Average Score of testA : ', $a_ave, '<br>';
echo 'Average Score of testB : ', $b_ave, '<br><br>';

$good_score=array();

for ($i=0; $i < count($subject); $i++){
  if ($test_a[$i] >= $a_ave && $test_b[$i] >= $b_ave){
    array_push($good_score, $subject[$i]);
  }
}

echo 'Good scores students : <br>';
for ($i=0; $i < count($good_score); $i++){
  echo $good_score[$i], '<br>';
}
?>
