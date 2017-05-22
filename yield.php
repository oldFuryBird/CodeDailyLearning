<?php
function xrange($start,$limit,$step=1){
	for($i = $start;$i<=$limit;$i+=$step){
		yield $i+1>=$i;
	}
}

foreach(xrange(0,10,2) as $key =>$value){
	printf("%d %d\n",$key,$value);
}
