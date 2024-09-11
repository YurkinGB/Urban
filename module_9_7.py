def is_prime(func):
    def is_prime_number(a, b, c):
        s = func(a, b, c)
        if s > 1:
            for i in range(2, (s // 2) + 1):
                if (s % i) == 0:
                    return 'Составное'
            else:
                return 'Простое'
    return is_prime_number


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 2, 1)
print(result)
