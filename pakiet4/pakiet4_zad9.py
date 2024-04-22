#9) Napisz funkcję, 
#która przyjmuje listę krotek i zwraca listę, 
#w której każdy element jest wynikiem zastosowania funkcji do elementów krotek.

def fun(li, func):
    return [func(*kro) for kro in li]

print(fun([(1,2),(3,4)], lambda x, y: x * y))