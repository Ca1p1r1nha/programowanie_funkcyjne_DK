def compose(x,y):
    return lambda a: x(y(a))

def fun1(a):
    return a*4

def fun2(a):
    return a/6

oba = compose(fun1, fun2)
print(oba(7))