#Funkcje ze zmiennymi funkcyjnymi i globalnymi


glo = 1

def localna_i_globalna(x):
    lokal = 3
    return x + lokal + lokal

print(localna_i_globalna(3 + glo))