#2) Napisz funkcję, która przyjmuje string i zwraca nowy string,
# w którym wszystkie wielkie litery są zamienione na małe, a małe na wielkie.

def fun(st):
    wynik = ""
    for x in st:
        if x == x.lower():
            wynik = wynik + x.upper()
        elif x == x.upper():
            wynik = wynik + x.lower()

    return wynik

print(fun("aLa"))
