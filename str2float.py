# _*_ coding: utf-8 _*_
from functools import reduce
def str2float(s):
    tmp = s if '.' in s else s+'.'
    l=s.split('.')
    if s.find('.')==0 or len(l)>2:
        return s+" 字符不合规范"
    return reduce(lambda x,y:x+y/10**len(l[1]),map(int,l))

print(str2float('1233.452.26'))
print(str2float('345.678'))       # 345.678
print(str2float('0'))             # 0.0
print(str2float('345.678'))       # 345.678
print(str2float('0.0'))             # 0.0
print(str2float('123.456'))       # 123.456
print(str2float('123.45600'))     # 123.456
print(str2float('0.1234'))        # 0.1234
print(str2float('.1234'))         # 0.1234
print(str2float('120.0034'))      # 120.0034
print(str2float('.'))             # 0.0
