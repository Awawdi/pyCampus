import functools


def add(x, y):
    return x + 1


shopping_list = [200, 120, 330, 50]
print(functools.reduce(add, shopping_list))
