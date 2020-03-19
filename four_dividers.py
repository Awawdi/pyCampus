import functools


def four_dividers(number):
    return list(filter(helpingFunction, range(1, number)))


def helpingFunction(num):
    return num % 4 == 0


print(four_dividers(9))
print(four_dividers(3))
