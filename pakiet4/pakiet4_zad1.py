#1) Napisz funkcję, która przyjmuje listę liczb całkowitych i zwraca sumę wszystkich parzystych liczb w tej liście.

def fun(li):
    wynik = 0
    for x in li:
        if x % 2 == 0:
            wynik = wynik + x
    return wynik

print(fun([1,2,3,4,5,6,7,8,9,10]))

