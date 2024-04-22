#8) Zdefiniuj funkcję partition_list, która dzieli listę na dwie części: jedną zawierającą elementy spełniające warunek,
#a drugą zawierającą pozostałe elementy.
def partition_list(li,war):
    l1 = [x for x in li if x <= war]
    l2 = [y for y in li if y > war]

    return l1, l2


print(partition_list([1,2,3,4,5,6,7,8,9,5,6,7,8,8], 5))
