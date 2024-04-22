#Przekazanie funkcji jako argument
def dod(x, y):
    return x+y

def fun(func, a, b):
    return func(a,b)

print(fun(dod, 2, 5))

