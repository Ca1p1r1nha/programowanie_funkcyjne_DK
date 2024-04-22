#8) Napisz funkcję, która zwraca najczęściej występujący element w liście. W przypadku remisu zwróć jeden z nich.
from collections import Counter

def fun(li):
    return Counter(li).most_common(1)[0][0]

print(fun([1,2,3,4,5,6,7,8,2]))