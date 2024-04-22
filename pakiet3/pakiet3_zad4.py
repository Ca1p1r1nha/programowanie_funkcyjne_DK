#4) Zdefiniuj funkcję remove_duplicates, która usuwa zduplikowane elementy z listy, zachowując kolejność wystąpienia 
#pierwszego wystąpienia każdego elementu.

lista =[5,1,2,1,3,2,1,4,3,2,1,4,5]

def remove_duplicates(li):
    wynik = []
    for x in li:
        if x not in wynik:
            wynik.append(x)
    return wynik

print(remove_duplicates(lista))
