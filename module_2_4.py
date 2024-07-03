numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = []
not_prime = []
prime_not_prime_dict = {}

numbers.remove(1)

for i in numbers:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            prime_not_prime_dict.update({i: is_prime})
            break

for i in numbers:
    if i != 1 and i not in list(prime_not_prime_dict.keys()):
        prime.append(i)
    else:
        not_prime.append(i)
print('Prime: ', prime)
print('Non prime: ', not_prime)
