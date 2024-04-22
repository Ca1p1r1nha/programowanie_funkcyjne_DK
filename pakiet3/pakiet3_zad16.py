#16) Zdefiniuj funkcję remove_whitespace, która usuwa białe znaki z każdego elementu listy stringów

def remove_whitespace(li):
    wynik = []
    slowo = ""
    for x in li:
        slowo = x.replace(" ", "")
        wynik.append(slowo)
    return wynik

print(remove_whitespace(['te st', 'cz y', 'dzia ła']))