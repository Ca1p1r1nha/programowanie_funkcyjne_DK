#11) Napisz funkcję find_max_min_diff, która znajduje różnicę między maksymalną a minimalną wartością w liście.

def find_max_min_diff(li):
    low = min(li)
    up = max(li)
    dif = up - low
    return dif

print(find_max_min_diff([1,2,3,4,5,6,7,8,9]))