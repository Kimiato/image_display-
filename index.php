<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>随机二刺猿图片</title>
		<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
	</head>
	<body>
		<h2 style="text-align:center;">刷新(点击图片)就会出现一张随机的图片❤
		</h2>
		<?php
			$servername = "localhost";
			$username = "username";
			$password = "password";
			$dbname = "dbname";
			 
			// 创建连接
			$conn = new mysqli($servername, $username, $password, $dbname);
			// Check connection
			if ($conn->connect_error) {
			    die("连接失败: " . $conn->connect_error);
			} 
			$sql = "SELECT * FROM image_info";
			$result = mysqli_query($conn, $sql);
			$random_id = mt_rand(0, $result->num_rows);
			//echo $random_id;
			$sql = "SELECT * FROM image_info where id = {$random_id}";
			$result = $conn->query($sql);
			$img_info = $result->fetch_assoc()['filename'];
			//echo $img_info;
			echo '<img style="cursor:pointer" alt="'.$img_info.'" src="图片文件夹地址'.$img_info.'" onclick="location.reload();" />';
			$conn->close();
		?>
	</body>
</html>
