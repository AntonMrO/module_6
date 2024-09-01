class Animal:
    alive = True    #параметр живой
    fed = False     #параметр накормленный
    def __init__(self, name):
        self.name = name

    def eat(self, food):        #метод для наследования для классов Mammal и Predator
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal): #наследование метода eat и атрибутов с Animal
    pass

class Predator(Animal):  #наследование метода eat и атрибутов с Animal
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True    #переопределен атрибут с Plant


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
a3 = Predator('Медведь')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
p3 = Fruit('Малина')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.

a3.eat(p3)
print(f'{a3.name} сыт - {a3.fed}')

