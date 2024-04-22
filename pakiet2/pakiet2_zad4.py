ListaPrzed = [1,2,3,4,5,6,7,8,9,10]
ListaPo = [n for x in ListaPrzed if (n:=x**2) > 10]

print(ListaPo)

