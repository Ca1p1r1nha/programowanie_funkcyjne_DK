#Użyj funkcji reduce() z modułu functools, aby znaleźć największą liczbę w liście.
#Napisać funkcję używając reduce(), która oblicza średnią z listy liczb.


from functools import reduce

liczby = [3, 7, 2, 8, 5]
duza_liczba = reduce(lambda x, y: x if x > y else y, liczby)

def srednia(cyfry):
    return reduce(lambda x, y: x + y, cyfry) / len(cyfry) if cyfry else 0

print(duza_liczba, srednia(liczby))