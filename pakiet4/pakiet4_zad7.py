#7) Napisz funkcję, która łączy dowolną liczbę słowników w 
#jeden słownik, gdzie wartości dla powtarzających się kluczy są sumowane.

def fun(*dicts):
    wynik = {}
    for d in dicts:
        for key, value in d.items():
            wynik[key] = wynik.get(key, 0) + value
    return wynik

print(fun({"a":1, 'b':2},{"c":61, 'd':5}))