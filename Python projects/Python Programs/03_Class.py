import random

class Dog:
    info = "Dog is a domesticated carnivore of the family Canidae."

    def __init__(self, name="Dog",age=0):
        self.lucky_number = random.randint(1, 10)
        self.name = name
        self.age = age

Dog1 = Dog("Tommy", 5)
Dog2 = Dog("Buddy", 3)
Dog3 = Dog()

print(Dog.info)
print(Dog1.lucky_number, Dog1.name, Dog1.age)
print(Dog2.lucky_number, Dog2.name, Dog2.age)
print(Dog3.lucky_number, Dog3.name, Dog3.age)
