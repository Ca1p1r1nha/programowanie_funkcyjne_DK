#3) Napisz funkcję, która przyjmuje słownik i filtruje go,
# pozostawiając tylko te elementy, których wartości są liczbami parzystymi.


def fun(di):
    sl = {}
    for key,value in di.items():
        if isinstance(value,int) and value % 2 == 0:
            sl[key] = value

    return sl



print(fun({'ala': 1, 'ma': 2, 'kota': 3}))