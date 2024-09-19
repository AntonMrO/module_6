# Реализовать классы Figure(родительский), Circle, Triangle и Cube,
# объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны
# интерфейсы взаимодействия (методы) - геттеры и сеттеры.
from math import pi, sqrt

class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = sides if len(sides) == self.sides_count else [1] * self.sides_count
        if self.__is_valid_color(color[0],color[1], color[2]):
            self.__color = color
        else:
            print ( f'Некорректное значение цвета: {color}, введите 3 значения от 0 до 255' )
            self.__color = (255,255,255)   #устанавливает значения по-умолчанию
        self.filled = False

    @staticmethod
    def __is_valid_color(r, g, b):
        return (0<=r<=255 and 0<=g<=255 and 0<=b<=255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print ( f'Некорректное значение нового цвета: {(r, g, b)}, цвет остался преждним. Введите заново...' )

    @classmethod
    def __is_valid_sides(cls, *sides):  #значение стороны "+" и целое, сравнение кол-ва с сущ. количеством сторон фигуры
        flag = True
        for side in sides:
            if side <= 0 or not isinstance(side,int):
                print(type(side))
                flag = False
                break
        return flag and len(sides)==cls.sides_count

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    # def set_sides(self, *new_sides):
    #     if self.__is_valid_sides(new_sides):
    #         self.__sides = new_sides
    #     else:
    #         print('не корректное количество сторон или значения величины одной из сторон')

    def set_sides(self, *new_sides):
        if len(new_sides)==self.sides_count:
            self.__sides = list(new_sides)
        else:
            print('не корректное количество сторон или значения величины одной из сторон')

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, len_sq):
        super().__init__(color, len_sq)
        self.__radius = len_sq / (2 * pi)

    def get_square(self):
        return (self.__radius ** 2) * pi

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides) :
        super().__init__ (color, *sides)

    def get_square(self):
        p = len(self) / 2
        S = sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))
        return S

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side) :
        sides = [side] * 12
        super().__init__(color,*sides)

    def get_volume(self):
        return self._Figure__sides[0]**3

# 1 треугольник
trig1 = Triangle((222, 200, 100), 10, 6, 6)
print(trig1.get_color())
print(len(trig1))
print(trig1.get_square())

# 2 треугольник
trig2 = Triangle((33, 22, 11), 10, 6) #стороны будут 1,1,1, т.к. не хватает 1 значения стороны
print(trig2.get_color())
print(len(trig2))
print(trig2.get_square())
trig2.set_color(333, 623, 72) #не изменится
print(trig2.get_color())

# круг
circle1 = Circle((266, 200, 100), 10) # (Цвет, стороны)
print(circle1.get_color())
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

# Проверка периметра (куба):
print(len(cube1))


# (222, 200, 100)
# 22
# 16.583123951777
# (33, 22, 11)
# 3
# 0.4330127018922193
# Некорректное значение нового цвета: (333, 623, 72), цвет остался преждним. Введите заново...
# (33, 22, 11)
# Некорректное значение цвета: (266, 200, 100), введите 3 значения от 0 до 255
# (255, 255, 255)
# (55, 66, 77)
# Некорректное значение нового цвета: (300, 70, 15), цвет остался преждним. Введите заново...
# (222, 35, 130)
# не корректное количество сторон или значения величины одной из сторон
# (6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6)
# [15]
# 15
# 216
# 72
