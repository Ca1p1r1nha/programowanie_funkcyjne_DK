#Wypracować 5 funkcji predefiniowanych
def kalk(op):
    def dod(x, y):
        return x + y

    def ode(x, y):
        return x - y

    def pom(x, y):
        return x * y

    def dzi(x, y):
        if y != 0:
            return x / y
        else:
            return "knie można dzielić przez 0"

    def pot(x, n):
        return x ** n



