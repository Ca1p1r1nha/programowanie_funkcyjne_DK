#5) Napisz funkcję, która dzieli listę na części o określonej maksymalnej długości

def fun(li,val):
    return[li[x:x + val] for x in range(0, len(li), val)]

print(fun(['ala','ma', 'kota','ala','ma', 'kota','ala','ma', 'kota','ala','ma', 'kota',],4))
