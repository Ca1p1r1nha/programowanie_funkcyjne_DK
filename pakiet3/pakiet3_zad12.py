#12) Zdefiniuj funkcję rotate_list, która obraca listę o zadaną liczbę kroków w prawo.

def rotate_list(li,kro):
    l1 = li[-kro:] + li[:-kro]
    return l1

print(rotate_list([1,2,3,4,5,6,7,8,9], 4))