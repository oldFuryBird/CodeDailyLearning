'''奇数生成器'''
def _odd_iter():
    n=1
    while True:
        n =n+2
        yield n
'''筛选器'''
def _not_divisiable(n):
    return lambda x: x%n>0
''' _not_divisiable 返回的是一个函数'''
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n= next(it)
        yield n
        it = filter(_not_divisiable(n),it)
''' _not_divisiable(n) 相当于 def(x):
                                return x%n>0
        iter 是所有奇数的集合
        每次迭代过滤能被上一个整除的数
        返回3，第一次过滤生成器所有能被3整除的
        返回5，第二次过滤生成器所有能被5整除的
        
        
                                '''

for  n in primes():
    if n <=1103:
        print(n)
    else:
        break




