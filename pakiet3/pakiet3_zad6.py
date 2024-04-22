#6) Zaimplementuj funkcję map_nested, która stosuje funkcję do każdego elementu zagnieżdżonej listy.

def map_nested(li):

    wynik = []
    for x in li:
        for y in x:
            wynik.append(y*2)

    return wynik


print(map_nested([[1,2,3,4],[5,6,7,8]]))