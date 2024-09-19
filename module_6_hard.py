# Реализовать классы Figure(родительский), Circle, Triangle и Cube,
# объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны
# интерфейсы взаимодействия (методы) - геттеры и сеттеры.
from math import pi

class Figure:
    def __init__(self, color, *sides):
        self.sides_count = 0
        self.__sides = sides
        if self.__is_valid_color(color[0],color[1], color[2]):
            self.__color = color
        else:
            print ( f'Некорректное значение цвета: {color}, введите заново' )
            self.__color = ('-','-','-')
        self.filled = False

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __valid_c(self, a, b, c):     #проверка 1 из значений числа цвета на соответствие 0-255 и целое
        if a in range (0, 256) and b in range (0, 256) and c in range (0, 256):
            return True

    def __is_valid_color(self, r, g, b):    #проверка RGB на соответствие параметрам с помощью метода __valid_c
        if self.__valid_c(r, g, b):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        # else:
        #     print ( f'Некорректное значение цвета: {(r, g, b)}, введите заново' )

    def __is_valid_sides(self, *sides):  #значение стороны "+" и целое, сравнение кол-ва с сущ. количеством сторон фигуры
        fl = False
        for i in sides:
            if isinstance(i, int) and i > 0 and len(sides) == self.sides_count:
                fl = True
            else: fl = False
        return fl

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides
        else:
            print('не корректное количество сторон или значения величины одной из сторон')

    def __len__(self):
        perimeter = 0
        for i in range(len(self.__sides)):
            perimeter += self.__sides[i-1]
        return perimeter

class Circle(Figure):
    def __init__(self, color, len_sq):
        super ().__init__ (color, len_sq)
        self.sides_count = 1
        self.__radius = len_sq / (2 * pi)

    def get_square(self):
        return (self.__radius ** 2) * pi

class Triangle(Figure):
    def __init__(self, color, *side) :
        self.sides_count = 3
        super ().__init__ (color)

    def get_square(self):
        Len_2 = self.__len__() / 2
        S = marh.sqrt(Len_2 * (Len_2 - self.__sides[0]) * (Len_2 - self.__sides[1]) * (Len_2 - self.__sides[2]))

class Cube(Figure):
    def __init__(self, color, *sides) :
        self.sides_count = 12
        self.__sides = sides * 12
        super ().__init__ ( color, *sides )

    def get_volume(self):
        return self.__sides[0]**3

# trig1 = Triangle((200, 200, 100), 10, 6)
# print(trig1.get_color())
# print(len(trig1))
#
# fg1 = Figure((255,0,250),12)
# print(fg1.get_color())
# fg1.set_color(255, 266, 77)
# print(fg1.get_color())
# print(len(fg1))



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
