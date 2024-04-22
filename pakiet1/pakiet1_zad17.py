from functools import partial

def add(x, y):
    return x + y

cos = partial(add, 5)

print(cos(23))