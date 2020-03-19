def combine_coins(coin, lst):
    return ",".join(map(lambda x: coin + str(x), lst))

def combine_coins2(coin, numbers):
    return ",".join(map(lambda s,n : s + str(n), [coin for i in numbers],numbers))

print(combine_coins('$', range(5)))
print(combine_coins2('$', range(5)))

