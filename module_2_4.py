numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = []
not_prime = []
prime_not_prime_dict = {}
is_prime = True

for i in numbers:
    if i != 1:
        prime_not_prime_dict.update({i: is_prime})

for i in list(prime_not_prime_dict.keys()):
    for j in range(2, i):
        if i % j == 0:
            prime_not_prime_dict.update({i: False})
            break

for i in list(prime_not_prime_dict.keys()):
    if prime_not_prime_dict[i] == is_prime:
        prime.append(i)
    else:
        not_prime.append(i)

print('Prime: ', prime)
print('Non prime: ', not_prime)
