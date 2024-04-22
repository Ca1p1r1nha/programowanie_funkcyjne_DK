#10) Napisz funkcję, która generuje wszystkie permutacje elementów listy.

from itertools import permutations

def fun(li):
    return list(permutations(li))

print(fun([1,2,3,4,]))
