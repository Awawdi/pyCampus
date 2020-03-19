def first_prime_over(n):
    gen = (i for i in range(n, n + 1000) if is_prime(i))

    return next(gen)


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(first_prime_over(1055))
