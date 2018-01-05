
def Count1(num):
  n = 0
  while num!=0:
    if num%10==1:
      n +=1
    # print(num)
    num = int(num/10)
  return n
def Count1str(num):
   return str(num).count("1")
# def f(n):
#   icnt = 0
#   for i in range(1,n):
#     # icnt+=Count1(i)
#     icnt+=Count1str(i)
#   return icnt  

def f(n):
  '''
  f(n)= 每个位上统计的1的数相加
  f(123) = 百位(100-123) 24 + 十位（10-19,110-119） 20 + 个位(1,11,21,31,41....121)
  12+1=13
  总共  57
  f(n)  位数 = len(str(n))
  从个位开始一直到最后一位， 每位上面出现1的数可以归纳为

  n       个     十  ...     result
  13 --->1+1=2 + 3
  23 --->1+2=3 + 10
  33 --->1+3=4 + 10
  ...
  123--->1+12    2*10 23+1    57
  223--->1+22    3*10 100     153
  ...
  1223-->1+122  13*10 2*100  223+1  =  677
  2223-->1+222  23*10 3*100  1000   = 1753

  最大的f(N)=N
数学归纳法证明 证明 条件f(n)=n的数存在一个上界
  '''
  higher = 0
  icurrent = 0
  factor = 1
  count = 0
  low = 0
  while int(n/factor) !=0:
    icurrent= int(n/factor)%10
    higher = int(n/(factor*10))
    lower  = n - int(n/factor)*factor;
    if icurrent == 0:
      count +=higher*factor
    elif icurrent == 1:
      count+=higher*factor+1+lower
    else:
      count+=(higher+1)*factor
    factor *=10
  return count



if __name__=="__main__":
  num1 = 13
  num2 = 33
  num3 =2
  print(f(13))
  print(f(223))
  # print(f(num2))
  # print(f(num3))
  # print(f(30000000000000))