def fun():
    num = 0
    while True:
        yield num
        num += 2

wynik = fun()
for x in range(10):
    print(next(wynik))