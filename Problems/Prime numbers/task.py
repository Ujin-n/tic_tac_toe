prime_numbers = [x for x in range(2, 1001) if all(x % i for i in range(2, x))]
