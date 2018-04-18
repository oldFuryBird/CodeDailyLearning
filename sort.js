// 快速排序
var arr = [ 6,4,2,7,8,1,9,10];

qsort(arr)
console.log(arr)
console.log(bsearch(arr,9))
function qsort(arr){
   quick_sort(arr,0,arr.length-1)
}
function quick_sort(arr,left,right){
  let index;
  if(arr.length>0){
      index = partition(arr,left,right);
    if(left < index-1){
      quick_sort(arr,left,index-1);
    }
    if(right>index){
      quick_sort(arr,index,right);
    }
  }

}
function partition(arr,left,right){
  let pivot = arr[Math.floor((left+right)/2)];
  let i=left;
  let j=right;
  while (i<=j) {
    while (arr[i]<pivot) {//比基准小就移动
      i++;
    }
    while (arr[j]>pivot) {//比基准大就移动
      j--;
    }
    if(i<=j){
      let temp = arr[i];
      arr[i]=arr[j]
      arr[j]=temp;
      i++;
      j--;
    }

  }
  return i;
}


function bsearch(arr,item)
{
  let low=0;
  let high = arr.length-1;
  let mid;
  while(low<=high){
    mid =Math.floor((low+high)/2);
    if(arr[mid]>item){
      high =mid-1;
    }else if (arr[mid]<item) {
      low = mid +1;
    }else{
      return mid;
    }

  }
  return -1;
}
