<?php

$file=fopen("./content.csv", "r");

if($file){
  $name=array();
  $area=array();
  $place=array();
  $reason=array();

  while($line = fgetcsv($file)){
    array_push($name, $line[0]);
    array_push($area, $line[1]);
    array_push($place, $line[2]);
    array_push($reason, $line[3]);
  }
}
fclose($file);
?>

<!DOCTYPE HTML>
<html>
<head>
  <title>1910204's Portfolio</title>
  <meta charset="utf-8" />
  <link rel="stylesheet" href="components/css/main.css" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Lato:400,700|Noto+Sans+JP:400,700" rel="stylesheet">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  <script defer src="https://use.fontawesome.com/releases/v5.8.2/js/all.js" integrity="sha384-DJ25uNYET2XCl5ZF++U8eNxPWqcKohUUBUpKGlNLMchM7q4Wjg2CUpjHLaL8yYPH" crossorigin="anonymous"></script>
</head>

<body>
  <nav class="navbar navbar-expand-lg bg-dark navbar-dark p-2">
    <a class="navbar-brand" href="#"></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="collapsibleNavbar">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="./final.php"><i class="fa fa-home fa-2x space"></i></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="./work.php"><i class="fa fa-bus fa-2x space"></i></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="./ted.html"><i class="fa fa-folder fa-2x space"></i></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="./sharetravel.php">
            <i class="fas fa-camera-retro fa-2x space"></i></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://www.instagram.com/sntka.20/?hl=ja">
            <i class="fab fa-instagram fa-2x space"></i></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/riy0">
            <i class="fab fa-github fa-2x space"></i></a>
        </li>
      </ul>
    </div>
  </nav>

  <div class="container" style="margin-top:40px">
    <div class="row">
      <!-- left zoon-->
      <div class="col-sm-1">
      </div>

      <!-- main -->
      <div class="col-sm-10">
        <h4 class="media-heading topic"> みんなのおすすめの場所</h4>
        <div class="media">
					<div class="media-body"><hr/>
            <?php for ($i =count($name)-1; $i > 0 ; $i--): ?>
              <div class="well">
                <ul class="list-group">
                  <li class="list-group-item">
                    <?php echo $name[$i]?>さんのおすすめの場所：
                    <?php echo $area[$i]." / ".$place[$i] ?>
                  </li>

                  <li class="list-group-item">良いところ：<?php echo $reason[$i] ?> </li>
                </ul>
              </div>
            <?php endfor;?>
          </div>
        </div>
      </div>

      <div class="col-sm-1"></div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="page-footer font-small blue pt-4">
    <hr />
    <div class="footer-copyright text-center py-3">
      Contact :s1910204@jaist.ac.jp
    </div>
  </footer>

</body>
</html>
