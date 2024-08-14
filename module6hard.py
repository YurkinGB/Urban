import math


class Figure:
    sides_count = 0

    def __init__(self,  __color, __sides, filled=False):
        self.__color = list(__color)
        self.__sides = __sides
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return r in range(0, 256) and g in range(0, 256) and b in range(0, 256)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_sides(self, *args):
        for arg in args:
            if arg not in range(0, 256):
                return False
        else:
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if isinstance(self, Circle):
            return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            for i in range(self.sides_count):
                self.__sides[i] = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides, filled=False):
        super().__init__(__color, __sides)
        self.__radius = round(__sides / (2 * math.pi), 2)

    def get_square(self):
        return round(math.pi * (self.__radius ** 2), 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, filled)
        self.__sides = __sides
        self.__height = (2 * self.get_square()) / self.__sides[0]

    def get_square(self):
        p = (self.__sides[0] + self.__sides[1] + self.__sides[2]) / 2
        return round(math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])), 2)



def main():
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    print(len(circle1))
    print(circle1.get_square())

    tr = Triangle((100, 100, 100), 4, 9, 6)
    print(tr.get_square())


if __name__ == '__main__':
    main()


