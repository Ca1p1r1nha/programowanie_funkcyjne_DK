def add(x, y):
    return x+y

def fun1(x):
    def fun2(y):
        return add(x, y)
    return fun2

print(fun1(2)(3))
