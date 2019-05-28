<?php
header('Content-Type: text/html; charset=UTF-8');
?>

<table border="1">
    <tr>
        <th>Sun</th>
        <th>Mon</th>
        <th>Tue</th>
        <th>Wed</th>
        <th>Thu</th>
        <th>Fri</th>
        <th>Sat</th>
    </tr>
<?php

$first_day = mktime(0,0,0,6,1,2019);
$end_day=30;

for( $j=1; $j <= $end_day; $j++ ) {
  if($j === 1) {
    echo '<tr>';
    $weekday = date("w", $first_day);

		for( $k=0; $k<$weekday; $k++ ) {
      echo '<td></td>';
		}
	}

  if($weekday ==0){
    echo '<td bgcolor ="blue">'.$j.'</td>';
  }
  elseif($weekday ==6){
    echo '<td bgcolor ="red">'.$j.'</td>';
  }
  else{
    echo '<td >'.$j.'</td>';
  }

  $weekday++;
  if($weekday >6) {
		echo '</tr><tr>';
    $weekday = 0;
	}
}

?>
</table >
