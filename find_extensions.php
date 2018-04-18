<?php
$path = 'aa/bb/cc/dd.php';
$email = "cc-wc1@163.com";
var_dump(strrchr($path,'.'));
preg_match('/^[\w-]+@[\w-]+(\.[\w\-]+)+$/',$email,$matchs);
var_dump($matchs);
// getExt1($path);
// function getExt1($path){
//   $pattern = '/.*\.(\w+)$/';
//  preg_match($pattern,$path,$out);
//   var_dump($out);
//
// }

 ?>
