//插入排序

var arr = [3,2,4,2,5,9,8];

function isort(arr)
{
  let len = arr.length;
  let j,temp;

  for(let i=1;i<len;i++){

      temp = arr[i];// 把当前值保存临时变量
      j=i;
      while(j>0 && arr[j-1]<temp)
      {
        arr[j] = arr[j-1]; //讲比我大的值插入到我的位置
        j--;
      }
      arr[j]=temp;
  }
  return arr;
}
console.log(isort(arr))