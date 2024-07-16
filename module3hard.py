data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum = 0


def calculate_structure_sum(*args):
    global sum
    for arg in args:
        if isinstance(arg, int):
            sum += arg
        elif isinstance(arg, str):
            sum += len(arg)
        elif isinstance(arg, dict):
            calculate_structure_sum(*arg.items())
        else:
            calculate_structure_sum(*arg)
    return sum


result = calculate_structure_sum(data_structure)
print(result)
