#7) Napisz funkcję flatten_list, która spłaszcza zagnieżdżone listy do pojedynczej listy.

def flatten_list(li):
    wynik = []
    for x in li:
        for y in x:
            wynik.append(y)

    return wynik

print(flatten_list([[0,1,2,3,4],[5,6,7,8,9],[11,12,13]]))
