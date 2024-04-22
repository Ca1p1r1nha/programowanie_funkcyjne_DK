#Napisać dwie funkcje: jedna, która podnosi liczbę do kwadratu, a druga, która dodaje do liczby 5.
#Stwórz funkcję, która łączy funkcje, aby zastosować obie funkcje do listy liczb.
#Następnie aplikuj wszystkie funkcje do tej wartości.


def kwadrat(x):
    return x ** 2

def dodaj(x):
    return x + 5

def fun(y):
    return list(map(lambda x: dodaj(kwadrat(x)), y))

y = [1, 2, 3, 4, 5, 7, 8, 9]
print(fun(y))