def get_fibo():
    n1, n2 = 0, 1
    while True:
        nth = n1 + n2
        yield  nth
        n1 = n2
        n2 = nth

fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))