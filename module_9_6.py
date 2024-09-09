def all_variants(text):
    for i in text:
        yield i


a = all_variants("abc")
for i in a:
    print(i)
