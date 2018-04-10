<?php

# 遍历全部文件  
# is_dir 是否目录
#  opendir ,打开目录
# readdir 读取目录

function scanFiles($path)
{
  $files = [];
  $queue = [$path];
  while($data = array_pop($queue)){
    $dir = $data;
    if(is_dir($dir) && $handle=opendir($dir)){
        while (false!==($file=readdir($handle))) {
          if($file!='.' && $file!='..'){
            $str = $dir.'/'.$file;
            $files[]=$str;
            if (is_dir($str)) {
              yield $str .'     d';
              $queue[]=$str;
            }else{
              
            yield $str.'     f';;
            }
        }

    }
    
  }
  @closedir($handle); 
  }
}
$a = scanFiles('.');

while($a->valid()){
  echo $a->current().PHP_EOL;
  $a->next();
}
