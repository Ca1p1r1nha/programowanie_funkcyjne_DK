#5) Napisz funkcję generate_fibonacci, która zwraca generator ciągu liczb Fibonacciego.

def fun():
    x = 0
    y = 1
    while True:
        yield x
        x, y = y, x + y

wynik = fun()
while True:
    print(next(wynik))

