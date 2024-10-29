class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может есть {food}")


class Plant:
    edible = False
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

animal_1 = Predator('Волк с Уолл-Стрит')
animal_2 = Mammal('Хатико')
plant_1 = Flower('Цветик семицветик')
plant_2 = Fruit('Заводной апельсин')

print(animal_1.name)
print(plant_1.name)

print(animal_1.alive)
print(animal_2.fed)
animal_1.eat(plant_1)
animal_2.eat(plant_2)
print(animal_1.alive)
print(animal_2.fed)
