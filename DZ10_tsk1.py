"""Доработаем задачи 5. Создайте класс-фабрику. 
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""


class Kingdom_Animals():
    def __init__(self, name: str, ) -> None:
        self.name = name

class Fishs(Kingdom_Animals):
    def __init__(self, name, fins: bool, color: str, size: int) -> None:
        super().__init__(name)
    # def __init__(self, name: str, fins: bool ):
    #     self.name = name
        self.fins = True
        self.color = color
        self.size = size

    def swimm(self):
        if self.fins == True:
            return print(f'{self.name}, can swimm')
        else:
            return print(f' Is not fish')
        

class Animals(Kingdom_Animals):
    def __init__(self, name: str, limbs: bool) -> None:
        super().__init__(name)
        self.limbs = True

class Dog(Animals):
    def __init__(self, name: str, limbs: bool, breed, age) -> None:
        super().__init__(name, limbs)
        self.breed = breed
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking like a {self.breed}.")

class Hooves(Animals):
    def __init__(self, name: str, limbs: bool, hooves: bool):
        self.hooves = True
        super().__init__(name, limbs)

class Birds(Kingdom_Animals):
    def __init__(self, name, wings: bool, can_fly: bool):
        super().__init__(name)
        self.wings = True
        self.wings = False
        self.can_fly = True
        self.can_fly = False
    
    def fly(self):
        if self.can_fly != False:
            print(f"{self.name} is flying")
        else:
            print(f"{self.name} cannot fly.")


# f1 = Fishs('Clownfish', fins=True, 'orange', 5)
f1 = Fishs('Clownfish',False,'orange', 5)
print(f1.swimm())

b1 = Birds("Colibri",True,True)
# b1 = Birds('Colibri',True, True)
print(b1.fly())
b2 = Birds('Penguin',True, False)
print(b2.fly())
# print(b2.exceptions_birds)