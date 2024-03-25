import itertools

li = []
for x in range(1,31):
    li.append(x)
li2 = []

def fun(n):
    return n % 2 ==0

groups = itertools.groupby(li, key = fun)

cos = [list(g) for k,g in groups]

print(groups)

