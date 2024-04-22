#1) Napisz funkcję double_list_elements, która przyjmuje listę liczb i zwraca nową listę, w której każdy element 
#jest podwójny w stosunku do odpowiadającego elementu w pierwotnej liście.


def double_list_elements(li):
    wynik=[]
    for x in li:
        wynik.append(x)
        wynik.append(x)
    return wynik

print(double_list_elements([1,2,3,4]))
