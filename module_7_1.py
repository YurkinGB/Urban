class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        name = self.__file_name
        file = open(name, 'r')
        text_file = file.read()
        file.close()
        return text_file

    def add(self, *products):
        name = self.__file_name
        file = open(name, 'a')
        text_file = self.get_products()

        for product in products:
            if product.name not in text_file:
                file.write(f'{product.name}, {product.weight}, {product.category}\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()


def main():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())


if __name__ == '__main__':
    main()
