#Napisz funkcję split_list, która dzieli listę na podlisty o zadanej długości.

def split_list(li,zak):
    l1 = [x for x in li if x <= zak]
    l2 = [y for y in li if y > zak]

    return l1, l2


print(split_list([1,2,3,4,5,6,7,8,9,5,6,7,8,8], 5))