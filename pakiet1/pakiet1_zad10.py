def fun():
    num = 0
    while True:
        yield num
        num += 2

wynik = fun()
while True:
    print(next(wynik))

