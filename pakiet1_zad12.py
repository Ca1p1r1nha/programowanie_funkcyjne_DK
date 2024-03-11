from functools import partial

def mul(x, y):
    return x * y

cos = partial(mul, 3)

print(cos(19))
