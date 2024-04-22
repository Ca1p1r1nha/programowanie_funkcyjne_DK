#Korzystając z funkcji filter(), wyodrębnić z danej listy słów te, które zaczynają się na literę 'a'.
#Użyj funkcji map() do przekształcenia listy liczb w listę ich kwadratów.

wynik1 = list(filter(lambda slowo: slowo.startswith('a'),["ala", "ma", "kota"]))

wynik2 = list(map(lambda x: x ** 2, [1,2,3,4,5,6,7,8,9]))

print(wynik1,wynik2)