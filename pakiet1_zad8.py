import functools

numb = [1,2,3,4,5,6,7,8,9]

print(functools.reduce(lambda x, y: x+y, numb))