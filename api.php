<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "dbname";
//header('Content-Type: text/html;charset=utf-8');
//header('Access-Control-Allow-Origin:*'); // *代表允许任何网址请求
//header('Access-Control-Allow-Methods:POST,GET,OPTIONS,DELETE'); // 允许请求的类型
//header('Access-Control-Allow-Credentials: true'); // 设置是否允许发送 cookies
//header('Access-Control-Allow-Headers: Content-Type,Content-Length,Accept-Encoding,X-Requested-with, Origin'); // 设置允许自定义请求头的字段

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
$img_info = $result->fetch_assoc()['filepath'];
$img_path = '网站域名'.$img_info;
echo $img_path;
$conn->close();
?>
