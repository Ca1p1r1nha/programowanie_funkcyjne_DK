def AddTo(krotka, war):
    lista = list(krotka)
    lista.append(war)
    return tuple(lista)


print(AddTo((1,2,3,4), 5))