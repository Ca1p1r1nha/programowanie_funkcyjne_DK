def fun():
    x = 0
    y = 1
    while True:
        yield x
        x, y = y, x + y

wynik = fun()
for x in range(10):
    print(next(wynik))