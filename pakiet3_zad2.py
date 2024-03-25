#2) Zaimplementuj funkcję filter_long_words, która przyjmuje listę stringów i zwraca listę zawierającą tylko te stringi, 
#których długość jest większa niż średnia długość wszystkich stringów w liście.

def ilter_long_words(li):
    dlugosc = len(li)
    ilosc = 0
    slowa = []
    for x in li:
        ilosc = ilosc + len(x)
    
    srednia = ilosc / dlugosc
    for y in li:
        if len(y) > srednia:
            slowa.append(y)
    return slowa




print(ilter_long_words(['ala', 'kot','pies']))