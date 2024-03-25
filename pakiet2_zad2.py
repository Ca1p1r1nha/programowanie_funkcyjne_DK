import itertools
li = [1,2,3,4,5]

for i in itertools.product(li,li):
    print(i)