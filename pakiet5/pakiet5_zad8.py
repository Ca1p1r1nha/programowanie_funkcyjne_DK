#Stwórz listę zawierającą pierwsze 10 liczb kwadratowych (1, 4, 9, ...) używając list comprehensions.
#Użyj list comprehensions, aby z danej listy słów stworzyć listę długości tych słów.


kwadraty = [x ** 2 for x in range(1, 11)]

slowa = ["ala","ma","kota"]
dl = [len(x) for x in slowa]

print(kwadraty, dl)