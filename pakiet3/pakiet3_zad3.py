#3) Napisz funkcję recursive_sum, która przyjmuje listę liczb zagnieżdżonych i oblicza sumę wszystkich liczb, 
#uwzględniając zagnieżdżone listy.
lista = [[1,2,3],[4,5,6],[7,8,9]]

def recursive_sum(li):
    wynik = 0
    for x in li:
        for y in x:
            wynik = wynik + y

    return wynik

print(recursive_sum(lista))