<?php
include('config.php');
// 创建连接
$conn = new mysqli($host, $user, $password, $dbname);
// Check connection
if ($conn->connect_error) {
die("连接失败: " . $conn->connect_error);
}
$sql = "SELECT * FROM view_statistics where id = 1";
$result = mysqli_query($conn, $sql);
$view_count = $result-> fetch_object()-> view_count;
echo "当前服务已调用{$view_count}";
?>