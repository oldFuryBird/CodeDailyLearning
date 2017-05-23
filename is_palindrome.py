'''回数'''
# -*- coding:utf-8 -*-
def is_palindrome(n):
    strnum = str(n)
    l = len(strnum)-1
    for i in range(l):
        if(strnum[i]!=strnum[l-i]):
            return False
    return True
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n
output = filter(is_palindrome,range(1,1000))
print(list(output))

