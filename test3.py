import functools


def function(num, item):
    return num + 1


mylist = [1,2,3,4]

print(functools.reduce(function, mylist))
