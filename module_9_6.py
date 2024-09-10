from itertools import product


def all_variants(text):
    for i in range(1, len(text) + 1):
        for ch in product(text, repeat=i):
            if "".join(ch) in text:
                yield "".join(ch)

a = all_variants("abc")
for i in a:
    print(i)