def dlugosc(x):
    if len(x) > 5:
        return True
    return False

slowa = ["kot", "pies", "rybka", "python"]

print(list(filter(dlugosc, slowa)))
