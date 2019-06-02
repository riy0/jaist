<!DOCTYPE HTML>
<html>

<head>
	<title>1910204's Portfolio</title>
	<meta charset="utf-8"/>
	<link rel="stylesheet" href="components/css/main.css"/>
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
			<div class="col-sm-1"> </div>

			<!-- main -->
			<div class="col-sm-10">
				<h3 class="topic">島根のよいとこ</h3>
				<hr/>
				<!-- Media -->
				<div class="media">
					<a class="media-left"> <img class="media-object share" src="components/css/images/wedding.jpg"></a>
					<div class="media-body">
						<h4 class="media-heading">縁結び</h4><br>
						<p>近年の島根県では観光客が増えています。<br><br>
							 これも出雲大社のおかげですね。<br>
							 その他にも縁結びでご利益があるとされています八重垣神社｡<br>
							 美容では、玉造温泉を中心に多くの若い女性が訪れています。<br><br>
							 JAISTで疲れたみなさま、縁を結びたい人はリンクをクリック<br><br>

							 Website : <a href="https://www.kankou-shimane.com/"> しまね観光ナビ</a>
						</p>
					</div>
				</div>
				<hr/>
				<div class="media">
					<div class="media-body" style="margin-left:50px">
						<h4 class="media-heading">旅に出よう。</h4><br>
						<p style="margin-left:30px">
							ということで、とにかく！<br><br>
							おでかけしましょう！ <br><br>
							素敵な写真をシェアしてください！<br>
							<h5 style="margin:60px">instagram <i class="fa fa-angle-double-right fa-2x"></i>
							<a href="https://www.instagram.com/sntka.20/?hl=ja">
								<i class="fab fa-instagram fa-3x"></i></a></h5>
						</p>
					</div>
					<a class="media-right"> <img class="media-object share" src="components/css/images/trip.jpg"> </a>
				</div>
				<hr>
				<hr>



		 		<div class="panel panel-default" style="margin-left:5em">
					<h4 class="panel-heading">Post your Favorite Place /
					 	おすすめの場所を教えてください</h4>
			 		<div class="panel-body">
				 	<form class="form-horizontal" method="POST" action="confirmation.php">
					 	<div class="form-group">
						 <label class="col-sm-2 control-label">Name</label>
						 <div class="col-sm-3">
							 <input class="form-control" type="text" name="name" required>
						 </div>
					 </div>

					 <div class="form-group">
						 <label class="col-sm-2 control-label">Favorite Country</label>
						 <div class="col-sm-10">
							 <select class="form-control" name="area">
								 <option value="japan">Japan</option>
								 <option value="europe">Europe</option>
								 <option value="asia">Asia</option>
							 </select>
						 </div>
					 </div>

					 <div class="form-group">
						 <label class="col-sm-2 control-label">Place</label>
						 <div class="col-sm-10">
							 <input class="form-control" type="text" name="place" required>
						 </div>
					 </div>

					 <div class="form-group">
						 <label class="col-sm-2 control-label">Reason</label>
						 <div class="col-sm-10">
							 <input class="form-control" type="text" name="reason" r ="2" required>
						 </div>
					 </div>

					 <!--
					 <div class="form-group">
						 <label class="col-sm-2 control-label">photo</label>
						 <div class="col-sm-10">
							 <span>
							 		<input type="file" name="photo" enctype="multipart/form-data">
							 </span>
						 </div>
					 </div>
				 -->

					 <div class="form-group">
						 <div class="col-sm-offset-2 col-sm-10">
							 <button class="btn btn-primary">送信</button>
						 </div>
					 </div>
				 </form>
			 </div>
		 </div>
	 </div>
			</div>
			</div>

			<div class="col-sm-1"></div>

		</div>
	</div>

	<!-- Footer -->
	<footer class="page-footer font-small blue pt-4">
		<hr />
		<div class="footer-copyright text-center py-3">Contact :
			<a href="https://mdbootstrap.com/education/bootstrap/"> s1910204@jaist.ac.jp</a>
		</div>

	</footer>
	<!-- Footer -->

</body>
</html>
