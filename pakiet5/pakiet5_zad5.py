#Napisać funkcję, która przyjmuje listę liczb i zwraca listę zawierającą tylko te liczby, które są parzyste.
#Użyj wyrażenia lambda do stworzenia funkcji, która oblicza pole prostokąta na podstawie długości jego boków.

parzyste = lambda lista: [x for x in lista if x % 2 == 0]

pole = lambda a, b: a * b

print(parzyste([1, 2, 3, 4, 5, 6]))
print(pole(70, 6))