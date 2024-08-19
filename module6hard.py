import math


class Figure:
    sides_count = 0

    def __init__(self, __color, __sides, filled=False):
        self.__color = list(__color)
        self.__sides = list(__sides)
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
        if len(args[0]) != self.sides_count:
            return False
        else:
            for arg in args[0]:
                if not (isinstance(arg, int) and arg > 0):
                    return False
            else:
                return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        p = 0
        if isinstance(self, Circle):
            return self.get_sides()[0]
        else:
            for side in self.get_sides():
                p += side
            return p

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, self.__set_circle_sides(__sides))
        self.__radius = round(__sides[0] / (2 * math.pi), 2)

    def get_square(self):
        return round(math.pi * (self.__radius ** 2), 2)

    def __set_circle_sides(self, side):
        lst = [1]
        if len(side) == self.sides_count:
            lst[0] = side[0]
            return lst
        else:
            return lst


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, self.__set_triangle_sides(__sides))
        self.__height = (2 * self.get_square()) / self.get_sides()[0]

    def get_square(self):
        p = (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2]) / 2
        return round(math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])),
                     2)

    def __set_triangle_sides(self, sides):
        if len(sides) == self.sides_count:
            return sides
        else:
            return 1, 1, 1


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, self.__set_cube_sides(__sides))

    def __set_cube_sides(self, side):
        if len(side) == 1:
            return [side[0] for i in range(self.sides_count)]
        else:
            return [1 for i in range(self.sides_count)]

    def get_volume(self):
        return self.get_sides()[0] * self.get_sides()[1] * self.get_sides()[2]


def main():
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())


if __name__ == '__main__':
    main()
