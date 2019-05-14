表单页a.php：
<form action="b.php" method="get">
<input name="content" type="text" />
<label>
<input type="submit" name="Submit" value="提交">
</label>
</form>

写入页 b.php：
<?
$str=$_GET[content];
echo $str."<br>";
$fp=fopen("b.txt","w");
fwrite($fp,$str);//写入
fclose($fp);
readfile("b.txt");//读取
?>