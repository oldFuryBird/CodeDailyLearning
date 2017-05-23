'''闭包'''
def count():
    fs =[]
    def f(j):
        def g():
            return j*j
        return g
    for n in range(1,4):
        fs.append(f(n))
    return fs
f1,f2,f3 = count()
print(f1())

print(f2())
print(f3())
