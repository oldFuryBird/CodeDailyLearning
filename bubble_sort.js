var arr = [ 6,4,2,7,8,1,9,10];
isort(arr)
// ssort(arr)
// bbsort(arr)
console.log(arr)
function bbsort(arr){

    for (let i = 0; i < arr.length; i++) {
      for (let j = i; j < arr.length; j++) {
          if(arr[j]<arr[i]&&j!=i){
            let tmp = arr[j];
            arr[j]=arr[i];
            arr[i]=tmp;
          }
      }
    }
}

//选择排序
function ssort(arr){
  for (let i = 0; i < arr.length; i++) {
    let minIndex =i;
    for (let j = i; j < arr.length; j++) {
        if (arr[j]<arr[minIndex]) {
            minIndex=j
        }
    }
    if(minIndex!==i){
      let tmp = arr[i];
      arr[i]=arr[minIndex];
      arr[minIndex]=tmp;
    }
  }
}

// 插入排序
function isort(arr)
{
  for (let i = 1; i < arr.length; i++) {
    let tmp = arr[i];
    let j = i;
    while (j>0 && arr[j-1]>tmp) {
        arr[j]=arr[j-1]
        j--
    }
    arr[j]=tmp
  }
}
