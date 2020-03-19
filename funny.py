def is_funny(myString):
    return all(map(lambda x : True if x == 'h' or x == 'a' else False,myString))


print(is_funny("hahahahaha"))
