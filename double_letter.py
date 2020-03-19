import functools


def double_letter(my_str):
    return "".join(map(dbl, my_str))


def dbl(char):
    return char * 2


print(double_letter("python"))
print(double_letter("we are the champions!"))