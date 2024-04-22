#9) Napisz funkcję zip_with_index, która łączy elementy listy z ich indeksami.

def zip_with_index(li):
    ex = []
    for x in range(len(li)):
        ex.append(x)

    wynik = {ex[i]: li[i] for i in range(len(li))}

    return wynik

print(zip_with_index([9,8,7,6,5,4,3,2,1,9,6]))

