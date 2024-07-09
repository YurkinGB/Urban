values_list = [2, 'fox_for_fox', False]
values_dict = {'a': 5, 'b': 'fox', 'c': True}
values_list_2 = [6, 'The_living_reaches_out_to_the_living']


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)