class Vehicle:
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = str(color).upper()
        self.__engine_power = engine_power

    __COLOR_VARIANTS = ['black', 'white', 'blue', 'red', 'grey', 'orange'] #цвет-черный, белый, синий, красный, серый, оранжевый

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец:', self.owner)

    def set_color(self, new_color):
        if new_color.casefold() in Vehicle.__COLOR_VARIANTS: # проверка наличия цветва в _Vehicle__COLOR_VARIANTS
            self.__color = new_color.upper()
        else:
            print(f'Нельзя сменить цвет на {new_color.upper()}!')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('PinK')
vehicle1.set_color('blacK')
vehicle1.owner = 'Vasyok'

# Проверяем, что поменялось
vehicle1.print_info()