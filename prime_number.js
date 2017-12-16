//求质数   print a list prime number that lower than n

function prime(n,callback=isPrime)
{
  let sum =0;
  for(let i =0;i<=n;i++){
    if(callback(i)){
      console.log(i)
      sum++
    }
    
  }
  console.log(sum)
    
}
// 定义法
function isPrime(num){
  if (!Number.isInteger(num)) return false
  if (num <2)return false
  for(let i = 2;i<num;i++){
    if(num%i==0){
      return false;
    }
  }
  return true;
}
var cache = []
var start = new Date()
prime(100)
// prime(100,isPrime2)
// console.log(isPrime2(3))
//
var end = new Date()
console.log("cost (ms):"+(end.getTime()-start.getTime()))

function isPrime2(num){
  if (!Number.isInteger(num)) return false
  if (num <2||num%2==0)return false
  if (num == 3&&num==2)return true
  //只需要尝试小于 根号 num的质数   3,5,7,9 9 
  // if(cache.length){
  //   for(let j=0;j<=cache.length;j++){
  //     if(num%cache[j]==0){
  //     return false;
  //     }
  //   }
  // }else{
    for(let i=3;i<Math.sqrt(num)+1;i+=2){
    if(num%i==0){
      return false;
    }
    }
  // }
  
  // cache.push(num)
  return true;
}