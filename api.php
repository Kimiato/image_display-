<?php
$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "dbname";
header('Content-Type: text/html;charset=utf-8');
header('Access-Control-Allow-Origin:*'); // *代表允许任何网址请求
header('Access-Control-Allow-Methods:POST,GET,OPTIONS,DELETE'); // 允许请求的类型
header('Access-Control-Allow-Credentials: true'); // 设置是否允许发送 cookies
header('Access-Control-Allow-Headers: Content-Type,Content-Length,Accept-Encoding,X-Requested-with, Origin'); // 设置允许自定义请求头的字段

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
$img_path = $img_info;
echo $img_path;
//访客统计
$sql = "SELECT count(*) from view_statistics";
$result = $conn->query($sql)->fetch_assoc()['count(*)'];
if ($result) {
    $sql = "SELECT view_count FROM view_statistics WHERE id=1";
    $view_count = $conn->query($sql)->fetch_assoc()['view_count'];
    $view_count += 1;
    $sql = "UPDATE view_statistics SET view_count={$view_count} WHERE id=1";
    $conn->query($sql);
}
else {
    $sql = "INSERT INTO view_statistics (view_count) VALUES (1)";
    $conn->query($sql);
}
$conn->close();
?>
