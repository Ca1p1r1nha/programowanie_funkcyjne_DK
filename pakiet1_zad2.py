def make_multiplier(x):

    def multiplaier(n):
        return x * n

    return multiplaier

double = make_multiplier(2)

print(double(6))
