def foo(s):
    n=int(s)
    assert n!=0 ,'n is zero!'
    return 10/n
if __name__=='__main__':
    foo('0')
