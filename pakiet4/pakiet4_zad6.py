#6) Napisz funkcję, która przyjmuje listę i funkcję, a następnie zwraca nową listę,
# gdzie każdy element jest wynikiem zastosowania funkcji do dotychczasowych elementów.

def fun(li, func):
    return [func(x) for x in li]

print(fun([1,2,3,4,5,6,7,8,9], lambda x: x**2))